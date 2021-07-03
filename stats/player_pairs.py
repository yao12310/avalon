"""
Player pair (same team, win rate, opposing, etc.) methods.
"""

import sys

from collections import defaultdict
from itertools import product

import numpy as np
import pandas as pd

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.player_pairs':
    from ..utils.constants import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

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
