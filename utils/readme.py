"""
Utilities for writing to README.md file (updating with stats/figures).
"""

import sys

from shutil import copyfile

import tabulate

# hack, but needed for testing in jupyter
if __name__ == 'avalon.utils.readme':
    from .constants import *
    from .stats import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.stats import *

def write_stats():
    copyfile(README_DEFAULT, README)
    
    with open(README, 'a') as f:
        f.write("## Stats\n")

        f.write("\n")
        f.write("**Good win %:**\n")
        f.write("Cheesy wins included: {:.4f}\n".format(good_win_rate(False)))
        f.write("\n")
        f.write("Cheesy wins excluded: {:.4f}\n".format(good_win_rate(True)))

        f.write("\n")
        f.write("**Good win % w.r.t. # players:**\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")   
        df = good_win_rates_n_players(False)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")        
        df = good_win_rates_n_players(True)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Good win % w.r.t. # Percival claims:**\n")
        f.write("Cheesy wins included:\n")
        f.write("\n") 
        df = good_win_rates_n_percivals(False)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = good_win_rates_n_percivals(True)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Mean and SD game length by winning team:**\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = win_lengths(False)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = win_lengths(True)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Number of carries by player:**\n")
        f.write("\n")  
        df = carries()
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Win rate leaderboard (minimum 5 games):**\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = top_win_rates(False)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = top_win_rates(True)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Kate Good Theorem statistics:**\n")
        dfs = kgt_stats()
        for df in dfs:
            f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
            f.write("\n")
            
        f.write("\n")
        f.write("**Player/role counts:**\n")
        for role in ROLES:
            if role in LOYALS:
                continue
            df = player_role_cnts(role)
            f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
            f.write("\n")
        