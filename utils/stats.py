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

def good_win_rate(ex_ch=False):
    """
    Compute overall win rate of good team.
    ex_ch : bool
        exclude cheesy wins
    return : float
    """
    df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    return df[GOOD_WIN].mean()
    
def good_win_rates_n_players(ex_ch=False):
    """
    Compute win rate of good team w.r.t. game size.
    return : pd.DataFrame
    """
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

def good_win_rates_n_percivals(ex_ch=False):
    """
    Compute win rate of good team w.r.t. number of percival claims
    ex_ch : bool
        exclude cheesy wins
    return : pd.DataFrame
    """
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

def win_lengths(ex_ch=False):
    """
    Compute mean/sd length of games won by good and bad teams.
    ex_ch : bool
        exclude cheesy wins
    return : pd.DataFrame
    """
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

def carries():
    """
    Compute number of times each player has carried.
    return : pd.DataFrame
    """
    fails_col = FAILS_ROUND.format(MAX_ROUNDS)
    
    df = fetch_game_log(parse_cols=True)
    df = df[~df[fails_col].isin([NA, UTD, 'None'])]
    df = df[[GAME_INDEX, fails_col]].groupby(fails_col).count()
    df = df.reset_index()
    df.columns = ["Player", "# Carries"]
    return df

def top_win_rates(ex_ch=False, n=5, thresh=5):
    """
    Compute win rate leaderboard.
    ex_ch : bool
        exclude cheesy wins
    n : int
        leaderboard size
    thresh : int
        minimum # games played
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
    
    df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    for idx, row in df.iterrows():
        for role in ROLES:
            player = row[role]
            if player == NA:
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

def kgt_stats(ex_ch=False):
    """
    Compute KGT-related win statistics.
    ex_ch : bool
        exclude cheesy wins
    return pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    """
    df = fetch_game_log(parse_cols=True)
    if ex_ch:
        df = df[~(df[CHEESY_WIN] == 'Yes')]
    
    df1 = df[[GAME_INDEX, WEAK_KGT_SUCCESS]][~df[WEAK_KGT_SUCCESS].isin([NA, UTD])] \
              .groupby(WEAK_KGT_SUCCESS) \
              .count() \
              .reset_index()
    df1.columns = ["Weak Success", "Count"]
    
    df2 = df[[GAME_INDEX, STRONG_KGT_SUCCESS]][~df[STRONG_KGT_SUCCESS].isin([NA, UTD])] \
              .groupby(STRONG_KGT_SUCCESS) \
              .count() \
              .reset_index()
    df2.columns = ["Strong Success", "Count"]    
    
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

def player_role_cnts(role):
    """
    Count number of times each player has had a given role.
    role : str
        role name
    return : pd.DataFrame
    """
    player_cnts = defaultdict(int)
    df = fetch_game_log(parse_cols=True)
    df = df[~df[role].isin([UNK, NA])]
    
    for idx, row in df.iterrows():
        player_cnts[row[role]] += 1
    
    df = pd.DataFrame(list(player_cnts.items()), columns=[role, "Count"])
    df = df.sort_values("Count", ascending=False)
    return df
