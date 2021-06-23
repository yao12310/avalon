# TODO: break up into separate utils

"""
Utilities for computing avalon game- and player-level stats.
"""

import sys

from collections import defaultdict
from itertools import product

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
    # only counts as a carry if there was only one fail
    df = df[df[fails_col].apply(lambda fails: len(fails.split(', ')) == 1)]
    df = df[[GAME_INDEX, fails_col]].groupby(fails_col).count()
    df = df.reset_index()
    df.columns = ["Player", "# Carries"]
    df = df.sort_values("# Carries", ascending=False)
    return df

def top_win_rates(ex_ch=False, n=5, thresh=SAMPLE_THRESH, df=None):
    """
    Compute win rate leaderboard.
    ex_ch : bool
        exclude cheesy wins
    n : int
        leaderboard size (if -1, use full leaderboard)
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
    
    ldbrd = []
    for player in player_wl:
        if player_wl[player]['good_w'] + player_wl[player]['good_l']:
            good_win_pct = player_wl[player]['good_w']/ (player_wl[player]['good_w'] + player_wl[player]['good_l'])
        else:
            good_win_pct = -1
            
        if player_wl[player]['bad_w'] + player_wl[player]['bad_l']:
            bad_win_pct = player_wl[player]['bad_w'] / (player_wl[player]['bad_w'] + player_wl[player]['bad_l'])
        else:
            bad_win_pct = -1
            
        ldbrd.append(
            (
                player,
                (player_wl[player]['good_w'] + player_wl[player]['bad_w']) / sum(player_wl[player].values()),
                good_win_pct,
                bad_win_pct,
                sum(player_wl[player].values()),
                player_wl[player]['good_w'] + player_wl[player]['bad_w'],
                player_wl[player]['good_l'] + player_wl[player]['bad_l']
            )
        )
    
    ldbrd = pd.DataFrame(ldbrd, columns=("Player", "Win %", "Good Win %", "Bad Win %", "Sample Size", "Wins", "Losses"))
    ldbrd = ldbrd[ldbrd["Sample Size"] >= thresh]
    ldbrd = ldbrd.sort_values(["Win %", "Sample Size"], ascending=False)
    
    top_player = ldbrd["Player"].iloc[0]
    top_wins = ldbrd["Wins"].iloc[0]
    top_losses = ldbrd["Losses"].iloc[0]
    games_behind = [0]
    for i in range(1, ldbrd.shape[0]):
        curr_wins = ldbrd["Wins"].iloc[i]
        curr_losses = ldbrd["Losses"].iloc[i]
        behind = (top_wins * (curr_wins + curr_losses) - curr_wins * (top_wins + top_losses)) / top_losses
        games_behind.append(int(behind + 1))
        
    ldbrd["Games Behind {}".format(top_player)] = games_behind
    
    if n == -1:
        n = ldbrd.shape[0]
    
    return ldbrd.iloc[:n].reset_index().drop("index", axis=1)

def top_win_rates_role(role, ex_ch=False, n=5, thresh=SAMPLE_THRESH, df=None):
    """
    Compute win rate leaderboard for given role.
    role : str
        game role
    ex_ch : bool
        exclude cheesy wins
    n : int
        leaderboard size (if -1, use full leaderboard)
    thresh : int
        minimum # games played
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return pd.DataFrame
    """
    assert(role in ROLES or role == LOYAL_SERVANT)
    player_wl = defaultdict(
        lambda: {
            'wins': 0,
            'losses': 0
        }
    )
    
    if df is None:
        df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
        
    for idx, row in df.iterrows():
        if role == LOYAL_SERVANT:
            players = [row[loyal] for loyal in LOYALS if row[loyal] not in [NA, UNK]]
            if row[WINNER] == GOOD:
                for player in players:
                    player_wl[player]['wins'] += 1
            else:
                for player in players:
                    player_wl[player]['losses'] += 1
        elif role in BADS:
            player = row[role]
            if player == NA:
                continue
            if row[WINNER] == BAD:
                player_wl[player]['wins'] += 1
            else:
                player_wl[player]['losses'] += 1
        else:
            player = row[role]
            if player == NA:
                continue
            if row[WINNER] == GOOD:
                player_wl[player]['wins'] += 1
            else:
                player_wl[player]['losses'] += 1
    
    ldbrd = []
    for player in player_wl:
        if player_wl[player]['wins'] + player_wl[player]['losses']:
            win_pct = player_wl[player]['wins']/ (player_wl[player]['wins'] + player_wl[player]['losses'])
        else:
            win_pct = -1
            
        ldbrd.append(
            (
                player,
                win_pct,
                sum(player_wl[player].values()),
                player_wl[player]['wins'],
                player_wl[player]['losses']
            )
        )
    
    ldbrd = pd.DataFrame(ldbrd, columns=("Player", "Win %", "Sample Size", "Wins", "Losses"))
    ldbrd = ldbrd[ldbrd["Sample Size"] >= thresh]
    ldbrd = ldbrd.sort_values(["Win %", "Sample Size"], ascending=False)
    
    top_player = ldbrd["Player"].iloc[0]
    top_wins = ldbrd["Wins"].iloc[0]
    top_losses = ldbrd["Losses"].iloc[0]
    games_behind = [0]
    for i in range(1, ldbrd.shape[0]):
        curr_wins = ldbrd["Wins"].iloc[i]
        curr_losses = ldbrd["Losses"].iloc[i]
        if top_losses:
            behind = (top_wins * (curr_wins + curr_losses) - curr_wins * (top_wins + top_losses)) / top_losses
            games_behind.append(int(behind + 1))
        else:
            games_behind.append(np.nan)
        
        
    ldbrd["Games Behind {}".format(top_player)] = games_behind
    
    if n == -1:
        n = ldbrd.shape[0]
    
    return ldbrd.iloc[:n].reset_index().drop("index", axis=1)

def win_pct_ev(ex_ch=False, use_theoretical_rates=False, thresh=SAMPLE_THRESH, df=None):
    """
    Find expected win rates of players (controlling for game size / # games as good or bad).
    ex_ch : bool
        exclude cheesy wins
    use_theoretical_rates : bool
        use theoretical good win rates, or rates from data
    thresh : int
        minimum # games played
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    
    d_keys = list(product(SIZES, [GOOD, BAD]))
    player_size_team_cnts = defaultdict(lambda: dict(zip(d_keys, [0] * len(d_keys)))) # dict[str, dict[(int, str), int]]
    player_game_cnts = defaultdict(int)
    for idx, row in df.iterrows():
        if ex_ch and row[CHEESY_WIN] == "Yes":
            continue
        num_players = row[NUM_PLAYERS]
        for role in ROLES:
            player = row[role]
            if player in [NA, UNK]:
                continue
            player_game_cnts[player] += 1
            if role in BADS:
                player_size_team_cnts[player][(num_players, BAD)] += 1
            else:
                player_size_team_cnts[player][(num_players, GOOD)] += 1
    
    if use_theoretical_rates:
        good_win_rates = GOOD_WIN_RATES_BALANCE
    else:
        good_win_rates = good_win_rates_n_players(ex_ch=ex_ch, df=df)[["# Players", "Good Win %"]] \
                             .set_index("# Players") \
                             .to_dict()["Good Win %"]
    
    player_size_good_pcts = {}
    player_size_bad_pcts = {}
    for player in player_size_team_cnts:
        player_size_good_pcts[player] = defaultdict(
            int,
            {
                key[0]: player_size_team_cnts[player][key] / player_game_cnts[player]
                    for key in player_size_team_cnts[player] if GOOD in key
            }
        )
        player_size_bad_pcts[player] = defaultdict(
            int,
            {
                key[0]: player_size_team_cnts[player][key] / player_game_cnts[player]
                    for key in player_size_team_cnts[player] if BAD in key
            }
        )
        
    player_win_pct_evs = {}
    for player in player_size_good_pcts:
        if player_game_cnts[player] < thresh:
            continue
        ev = 0
        for size in player_size_good_pcts[player]:
            if size not in good_win_rates:
                continue
            ev += player_size_good_pcts[player][size] * good_win_rates[size] + player_size_bad_pcts[player][size] * (1 - good_win_rates[size])
        
        player_win_pct_evs[player] = ev
            
    return pd.DataFrame(player_win_pct_evs.items(), columns=["Player", "Expected Win %"]).sort_values("Expected Win %", ascending=False)

def win_pct_over_ev_rank(ex_ch=False, n=5, use_theoretical_rates=False, thresh=SAMPLE_THRESH, df=None):
    """
    Find expected win rates of players (controlling for game size / # games as good or bad).
    ex_ch : bool
        exclude cheesy wins
    n : int
        leaderboard size (if -1, use full leaderboard)
    use_theoretical_rates : bool
        use theoretical good win rates, or rates from data
    thresh : int
        minimum # games played
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    win_pcts = top_win_rates(ex_ch=ex_ch, n=-1, thresh=SAMPLE_THRESH, df=df).set_index("Player")
    win_evs = win_pct_ev(ex_ch=ex_ch, use_theoretical_rates=use_theoretical_rates, thresh=thresh, df=df).set_index("Player")
    team_cnts = good_pct_rank(thresh=thresh, df=df).set_index("Player")
    
    ev_score = [
        (
            player,
            win_pcts.loc[player]["Win %"] - win_evs.loc[player]["Expected Win %"],
            win_pcts.loc[player]["Win %"],
            win_evs.loc[player]["Expected Win %"],
            team_cnts.loc[player]["Good %"]
        ) for player in win_evs.index
    ]
    
    if n == -1:
        n = len(ev_score)
    
    return pd.DataFrame(ev_score, columns=["Player", "Win % Over Expected", "Win %", "Expected Win %", "Good %"]) \
               .sort_values("Win % Over Expected", ascending=False) \
               .iloc[:n]

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

def good_pct_rank(thresh=SAMPLE_THRESH, df=None):
    """
    Find ranking of good team %.
    thresh : int
        minimum # games played
    df : pd.DataFrame
        game data llog (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
        
    player_good_cnt = defaultdict(int)
    player_game_cnt = defaultdict(int)
    
    for idx, row in df.iterrows():
        for role in ROLES:
            player = row[role]
            if player == NA or player == UNK:
                continue
            player_game_cnt[player] += 1
            if role not in BADS:
                player_good_cnt[player] += 1
                
    player_good_pct = [(player, player_good_cnt[player] / cnt, player_good_cnt[player], cnt - player_good_cnt[player]) 
                           for player, cnt in player_game_cnt.items() if cnt >= thresh]
    
    return pd.DataFrame(player_good_pct, columns=["Player", "Good %", "# Good", "# Bad"]).sort_values("Good %", ascending=False)
    
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

def player_pair_pcts(thresh=SAMPLE_THRESH, rounding=2, ex_ch=False, df=None, bad=False):
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
    bad : bool
        only count bad team games
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
                if bad and (role1 not in BADS or role2 not in BADS):
                    continue
                if role1 in BADS and role2 not in BADS:
                    continue
                if role1 not in BADS and role2 in BADS:
                    continue

                player_pair_team_cnts[player1][player2] += 1
                
    insuff_data = []
    for player1 in player_pair_game_cnts:
        if all(player_pair_game_cnts[player1][player2] < thresh for player2 in player_pair_game_cnts[player1]):
            insuff_data.append(player1)
    
    df = []
    players = list(player_pair_game_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh and p not in insuff_data, players))
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(1.0 if not bad else -1)
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
    Compute percentage of times two players have been on opposite teams.
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
                
    insuff_data = []
    for player1 in player_pair_game_cnts:
        if all(player_pair_game_cnts[player1][player2] < thresh for player2 in player_pair_game_cnts[player1]):
            insuff_data.append(player1)
    
    df = []
    players = list(player_pair_game_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh and p not in insuff_data, players))
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(0.0)
            elif player_pair_game_cnts[p1][p2] >= thresh:
                df[-1].append(player_pair_team_cnts[p1][p2] / player_pair_game_cnts[p1][p2])
            else:
                df[-1].append(-1)
    
    df = pd.DataFrame(df, columns=players, index=players)
    df = df.apply(lambda x: np.round(x, rounding))
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def player_pair_cnts(ex_ch=False, df=None, bad=False):
    """
    Compute number of times two players have been on the same team.
    ex_ch : bool
        exclude cheesy wins
    df : pd.DataFrame
        game data log (if None, fetch from API)
    bad : bool
        only count bad team games
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
                
                if bad and (role1 not in BADS or role2 not in BADS):
                    continue
                if role1 in BADS and role2 not in BADS:
                    continue
                if role1 not in BADS and role2 in BADS:
                    continue

                player_pair_team_cnts[player1][player2] += 1
    
    df = []
    players = list(player_pair_game_cnts.keys())
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(player_cnts[p1] if not bad else -1)
            else:
                df[-1].append(player_pair_team_cnts[p1][p2])
    
    df = pd.DataFrame(df, columns=players, index=players)
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def player_pair_opp_cnts(ex_ch=False, df=None):
    """
    Compute number of times two players have been on opposite teams.
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
    for p1 in players:
        df.append([])
        for p2 in players:
            if p1 == p2:
                df[-1].append(0)
            else:
                df[-1].append(player_pair_team_cnts[p1][p2])
    
    df = pd.DataFrame(df, columns=players, index=players)
    df.index = df.index.rename("Player")
    
    return df.reset_index()

def player_pair_win_pcts(thresh=SAMPLE_THRESH, rounding=2, ex_ch=False, df=None, bad=False):
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
    bad : bool
        only count bad team games
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
                if bad and (role1 not in BADS or role2 not in BADS):
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
                
    insuff_data = []
    for player1 in player_pair_team_cnts:
        if all(player_pair_team_cnts[player1][player2] < thresh for player2 in player_pair_team_cnts[player1]):
            insuff_data.append(player1)
    
    df = []
    players = list(player_pair_team_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh and p not in insuff_data, players))
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
                
    insuff_data = []
    for player1 in player_pair_opp_cnts:
        if all(player_pair_opp_cnts[player1][player2] < thresh for player2 in player_pair_opp_cnts[player1]):
            insuff_data.append(player1)
    
    df = []
    players = list(player_pair_opp_cnts.keys())
    players = list(filter(lambda p: player_cnts[p] >= thresh and p not in insuff_data, players))
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
    
    df = [["3+1", threeone_win / threeone_cnt, threeone_cnt], ["2+2", twotwo_win / twotwo_cnt, twotwo_cnt]]
    
    return pd.DataFrame(df, columns=["Strategy", "Win %", "Sample Size"])

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

    df = [["Fail", fail_win / fail_cnt, fail_cnt], ["Success", succeed_win / succeed_cnt, succeed_cnt]]
    
    return pd.DataFrame(df, columns=["R1 Outcome", "Win %", "Sample Size"])

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

def fake_percival_claim_pct(rounding=5, df=None):
    """
    Compute % of times each role fake claims Percival.
    rounding : int
        num decimal places to round to
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    
    num_games = defaultdict(int)
    num_fake_claims = defaultdict(int)
    
    for idx, row in df.iterrows():
        for role in ROLES:
            if row[role] == NA:
                continue
            if role in LOYALS:
                num_games[LOYAL_SERVANT] += 1
            else:
                num_games[role] += 1
                
        if row[FAKE_PERCIVAL] == 'None':
            continue
        fakes = row[FAKE_PERCIVAL].split(', ')
                
        for fake in fakes:
            for role in ROLES:
                if row[role] == fake:
                    if role in LOYALS:
                        num_fake_claims[LOYAL_SERVANT] += 1
                    else:
                        num_fake_claims[role] += 1
                        
    df = pd.DataFrame(
        [
            (
                role,
                num_fake_claims[role] / num_games[role],
                num_games[role],
                num_fake_claims[role]
            ) for role in num_games if role != PERCIVAL
        ],
        columns=["Role", "Fake Percival Claim %", "Sample Size", "# Fake Claims"]
    ).set_index("Role")
    
    df["Fake Percival Claim %"] = df["Fake Percival Claim %"].apply(lambda x: np.round(x, rounding))
    
    return df.reset_index()
    
def wrong_assassination_player(thresh=SAMPLE_THRESH, df=None):
    """
    As a non-Merlin good guy, find how often each player is incorrectly assassinated.
    thresh : int
        minimum number of good guy games
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
        
    num_games = defaultdict(int)
    num_assassinations = defaultdict(int)
    for idx, row in df.iterrows():
        if row[ASSASSINATION] in [UNK, NA]:
            continue
        if row[WINNER] != GOOD:
            continue
        for role in ROLES:
            if role in BADS or role == MERLIN:
                continue
            if row[role] in [UNK, NA]:
                continue
            num_games[row[role]] += 1
            
        if row[MERLIN] != row[ASSASSINATION]:
            num_assassinations[row[ASSASSINATION]] += 1
            
    return pd.DataFrame(
        [
            (
                player, 
                num_assassinations[player] / num_games[player], 
                num_assassinations[player], 
                num_games[player]
            ) for player in num_games if num_games[player] >= thresh
        ],
        columns=["Player", "Incorrect Assassination %", "# Assassinations", "Sample Size"]
    ).sort_values("Incorrect Assassination %", ascending=False)

def correct_assassination_player(thresh=SAMPLE_THRESH, df=None):
    """
    As Merlin, find how often each player is assassinated.
    thresh : int
        minimum number of Merlin games
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
        
    num_games = defaultdict(int)
    num_assassinations = defaultdict(int)
    for idx, row in df.iterrows():
        merlin = row[MERLIN]
        if merlin in [NA, UNK]:
            continue
            
        num_games[merlin] += 1
        if row[ASSASSINATION] == merlin:
            num_assassinations[merlin] += 1
            
    return pd.DataFrame(
        [
            (
                player, 
                num_assassinations[player] / num_games[player], 
                num_assassinations[player], 
                num_games[player]
            ) for player in num_games if num_games[player] >= thresh
        ],
        columns=["Player", "Assassination %", "# Assassinations", "Sample Size"]
    ).sort_values("Assassination %")

def merlin_assassination_breakdown(df=None):
    """
    Compute % of games which reach assassination phase that end in correct assassination, by game size.
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    
    num_games = defaultdict(int) # num games reaching assassination phase
    num_assassinations = defaultdict(int)
    for idx, row in df.iterrows():
        if row[ASSASSINATION] in [UNK, NA]: # filtering NA accounts for cases where bad won on missions
            continue
        num_games[row[NUM_PLAYERS]] += 1
        if row[WINNER] == BAD:
            num_assassinations[row[NUM_PLAYERS]] += 1
    
    return pd.DataFrame(
        [
            (
                num_players,
                num_assassinations[num_players] / num_games[num_players],
                num_assassinations[num_players],
                num_games[num_players]
            ) for num_players in num_games
        ],
        columns=["# Players", "Assassination %", "# Assassinations", "Sample Size"]
    ).sort_values("# Players")

def merlin_assassination_breakdown_percival(df=None):
    """
    Compute % of games which reach assassination phase that end in correct assassination, by game size and # percival claims.
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
    """
    if df is None:
        df = fetch_game_log(parse_cols=True)
    
    num_games = defaultdict(lambda: defaultdict(int)) # num games reaching assassination phase
    num_assassinations = defaultdict(lambda: defaultdict(int))
    num_percivals = set()
    for idx, row in df.iterrows():
        if row[ASSASSINATION] in [UNK, NA]: # filtering NA accounts for cases where bad won on missions
            continue
        num_games[row[NUM_PLAYERS]][row[NUM_PERCIVAL]] += 1
        if row[WINNER] == BAD:
            num_assassinations[row[NUM_PLAYERS]][row[NUM_PERCIVAL]] += 1
        num_percivals.add(row[NUM_PERCIVAL])
    
    df = []
    for num_players in num_games:
        for num_percival in num_percivals:
            if not num_games[num_players][num_percival]:
                continue
            df.append(
                (
                    num_players,
                    num_percival,
                    num_assassinations[num_players][num_percival] / num_games[num_players][num_percival],
                    num_assassinations[num_players][num_percival],
                    num_games[num_players][num_percival]   
                )
            )
    
    return pd.DataFrame(df, columns=["# Players", "# Percival Claims", "Assassination %", "# Assassinations", "Sample Size"]) \
               .set_index(["# Players", "# Percival Claims"]) \
               .sort_index() \
               .reset_index()