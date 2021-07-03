"""
General non-win rate-based player statistics.
"""

import sys

from collections import defaultdict
from itertools import product

import numpy as np
import pandas as pd

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.players':
    from ..utils.constants import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

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
