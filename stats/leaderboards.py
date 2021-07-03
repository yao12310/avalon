"""
Win rate leaderboard methods.
"""

import sys

from collections import defaultdict
from itertools import product

import numpy as np
import pandas as pd

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.leaderboards':
    from ..utils.constants import *
    from ..utils.sheets import *
    from ..stats.aggregates import good_win_rates_n_players
    from ..stats.players import good_pct_rank
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

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

def top_win_rates_role(role, ex_ch=False, n=3, thresh=SAMPLE_THRESH, df=None):
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
