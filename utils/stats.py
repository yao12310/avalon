# TODO: break up into separate utils

"""
Utilities for computing avalon game- and player-level stats.
"""

import sys

from collections import defaultdict

import numpy as np
import pandas as pd

# hack, but needed for testing in jupyter
if __name__ == 'avalon.utils.stats':
    from .constants import *
    from .sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

def good_win_rate(ex_ch=False, df=None):
    """
    Compute overall win rate of good team.
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : float, int
        good win rate, sample size
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    return df[GOOD_WIN].mean(), df.shape[0]
    
def good_win_rates_n_players(ex_ch=False, df=None):
    """
    Compute win rate of good team w.r.t. game size.
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    df = df[[GAME_INDEX, GOOD_WIN, NUM_PLAYERS]].groupby(NUM_PLAYERS) \
            .agg(
                    {
                        GAME_INDEX: 'count',
                        GOOD_WIN: 'mean'
                    }
                ) \
            .rename(
                {
                    GAME_INDEX: "Sample Size",
                    GOOD_WIN: "Good Win %"
                },
                axis=1
            )
    
    return df.reset_index()

def good_win_rates_n_percivals(ex_ch=False, df=None):
    """
    Compute win rate of good team w.r.t. number of percival claims
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    df = df[[GAME_INDEX, GOOD_WIN, NUM_PERCIVAL]].groupby(NUM_PERCIVAL) \
            .agg(
                    {
                        GAME_INDEX: 'count',
                        GOOD_WIN: 'mean'
                    }
                ) \
            .rename(
                {
                    GAME_INDEX: "Sample Size",
                    GOOD_WIN: "Good Win %"
                },
                axis=1
            )
    
    return df.reset_index()

def win_lengths(ex_ch=False, df=None):
    """
    Compute mean/sd length of games won by good and bad teams.
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    df = df[df[LENGTH] != -1]
    df = df[[GAME_INDEX, WINNER, LENGTH]].groupby(WINNER) \
            .agg(
                    {
                        GAME_INDEX: 'count',
                        LENGTH: ['mean', 'std']
                    }
                )
    df.columns = df.columns.get_level_values(0)
    df.columns = ["Sample Size", "Mean Length", "SD Length"]
    return df.reset_index()

def carries(df=None):
    """
    Compute number of times each player has carried.
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    fails_col = FAILS_ROUND.format(MAX_ROUNDS)
    
    if df is None:
        df = fetch_game_log(parse_cols=True)
    df = df[~df[fails_col].isin([NA, UTD, 'None'])]
    df = df[[GAME_INDEX, fails_col]].groupby(fails_col).count()
    df = df.reset_index()
    df.columns = ["Player", "# Carries"]
    return df

def top_win_rates(ex_ch=False, n=5, thresh=SAMPLE_THRESH, df=None):
    """
    Compute win rate leaderboard.
    ex_ch : bool
        exclude cheesy wins
    n : int
        leaderboard size
    thresh : int
        minimum # games played
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return pd.DataFrame
    """
    player_wl = defaultdict(
        lambda: {
            'good_w': 0,
            'good_l': 0,
            'bad_w': 0,
            'bad_l': 0
        }
    )
    
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    for idx, row in df.iterrows():
        for role in ROLES:
            player = row[role]
            if player == NA or player == UNK:
                continue
            if row[GOOD_WIN]:
                if role in BADS:
                    player_wl[player]['bad_l'] += 1
                else:
                    player_wl[player]['good_w'] += 1
            else:
                if role in BADS:
                    player_wl[player]['bad_w'] += 1
                else:
                    player_wl[player]['good_l'] += 1
    
    ldbrd = pd.DataFrame(
        [
            (
                player,
                (player_wl[player]['good_w'] + player_wl[player]['bad_w']) / sum(player_wl[player].values()),
                player_wl[player]['good_w'] / (player_wl[player]['good_w'] + player_wl[player]['good_l']),
                player_wl[player]['bad_w'] / (player_wl[player]['bad_w'] + player_wl[player]['bad_l']),
                sum(player_wl[player].values())
            ) for player in player_wl if ((player_wl[player]['good_w'] + player_wl[player]['good_l']) and 
                                          (player_wl[player]['bad_w'] + player_wl[player]['bad_l']))
        ],
        columns=("Player", "Win %", "Good Win %", "Bad Win %", "Sample Size")
    )
    ldbrd = ldbrd[ldbrd["Sample Size"] >= thresh]
    ldbrd = ldbrd.sort_values("Win %", ascending=False)
    return ldbrd.iloc[:n].reset_index().drop("index", axis=1)

def games_played_rank(thresh=SAMPLE_THRESH, df=None):
    """
    Find ranking of total games played.
    thresh : int
        minimum # games played
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    
    player_game_cnt = defaultdict(int)
    for idx, row in df.iterrows():
        for role in ROLES:
            player = row[role]
            if player == NA or player == UNK:
                continue
            player_game_cnt[player] += 1
            
    player_game_cnt = {player: cnt for player, cnt in player_game_cnt.items() if cnt >= thresh}
    
    return pd.DataFrame(player_game_cnt.items(), columns=["Player", "Games Played"]).sort_values("Games Played", ascending=False)

def kgt_stats(ex_ch=False, df=None):
    """
    Compute KGT-related win statistics.
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    df1 = df[[GAME_INDEX, GOOD_WIN, WEAK_KGT_SUCCESS]][~df[WEAK_KGT_SUCCESS].isin([NA, UTD])] \
              .groupby(WEAK_KGT_SUCCESS) \
              .agg(
                      {
                          GAME_INDEX: 'count',
                          GOOD_WIN: 'mean'
                      }
              ) \
              .reset_index()
    df1.columns = ["Weak Success", "Count", "Good Win %"]
    
    df2 = df[[GAME_INDEX, GOOD_WIN, STRONG_KGT_SUCCESS]][~df[STRONG_KGT_SUCCESS].isin([NA, UTD])] \
              .groupby(STRONG_KGT_SUCCESS) \
              .agg(
                      {
                          GAME_INDEX: 'count',
                          GOOD_WIN: 'mean'
                      }
              ) \
              .reset_index()
    df2.columns = ["Strong Success", "Count", "Good Win %"]    
    
    df3 = df[[GAME_INDEX, GOOD_WIN, WEAK_KGT_APPLY]][~(df[WEAK_KGT_APPLY] == UTD)] \
            .groupby(WEAK_KGT_APPLY) \
            .agg(
                    {
                        GAME_INDEX: 'count',
                        GOOD_WIN: 'mean'
                    }
                ) \
            .rename(
                {
                    GAME_INDEX: "Sample Size",
                    GOOD_WIN: "Good Win %"
                },
                axis=1
            ) \
            .reset_index()
    
    df4 = df[[GAME_INDEX, GOOD_WIN, STRONG_KGT_APPLY]][~(df[STRONG_KGT_APPLY] == UTD)] \
            .groupby(STRONG_KGT_APPLY) \
            .agg(
                    {
                        GAME_INDEX: 'count',
                        GOOD_WIN: 'mean'
                    }
                ) \
            .rename(
                {
                    GAME_INDEX: "Sample Size",
                    GOOD_WIN: "Good Win %"
                },
                axis=1
            ) \
            .reset_index()
    
    return df1, df2, df3, df4

def player_role_cnts(role, df=None):
    """
    Count number of times each player has had a given role.
    role : str
        role name
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    player_cnts = defaultdict(int)
    if df is None:
        df = fetch_game_log(parse_cols=True)
    df = df[~df[role].isin([UNK, NA])]
    
    for idx, row in df.iterrows():
        player_cnts[row[role]] += 1
    
    df = pd.DataFrame(list(player_cnts.items()), columns=[role, "Count"])
    df = df.sort_values("Count", ascending=False)
    return df

def player_cnts_all_roles(thresh=SAMPLE_THRESH, norm_axis=-1, rounding=3, df=None):
    """
    Compute metrics for number/% of times a player has been each role.
    thresh : int
        minimum number of games
    norm_axis : int
        if -1, no normalization
        if 0, normalize by # of appearances for each role
        if 1, normalize by # of games for each player
    rounding : int
        number of places to round to
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    dfs = {role: player_role_cnts(role, df) for role in ROLES}

    df = dfs[MERLIN].set_index(MERLIN)
    df.columns = [MERLIN]
    for role in ROLES[1:]:
        curr_df = dfs[role].set_index(role)
        curr_df.columns = [role]
        df = df.join(curr_df, how='outer')
        
    df = df.fillna(0).astype(int)
    
    df[LOYAL_SERVANT] = pd.concat([df[loyal] for loyal in LOYALS], axis=1).sum(1)
    df = df.drop(LOYALS, axis=1)
    
    if norm_axis == -1:
        df["Sample Size"] = df.sum(axis=1)
        df.index = df.index.rename("Player")
        return df[df["Sample Size"] >= thresh].reset_index()
    else:
        sample_sizes = df.sum(axis=1)
        df = df.divide(df.sum(axis=norm_axis), axis=(1 - norm_axis))
        df = df.apply(lambda x: np.round(x, rounding))
        df["Sample Size"] = sample_sizes
        df.index = df.index.rename("Player")
        return df[sample_sizes >= thresh].reset_index()

def player_pair_pcts(thresh=SAMPLE_THRESH, rounding=2, ex_ch=False, df=None):
    """
    Compute percentage of times two players have been on the same team.
    thresh : int
        minimum number of games both players were in the same game
    rounding : int
        number of places to round to
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    player_cnts = defaultdict(int)
    player_pair_game_cnts = defaultdict(lambda: defaultdict(int))
    player_pair_team_cnts = defaultdict(lambda: defaultdict(int))
    for idx, row in df.iterrows():
        for role1 in ROLES:
            player1 = row[role1]
            player_cnts[player1] += 1
            for role2 in ROLES:
                if role1 == role2:
                    continue
                player2 = row[role2]
                if player1 in [UNK, NA] or player2 in [UNK, NA]:
                    continue

                player_pair_game_cnts[player1][player2] += 1

                if role1 in BADS and role2 not in BADS:
                    continue
                if role1 not in BADS and role2 in BADS:
                    continue

                player_pair_team_cnts[player1][player2] += 1
                
    df = []
    players = list(player_pair_game_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh, players))
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(-1)
            elif player_pair_game_cnts[p1][p2] >= thresh:
                df[-1].append(player_pair_team_cnts[p1][p2] / player_pair_game_cnts[p1][p2])
            else:
                df[-1].append(-1)
    
    df = pd.DataFrame(df, columns=players, index=players)
    df = df.apply(lambda x: np.round(x, rounding))
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def player_pair_opp_pcts(thresh=SAMPLE_THRESH, rounding=2, ex_ch=False, df=None):
    """
    Compute percentage of times two players have been on the same team.
    thresh : int
        minimum number of games both players were in the same game
    rounding : int
        number of places to round to
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    player_cnts = defaultdict(int)
    player_pair_game_cnts = defaultdict(lambda: defaultdict(int))
    player_pair_team_cnts = defaultdict(lambda: defaultdict(int))
    for idx, row in df.iterrows():
        for role1 in ROLES:
            player1 = row[role1]
            player_cnts[player1] += 1
            for role2 in ROLES:
                if role1 == role2:
                    continue
                player2 = row[role2]
                if player1 in [UNK, NA] or player2 in [UNK, NA]:
                    continue

                player_pair_game_cnts[player1][player2] += 1

                if role1 in BADS and role2 in BADS:
                    continue
                if role1 not in BADS and role2 not in BADS:
                    continue

                player_pair_team_cnts[player1][player2] += 1
                
    df = []
    players = list(player_pair_game_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh, players))
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(-1)
            elif player_pair_game_cnts[p1][p2] >= thresh:
                df[-1].append(player_pair_team_cnts[p1][p2] / player_pair_game_cnts[p1][p2])
            else:
                df[-1].append(-1)
    
    df = pd.DataFrame(df, columns=players, index=players)
    df = df.apply(lambda x: np.round(x, rounding))
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def player_pair_win_pcts(thresh=SAMPLE_THRESH, rounding=2, ex_ch=False, df=None):
    """
    Compute percentage of times two players have won after being on the same team.
    thresh : int
        minimum number of games both players were on the same team
    rounding : int
        number of places to round to
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    player_cnts = defaultdict(int)
    player_pair_team_cnts = defaultdict(lambda: defaultdict(int))
    player_pair_win_cnts = defaultdict(lambda: defaultdict(int))
    for idx, row in df.iterrows():
        for role1 in ROLES:
            player1 = row[role1]
            player_cnts[player1] += 1
            for role2 in ROLES:
                if role1 == role2:
                    continue
                player2 = row[role2]
                if player1 in [UNK, NA] or player2 in [UNK, NA]:
                    continue

                if role1 in BADS and role2 in BADS:
                    player_pair_team_cnts[player1][player2] += 1
                    if row[WINNER] == BAD:
                        player_pair_win_cnts[player1][player2] += 1
                if role1 not in BADS and role2 not in BADS:
                    player_pair_team_cnts[player1][player2] += 1
                    if row[WINNER] == GOOD:
                        player_pair_win_cnts[player1][player2] += 1
                
    df = []
    players = list(player_pair_team_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh, players))
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(-1)
            elif player_pair_team_cnts[p1][p2] >= thresh:
                df[-1].append(player_pair_win_cnts[p1][p2] / player_pair_team_cnts[p1][p2])
            else:
                df[-1].append(-1)
    
    df = pd.DataFrame(df, columns=players, index=players)
    df = df.apply(lambda x: np.round(x, rounding))
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def player_pair_vs_win_pcts(thresh=SAMPLE_THRESH, rounding=2, ex_ch=False, df=None):
    """
    Compute win percentage between all pairs of players when on different teams.
    thresh : int
        minimum number of games both players were on different teams
    rounding : int
        number of places to round to
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    player_cnts = defaultdict(int)
    player_pair_opp_cnts = defaultdict(lambda: defaultdict(int))
    player_pair_win_cnts = defaultdict(lambda: defaultdict(int))
    for idx, row in df.iterrows():
        for role1 in ROLES:
            player1 = row[role1]
            player_cnts[player1] += 1
            for role2 in ROLES:
                if role1 == role2:
                    continue
                player2 = row[role2]
                if player1 in [UNK, NA] or player2 in [UNK, NA]:
                    continue

                if role1 in BADS and role2 not in BADS:
                    player_pair_opp_cnts[player1][player2] += 1
                    if row[WINNER] == BAD:
                        player_pair_win_cnts[player1][player2] += 1
                if role1 not in BADS and role2 in BADS:
                    player_pair_opp_cnts[player1][player2] += 1
                    if row[WINNER] == GOOD:
                        player_pair_win_cnts[player1][player2] += 1
                
    df = []
    players = list(player_pair_opp_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh, players))
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(-1)
            elif player_pair_opp_cnts[p1][p2] >= thresh:
                df[-1].append(player_pair_win_cnts[p1][p2] / player_pair_opp_cnts[p1][p2])
            else:
                df[-1].append(-1)
    
    df = pd.DataFrame(df, columns=players, index=players)
    df = df.apply(lambda x: np.round(x, rounding))
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def r1_r2_strat(ex_ch=False, df=None):
    """
    Compare 2+2 vs 3+1 round 1 to round 2 team selection strats.
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    twotwo_cnt = 0
    twotwo_win = 0
    threeone_cnt = 0
    threeone_win = 0

    for idx, row in df.iterrows():
        percival = row[PERCIVAL]
        round_one_team = set(row[TEAM_ROUND.format(1)].split(', '))
        round_one_fails = row[FAILS_ROUND.format(1)]
        if round_one_fails != 'None':
            continue
        if percival not in round_one_team:
            continue

        round_two_team = set(row[TEAM_ROUND.format(2)].split(', '))

        if len(round_one_team.intersection(round_two_team)) == 3:
            threeone_cnt += 1
            if row[WINNER] == GOOD:
                threeone_win += 1
        else:
            twotwo_cnt += 1
            if row[WINNER] == GOOD:
                twotwo_win += 1
    
    df = [[threeone_win / threeone_cnt, threeone_cnt], [twotwo_win / twotwo_cnt, twotwo_cnt]]
    
    return pd.DataFrame(df, columns=["Win %", "Sample Size"], index=["3+1", "2+2"])

def r1_fail(ex_ch=False, filter_percival=False, df=None):
    """
    Compute win rate when round 1 fails versus not.
    ex_ch : bool
        exclude cheesy wins
    filter_percival : bool
        exclude games where percival is on r1
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    fail_cnt = 0
    fail_win = 0
    succeed_cnt = 0
    succeed_win = 0

    for idx, row in df.iterrows():
        if filter_percival:
            percival = row[PERCIVAL]
        
        bad_players = set([row[role] for role in BADS])
        round_one_team = set(row[TEAM_ROUND.format(1)].split(', '))
        
        if filter_percival:
            if percival in round_one_team:
                continue
        
        if not bad_players.intersection(round_one_team):
            continue
        
        round_one_fails = row[FAILS_ROUND.format(1)]
        
        if round_one_fails == UTD:
            continue
        if round_one_fails != 'None':
            fail_cnt += 1
            if row[WINNER] == GOOD:
                fail_win += 1
        else:
            succeed_cnt += 1
            if row[WINNER] == GOOD:
                succeed_win += 1

    df = [[fail_win / fail_cnt, fail_cnt], [succeed_win / succeed_cnt, succeed_cnt]]
    
    return pd.DataFrame(df, columns=["Win %", "Sample Size"], index=["R1 Fail", "R1 Succeed"])

def flip_win_pcts(missions, ns=2, df=None):
    """
    Given that there are n non-Oberon bad guys on a mission, find % chance of failing/successing flip and win %.
    missions : []int
        mission indices
    ns : []int
        number of bad guys
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
        
    total = 0
    fail_cnts = defaultdict(int)
    good_win_fail_cnts = defaultdict(int)
    
    for idx, row in df.iterrows():
        for mission in missions:
            bads = set([row[bad] for bad in BADS if bad != OBERON and row[bad] not in [NA, UNK]])
            team = set(row[TEAM_ROUND.format(mission)].split(', '))
            fails = set(row[FAILS_ROUND.format(mission)].split(', '))
            if team in [UTD, UNK, NA] or fails in [UTD, UNK, NA]:
                continue
            if len(team.intersection(bads)) in ns:
                total += 1
                num_fails = len([fail for fail in fails if fail != 'None'])
                fail_cnts[num_fails] += 1
                if row[WINNER] == GOOD:
                    good_win_fail_cnts[num_fails] += 1
            
    return pd.DataFrame(
        [
            (num_fails, fail_cnts[num_fails], fail_cnts[num_fails] / total, good_win_fail_cnts[num_fails] / fail_cnts[num_fails])
            for num_fails in range(max(ns) + 1) if fail_cnts[num_fails]
        ],
        columns=["# Fails", "Count", "%", "Good Win %"]
    )
