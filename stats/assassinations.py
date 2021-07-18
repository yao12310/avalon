"""
Assassination statistics.
"""

import sys

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.assassinations':
    from ..utils.constants import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

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
        if row[ASSASSINATION] == NA: # discount games where assassination was not reached
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
