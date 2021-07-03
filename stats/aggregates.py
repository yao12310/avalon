"""
Aggregate game-level statistics.
"""

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.aggregates':
    from ..utils.constants import *
    from ..utils.sheets import *
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
