"""
Mission pass/fail statistics.
"""

import sys

from itertools import product

# hack, but needed for testing in jupyter
if __name__ == 'avalon.stats.missions':
    from ..utils.constants import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.sheets import *

def mission_patterns(n, df=None):
    """
    For a given number of missions, find the number of 
    times each possible pattern of successes/fails has occurred
    n : int
        length of sequence
    df : pd.DataFrame
        game data log (if None, fetch from API)
    return : pd.DataFrame
        mapping of sequence to count, frequency
    """
    def valid_seq(seq):
        """
        Determine if a sequence is valid (according to first-to-3)
        seq : []str
            sequence of mission outcomes
        return : bool
        """
        subseq = seq[:-1]
        if subseq.count(SUCCESS) >= 3 or subseq.count(FAIL) >= 3:
            return False
        else:
            return True
    
    if df is None:
        df = fetch_game_log(parse_cols=True)
    
    poss = list(filter(valid_seq, product([SUCCESS, FAIL], repeat=n)))
    counts = {seq: 0 for seq in poss}
    good_wins = {seq: 0 for seq in poss}
    for idx, row in df.iterrows():
        curr_seq = []
        for mission in range(1, n + 1):
            fails = row[FAILS_ROUND.format(mission)]
            double_fail_req = len(fails.split(', ')) == 1 and R4_DOUBLE_FAIL_REQ[row[NUM_PLAYERS]]
            if fails == NA or fails == UTD:
                break
            elif fails == NONE or (mission == 4 and double_fail_req):
                curr_seq.append(SUCCESS)
            else:
                curr_seq.append(FAIL)
        if len(curr_seq) == n:
            try:
                counts[tuple(curr_seq)] += 1
                if row[WINNER] == GOOD:
                    good_wins[tuple(curr_seq)] += 1
            except KeyError: # bad sequence due to incorrect game data
                continue
    
    return pd.DataFrame(
        [
            (
                ', '.join(seq),
                counts[seq],
                counts[seq] / sum(counts.values()),
                good_wins[seq] / counts[seq] if counts[seq] else NA
            ) for seq in counts
        ],
        columns=["Sequence", "Count", "Frequency", "Good Win %"]
    )
