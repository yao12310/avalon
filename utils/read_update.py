"""
Utilities for writing to README.md file (updating with stats/figures).
"""

import sys

from shutil import copyfile

import tabulate

# hack, but needed for testing in jupyter
if __name__ == 'avalon.utils.read_update':
    from ..utils.constants import *
    from ..stats.aggregates import *
    from ..stats.assassinations import *
    from ..stats.leaderboards import *
    from ..stats.missions import *
    from ..stats.percival import *
    from ..stats.player_pairs import *
    from ..stats.players import *
    from ..stats.strats import *
    from ..utils.sheets import *
else:
    sys.path.append('..')
    from utils.constants import *
    from stats.aggregates import *
    from stats.assassinations import *
    from stats.leaderboards import *
    from stats.missions import *
    from stats.percival import *
    from stats.player_pairs import *
    from stats.players import *
    from stats.strats import *
    from utils.sheets import fetch_game_log

def write_stats():
    copyfile(README_DEFAULT, README)
    game_log = fetch_game_log(parse_cols=True)
    game_log_competitive = game_log[game_log[NON_COMPETITIVE] == 'No']
    
    with open(README, 'a') as f:
        f.write("## Table of Contents\n")
        f.write("1. [Good win %](#good-win)\n")
        f.write("2. [Mean and SD game length by winning team](#game-length)\n")
        f.write("3. [Number of carries by player](#carries)\n")
        f.write("4. [Win rate leaderboard](#win-rate-leaderboard)\n")
        f.write("5. [Win rate over expected value leaderboard](#eev-leaderboard)\n")
        f.write("6. [Win rate leaderboard by role](#role-win-rates)\n")
        f.write("7. [Games played ranking](#games-played)\n")
        f.write("8. [Percentage good ranking](#good-percentage)\n")
        f.write("9. [Player/role counts/percentages](#player-role-cnts-pcts)\n")
        f.write("10. [Percentage of times two players are on the same team](#pair-teams-pct)\n")
        f.write("11. [Percentage of times two players are both bad](#pair-bad-team-pct)\n")        
        f.write("12. [Percentage of times two players are on different teams](#pair-opp-teams-pct)\n")
        f.write("13. [Count of times two players are on the same team](#pair-teams-cnt)\n")
        f.write("14. [Count of times two players are both bad](#pair-bad-team-cnt)\n")        
        f.write("15. [Count of times two players are on different teams](#pair-opp-teams-cnt)\n")
        f.write("16. [Percentage of times two players win, given that they are on the same team](#pair-teams-win-pct)\n")
        f.write("17. [Percentage of times two players win, given that they are both bad](#pair-bad-team-win-pct)\n")        
        f.write("18. [Percentage of times two players win, given that they are on opposite teams](#pair-opp-teams-win-pct)\n")
        f.write("19. [3+1 vs 2+2 strategy success rate](#mission2)\n")
        f.write("20. [Good win rate w.r.t. R1 fail](#r1-fail)\n")
        f.write("21. [Flip statistics for different # bad guys and mission index](#flip-stats)\n")
        f.write("22. [Good win % w.r.t. # Percival claims](#good-win-num-percival)\n")
        f.write("23. [Percentage of time each role fake claims Percival](#role-fake-percival)\n")
        f.write("24. [% of time players are wrongly assassinated as non-Merlin good guy](#wrongly-assassinated)\n")
        f.write("25. [% of time players are correctly assassinated as Merlin](#correctly-assassinated)\n")
        f.write("26. [% of time Merlin is assassinated by game size](#assassination-game-size)\n")        
        f.write("27. [% of time Merlin is assassinated by game size and # Percival claims](#assassination-game-size-percival)\n")
        f.write("28. [Mission success/fail sequence counts](#pass-fail-sequences)\n")
        
        f.write("## Stats\n")
        
        f.write("\n")
        f.write("Note: The friends and memories made in this game far outweigh any statistic you will find on this page. ")
        f.write("In any case, most of these stats are super high variance: especially individual stats, which depend heavily on team composition.")
        f.write("\n")
        
        f.write("\n")
        f.write('### <a id="good-win"></a>Good win %\n')
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
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")        
        df = good_win_rates_n_players(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="game-length"></a>Mean and SD game length by winning team\n')
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = win_lengths(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = win_lengths(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="carries"></a>Number of carries by player\n')
        f.write("\n")  
        df = carries(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="win-rate-leaderboard"></a>Win rate leaderboard (minimum 5 games)\n')
        f.write("\n")
        f.write("\n*Competitive games only statistic.*")
        f.write("\n")
        f.write("\n")
        f.write("*Games Behind column reports # games needed to win in a row in order to pass leader.*\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = top_win_rates(False, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = top_win_rates(True, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)\n')
        f.write("\n")
        f.write("\n*Competitive games only statistic.*")
        f.write("\n")
        f.write("\n")
        f.write("*Expected value computed based on good/bad % for different game sizes.*\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = win_pct_over_ev_rank(ex_ch=False, n=-1, df=game_log_competitive)
        df = df[df["Win % Over Expected"] > .01]
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = win_pct_over_ev_rank(ex_ch=True, n=-1, df=game_log_competitive)
        df = df[df["Win % Over Expected"] > .01]
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)\n')
        f.write("\n")
        f.write("\n*Competitive games only statistic. Oberon and Minion games excluded.*")
        f.write("\n")
        f.write("\n*Cheesy wins included.*")
        f.write("\n")
        f.write("\n")
        for role in ROLES + [LOYAL_SERVANT]:
            if role in [OBERON, MINION] + LOYALS:
                continue
            df = top_win_rates_role(role, df=game_log_competitive)
            f.write("\n")
            f.write("*{}:*\n".format(role))
            f.write("\n")
            f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write("\n*Cheesy wins excluded.*")
        f.write("\n")
        f.write("\n")
        for role in ROLES + [LOYAL_SERVANT]:
            if role in [OBERON, MINION] + LOYALS:
                continue
            df = top_win_rates_role(role, ex_ch=True, df=game_log_competitive)
            f.write("\n")
            f.write("*{}:*\n".format(role))
            f.write("\n")
            f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="games-played"></a>Games played ranking (minimum 5 games)\n')
        f.write("\n")  
        df = games_played_rank(thresh=SAMPLE_THRESH, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)\n')
        f.write("**Percentage good ranking (minimum 5 games):**\n")
        f.write("\n")  
        df = good_pct_rank(thresh=SAMPLE_THRESH, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
            
        f.write("\n")
        f.write('### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)\n')
        f.write("\n")
        f.write("Total count:\n")
        f.write("\n")  
        df = player_cnts_all_roles(norm_axis=-1, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Normalized by role (i.e. divided by occcurrences for each role):\n")
        f.write("\n")
        f.write("*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*\n")
        f.write("\n")
        df = player_cnts_all_roles(norm_axis=0, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Normalized by player (i.e. divided by games played for each player):\n")
        f.write("\n")
        f.write("*Row values should sum to 1.*\n")
        f.write("\n")
        df = player_cnts_all_roles(norm_axis=1, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)\n')
        f.write("\n")
        df = player_pair_pcts(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)\n')
        f.write("**Percentage of times two players are both bad (minimum 5 games both played, else -1):**\n")
        f.write("\n")
        df = player_pair_pcts(bad=True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)\n')
        f.write("**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**\n")
        f.write("\n")
        df = player_pair_opp_pcts(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-teams-cnt"></a>Count of times two players are on the same team\n')
        f.write("\n")
        df = player_pair_cnts(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad\n')
        f.write("\n")
        df = player_pair_cnts(bad=True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams\n')
        f.write("\n")
        df = player_pair_opp_cnts(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)\n')
        f.write("\n")
        f.write("\n*Competitive games only statistic.*")
        f.write("\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = player_pair_win_pcts(ex_ch=False, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = player_pair_win_pcts(ex_ch=True, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)\n')
        f.write("\n")
        f.write("\n*Competitive games only statistic.*")
        f.write("\n")
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = player_pair_win_pcts(thresh=3, bad=True, ex_ch=False, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = player_pair_win_pcts(thresh=3, bad=True, ex_ch=True, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)\n')
        f.write("\n")
        f.write("\n*Win percentages are presented as row player vs column player.*")
        f.write("\n")
        f.write("\n*Competitive games only statistic.*")
        f.write("\n")        
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = player_pair_vs_win_pcts(ex_ch=False, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = player_pair_vs_win_pcts(ex_ch=True, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)\n')
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = r1_r2_strat(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = r1_r2_strat(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)\n')
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n")  
        df = r1_fail(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = r1_fail(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index\n')
        f.write("\n")
        f.write("\n*Excludes Oberon in 10-person games.*")
        df = flip_win_pcts([1, 2, 3], [2, 3])
        f.write("\n")
        f.write("\n")
        f.write("*Overall:*\n")
        f.write("\n")
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        for n in [2, 3]:
            for mission in [1, 2, 3]:
                df = flip_win_pcts([mission], [n], df=game_log)
                if df.empty:
                    continue
                f.write("\n")
                f.write("*{} bad guys on mission {}:*\n".format(n, mission))
                f.write("\n")
                f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
                
        f.write("\n")
        f.write('### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims\n')
        f.write("\n")
        f.write("Cheesy wins included:\n")
        f.write("\n") 
        df = good_win_rates_n_percivals(False, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        f.write("\n")
        f.write("Cheesy wins excluded:\n")
        f.write("\n")
        df = good_win_rates_n_percivals(True, df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival\n')
        f.write("\n")
        df = fake_percival_claim_pct(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)\n')
        f.write("\n")
        f.write("*Excludes games where Merlin assassination is unknown.*\n")
        f.write("\n")  
        df = wrong_assassination_player(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)\n')
        f.write("\n")
        f.write("\n*Competitive games only statistic.*")
        f.write("\n")
        f.write("\n")
        df = correct_assassination_player(thresh=3, df=game_log_competitive)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size\n')
        f.write("\n")  
        df = merlin_assassination_breakdown(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims\n')
        f.write("\n")  
        df = merlin_assassination_breakdown_percival(df=game_log)
        f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
        
        f.write("\n")
        f.write('### <a id="pass-fail-sequences"></a>Mission success/fail sequence counts\n')
        f.write("\n")  
        for seq_len in range(1, MAX_ROUNDS + 1):
            df = mission_patterns(seq_len, game_log)
            f.write("\n")
            f.write("*Lengths: {}*\n".format(seq_len))
            f.write("\n")
            f.write(tabulate.tabulate(df.values, df.columns, tablefmt="pipe").replace(':', '') + '\n')
