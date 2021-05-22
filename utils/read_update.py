"""
Utilities for writing to README.md file (updating with stats/figures).
"""

import sys

from shutil import copyfile

import tabulate

# hack, but needed for testing in jupyter
if __name__ == 'avalon.utils.read_update':
    from .constants import *
    from .stats import *
else:
    sys.path.append('..')
    from utils.constants import *
    from utils.stats import *
    from utils.sheets import fetch_game_log

def write_stats():
    copyfile(README_DEFAULT, README)
    game_log = fetch_game_log(parse_cols=True)
    
    with open(README, 'a') as f:
        f.write("## Stats\n")

        f.write("\n")
        f.write("**Good win %:**\n")
        f.write("\n")
        f.write("Cheesy wins included: {:.4f} (n = {})\n".format(*good_win_rate(False)))
        f.write("\n")
        f.write("Cheesy wins excluded: {:.4f} (n = {})\n".format(*good_win_rate(True)))

        f.write("\n")
        f.write("**Good win % w.r.t. # players:**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")   
        df = good_win_rates_n_players(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")        
        df = good_win_rates_n_players(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Good win % w.r.t. # Percival claims:**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n") 
        df = good_win_rates_n_percivals(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = good_win_rates_n_percivals(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Mean and SD game length by winning team:**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = win_lengths(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = win_lengths(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Number of carries by player:**\n")
        f.write("\n")  
        df = carries(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Win rate leaderboard (minimum 5 games):**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = top_win_rates(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = top_win_rates(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Kate Good Theorem statistics:**\n")
        dfs = kgt_stats()
        for df in dfs:
            f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
            f.write("\n")
            
        f.write("\n")
        f.write("**Player/role counts/percentages (minimum 5 games):**\n")
        f.write("\n")
        f.write("Total count:\n")
        f.write("\n")  
        df = player_cnts_all_roles(norm_axis=-1, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Normalized by role (i.e. divided by occcurrences for each role):\n")
        f.write("\n")
        df = player_cnts_all_roles(norm_axis=0, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Normalized by player (i.e. divided by games played for each player):\n")
        f.write("\n")
        df = player_cnts_all_roles(norm_axis=1, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Percentage of times two players are on the same team (minimum 5 games both played, else -1):**\n")
        f.write("\n")
        df = player_pair_pcts(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1):**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = player_pair_win_pcts(ex_ch=False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = player_pair_win_pcts(ex_ch=True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1):**\n")
        f.write("\n")
        f.write("\n*Win percentages are presented as row player vs column player.*")
        f.write("\n")        
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = player_pair_vs_win_pcts(ex_ch=False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = player_pair_vs_win_pcts(ex_ch=True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**3+1 vs 2+1 strategy success rate:**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = r1_r2_strat(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = r1_r2_strat(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        
        f.write("\n")
        f.write("**Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1):**\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = r1_fail(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = r1_fail(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        