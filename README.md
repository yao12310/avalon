# Avalon
SAAS Avalon analysis code

## Usage

Setup:
```
pip install gspread oauth2client tabulate
git clone https://github.com/yao12310/avalon.git
mkdir avalon/keys
mkdir avalon/data
mv path/to/key/client.json avalon/keys/
```

Updating DB:
```
python -m avalon.main db_write --row {equals sign-separated list of values, optional} --player_write {True/False, optional, default=True}
```

If `--row` is excluded, then the script will prompt you to enter each value one-by-one. (Recommended method.)

Updating README Stats:
```
python -m avalon.main update_stat
```
## Table of Contents
1. [Good win %](#good-win)
2. [Mean and SD game length by winning team](#game-length)
3. [Number of carries by player](#carries)
4. [Win rate leaderboard](#win-rate-leaderboard)
5. [Win rate over expected value leaderboard](#eev-leaderboard)
6. [Win rate leaderboard by role](#role-win-rates)
7. [Games played ranking](#games-played)
8. [Percentage good ranking](#good-percentage)
9. [Kate Good Theorem statistics](#kgt-stats)
10. [Player/role counts/percentages](#player-role-cnts-pcts)
11. [Percentage of times two players are on the same team](#pair-teams-pct)
12. [Percentage of times two players are both bad](#pair-bad-team-pct)
13. [Percentage of times two players are on different teams](#pair-opp-teams-pct)
14. [Count of times two players are on the same team](#pair-teams-cnt)
15. [Count of times two players are both bad](#pair-bad-team-cnt)
16. [Count of times two players are on different teams](#pair-opp-teams-cnt)
17. [Percentage of times two players win, given that they are on the same team](#pair-teams-win-pct)
18. [Percentage of times two players win, given that they are both bad](#pair-bad-team-win-pct)
19. [Percentage of times two players win, given that they are on opposite teams](#pair-opp-teams-win-pct)
20. [3+1 vs 2+2 strategy success rate](#mission2)
21. [Good win rate w.r.t. R1 fail](#r1-fail)
22. [Flip statistics for different # bad guys and mission index](#flip-stats)
23. [Good win % w.r.t. # Percival claims](#good-win-num-percival)
24. [Percentage of time each role fake claims Percival](#role-fake-percival)
25. [% of time players are wrongly assassinated as non-Merlin good guy](#wrongly-assassinated)
26. [% of time players are correctly assassinated as Merlin](#correctly-assassinated)
27. [% of time Merlin is assassinated by game size](#assassination-game-size)
28. [% of time Merlin is assassinated by game size and # Percival claims](#assassination-game-size-percival)
## Stats

Note: The friends and memories made in this game far outweigh any statistic you will find on this page. In any case, most of these stats are super high variance—especially individual stats, which depend heavily on team composition.

### <a id="good-win"></a>Good win %

Cheesy wins included: 0.4058 (n = 138)

Cheesy wins excluded: 0.3692 (n = 130)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            24 |     0.416667 |
| 5           |             4 |     0.25     |
| 5O          |             2 |     0.5      |
| 6           |            14 |     0.571429 |
| 6M          |             3 |     1        |
| 6O          |             3 |     0.666667 |
| 7           |            20 |     0.5      |
| 7O          |             3 |     0.333333 |
| 8           |            29 |     0.310345 |
| 8O          |             3 |     0        |
| 9           |            31 |     0.322581 |
| 9O          |             2 |     0.5      |

Cheesy wins excluded:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            23 |     0.391304 |
| 5           |             4 |     0.25     |
| 5O          |             2 |     0.5      |
| 6           |            13 |     0.538462 |
| 6M          |             3 |     1        |
| 6O          |             3 |     0.666667 |
| 7           |            17 |     0.411765 |
| 7O          |             3 |     0.333333 |
| 8           |            29 |     0.310345 |
| 8O          |             3 |     0        |
| 9           |            28 |     0.25     |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            67 |       32.6716 |     21.3715 |
| Good     |            44 |       23.6364 |     17.5368 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            67 |       32.6716 |     21.3715 |
| Good     |            40 |       25.125  |     17.7203 |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|----------|-------------|
| Kate     |           5 |
| Abishek  |           4 |
| Peter    |           4 |
| Brian    |           2 |
| Minh     |           1 |
| Rachel   |           1 |
| Sachin   |           1 |
| Sushant  |           1 |

### <a id="win-rate-leaderboard"></a>Win rate leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Games Behind column reports # games needed to win in a row in order to pass leader.*

Cheesy wins included:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|--------------|-------------|---------------|--------|----------|------------------------|
| Abishek  | 0.607843 |     0.508475 |    0.744186 |           102 |     62 |       40 |                      0 |
| Brian    | 0.561905 |     0.464789 |    0.764706 |           105 |     59 |       46 |                     13 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                      4 |
| Kate     | 0.528736 |     0.464286 |    0.645161 |            87 |     46 |       41 |                     18 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|----------|----------|--------------|-------------|---------------|--------|----------|------------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.589474 |     0.45283  |    0.761905 |            95 |     56 |       39 |                      3 |
| Brian    | 0.540816 |     0.415385 |    0.787879 |            98 |     53 |       45 |                     15 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kate     | 0.506173 |     0.411765 |    0.666667 |            81 |     41 |       40 |                     20 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Abishek  |             0.0950034 | 0.607843 |         0.51284  | 0.578431 |
| Kish     |             0.0918311 | 0.529412 |         0.437581 | 0.588235 |
| Brian    |             0.0893898 | 0.561905 |         0.472515 | 0.67619  |
| Kate     |             0.0472752 | 0.528736 |         0.48146  | 0.643678 |
| Ewen     |             0.0351392 | 0.538462 |         0.503322 | 0.615385 |
| Anthony  |             0.0218855 | 0.5      |         0.478114 | 0.166667 |
| Jackie   |             0.0114822 | 0.448276 |         0.436794 | 0.741379 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Anthony  |             0.0943723 | 0.6      |         0.505628 | 0.166667 |
| Abishek  |             0.0852862 | 0.589474 |         0.504188 | 0.578431 |
| Brian    |             0.0810434 | 0.540816 |         0.459773 | 0.67619  |
| Ewen     |             0.0566769 | 0.538462 |         0.481785 | 0.615385 |
| Kish     |             0.0393385 | 0.5      |         0.460662 | 0.588235 |
| Kate     |             0.0338277 | 0.506173 |         0.472345 | 0.643678 |
| Jade     |             0.0143121 | 0.333333 |         0.319021 | 1        |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|---------|---------------|--------|----------|----------------------|
| Brian    |     0.6 |            10 |      6 |        4 |                    0 |
| Kate     |     0.6 |            10 |      6 |        4 |                    1 |
| Minh     |     0.5 |             6 |      3 |        3 |                    2 |

*Percival:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|---------|---------------|--------|----------|-----------------------|
| Jackie   |   0.625 |             8 |      5 |        3 |                     0 |
| Kate     |   0.6   |            10 |      6 |        4 |                     1 |
| Sushant  |   0.6   |             5 |      3 |        2 |                     1 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.75     |            12 |      9 |        3 |                      0 |
| Brian    | 0.7      |            10 |      7 |        3 |                      3 |
| Sushant  | 0.666667 |            12 |      8 |        4 |                      5 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Brian    | 0.733333 |            15 |     11 |        4 |                     14 |
| Kate     | 0.666667 |             9 |      6 |        3 |                     13 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 1        |             9 |      9 |        0 |                   0 |
| Brian    | 1        |             8 |      8 |        0 |                 nan |
| Peter    | 0.857143 |             7 |      6 |        1 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.633333 |            30 |     19 |       11 |                      0 |
| Ruhi     | 0.5      |            12 |      6 |        6 |                      5 |
| Rachel   | 0.448276 |            29 |     13 |       16 |                     15 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 0.6      |            10 |      6 |        4 |                   0 |
| Brian    | 0.555556 |             9 |      5 |        4 |                   2 |
| Sushant  | 0.428571 |            14 |      6 |        8 |                   7 |

*Percival:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|---------|---------------|--------|----------|-----------------------|
| Jackie   |   0.625 |             8 |      5 |        3 |                     0 |
| Sushant  |   0.6   |             5 |      3 |        2 |                     1 |
| Kate     |   0.5   |             8 |      4 |        4 |                     3 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.818182 |            11 |      9 |        2 |                      0 |
| Sushant  | 0.727273 |            11 |      8 |        3 |                      6 |
| Brian    | 0.7      |            10 |      7 |        3 |                      7 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Brian    | 0.785714 |            14 |     11 |        3 |                      8 |
| Kate     | 0.666667 |             9 |      6 |        3 |                     13 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 1        |             9 |      9 |        0 |                   0 |
| Brian    | 1        |             8 |      8 |        0 |                 nan |
| Peter    | 0.857143 |             7 |      6 |        1 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.56     |            25 |     14 |       11 |                      0 |
| Rachel   | 0.407407 |            27 |     11 |       16 |                     10 |
| Ruhi     | 0.4      |            10 |      4 |        6 |                      4 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|----------|----------------|
| Brian    |            124 |
| Abishek  |            116 |
| Peter    |            105 |
| Kate     |            104 |
| Sushant  |             98 |
| Rachel   |             85 |
| Jackie   |             82 |
| Alex     |             82 |
| Jai      |             51 |
| Minh     |             49 |
| Ruhi     |             35 |
| Jay      |             19 |
| Kish     |             17 |
| Jeron    |             17 |
| Ewen     |             13 |
| Jade     |             13 |
| Justin   |              9 |
| Sai      |              8 |
| Gathenji |              7 |
| Anthony  |              6 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|----------|----------|----------|---------|
| Gathenji | 0.857143 |        6 |       1 |
| Jade     | 0.769231 |       10 |       3 |
| Jackie   | 0.743902 |       61 |      21 |
| Jeron    | 0.705882 |       12 |       5 |
| Rachel   | 0.694118 |       59 |      26 |
| Justin   | 0.666667 |        6 |       3 |
| Kate     | 0.653846 |       68 |      36 |
| Jai      | 0.647059 |       33 |      18 |
| Alex     | 0.646341 |       53 |      29 |
| Brian    | 0.645161 |       80 |      44 |
| Jay      | 0.631579 |       12 |       7 |
| Sai      | 0.625    |        5 |       3 |
| Ewen     | 0.615385 |        8 |       5 |
| Peter    | 0.6      |       63 |      42 |
| Kish     | 0.588235 |       10 |       7 |
| Abishek  | 0.586207 |       68 |      48 |
| Sushant  | 0.571429 |       56 |      42 |
| Minh     | 0.530612 |       26 |      23 |
| Ruhi     | 0.485714 |       17 |      18 |
| Anthony  | 0.166667 |        1 |       5 |

### <a id="kgt-stats"></a>Kate Good Theorem statistics
| Weak Success   |   Count |   Good Win % |
|----------------|---------|--------------|
| No             |       3 |            0 |
| Yes            |       7 |            0 |

| Strong Success   |   Count |   Good Win % |
|------------------|---------|--------------|
| No               |       4 |            0 |
| Yes              |       6 |            0 |

| Weak KGT Applied   |   Sample Size |   Good Win % |
|--------------------|---------------|--------------|
| No                 |           124 |     0.435484 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           124 |     0.435484 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       15 |         19 |         14 |        15 |         6 |        7 |           6 |              34 |           116 |
| Alex     |        8 |         13 |         12 |        11 |         4 |        1 |           1 |              32 |            82 |
| Anthony  |        0 |          1 |          3 |         2 |         0 |        0 |           0 |               0 |             6 |
| Brian    |       12 |         20 |         11 |        22 |        10 |        0 |           1 |              48 |           124 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       14 |         11 |          5 |         7 |         4 |        4 |           1 |              36 |            82 |
| Jade     |        3 |          1 |          0 |         1 |         1 |        1 |           0 |               6 |            13 |
| Jai      |        7 |          4 |          5 |         5 |         5 |        3 |           0 |              22 |            51 |
| Jay      |        3 |          3 |          3 |         0 |         3 |        1 |           0 |               6 |            19 |
| Jeron    |        3 |          7 |          1 |         2 |         1 |        1 |           0 |               2 |            17 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       11 |         11 |          8 |        10 |         9 |        7 |           2 |              46 |           104 |
| Kish     |        1 |          3 |          1 |         3 |         2 |        0 |           1 |               6 |            17 |
| Minh     |        6 |          4 |         10 |         5 |         5 |        1 |           2 |              16 |            49 |
| Peter    |       16 |         12 |         16 |        12 |         8 |        4 |           2 |              35 |           105 |
| Rachel   |       15 |         11 |          8 |         8 |         9 |        0 |           1 |              33 |            85 |
| Ruhi     |        1 |          4 |          4 |         7 |         6 |        1 |           0 |              12 |            35 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       15 |          6 |         13 |        17 |         8 |        2 |           2 |              35 |            98 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.111 |      0.14  |      0.116 |     0.113 |     0.07  |    0.189 |       0.316 |           0.085 |           116 |
| Alex     |    0.059 |      0.096 |      0.099 |     0.083 |     0.047 |    0.027 |       0.053 |           0.08  |            82 |
| Anthony  |    0     |      0.007 |      0.025 |     0.015 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.089 |      0.147 |      0.091 |     0.165 |     0.116 |    0     |       0.053 |           0.12  |           124 |
| Ewen     |    0.007 |      0.015 |      0.017 |     0.008 |     0     |    0.054 |       0     |           0.012 |            13 |
| Gathenji |    0     |      0     |      0     |     0.008 |     0     |    0     |       0     |           0.015 |             7 |
| Jackie   |    0.104 |      0.081 |      0.041 |     0.053 |     0.047 |    0.108 |       0.053 |           0.09  |            82 |
| Jade     |    0.022 |      0.007 |      0     |     0.008 |     0.012 |    0.027 |       0     |           0.015 |            13 |
| Jai      |    0.052 |      0.029 |      0.041 |     0.038 |     0.058 |    0.081 |       0     |           0.055 |            51 |
| Jay      |    0.022 |      0.022 |      0.025 |     0     |     0.035 |    0.027 |       0     |           0.015 |            19 |
| Jeron    |    0.022 |      0.051 |      0.008 |     0.015 |     0.012 |    0.027 |       0     |           0.005 |            17 |
| Justin   |    0.015 |      0     |      0.008 |     0.008 |     0.012 |    0     |       0     |           0.01  |             9 |
| Kate     |    0.081 |      0.081 |      0.066 |     0.075 |     0.105 |    0.189 |       0.105 |           0.115 |           104 |
| Kish     |    0.007 |      0.022 |      0.008 |     0.023 |     0.023 |    0     |       0.053 |           0.015 |            17 |
| Minh     |    0.044 |      0.029 |      0.083 |     0.038 |     0.058 |    0.027 |       0.105 |           0.04  |            49 |
| Peter    |    0.119 |      0.088 |      0.132 |     0.09  |     0.093 |    0.108 |       0.105 |           0.087 |           105 |
| Rachel   |    0.111 |      0.081 |      0.066 |     0.06  |     0.105 |    0     |       0.053 |           0.082 |            85 |
| Ruhi     |    0.007 |      0.029 |      0.033 |     0.053 |     0.07  |    0.027 |       0     |           0.03  |            35 |
| Sai      |    0.007 |      0.007 |      0     |     0.008 |     0.023 |    0     |       0     |           0.007 |             8 |
| Sushant  |    0.111 |      0.044 |      0.107 |     0.128 |     0.093 |    0.054 |       0.105 |           0.087 |            98 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.129 |      0.164 |      0.121 |     0.129 |     0.052 |    0.06  |       0.052 |           0.293 |           116 |
| Alex     |    0.098 |      0.159 |      0.146 |     0.134 |     0.049 |    0.012 |       0.012 |           0.39  |            82 |
| Anthony  |    0     |      0.167 |      0.5   |     0.333 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.097 |      0.161 |      0.089 |     0.177 |     0.081 |    0     |       0.008 |           0.387 |           124 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.171 |      0.134 |      0.061 |     0.085 |     0.049 |    0.049 |       0.012 |           0.439 |            82 |
| Jade     |    0.231 |      0.077 |      0     |     0.077 |     0.077 |    0.077 |       0     |           0.462 |            13 |
| Jai      |    0.137 |      0.078 |      0.098 |     0.098 |     0.098 |    0.059 |       0     |           0.431 |            51 |
| Jay      |    0.158 |      0.158 |      0.158 |     0     |     0.158 |    0.053 |       0     |           0.316 |            19 |
| Jeron    |    0.176 |      0.412 |      0.059 |     0.118 |     0.059 |    0.059 |       0     |           0.118 |            17 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.106 |      0.106 |      0.077 |     0.096 |     0.087 |    0.067 |       0.019 |           0.442 |           104 |
| Kish     |    0.059 |      0.176 |      0.059 |     0.176 |     0.118 |    0     |       0.059 |           0.353 |            17 |
| Minh     |    0.122 |      0.082 |      0.204 |     0.102 |     0.102 |    0.02  |       0.041 |           0.327 |            49 |
| Peter    |    0.152 |      0.114 |      0.152 |     0.114 |     0.076 |    0.038 |       0.019 |           0.333 |           105 |
| Rachel   |    0.176 |      0.129 |      0.094 |     0.094 |     0.106 |    0     |       0.012 |           0.388 |            85 |
| Ruhi     |    0.029 |      0.114 |      0.114 |     0.2   |     0.171 |    0.029 |       0     |           0.343 |            35 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.153 |      0.061 |      0.133 |     0.173 |     0.082 |    0.02  |       0.02  |           0.357 |            98 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.45 |    0.46 |      0.33 |   0.36 |  0.62 |     0.52 |   0.48 |      0.46 |      0.36 |   0.35 |   0.58 |   0.56 |    0.9  |     0.57 |   0.75 |  0.62 |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.45 |   0.17 |    1    |    0.53 |     -1    |   0.38 |  0.44 |     0.49 |   0.36 |      0.51 |      0.46 |   0.5  |   0.62 |   0.43 |    0.36 |     0.78 |   0.7  |  0.69 |      -1    |  0.29 |
| Brian    |     0.46 |   0.83 |    0.53 |    1    |      0.33 |   0.37 |  0.51 |     0.53 |   0.52 |      0.41 |      0.5  |   0.35 |   0.35 |   0.48 |    0.6  |     0.44 |   0.6  |  0.2  |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |      1    |   0.5  | -1    |    -1    |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.36 |   0.4  |    0.38 |    0.37 |      0.5  |   1    |  0.5  |     0.44 |   0.46 |      0.6  |      0.55 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.62 |   0.4  |    0.44 |    0.51 |     -1    |   0.5  |  1    |     0.5  |   0.61 |      0.35 |      0.42 |   0.23 |  -1    |   0.53 |   -1    |    -1    |   0.4  |  0.29 |       0.8  | -1    |
| Jackie   |     0.52 |   0.33 |    0.49 |    0.53 |     -1    |   0.44 |  0.5  |     1    |   0.54 |      0.48 |      0.43 |   0.38 |   0.43 |   0.58 |    0.64 |    -1    |   0.29 |  0.62 |      -1    |  0.4  |
| Kate     |     0.48 |   0.45 |    0.36 |    0.52 |      0.33 |   0.46 |  0.61 |     0.54 |   1    |      0.44 |      0.5  |   0.41 |   0.29 |   0.44 |    0.78 |     0.83 |   0.4  |  0.33 |       0.57 |  0.5  |
| Sushant  |     0.46 |   0.43 |    0.51 |    0.41 |     -1    |   0.6  |  0.35 |     0.48 |   0.44 |      1    |      0.48 |   0.48 |   0.5  |   0.44 |    0.27 |     0.17 |   0.5  |  0.53 |       0.5  |  0.38 |
| Abishek  |     0.36 |   0.56 |    0.46 |    0.5  |      0.2  |   0.55 |  0.42 |     0.43 |   0.5  |      0.48 |      1    |   0.44 |   0.46 |   0.45 |    0.13 |     0.38 |   0.67 |  0.53 |       0.29 |  0.62 |
| Ruhi     |     0.35 |  -1    |    0.5  |    0.35 |     -1    |   0.56 |  0.23 |     0.38 |   0.41 |      0.48 |      0.44 |   1    |   0.67 |   0.53 |    0.17 |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.58 |   0    |    0.62 |    0.35 |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.56 |   0.2  |    0.43 |    0.48 |     -1    |   0.32 |  0.53 |     0.58 |   0.44 |      0.44 |      0.45 |   0.53 |  -1    |   1    |    0.67 |     0.67 |   0.2  |  0.44 |       0.4  |  0.5  |
| Jeron    |     0.9  |  -1    |    0.36 |    0.6  |     -1    |   0.33 | -1    |     0.64 |   0.78 |      0.27 |      0.13 |   0.17 |  -1    |   0.67 |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.75 |  -1    |    0.7  |    0.6  |     -1    |   0    |  0.4  |     0.29 |   0.4  |      0.5  |      0.67 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.62 |  -1    |    0.69 |    0.2  |     -1    |  -1    |  0.29 |     0.62 |   0.33 |      0.53 |      0.53 |   0.57 |  -1    |   0.44 |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.06 |    0.06 |      0.33 |   0.12 |  0.13 |     0.06 |   0.09 |      0.11 |      0.06 |   0.1  |   0.17 |   0.12 |    0.1  |     0    |   0.12 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.06 |   0    |   -1    |    0.15 |     -1    |   0.16 |  0.14 |     0.06 |   0.05 |      0.17 |      0.16 |   0.2  |   0    |   0.07 |    0    |     0.11 |   0.2  |  0.31 |      -1    |  0    |
| Brian    |     0.06 |   0.25 |    0.15 |   -1    |      0.33 |   0.12 |  0.05 |     0.1  |   0.12 |      0.08 |      0.14 |   0.03 |   0.12 |   0.09 |    0.07 |     0    |   0    |  0    |       0    |  0.12 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |     -1    |   0.33 | -1    |    -1    |   0.17 |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.12 |   0.2  |    0.16 |    0.12 |      0.33 |  -1    |  0.14 |     0.03 |   0.15 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.13 |   0    |    0.14 |    0.05 |     -1    |   0.14 | -1    |     0.03 |   0.16 |      0.1  |      0.12 |   0.15 |  -1    |   0.16 |   -1    |    -1    |   0    |  0.14 |       0    | -1    |
| Jackie   |     0.06 |   0    |    0.06 |    0.1  |     -1    |   0.03 |  0.03 |    -1    |   0.07 |      0.09 |      0.07 |   0.08 |   0.29 |   0.08 |    0.18 |    -1    |   0    |  0    |      -1    |  0.2  |
| Kate     |     0.09 |   0.09 |    0.05 |    0.12 |      0.17 |   0.15 |  0.16 |     0.07 |  -1    |      0.12 |      0.12 |   0.11 |   0    |   0.1  |    0.22 |     0.33 |   0.1  |  0.06 |       0    |  0.12 |
| Sushant  |     0.11 |   0.14 |    0.17 |    0.08 |     -1    |   0.23 |  0.1  |     0.09 |   0.12 |     -1    |      0.17 |   0.21 |   0    |   0.11 |    0    |     0    |   0.1  |  0.16 |       0    |  0.12 |
| Abishek  |     0.06 |   0.11 |    0.16 |    0.14 |      0    |   0.12 |  0.12 |     0.07 |   0.12 |      0.17 |     -1    |   0.18 |   0.15 |   0.11 |    0    |     0.25 |   0    |  0.11 |       0    |  0.12 |
| Ruhi     |     0.1  |  -1    |    0.2  |    0.03 |     -1    |   0.22 |  0.15 |     0.08 |   0.11 |      0.21 |      0.18 |  -1    |   0.17 |   0.35 |    0    |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.17 |   0    |    0    |    0.12 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.12 |   0    |    0.07 |    0.09 |     -1    |   0.08 |  0.16 |     0.08 |   0.1  |      0.11 |      0.11 |   0.35 |  -1    |  -1    |    0.17 |     0    |   0    |  0.11 |       0    |  0.17 |
| Jeron    |     0.1  |  -1    |    0    |    0.07 |     -1    |   0.17 | -1    |     0.18 |   0.22 |      0    |      0    |   0    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.12 |  -1    |    0.2  |    0    |     -1    |   0    |  0    |     0    |   0.1  |      0.1  |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jay      |     0    |  -1    |    0.31 |    0    |     -1    |  -1    |  0.14 |     0    |   0.06 |      0.16 |      0.11 |   0.43 |  -1    |   0.11 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     0    |   0.5  |    0.55 |    0.54 |      0.67 |   0.64 |  0.38 |     0.48 |   0.52 |      0.54 |      0.64 |   0.65 |   0.42 |   0.44 |    0.1  |     0.43 |   0.25 |  0.38 |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.55 |   0.83 |    0    |    0.47 |     -1    |   0.62 |  0.56 |     0.51 |   0.64 |      0.49 |      0.54 |   0.5  |   0.38 |   0.57 |    0.64 |     0.22 |   0.3  |  0.31 |      -1    |  0.71 |
| Brian    |     0.54 |   0.17 |    0.47 |    0    |      0.67 |   0.63 |  0.49 |     0.47 |   0.48 |      0.59 |      0.5  |   0.65 |   0.65 |   0.52 |    0.4  |     0.56 |   0.4  |  0.8  |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |   -1    |    0.67 |      0    |   0.5  | -1    |    -1    |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.64 |   0.6  |    0.62 |    0.63 |      0.5  |   0    |  0.5  |     0.56 |   0.54 |      0.4  |      0.45 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   1    | -1    |      -1    | -1    |
| Jai      |     0.38 |   0.6  |    0.56 |    0.49 |     -1    |   0.5  |  0    |     0.5  |   0.39 |      0.65 |      0.57 |   0.77 |  -1    |   0.47 |   -1    |    -1    |   0.6  |  0.71 |       0.2  | -1    |
| Jackie   |     0.48 |   0.67 |    0.51 |    0.47 |     -1    |   0.56 |  0.5  |     0    |   0.46 |      0.52 |      0.57 |   0.62 |   0.57 |   0.42 |    0.36 |    -1    |   0.71 |  0.38 |      -1    |  0.6  |
| Kate     |     0.52 |   0.55 |    0.64 |    0.48 |      0.67 |   0.54 |  0.39 |     0.46 |   0    |      0.56 |      0.5  |   0.59 |   0.71 |   0.56 |    0.22 |     0.17 |   0.6  |  0.67 |       0.43 |  0.5  |
| Sushant  |     0.54 |   0.57 |    0.49 |    0.59 |     -1    |   0.4  |  0.65 |     0.52 |   0.56 |      0    |      0.52 |   0.52 |   0.5  |   0.56 |    0.73 |     0.83 |   0.5  |  0.47 |       0.5  |  0.62 |
| Abishek  |     0.64 |   0.44 |    0.54 |    0.5  |      0.8  |   0.45 |  0.57 |     0.57 |   0.5  |      0.52 |      0    |   0.56 |   0.54 |   0.55 |    0.87 |     0.62 |   0.33 |  0.47 |       0.71 |  0.38 |
| Ruhi     |     0.65 |  -1    |    0.5  |    0.65 |     -1    |   0.44 |  0.77 |     0.62 |   0.59 |      0.52 |      0.56 |   0    |   0.33 |   0.47 |    0.83 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.42 |   1    |    0.38 |    0.65 |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.44 |   0.8  |    0.57 |    0.52 |     -1    |   0.68 |  0.47 |     0.42 |   0.56 |      0.56 |      0.55 |   0.47 |  -1    |   0    |    0.33 |     0.33 |   0.8  |  0.56 |       0.6  |  0.5  |
| Jeron    |     0.1  |  -1    |    0.64 |    0.4  |     -1    |   0.67 | -1    |     0.36 |   0.22 |      0.73 |      0.87 |   0.83 |  -1    |   0.33 |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.25 |  -1    |    0.3  |    0.4  |     -1    |   1    |  0.6  |     0.71 |   0.6  |      0.5  |      0.33 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.38 |  -1    |    0.31 |    0.8  |     -1    |  -1    |  0.71 |     0.38 |   0.67 |      0.47 |      0.47 |   0.43 |  -1    |   0.56 |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|
| Rachel   |       85 |      4 |      29 |      33 |         2 |     12 |    24 |       27 |     31 |        30 |        26 |      7 |      7 |     27 |          1 |        1 |        0 |       9 |        0 |        4 |      6 |       0 |     8 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       29 |      1 |     105 |      49 |         0 |     12 |    19 |       35 |     27 |        39 |        40 |     10 |      5 |     29 |          1 |        1 |        0 |       4 |        0 |        7 |      7 |       0 |     9 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |
| Brian    |       33 |     10 |      49 |     124 |         2 |     16 |    22 |       38 |     49 |        36 |        52 |     12 |      6 |     33 |          1 |        1 |        0 |       9 |        0 |        4 |      6 |       0 |     3 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |         6 |      3 |     0 |        0 |      2 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       12 |      2 |      12 |      16 |         3 |     49 |     7 |       16 |     18 |        18 |        22 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |
| Jai      |       24 |      2 |      19 |      22 |         0 |      7 |    51 |       16 |     27 |        14 |        17 |      3 |      2 |     17 |          0 |        0 |        0 |       3 |        0 |        0 |      2 |       0 |     2 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |       27 |      2 |      35 |      38 |         0 |     16 |    16 |       82 |     33 |        28 |        29 |      5 |      3 |     29 |          0 |        0 |        1 |       7 |        1 |        1 |      2 |       1 |     5 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       0 |
| Kate     |       31 |      5 |      27 |      49 |         2 |     18 |    27 |       33 |    104 |        32 |        44 |     11 |      4 |     28 |          0 |        0 |        0 |       7 |        0 |        5 |      4 |       1 |     6 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |
| Sushant  |       30 |      3 |      39 |      36 |         0 |     18 |    14 |       28 |     32 |        98 |        44 |     14 |      5 |     29 |          2 |        0 |        0 |       4 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Abishek  |       26 |      5 |      40 |      52 |         1 |     22 |    17 |       29 |     44 |        44 |       116 |     15 |      6 |     33 |          0 |        0 |        0 |       2 |        0 |        3 |      6 |       0 |    10 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |
| Ruhi     |        7 |      2 |      10 |      12 |         0 |      5 |     3 |        5 |     11 |        14 |        15 |     35 |      4 |      9 |          0 |        0 |        0 |       1 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        7 |      0 |       5 |       6 |         1 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     17 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       27 |      1 |      29 |      33 |         0 |      8 |    17 |       29 |     28 |        29 |        33 |      9 |      2 |     82 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       1 |     4 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        9 |      0 |       4 |       9 |         0 |      2 |     3 |        7 |      7 |         4 |         2 |      1 |      1 |      4 |          0 |        0 |        1 |      17 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |       0 |
| Jade     |        6 |      2 |       7 |       6 |         0 |      0 |     2 |        2 |      4 |         5 |         6 |      2 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |     13 |       0 |     1 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sofia    |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jay      |        8 |      1 |       9 |       3 |         0 |      1 |     2 |        5 |      6 |        10 |        10 |      4 |      1 |      4 |          0 |        0 |        0 |       2 |        0 |        0 |      1 |       0 |    19 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Derek    |        1 |      0 |       2 |       3 |         0 |      0 |     0 |        1 |      1 |         3 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       4 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Gathenji |        6 |      0 |       1 |       3 |         0 |      0 |     4 |        2 |      4 |         3 |         2 |      2 |      1 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          7 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      2 |         1 |         1 |      2 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      3 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sai      |        2 |      1 |       2 |       5 |         0 |      2 |     2 |        2 |      4 |         3 |         5 |      0 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     8 |        0 |        0 |      0 |     0 |       0 |       0 |
| Nabeel   |        0 |      1 |       2 |       1 |         0 |      0 |     0 |        2 |      3 |         0 |         2 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        4 |        0 |      0 |     0 |       0 |       0 |
| Ronnie   |        1 |      0 |       2 |       0 |         0 |      1 |     0 |        2 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        2 |      0 |     0 |       0 |       0 |
| Neha     |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |
| Kawin    |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |
| Abrar    |        1 |      0 |       1 |       0 |         0 |      0 |     0 |        0 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|
| Rachel   |       -1 |      2 |       4 |       4 |         2 |      4 |     5 |        3 |      6 |         7 |         4 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Peter    |        4 |      0 |      -1 |      14 |         0 |      5 |     6 |        4 |      4 |        13 |        14 |      4 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        1 |      2 |       0 |     4 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Brian    |        4 |      3 |      14 |      -1 |         2 |      5 |     2 |        7 |     11 |         7 |        15 |      1 |      2 |      6 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |        -1 |      2 |     0 |        0 |      1 |         0 |         0 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |        4 |      1 |       5 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jai      |        5 |      0 |       6 |       2 |         0 |      2 |    -1 |        1 |      7 |         4 |         5 |      2 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |        3 |      0 |       4 |       7 |         0 |      1 |     1 |       -1 |      4 |         5 |         5 |      1 |      2 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Kate     |        6 |      1 |       4 |      11 |         1 |      6 |     7 |        4 |     -1 |         9 |        11 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |
| Sushant  |        7 |      1 |      13 |       7 |         0 |      7 |     4 |        5 |      9 |        -1 |        16 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Abishek  |        4 |      1 |      14 |      15 |         0 |      5 |     5 |        5 |     11 |        16 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Ruhi     |        2 |      1 |       4 |       1 |         0 |      2 |     2 |        1 |      3 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        2 |      0 |       0 |       2 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     5 |        4 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        1 |      0 |       0 |       1 |         0 |      1 |     0 |        2 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jade     |        1 |      0 |       2 |       0 |         0 |      0 |     0 |        0 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sofia    |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |      -1 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jay      |        0 |      0 |       4 |       0 |         0 |      1 |     1 |        0 |      1 |         3 |         2 |      3 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |    -1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Greg     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |     -1 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Gathenji |        1 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |         -1 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        1 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |     -1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sai      |        1 |      0 |       0 |       1 |         0 |      0 |     1 |        1 |      1 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |    -1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Nabeel   |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |       -1 |        0 |      0 |     0 |       0 |       0 |
| Ronnie   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |       -1 |      0 |     0 |       0 |       0 |
| Neha     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |     -1 |     0 |       0 |       0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |    -1 |       0 |       0 |
| Kawin    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |      -1 |       0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |      -1 |

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|
| Rachel   |        0 |      4 |      35 |      38 |         4 |     21 |    15 |       25 |     33 |        35 |        46 |     13 |      5 |     21 |          1 |        0 |        1 |       1 |        1 |        3 |      2 |       1 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       35 |      5 |       0 |      43 |         1 |     20 |    24 |       37 |     49 |        38 |        47 |     10 |      3 |     38 |          1 |        0 |        1 |       7 |        1 |        2 |      3 |       2 |     4 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       0 |
| Brian    |       38 |      2 |      43 |       0 |         4 |     27 |    21 |       34 |     45 |        52 |        53 |     22 |     11 |     36 |          1 |        0 |        1 |       6 |        1 |        5 |      4 |       2 |    12 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       0 |
| Anthony  |        4 |      0 |       1 |       4 |         0 |      3 |     1 |        1 |      4 |         1 |         4 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       21 |      3 |      20 |      27 |         3 |      0 |     7 |       20 |     21 |        12 |        18 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      5 |       0 |     3 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |
| Jai      |       15 |      3 |      24 |      21 |         1 |      7 |     0 |       16 |     17 |        26 |        23 |     10 |      0 |     15 |          1 |        0 |        0 |       1 |        0 |        2 |      3 |       0 |     5 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |
| Jackie   |       25 |      4 |      37 |      34 |         1 |     20 |    16 |        0 |     28 |        30 |        38 |      8 |      4 |     21 |          0 |        1 |        0 |       4 |        0 |        2 |      5 |       1 |     3 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |
| Kate     |       33 |      6 |      49 |      45 |         4 |     21 |    17 |       28 |      0 |        41 |        44 |     16 |     10 |     35 |          2 |        0 |        0 |       2 |        0 |        1 |      6 |       1 |    12 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |
| Sushant  |       35 |      4 |      38 |      52 |         1 |     12 |    26 |       30 |     41 |         0 |        48 |     15 |      5 |     37 |          0 |        0 |        0 |      11 |        0 |        5 |      5 |       0 |     9 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |
| Abishek  |       46 |      4 |      47 |      53 |         4 |     18 |    23 |       38 |     44 |        48 |         0 |     19 |      7 |     41 |          0 |        0 |        0 |      13 |        0 |        5 |      3 |       1 |     9 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |
| Ruhi     |       13 |      1 |      10 |      22 |         0 |      4 |    10 |        8 |     16 |        15 |        19 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        5 |      5 |       3 |      11 |         2 |      2 |     0 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       21 |      4 |      38 |      36 |         0 |     17 |    15 |       21 |     35 |        37 |        41 |      8 |      1 |      0 |          1 |        0 |        0 |       2 |        0 |        2 |      4 |       0 |     5 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        1 |      1 |       7 |       6 |         0 |      4 |     1 |        4 |      2 |        11 |        13 |      5 |      1 |      2 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jade     |        2 |      0 |       3 |       4 |         0 |      5 |     3 |        5 |      6 |         5 |         3 |      2 |      0 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sofia    |        1 |      0 |       2 |       2 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jay      |        5 |      1 |       4 |      12 |         0 |      3 |     5 |        3 |     12 |         9 |         9 |      3 |      0 |      5 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Derek    |        3 |      0 |       2 |       1 |         0 |      0 |     2 |        1 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Gathenji |        1 |      0 |       3 |       3 |         0 |      0 |     1 |        2 |      3 |         3 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Caro     |        1 |      0 |       0 |       3 |         0 |      1 |     0 |        1 |      1 |         2 |         2 |      1 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sai      |        1 |      0 |       5 |       3 |         0 |      2 |     1 |        3 |      4 |         5 |         3 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Nabeel   |        2 |      3 |       0 |       3 |         0 |      0 |     1 |        2 |      1 |         0 |         2 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Ronnie   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      1 |         1 |         2 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Neha     |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |
| Ira      |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      1 |     0 |       1 |       0 |
| Kawin    |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        1 |      0 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |

### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   -1   |    0.23 |    0.45 |   0.44 |  0.23 |     0.38 |   0.42 |      0.37 |      0.57 |   0.14 |   0.43 |   0.38 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.23 |   -1   |   -1    |    0.5  |   0.43 |  0.31 |     0.38 |   0.5  |      0.41 |      0.6  |   0.4  |   0.2  |   0.3  |   -1    |     0.14 |    0.2 |  0.5  |      -1    |  -1   |
| Brian    |     0.45 |    0.5 |    0.5  |   -1    |   0.38 |  0.4  |     0.44 |   0.6  |      0.51 |      0.63 |   0.58 |   0.83 |   0.54 |    0.5  |    -1    |    0.5 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |    0.43 |    0.38 |  -1    |  0    |     0.25 |   0.53 |      0.38 |      0.45 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.23 |   -1   |    0.31 |    0.4  |   0    | -1    |     0.09 |   0.35 |      0.31 |      0.53 |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.38 |   -1   |    0.38 |    0.44 |   0.25 |  0.09 |    -1    |   0.5  |      0.48 |      0.52 |   0    |  -1    |   0.5  |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.42 |    0.6 |    0.5  |    0.6  |   0.53 |  0.35 |     0.5  |  -1    |      0.45 |      0.62 |   0.27 |  -1    |   0.58 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.37 |   -1   |    0.41 |    0.51 |   0.38 |  0.31 |     0.48 |   0.45 |     -1    |      0.57 |   0.43 |   0.4  |   0.44 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1   |
| Abishek  |     0.57 |    0.4 |    0.6  |    0.63 |   0.45 |  0.53 |     0.52 |   0.62 |      0.57 |     -1    |   0.53 |   0.83 |   0.55 |   -1    |    -1    |    0.5 |  0.57 |      -1    |   0.2 |
| Ruhi     |     0.14 |   -1   |    0.4  |    0.58 |   0.2  | -1    |     0    |   0.27 |      0.43 |      0.53 |  -1    |  -1    |   0.56 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Alex     |     0.38 |   -1   |    0.3  |    0.54 |   0.4  |  0.33 |     0.5  |   0.58 |      0.44 |      0.55 |   0.56 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jade     |    -1    |   -1   |    0.2  |    0.5  |  -1    | -1    |    -1    |  -1    |     -1    |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|
| Rachel   |    -1    |   -1   |    0.23 |    0.41 |   0.44 |  0.25 |     0.38 |   0.39 |      0.38 |      0.55 |   0    |   0.33 |   0.41 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.23 |   -1   |   -1    |    0.47 |   0.33 |  0.25 |     0.36 |   0.42 |      0.37 |      0.56 |   0.4  |  -1    |   0.27 |   -1    |     0.14 |    0.2 |  0.5  |      -1    |
| Brian    |     0.41 |    0.5 |    0.47 |   -1    |   0.33 |  0.37 |     0.42 |   0.57 |      0.5  |      0.6  |   0.5  |  -1    |   0.52 |    0.5  |    -1    |    0.5 | -1    |      -1    |
| Minh     |     0.44 |   -1   |    0.33 |    0.33 |  -1    |  0    |     0.1  |   0.46 |      0.29 |      0.42 |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.25 |   -1   |    0.25 |    0.37 |   0    | -1    |     0.09 |   0.35 |      0.31 |      0.5  |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.38 |   -1   |    0.36 |    0.42 |   0.1  |  0.09 |    -1    |   0.45 |      0.43 |      0.5  |   0    |  -1    |   0.47 |    0.33 |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.39 |    0.6 |    0.42 |    0.57 |   0.46 |  0.35 |     0.45 |  -1    |      0.38 |      0.58 |   0.27 |  -1    |   0.57 |    0.6  |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.38 |   -1   |    0.37 |    0.5  |   0.29 |  0.31 |     0.43 |   0.38 |     -1    |      0.55 |   0.43 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.12 |      -1    |
| Abishek  |     0.55 |    0.4 |    0.56 |    0.6  |   0.42 |  0.5  |     0.5  |   0.58 |      0.55 |     -1    |   0.5  |   0.8  |   0.54 |   -1    |    -1    |    0.5 |  0.57 |      -1    |
| Ruhi     |     0    |   -1   |    0.4  |    0.5  |   0.2  | -1    |     0    |   0.27 |      0.43 |      0.5  |  -1    |  -1    |   0.67 |   -1    |    -1    |   -1   | -1    |      -1    |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Alex     |     0.41 |   -1   |    0.27 |    0.52 |  -1    |  0.4  |     0.47 |   0.57 |      0.42 |      0.54 |   0.67 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jade     |    -1    |   -1   |    0.2  |    0.5  |  -1    | -1    |    -1    |  -1    |     -1    |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |
|----------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |   -1    |    -1    |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      0.83 |      1    |  -1    |    0.75 |    0.33 |     1    |   0.5  | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |   0    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.91 |   0.33 |    0.8  |    0.33 |     0.33 |   1    | -1    |
| Sushant  |   0.33 |     0.83 |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.91 |      0.79 |     -1    |   0.67 |    0.77 |    0.62 |     0.5  |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.5  |  0.33 |
| Brian    |  -1    |     0.75 |      1 | -1    |   0.8  |      0.71 |      0.77 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |
| Peter    |  -1    |     0.33 |     -1 |  0.25 |   0.33 |      0.58 |      0.62 |   0.75 |    0.89 |   -1    |     0.67 |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |   0.33 |      0.67 |      0.5  |  -1    |    0.8  |    0.67 |    -1    |  -1    | -1    |
| Alex     |  -1    |     0.5  |     -1 |  0    |   1    |      0.67 |      0.88 |   0.5  |    0.83 |    0.33 |    -1    |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |
|----------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |   -1    |    -1    |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      1    |      1    |  -1    |    0.75 |    0.33 |     1    |   0.75 | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |  -1    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.91 |   0.33 |    0.8  |    0.33 |     0.33 |   1    | -1    |
| Sushant  |   0.33 |     1    |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.91 |      0.79 |     -1    |   0.67 |    0.83 |    0.62 |     0.5  |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.75 |  0.33 |
| Brian    |  -1    |     0.75 |      1 | -1    |   0.8  |      0.71 |      0.83 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |
| Peter    |  -1    |     0.33 |     -1 |  0.25 |   0.33 |      0.58 |      0.62 |   0.75 |    0.89 |   -1    |     0.67 |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |   0.33 |      0.67 |      0.5  |  -1    |    0.8  |    0.67 |    -1    |  -1    | -1    |
| Alex     |  -1    |     0.75 |     -1 | -1    |   1    |      0.67 |      0.88 |   0.75 |    0.83 |    0.33 |    -1    |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Peter    |   -1    |    0.39 |   0.62 |     0.48 |    0.2 |  0.56 |     0.45 |   0.47 |      0.44 |      0.35 |   0.7  |  -1    |   0.6  |    0.4  |     -1   |   -1   | -1    |       -1   |   0.8 |
| Brian    |    0.61 |   -1    |   0.59 |     0.64 |   -1   |  0.69 |     0.57 |   0.55 |      0.57 |      0.47 |   0.73 |   0.64 |   0.64 |   -1    |      0.6 |   -1   |  0.55 |       -1   |  -1   |
| Minh     |    0.38 |    0.41 |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.27 |      0.33 |      0.4  |  -1    |  -1    |   0.33 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Rachel   |    0.52 |    0.36 |   0.5  |    -1    |   -1   |  0.55 |     0.55 |   0.4  |      0.44 |      0.32 |   0.62 |   0.6  |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.31 |  -1    |     0.45 |   -1   | -1    |     0.4  |   0.29 |      0.38 |      0.24 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jackie   |    0.55 |    0.43 |   0.5  |     0.45 |   -1   |  0.6  |    -1    |   0.45 |      0.35 |      0.38 |   0.5  |  -1    |   0.53 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Kate     |    0.53 |    0.45 |   0.73 |     0.6  |    0.5 |  0.71 |     0.55 |  -1    |      0.58 |      0.42 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |    0.8 |  0.44 |       -1   |  -1   |
| Sushant  |    0.56 |    0.43 |   0.67 |     0.56 |   -1   |  0.62 |     0.65 |   0.42 |     -1    |      0.36 |   0.6  |   0.4  |   0.42 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |   0.8 |
| Abishek  |    0.65 |    0.53 |   0.6  |     0.68 |   -1   |  0.76 |     0.62 |   0.57 |      0.64 |     -1    |   0.74 |   0.71 |   0.58 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1   |
| Ruhi     |    0.3  |    0.27 |  -1    |     0.38 |   -1   |  0.6  |     0.5  |   0.38 |      0.4  |      0.26 |  -1    |  -1    |   0.62 |    0.6  |     -1   |   -1   | -1    |       -1   |  -1   |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Alex     |    0.4  |    0.36 |   0.67 |     0.75 |   -1   |  0.75 |     0.47 |   0.48 |      0.58 |      0.42 |   0.38 |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jade     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|
| Peter    |   -1    |    0.37 |   0.62 |     0.44 |    0.2 |  0.53 |     0.45 |   0.47 |      0.42 |      0.33 |   0.67 |  -1    |   0.57 |    0.4  |     -1   |   -1   | -1    |       -1   |
| Brian    |    0.63 |   -1    |   0.6  |     0.62 |   -1   |  0.67 |     0.59 |   0.56 |      0.57 |      0.47 |   0.7  |   0.6  |   0.63 |   -1    |      0.6 |   -1   |  0.55 |       -1   |
| Minh     |    0.38 |    0.4  |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.29 |      0.33 |      0.38 |  -1    |  -1    |   0.29 |   -1    |     -1   |   -1   | -1    |       -1   |
| Rachel   |    0.56 |    0.38 |   0.5  |    -1    |   -1   |  0.6  |     0.58 |   0.43 |      0.47 |      0.34 |   0.62 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Jai      |    0.47 |    0.33 |  -1    |     0.4  |   -1   | -1    |     0.44 |   0.33 |      0.38 |      0.26 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |
| Jackie   |    0.55 |    0.41 |   0.5  |     0.42 |   -1   |  0.56 |    -1    |   0.45 |      0.35 |      0.36 |   0.43 |  -1    |   0.5  |   -1    |     -1   |   -1   | -1    |       -1   |
| Kate     |    0.53 |    0.44 |   0.71 |     0.57 |    0.5 |  0.67 |     0.55 |  -1    |      0.58 |      0.42 |   0.62 |   0.33 |   0.48 |   -1    |     -1   |    0.8 |  0.44 |       -1   |
| Sushant  |    0.58 |    0.43 |   0.67 |     0.53 |   -1   |  0.62 |     0.65 |   0.42 |     -1    |      0.35 |   0.57 |  -1    |   0.39 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |
| Abishek  |    0.67 |    0.53 |   0.62 |     0.66 |   -1   |  0.74 |     0.64 |   0.58 |      0.65 |     -1    |   0.71 |   0.67 |   0.56 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |
| Ruhi     |    0.33 |    0.3  |  -1    |     0.38 |   -1   |  0.6  |     0.57 |   0.38 |      0.43 |      0.29 |  -1    |  -1    |   0.62 |    0.6  |     -1   |   -1   | -1    |       -1   |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Alex     |    0.43 |    0.37 |   0.71 |     0.75 |   -1   |  0.75 |     0.5  |   0.52 |      0.61 |      0.44 |   0.38 |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Jade     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.36     |            25 |
| 2+2        | 0.382979 |            47 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.333333 |            24 |
| 2+2        | 0.325581 |            43 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.428571 |            21 |
| Success      | 0.343284 |            67 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.428571 |            21 |
| Success      | 0.323077 |            65 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      20 | 0.425532 |     0.35     |
|         1 |      19 | 0.404255 |     0.105263 |
|         2 |       8 | 0.170213 |     0.5      |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       7 | 0.636364 |     0.142857 |
|         1 |       4 | 0.363636 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       8 | 0.444444 |     0.5      |
|         1 |       7 | 0.388889 |     0.142857 |
|         2 |       3 | 0.166667 |     0.333333 |

*2 bad guys on mission 3:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       5 | 0.333333 |     0.4      |
|         1 |       6 | 0.4      |     0.166667 |
|         2 |       4 | 0.266667 |     0.5      |

*3 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         1 |       2 | 0.666667 |            0 |
|         2 |       1 | 0.333333 |            1 |

### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            27 |     0.481481 |
|                   1 |            92 |     0.358696 |
|                   2 |            14 |     0.571429 |
|                   3 |             5 |     0.4      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            25 |     0.44     |
|                   1 |            86 |     0.313953 |
|                   2 |            14 |     0.571429 |
|                   3 |             5 |     0.4      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.13043 |           138 |              18 |
| Assassin      |                 0.056   |           125 |               7 |
| Morgana       |                 0.07246 |           138 |              10 |
| Mordred       |                 0.01087 |            92 |               1 |
| Loyal Servant |                 0       |           415 |               0 |
| Oberon        |                 0.02703 |            37 |               1 |
| Minion #1     |                 0.05    |            20 |               1 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Alex     |                    0.4      |                  8 |            20 |
| Jai      |                    0.375    |                  3 |             8 |
| Rachel   |                    0.357143 |                  5 |            14 |
| Abishek  |                    0.346154 |                  9 |            26 |
| Minh     |                    0.285714 |                  2 |             7 |
| Jackie   |                    0.25     |                  5 |            20 |
| Kate     |                    0.25     |                  6 |            24 |
| Sushant  |                    0.2      |                  3 |            15 |
| Peter    |                    0.1875   |                  3 |            16 |
| Brian    |                    0.142857 |                  4 |            28 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Minh     |          0        |                  0 |             3 |
| Sushant  |          0.125    |                  1 |             8 |
| Brian    |          0.222222 |                  2 |             9 |
| Jeron    |          0.333333 |                  1 |             3 |
| Kate     |          0.4      |                  4 |            10 |
| Abishek  |          0.461538 |                  6 |            13 |
| Jackie   |          0.5      |                  5 |            10 |
| Alex     |          0.5      |                  3 |             6 |
| Peter    |          0.571429 |                  8 |            14 |
| Jai      |          0.6      |                  3 |             5 |
| Rachel   |          0.636364 |                  7 |            11 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

| # Players   |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
| 10          |          0.411765 |                  7 |            17 |
| 5           |          0.75     |                  3 |             4 |
| 5O          |          0.5      |                  1 |             2 |
| 6           |          0.333333 |                  4 |            12 |
| 6M          |          0        |                  0 |             3 |
| 6O          |          0.333333 |                  1 |             3 |
| 7           |          0.473684 |                  9 |            19 |
| 7O          |          0.666667 |                  2 |             3 |
| 8           |          0.5      |                  7 |            14 |
| 8O          |          0.666667 |                  2 |             3 |
| 9           |          0.5      |                  8 |            16 |
| 9O          |          0        |                  0 |             1 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

| # Players   |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
| 10          |                   1 |          0.461538 |                  6 |            13 |
| 10          |                   2 |          0        |                  0 |             3 |
| 10          |                   3 |          1        |                  1 |             1 |
| 5           |                   0 |          0.5      |                  1 |             2 |
| 5           |                   1 |          1        |                  2 |             2 |
| 5O          |                   0 |          0        |                  0 |             1 |
| 5O          |                   1 |          1        |                  1 |             1 |
| 6           |                   0 |          0.5      |                  2 |             4 |
| 6           |                   1 |          0.285714 |                  2 |             7 |
| 6           |                   3 |          0        |                  0 |             1 |
| 6M          |                   0 |          0        |                  0 |             2 |
| 6M          |                   1 |          0        |                  0 |             1 |
| 6O          |                   0 |          0.333333 |                  1 |             3 |
| 7           |                   0 |          0.5      |                  4 |             8 |
| 7           |                   1 |          0.555556 |                  5 |             9 |
| 7           |                   2 |          0        |                  0 |             1 |
| 7           |                   3 |          0        |                  0 |             1 |
| 7O          |                   0 |          1        |                  2 |             2 |
| 7O          |                   2 |          0        |                  0 |             1 |
| 8           |                   0 |          0.5      |                  1 |             2 |
| 8           |                   1 |          0.5      |                  6 |            12 |
| 8O          |                   1 |          0.666667 |                  2 |             3 |
| 9           |                   0 |          1        |                  2 |             2 |
| 9           |                   1 |          0.416667 |                  5 |            12 |
| 9           |                   2 |          0.5      |                  1 |             2 |
| 9O          |                   2 |          0        |                  0 |             1 |
