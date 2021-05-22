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
        f.write("Note: The friends and memories made in this game far outweigh any statistic you will find on this page.")
        f.write("In any case, most of these stats are super high variance—especially individual stats, which depend heavily on team composition.")
        f.write("\n")
        
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
        f.write("**Games played ranking (minimum 5 games):**\n")
        f.write("\n")  
        df = games_played_rank(thresh=SAMPLE_THRESH, df=game_log)
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
        f.write("*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*\n")
        f.write("\n")
        df = player_cnts_all_roles(norm_axis=0, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        f.write("\n")
        f.write("Normalized by player (i.e. divided by games played for each player):\n")
        f.write("\n")
        f.write("*Row values should sum to 1.*\n")
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
        
        f.write("\n")
        f.write("**Flip statistics for different # bad guys and mission index:**\n")
        f.write("\n")
        f.write("\n*Excludes Oberon in 10-person games.*")
        df = flip_win_pcts([1, 2, 3], [2, 3])
        f.write("\n")
        f.write("*Overall:*\n")
        f.write("\n")
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
        for n in [2, 3]:
            for mission in [1, 2, 3]:
                df = flip_win_pcts([mission], [n], df=game_log)
                if df.empty:
                    continue
                f.write("\n")
                f.write("*{} bad guys on mission {}:*\n".format(n, mission))
                f.write("\n")
                f.write(tabulate.tabulate(df.values, df.columns, tablefmt="github") + '\n')
                