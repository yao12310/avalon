"""
Percival-related statistics.
"""

import sys

from collections import defaultdict
from itertools import product

import numpy as np
import pandas as pd

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.percival':
    from ..utils.constants import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

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