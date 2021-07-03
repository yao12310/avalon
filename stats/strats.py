"""
Methods for evaluating strategies / analyses.
"""

import sys

from collections import defaultdict
from itertools import product

import numpy as np
import pandas as pd

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.strats':
    from ..utils.constants import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *


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
