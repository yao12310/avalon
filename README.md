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

Cheesy wins included: 0.3917 (n = 120)

Cheesy wins excluded: 0.3482 (n = 112)

**Good win % w.r.t. # players:**

Cheesy wins included:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           5 |             5 |     0.2      |
|           6 |            15 |     0.6      |
|           7 |            20 |     0.45     |
|           8 |            30 |     0.3      |
|           9 |            28 |     0.357143 |
|          10 |            22 |     0.409091 |

Cheesy wins excluded:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           5 |             5 |     0.2      |
|           6 |            14 |     0.571429 |
|           7 |            17 |     0.352941 |
|           8 |            30 |     0.3      |
|           9 |            25 |     0.28     |
|          10 |            21 |     0.380952 |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            58 |       32.3276 |     22.068  |
| Good     |            35 |       22.5714 |     15.7859 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            58 |       32.3276 |     22.068  |
| Good     |            31 |       24.3548 |     15.9239 |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|----------|-------------|
| Kate     |           5 |
| Peter    |           4 |
| Abishek  |           3 |
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
| Abishek  | 0.58427  |     0.481481 |    0.742857 |            89 |     52 |       37 |                      0 |
| Brian    | 0.569892 |     0.46875  |    0.793103 |            93 |     53 |       40 |                      4 |
| Jeron    | 0.545455 |     0.5      |    0.6      |            11 |      6 |        5 |                      2 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      2 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                      3 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|----------|----------|--------------|-------------|---------------|--------|----------|------------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.560976 |     0.416667 |    0.764706 |            82 |     46 |       36 |                      9 |
| Brian    | 0.546512 |     0.413793 |    0.821429 |            86 |     47 |       39 |                     12 |
| Jeron    | 0.545455 |     0.5      |    0.6      |            11 |      6 |        5 |                      2 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Brian    |             0.0980622 | 0.569892 |         0.47183  | 0.688172 |
| Kish     |             0.0870071 | 0.529412 |         0.442405 | 0.588235 |
| Abishek  |             0.0824217 | 0.58427  |         0.501848 | 0.606742 |
| Jackie   |             0.045348  | 0.488889 |         0.443541 | 0.711111 |
| Ewen     |             0.0415046 | 0.538462 |         0.496957 | 0.615385 |
| Kate     |             0.0304798 | 0.506173 |         0.475693 | 0.641975 |
| Jeron    |             0.0254079 | 0.545455 |         0.520047 | 0.545455 |
| Anthony  |             0.0190476 | 0.5      |         0.480952 | 0.166667 |
| Peter    |             0.0109513 | 0.470588 |         0.459637 | 0.647059 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Anthony  |             0.0922222 | 0.6      |         0.507778 | 0.166667 |
| Brian    |             0.0919419 | 0.546512 |         0.45457  | 0.688172 |
| Abishek  |             0.0752946 | 0.560976 |         0.485681 | 0.606742 |
| Ewen     |             0.0683946 | 0.538462 |         0.470067 | 0.615385 |
| Jeron    |             0.0388669 | 0.545455 |         0.506588 | 0.545455 |
| Kish     |             0.0333333 | 0.5      |         0.466667 | 0.588235 |
| Jackie   |             0.0281878 | 0.465116 |         0.436928 | 0.711111 |
| Kate     |             0.0132077 | 0.48     |         0.466792 | 0.641975 |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.6      |            10 |      6 |        4 |                    0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                    2 |
| Minh     | 0.5      |             6 |      3 |        3 |                    2 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|----------|---------------|--------|----------|-----------------------|
| Jackie   | 0.625    |             8 |      5 |        3 |                     0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                     2 |
| Brian    | 0.466667 |            15 |      7 |        8 |                     7 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.833333 |             6 |      5 |        1 |                    0 |
| Abishek  | 0.777778 |             9 |      7 |        2 |                    4 |
| Sushant  | 0.666667 |             9 |      6 |        3 |                   10 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.818182 |            11 |      9 |        2 |                      0 |
| Brian    | 0.733333 |            15 |     11 |        4 |                      8 |
| Kate     | 0.666667 |             9 |      6 |        3 |                      8 |

*Mordred:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|---------|---------------|--------|----------|---------------------|
| Kate     |       1 |             8 |      8 |        0 |                   0 |
| Brian    |       1 |             7 |      7 |        0 |                 nan |
| Peter    |       1 |             6 |      6 |        0 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.607143 |            28 |     17 |       11 |                      0 |
| Ruhi     | 0.5      |            12 |      6 |        6 |                      4 |
| Rachel   | 0.461538 |            26 |     12 |       14 |                     10 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.555556 |             9 |      5 |        4 |                    0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                    1 |
| Sushant  | 0.461538 |            13 |      6 |        7 |                    3 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|----------|---------------|--------|----------|-----------------------|
| Jackie   | 0.625    |             8 |      5 |        3 |                     0 |
| Kate     | 0.428571 |             7 |      3 |        4 |                     4 |
| Brian    | 0.333333 |            12 |      4 |        8 |                    10 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.875    |             8 |      7 |        1 |                      0 |
| Brian    | 0.833333 |             6 |      5 |        1 |                      3 |
| Sushant  | 0.75     |             8 |      6 |        2 |                      9 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.818182 |            11 |      9 |        2 |                      0 |
| Brian    | 0.785714 |            14 |     11 |        3 |                      3 |
| Kate     | 0.666667 |             9 |      6 |        3 |                      8 |

*Mordred:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|---------|---------------|--------|----------|---------------------|
| Kate     |       1 |             8 |      8 |        0 |                   0 |
| Brian    |       1 |             7 |      7 |        0 |                 nan |
| Peter    |       1 |             6 |      6 |        0 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.521739 |            23 |     12 |       11 |                      0 |
| Rachel   | 0.416667 |            24 |     10 |       14 |                      6 |
| Brian    | 0.405405 |            37 |     15 |       22 |                     10 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|----------|----------------|
| Brian    |            109 |
| Abishek  |             99 |
| Kate     |             96 |
| Peter    |             87 |
| Sushant  |             80 |
| Rachel   |             75 |
| Alex     |             71 |
| Jackie   |             64 |
| Minh     |             49 |
| Jai      |             45 |
| Ruhi     |             31 |
| Kish     |             17 |
| Jeron    |             16 |
| Jay      |             14 |
| Ewen     |             13 |
| Jade     |             10 |
| Justin   |              9 |
| Sai      |              8 |
| Gathenji |              7 |
| Anthony  |              6 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|----------|----------|----------|---------|
| Gathenji | 0.857143 |        6 |       1 |
| Jade     | 0.8      |        8 |       2 |
| Jackie   | 0.734375 |       47 |      17 |
| Jeron    | 0.6875   |       11 |       5 |
| Rachel   | 0.666667 |       50 |      25 |
| Justin   | 0.666667 |        6 |       3 |
| Brian    | 0.651376 |       71 |      38 |
| Kate     | 0.645833 |       62 |      34 |
| Jai      | 0.644444 |       29 |      16 |
| Alex     | 0.633803 |       45 |      26 |
| Sai      | 0.625    |        5 |       3 |
| Ewen     | 0.615385 |        8 |       5 |
| Peter    | 0.609195 |       53 |      34 |
| Abishek  | 0.606061 |       60 |      39 |
| Sushant  | 0.6      |       48 |      32 |
| Kish     | 0.588235 |       10 |       7 |
| Jay      | 0.571429 |        8 |       6 |
| Minh     | 0.530612 |       26 |      23 |
| Ruhi     | 0.483871 |       15 |      16 |
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
| No                 |           106 |     0.424528 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           106 |     0.424528 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       13 |         17 |         11 |        11 |         6 |        7 |           4 |              30 |            99 |
| Alex     |        6 |         10 |         11 |         9 |         4 |        1 |           1 |              29 |            71 |
| Anthony  |        0 |          1 |          3 |         2 |         0 |        0 |           0 |               0 |             6 |
| Brian    |       12 |         16 |          7 |        21 |         9 |        0 |           1 |              43 |           109 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       12 |         10 |          5 |         5 |         3 |        3 |           1 |              25 |            64 |
| Jade     |        3 |          1 |          0 |         0 |         1 |        1 |           0 |               4 |            10 |
| Jai      |        4 |          4 |          5 |         5 |         3 |        3 |           0 |              21 |            45 |
| Jay      |        2 |          2 |          3 |         0 |         2 |        1 |           0 |               4 |            14 |
| Jeron    |        3 |          7 |          1 |         2 |         1 |        1 |           0 |               1 |            16 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       10 |         10 |          8 |        10 |         8 |        6 |           2 |              42 |            96 |
| Kish     |        1 |          3 |          1 |         3 |         2 |        0 |           1 |               6 |            17 |
| Minh     |        6 |          4 |         10 |         5 |         5 |        1 |           2 |              16 |            49 |
| Peter    |       13 |         12 |         14 |         8 |         6 |        4 |           2 |              28 |            87 |
| Rachel   |       13 |          9 |          8 |         7 |         9 |        0 |           1 |              28 |            75 |
| Ruhi     |        1 |          2 |          4 |         7 |         4 |        1 |           0 |              12 |            31 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       13 |          5 |          9 |        14 |         7 |        1 |           1 |              30 |            80 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.111 |      0.144 |      0.103 |     0.096 |     0.081 |    0.206 |       0.25  |           0.086 |            99 |
| Alex     |    0.051 |      0.085 |      0.103 |     0.078 |     0.054 |    0.029 |       0.062 |           0.083 |            71 |
| Anthony  |    0     |      0.008 |      0.028 |     0.017 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.103 |      0.136 |      0.065 |     0.183 |     0.122 |    0     |       0.062 |           0.123 |           109 |
| Ewen     |    0.009 |      0.017 |      0.019 |     0.009 |     0     |    0.059 |       0     |           0.014 |            13 |
| Gathenji |    0     |      0     |      0     |     0.009 |     0     |    0     |       0     |           0.017 |             7 |
| Jackie   |    0.103 |      0.085 |      0.047 |     0.043 |     0.041 |    0.088 |       0.062 |           0.071 |            64 |
| Jade     |    0.026 |      0.008 |      0     |     0     |     0.014 |    0.029 |       0     |           0.011 |            10 |
| Jai      |    0.034 |      0.034 |      0.047 |     0.043 |     0.041 |    0.088 |       0     |           0.06  |            45 |
| Jay      |    0.017 |      0.017 |      0.028 |     0     |     0.027 |    0.029 |       0     |           0.011 |            14 |
| Jeron    |    0.026 |      0.059 |      0.009 |     0.017 |     0.014 |    0.029 |       0     |           0.003 |            16 |
| Justin   |    0.017 |      0     |      0.009 |     0.009 |     0.014 |    0     |       0     |           0.011 |             9 |
| Kate     |    0.085 |      0.085 |      0.075 |     0.087 |     0.108 |    0.176 |       0.125 |           0.12  |            96 |
| Kish     |    0.009 |      0.025 |      0.009 |     0.026 |     0.027 |    0     |       0.062 |           0.017 |            17 |
| Minh     |    0.051 |      0.034 |      0.093 |     0.043 |     0.068 |    0.029 |       0.125 |           0.046 |            49 |
| Peter    |    0.111 |      0.102 |      0.131 |     0.07  |     0.081 |    0.118 |       0.125 |           0.08  |            87 |
| Rachel   |    0.111 |      0.076 |      0.075 |     0.061 |     0.122 |    0     |       0.062 |           0.08  |            75 |
| Ruhi     |    0.009 |      0.017 |      0.037 |     0.061 |     0.054 |    0.029 |       0     |           0.034 |            31 |
| Sai      |    0.009 |      0.008 |      0     |     0.009 |     0.027 |    0     |       0     |           0.009 |             8 |
| Sushant  |    0.111 |      0.042 |      0.084 |     0.122 |     0.095 |    0.029 |       0.062 |           0.086 |            80 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.131 |      0.172 |      0.111 |     0.111 |     0.061 |    0.071 |       0.04  |           0.303 |            99 |
| Alex     |    0.085 |      0.141 |      0.155 |     0.127 |     0.056 |    0.014 |       0.014 |           0.408 |            71 |
| Anthony  |    0     |      0.167 |      0.5   |     0.333 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.11  |      0.147 |      0.064 |     0.193 |     0.083 |    0     |       0.009 |           0.394 |           109 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.188 |      0.156 |      0.078 |     0.078 |     0.047 |    0.047 |       0.016 |           0.391 |            64 |
| Jade     |    0.3   |      0.1   |      0     |     0     |     0.1   |    0.1   |       0     |           0.4   |            10 |
| Jai      |    0.089 |      0.089 |      0.111 |     0.111 |     0.067 |    0.067 |       0     |           0.467 |            45 |
| Jay      |    0.143 |      0.143 |      0.214 |     0     |     0.143 |    0.071 |       0     |           0.286 |            14 |
| Jeron    |    0.188 |      0.438 |      0.062 |     0.125 |     0.062 |    0.062 |       0     |           0.062 |            16 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.104 |      0.104 |      0.083 |     0.104 |     0.083 |    0.062 |       0.021 |           0.438 |            96 |
| Kish     |    0.059 |      0.176 |      0.059 |     0.176 |     0.118 |    0     |       0.059 |           0.353 |            17 |
| Minh     |    0.122 |      0.082 |      0.204 |     0.102 |     0.102 |    0.02  |       0.041 |           0.327 |            49 |
| Peter    |    0.149 |      0.138 |      0.161 |     0.092 |     0.069 |    0.046 |       0.023 |           0.322 |            87 |
| Rachel   |    0.173 |      0.12  |      0.107 |     0.093 |     0.12  |    0     |       0.013 |           0.373 |            75 |
| Ruhi     |    0.032 |      0.065 |      0.129 |     0.226 |     0.129 |    0.032 |       0     |           0.387 |            31 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.162 |      0.062 |      0.112 |     0.175 |     0.088 |    0.012 |       0.012 |           0.375 |            80 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.43 |    0.45 |      0.33 |   0.36 |  0.61 |     0.48 |   0.47 |      0.49 |      0.34 |   0.38 |   0.58 |   0.56 |    0.89 |     0.57 |   0.67 |  0.5  |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.43 |   0.17 |    1    |    0.49 |     -1    |   0.38 |  0.41 |     0.5  |   0.38 |      0.56 |      0.49 |   0.5  |   0.62 |   0.48 |    0.3  |     0.78 |   0.71 |  0.75 |      -1    |  0.29 |
| Brian    |     0.45 |   0.83 |    0.49 |    1    |      0.33 |   0.37 |  0.5  |     0.56 |   0.53 |      0.44 |      0.52 |   0.37 |   0.35 |   0.48 |    0.57 |     0.44 |   0.71 |  0.15 |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |      1    |   0.5  | -1    |    -1    |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.36 |   0.4  |    0.38 |    0.37 |      0.5  |   1    |  0.5  |     0.44 |   0.46 |      0.6  |      0.55 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.61 |   0.4  |    0.41 |    0.5  |     -1    |   0.5  |  1    |     0.46 |   0.65 |      0.35 |      0.44 |   0.2  |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |       0.8  | -1    |
| Jackie   |     0.48 |   0.33 |    0.5  |    0.56 |     -1    |   0.44 |  0.46 |     1    |   0.53 |      0.5  |      0.46 |   0.22 |   0.43 |   0.54 |    0.6  |    -1    |  -1    | -1    |      -1    |  0.4  |
| Kate     |     0.47 |   0.45 |    0.38 |    0.53 |      0.33 |   0.46 |  0.65 |     0.53 |   1    |      0.45 |      0.49 |   0.38 |   0.29 |   0.4  |    0.78 |     0.83 |   0.44 |  0.29 |       0.57 |  0.5  |
| Sushant  |     0.49 |   0.43 |    0.56 |    0.44 |     -1    |   0.6  |  0.35 |     0.5  |   0.45 |      1    |      0.47 |   0.48 |   0.5  |   0.44 |    0.29 |     0.17 |   0.57 |  0.5  |       0.5  |  0.38 |
| Abishek  |     0.34 |   0.56 |    0.49 |    0.52 |      0.2  |   0.55 |  0.44 |     0.46 |   0.49 |      0.47 |      1    |   0.47 |   0.46 |   0.44 |    0.14 |     0.38 |   0.71 |  0.57 |       0.29 |  0.62 |
| Ruhi     |     0.38 |  -1    |    0.5  |    0.37 |     -1    |   0.56 |  0.2  |     0.22 |   0.38 |      0.48 |      0.47 |   1    |   0.67 |   0.56 |    0.17 |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.58 |   0    |    0.62 |    0.35 |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.56 |   0.2  |    0.48 |    0.48 |     -1    |   0.32 |  0.5  |     0.54 |   0.4  |      0.44 |      0.44 |   0.56 |  -1    |   1    |    0.67 |     0.67 |   0.2  |  0.6  |       0.4  |  0.5  |
| Jeron    |     0.89 |  -1    |    0.3  |    0.57 |     -1    |   0.33 | -1    |     0.6  |   0.78 |      0.29 |      0.14 |   0.17 |  -1    |   0.67 |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.67 |  -1    |    0.71 |    0.71 |     -1    |   0    | -1    |    -1    |   0.44 |      0.57 |      0.71 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.5  |  -1    |    0.75 |    0.15 |     -1    |  -1    | -1    |    -1    |   0.29 |      0.5  |      0.57 |   0.57 |  -1    |   0.6  |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.07 |    0.06 |      0.33 |   0.12 |  0.15 |     0.07 |   0.1  |      0.11 |      0.05 |   0.12 |   0.17 |   0.14 |    0.11 |     0    |   0.17 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.07 |   0    |   -1    |    0.13 |     -1    |   0.16 |  0.14 |     0.06 |   0.06 |      0.17 |      0.16 |   0.25 |   0    |   0.09 |    0    |     0.11 |   0.29 |  0.38 |      -1    |  0    |
| Brian    |     0.06 |   0.25 |    0.13 |   -1    |      0.33 |   0.12 |  0.05 |     0.12 |   0.12 |      0.08 |      0.13 |   0.03 |   0.12 |   0.08 |    0.07 |     0    |   0    |  0    |       0    |  0.12 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |     -1    |   0.33 | -1    |    -1    |   0.17 |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.12 |   0.2  |    0.16 |    0.12 |      0.33 |  -1    |  0.14 |     0.03 |   0.15 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.15 |   0    |    0.14 |    0.05 |     -1    |   0.14 | -1    |     0    |   0.18 |      0.06 |      0.15 |   0.2  |  -1    |   0.14 |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Jackie   |     0.07 |   0    |    0.06 |    0.12 |     -1    |   0.03 |  0    |    -1    |   0.06 |      0.08 |      0.08 |   0    |   0.29 |   0.08 |    0.2  |    -1    |  -1    | -1    |      -1    |  0.2  |
| Kate     |     0.1  |   0.09 |    0.06 |    0.12 |      0.17 |   0.15 |  0.18 |     0.06 |  -1    |      0.12 |      0.12 |   0.08 |   0    |   0.09 |    0.22 |     0.33 |   0.11 |  0.07 |       0    |  0.12 |
| Sushant  |     0.11 |   0.14 |    0.17 |    0.08 |     -1    |   0.23 |  0.06 |     0.08 |   0.12 |     -1    |      0.15 |   0.16 |   0    |   0.11 |    0    |     0    |   0    |  0.14 |       0    |  0.12 |
| Abishek  |     0.05 |   0.11 |    0.16 |    0.13 |      0    |   0.12 |  0.15 |     0.08 |   0.12 |      0.15 |     -1    |   0.17 |   0.15 |   0.11 |    0    |     0.25 |   0    |  0.14 |       0    |  0.12 |
| Ruhi     |     0.12 |  -1    |    0.25 |    0.03 |     -1    |   0.22 |  0.2  |     0    |   0.08 |      0.16 |      0.17 |  -1    |   0.17 |   0.38 |    0    |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.17 |   0    |    0    |    0.12 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.14 |   0    |    0.09 |    0.08 |     -1    |   0.08 |  0.14 |     0.08 |   0.09 |      0.11 |      0.11 |   0.38 |  -1    |  -1    |    0.17 |     0    |   0    |  0.2  |       0    |  0.17 |
| Jeron    |     0.11 |  -1    |    0    |    0.07 |     -1    |   0.17 | -1    |     0.2  |   0.22 |      0    |      0    |   0    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.17 |  -1    |    0.29 |    0    |     -1    |   0    | -1    |    -1    |   0.11 |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jay      |     0    |  -1    |    0.38 |    0    |     -1    |  -1    | -1    |    -1    |   0.07 |      0.14 |      0.14 |   0.43 |  -1    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     0    |   0.5  |    0.57 |    0.55 |      0.67 |   0.64 |  0.39 |     0.52 |   0.53 |      0.51 |      0.66 |   0.62 |   0.42 |   0.44 |    0.11 |     0.43 |   0.33 |  0.5  |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.57 |   0.83 |    0    |    0.51 |     -1    |   0.62 |  0.59 |     0.5  |   0.62 |      0.44 |      0.51 |   0.5  |   0.38 |   0.52 |    0.7  |     0.22 |   0.29 |  0.25 |      -1    |  0.71 |
| Brian    |     0.55 |   0.17 |    0.51 |    0    |      0.67 |   0.63 |  0.5  |     0.44 |   0.47 |      0.56 |      0.48 |   0.63 |   0.65 |   0.52 |    0.43 |     0.56 |   0.29 |  0.85 |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |   -1    |    0.67 |      0    |   0.5  | -1    |    -1    |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.64 |   0.6  |    0.62 |    0.63 |      0.5  |   0    |  0.5  |     0.56 |   0.54 |      0.4  |      0.45 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   1    | -1    |      -1    | -1    |
| Jai      |     0.39 |   0.6  |    0.59 |    0.5  |     -1    |   0.5  |  0    |     0.54 |   0.35 |      0.65 |      0.56 |   0.8  |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |       0.2  | -1    |
| Jackie   |     0.52 |   0.67 |    0.5  |    0.44 |     -1    |   0.56 |  0.54 |     0    |   0.47 |      0.5  |      0.54 |   0.78 |   0.57 |   0.46 |    0.4  |    -1    |  -1    | -1    |      -1    |  0.6  |
| Kate     |     0.53 |   0.55 |    0.62 |    0.47 |      0.67 |   0.54 |  0.35 |     0.47 |   0    |      0.55 |      0.51 |   0.62 |   0.71 |   0.6  |    0.22 |     0.17 |   0.56 |  0.71 |       0.43 |  0.5  |
| Sushant  |     0.51 |   0.57 |    0.44 |    0.56 |     -1    |   0.4  |  0.65 |     0.5  |   0.55 |      0    |      0.53 |   0.52 |   0.5  |   0.56 |    0.71 |     0.83 |   0.43 |  0.5  |       0.5  |  0.62 |
| Abishek  |     0.66 |   0.44 |    0.51 |    0.48 |      0.8  |   0.45 |  0.56 |     0.54 |   0.51 |      0.53 |      0    |   0.53 |   0.54 |   0.56 |    0.86 |     0.62 |   0.29 |  0.43 |       0.71 |  0.38 |
| Ruhi     |     0.62 |  -1    |    0.5  |    0.63 |     -1    |   0.44 |  0.8  |     0.78 |   0.62 |      0.52 |      0.53 |   0    |   0.33 |   0.44 |    0.83 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.42 |   1    |    0.38 |    0.65 |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.44 |   0.8  |    0.52 |    0.52 |     -1    |   0.68 |  0.5  |     0.46 |   0.6  |      0.56 |      0.56 |   0.44 |  -1    |   0    |    0.33 |     0.33 |   0.8  |  0.4  |       0.6  |  0.5  |
| Jeron    |     0.11 |  -1    |    0.7  |    0.43 |     -1    |   0.67 | -1    |     0.4  |   0.22 |      0.71 |      0.86 |   0.83 |  -1    |   0.33 |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.33 |  -1    |    0.29 |    0.29 |     -1    |   1    | -1    |    -1    |   0.56 |      0.43 |      0.29 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.5  |  -1    |    0.25 |    0.85 |     -1    |  -1    | -1    |    -1    |   0.71 |      0.5  |      0.43 |   0.43 |  -1    |   0.4  |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|
| Rachel   |       75 |      4 |      23 |      29 |         2 |     12 |    20 |       20 |     28 |        27 |        21 |      6 |      7 |     24 |          1 |        1 |        0 |       8 |        0 |        4 |      4 |       0 |     4 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Peter    |       23 |      1 |      87 |      38 |         0 |     12 |    15 |       27 |     26 |        33 |        34 |      8 |      5 |     27 |          1 |        1 |        0 |       3 |        0 |        7 |      5 |       0 |     6 |      0 |       1 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |
| Brian    |       29 |     10 |      38 |     109 |         2 |     16 |    20 |       32 |     47 |        32 |        47 |     11 |      6 |     29 |          1 |        1 |        0 |       8 |        0 |        4 |      5 |       0 |     2 |      2 |       2 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |         6 |      3 |     0 |        0 |      2 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |       12 |      2 |      12 |      16 |         3 |     49 |     7 |       16 |     18 |        18 |        22 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |
| Jai      |       20 |      2 |      15 |      20 |         0 |      7 |    45 |       12 |     26 |        12 |        15 |      2 |      2 |     14 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     2 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |
| Jackie   |       20 |      2 |      27 |      32 |         0 |     16 |    12 |       64 |     28 |        20 |        23 |      2 |      3 |     21 |          0 |        0 |        1 |       6 |        1 |        1 |      1 |       1 |     2 |      0 |       0 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |
| Kate     |       28 |      5 |      26 |      47 |         2 |     18 |    26 |       28 |     96 |        29 |        39 |     10 |      4 |     23 |          0 |        0 |        0 |       7 |        0 |        5 |      4 |       1 |     4 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |
| Sushant  |       27 |      3 |      33 |      32 |         0 |     18 |    12 |       20 |     29 |        80 |        35 |     12 |      5 |     24 |          2 |        0 |        0 |       4 |        0 |        1 |      4 |       1 |     7 |      2 |       2 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |
| Abishek  |       21 |      5 |      34 |      47 |         1 |     22 |    15 |       23 |     39 |        35 |        99 |     14 |      6 |     28 |          0 |        0 |        0 |       2 |        0 |        3 |      5 |       0 |     8 |      1 |       1 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |
| Ruhi     |        6 |      2 |       8 |      11 |         0 |      5 |     2 |        2 |     10 |        12 |        14 |     31 |      4 |      9 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     4 |      1 |       0 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        7 |      0 |       5 |       6 |         1 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     17 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |
| Alex     |       24 |      1 |      27 |      29 |         0 |      8 |    14 |       21 |     23 |        24 |        28 |      9 |      2 |     71 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       1 |     3 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        8 |      0 |       3 |       8 |         0 |      2 |     3 |        6 |      7 |         4 |         2 |      1 |      1 |      4 |          0 |        0 |        1 |      16 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |
| Jade     |        4 |      2 |       5 |       5 |         0 |      0 |     0 |        1 |      4 |         4 |         5 |      1 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |     10 |       0 |     1 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        4 |      1 |       6 |       2 |         0 |      1 |     2 |        2 |      4 |         7 |         8 |      4 |      1 |      3 |          0 |        0 |        0 |       2 |        0 |        0 |      1 |       0 |    14 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Derek    |        1 |      0 |       1 |       2 |         0 |      0 |     0 |        0 |      1 |         2 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       2 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Gathenji |        6 |      0 |       1 |       3 |         0 |      0 |     4 |        2 |      4 |         3 |         2 |      2 |      1 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          7 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      2 |         1 |         1 |      2 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      3 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sai      |        2 |      1 |       2 |       5 |         0 |      2 |     2 |        2 |      4 |         3 |         5 |      0 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     8 |        0 |        0 |      0 |     0 |       0 |
| Nabeel   |        0 |      1 |       2 |       1 |         0 |      0 |     0 |        2 |      3 |         0 |         2 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        4 |        0 |      0 |     0 |       0 |
| Ronnie   |        1 |      0 |       2 |       0 |         0 |      1 |     0 |        2 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        2 |      0 |     0 |       0 |
| Neha     |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |
| Kawin    |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|
| Rachel   |       -1 |      2 |       4 |       4 |         2 |      4 |     5 |        3 |      6 |         6 |         3 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Peter    |        4 |      0 |      -1 |      10 |         0 |      5 |     5 |        3 |      4 |        10 |        11 |      4 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        1 |      2 |       0 |     3 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |
| Brian    |        4 |      3 |      10 |      -1 |         2 |      5 |     2 |        7 |     11 |         6 |        12 |      1 |      2 |      5 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |        -1 |      2 |     0 |        0 |      1 |         0 |         0 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |        4 |      1 |       5 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jai      |        5 |      0 |       5 |       2 |         0 |      2 |    -1 |        0 |      7 |         2 |         5 |      2 |      0 |      4 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Jackie   |        3 |      0 |       3 |       7 |         0 |      1 |     0 |       -1 |      3 |         3 |         4 |      0 |      2 |      3 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |
| Kate     |        6 |      1 |       4 |      11 |         1 |      6 |     7 |        3 |     -1 |         8 |        10 |      2 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |
| Sushant  |        6 |      1 |      10 |       6 |         0 |      7 |     2 |        3 |      8 |        -1 |        11 |      4 |      0 |      6 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       1 |     2 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Abishek  |        3 |      1 |      11 |      12 |         0 |      5 |     5 |        4 |     10 |        11 |        -1 |      5 |      2 |      7 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Ruhi     |        2 |      1 |       4 |       1 |         0 |      2 |     2 |        0 |      2 |         4 |         5 |     -1 |      1 |      6 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        2 |      0 |       0 |       2 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |
| Alex     |        6 |      0 |       5 |       5 |         0 |      2 |     4 |        3 |      5 |         6 |         7 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        1 |      0 |       0 |       1 |         0 |      1 |     0 |        2 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jade     |        1 |      0 |       2 |       0 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |      -1 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        0 |      0 |       3 |       0 |         0 |      1 |     1 |        0 |      1 |         2 |         2 |      3 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |    -1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Greg     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |     -1 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Gathenji |        1 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |         -1 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        1 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |     -1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sai      |        1 |      0 |       0 |       1 |         0 |      0 |     1 |        1 |      1 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |    -1 |        0 |        0 |      0 |     0 |       0 |
| Nabeel   |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |       -1 |        0 |      0 |     0 |       0 |
| Ronnie   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |       -1 |      0 |     0 |       0 |
| Neha     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |     -1 |     0 |       0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |    -1 |       0 |
| Kawin    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |      -1 |

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|
| Rachel   |        0 |      4 |      31 |      35 |         4 |     21 |    13 |       22 |     31 |        28 |        41 |     10 |      5 |     19 |          1 |        0 |        1 |       1 |        1 |        3 |      2 |       1 |     4 |      0 |       1 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |
| Peter    |       31 |      5 |       0 |      39 |         1 |     20 |    22 |       27 |     42 |        26 |        36 |      8 |      3 |     29 |          1 |        0 |        1 |       7 |        1 |        2 |      2 |       2 |     2 |      2 |       1 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |
| Brian    |       35 |      2 |      39 |       0 |         4 |     27 |    20 |       25 |     42 |        41 |        44 |     19 |     11 |     32 |          1 |        0 |        1 |       6 |        1 |        5 |      2 |       2 |    11 |      0 |       0 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |
| Anthony  |        4 |      0 |       1 |       4 |         0 |      3 |     1 |        1 |      4 |         1 |         4 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |       21 |      3 |      20 |      27 |         3 |      0 |     7 |       20 |     21 |        12 |        18 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      5 |       0 |     3 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |
| Jai      |       13 |      3 |      22 |      20 |         1 |      7 |     0 |       14 |     14 |        22 |        19 |      8 |      0 |     14 |          1 |        0 |        0 |       1 |        0 |        2 |      3 |       0 |     2 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Jackie   |       22 |      4 |      27 |      25 |         1 |     20 |    14 |        0 |     25 |        20 |        27 |      7 |      4 |     18 |          0 |        1 |        0 |       4 |        0 |        2 |      3 |       1 |     1 |      0 |       0 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |
| Kate     |       31 |      6 |      42 |      42 |         4 |     21 |    14 |       25 |      0 |        36 |        41 |     16 |     10 |     34 |          2 |        0 |        0 |       2 |        0 |        1 |      5 |       1 |    10 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |
| Sushant  |       28 |      4 |      26 |      41 |         1 |     12 |    22 |       20 |     36 |         0 |        40 |     13 |      5 |     31 |          0 |        0 |        0 |      10 |        0 |        5 |      3 |       0 |     7 |      0 |       0 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |
| Abishek  |       41 |      4 |      36 |      44 |         4 |     18 |    19 |       27 |     41 |        40 |         0 |     16 |      7 |     35 |          0 |        0 |        0 |      12 |        0 |        5 |      2 |       1 |     6 |      1 |       1 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |
| Ruhi     |       10 |      1 |       8 |      19 |         0 |      4 |     8 |        7 |     16 |        13 |        16 |      0 |      2 |      7 |          0 |        0 |        0 |       5 |        0 |        0 |      1 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        5 |      5 |       3 |      11 |         2 |      2 |     0 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |
| Alex     |       19 |      4 |      29 |      32 |         0 |     17 |    14 |       18 |     34 |        31 |        35 |      7 |      1 |      0 |          1 |        0 |        0 |       2 |        0 |        2 |      4 |       0 |     2 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        1 |      1 |       7 |       6 |         0 |      4 |     1 |        4 |      2 |        10 |        12 |      5 |      1 |      2 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Jade     |        2 |      0 |       2 |       2 |         0 |      5 |     3 |        3 |      5 |         3 |         2 |      1 |      0 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        1 |      0 |       2 |       2 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        4 |      1 |       2 |      11 |         0 |      3 |     2 |        1 |     10 |         7 |         6 |      3 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Derek    |        1 |      0 |       1 |       0 |         0 |      0 |     2 |        0 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Gathenji |        1 |      0 |       3 |       3 |         0 |      0 |     1 |        2 |      3 |         3 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Caro     |        1 |      0 |       0 |       3 |         0 |      1 |     0 |        1 |      1 |         2 |         2 |      1 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sai      |        1 |      0 |       5 |       3 |         0 |      2 |     1 |        3 |      4 |         5 |         3 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Nabeel   |        2 |      3 |       0 |       3 |         0 |      0 |     1 |        2 |      1 |         0 |         2 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Ronnie   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      1 |         1 |         2 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Neha     |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |
| Ira      |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      1 |     0 |       1 |
| Kawin    |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |

### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   -1   |    0.24 |    0.48 |   0.44 |  0.21 |     0.47 |   0.39 |      0.38 |      0.5  |   0.17 |   0.43 |   0.36 |     0.4 |    -1    |   -1   | -1    |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.24 |   -1   |   -1    |    0.53 |   0.43 |  0.33 |     0.47 |   0.5  |      0.42 |      0.6  |   0.5  |   0.2  |   0.32 |    -1   |     0.14 |   -1   |  0.6  |      -1    |  -1   |
| Brian    |     0.48 |    0.5 |    0.53 |   -1    |   0.38 |  0.39 |     0.48 |   0.58 |      0.5  |      0.61 |   0.64 |   0.83 |   0.56 |     0.6 |    -1    |    0.4 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |    0.43 |    0.38 |  -1    |  0    |     0.25 |   0.53 |      0.38 |      0.45 |   0.2  |  -1    |   0.4  |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.21 |   -1   |    0.33 |    0.39 |   0    | -1    |     0.11 |   0.35 |      0.33 |      0.5  |  -1    |  -1    |   0.36 |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.47 |   -1   |    0.47 |    0.48 |   0.25 |  0.11 |    -1    |   0.45 |      0.53 |      0.5  |  -1    |  -1    |   0.47 |     0.4 |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.39 |    0.6 |    0.5  |    0.58 |   0.53 |  0.35 |     0.45 |  -1    |      0.42 |      0.59 |   0.3  |  -1    |   0.5  |     0.6 |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.38 |   -1   |    0.42 |    0.5  |   0.38 |  0.33 |     0.53 |   0.42 |     -1    |      0.53 |   0.42 |   0.4  |   0.43 |    -1   |    -1    |   -1   |  0.17 |      -1    |  -1   |
| Abishek  |     0.5  |    0.4 |    0.6  |    0.61 |   0.45 |  0.5  |     0.5  |   0.59 |      0.53 |     -1    |   0.5  |   0.83 |   0.54 |    -1   |    -1    |    0.4 |  0.5  |      -1    |   0.2 |
| Ruhi     |     0.17 |   -1   |    0.5  |    0.64 |   0.2  | -1    |    -1    |   0.3  |      0.42 |      0.5  |  -1    |  -1    |   0.56 |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Alex     |     0.36 |   -1   |    0.32 |    0.56 |   0.4  |  0.36 |     0.47 |   0.5  |      0.43 |      0.54 |   0.56 |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jeron    |     0.4  |   -1   |   -1    |    0.6  |  -1    | -1    |     0.4  |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jay      |    -1    |   -1   |    0.6  |   -1    |  -1    | -1    |    -1    |  -1    |      0.17 |      0.5  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|
| Rachel   |    -1    |   -1   |    0.24 |    0.44 |   0.44 |  0.24 |     0.47 |   0.36 |      0.39 |      0.47 |  -1    |   0.33 |   0.4  |     0.4 |    -1    |   -1   | -1    |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.24 |   -1   |   -1    |    0.5  |   0.33 |  0.25 |     0.44 |   0.42 |      0.39 |      0.56 |   0.5  |  -1    |   0.29 |    -1   |     0.14 |   -1   |  0.6  |      -1    |
| Brian    |     0.44 |    0.5 |    0.5  |   -1    |   0.33 |  0.35 |     0.46 |   0.55 |      0.48 |      0.58 |   0.56 |  -1    |   0.54 |     0.6 |    -1    |    0.4 | -1    |      -1    |
| Minh     |     0.44 |   -1   |    0.33 |    0.33 |  -1    |  0    |     0.1  |   0.46 |      0.29 |      0.42 |   0.2  |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.24 |   -1   |    0.25 |    0.35 |   0    | -1    |     0.11 |   0.35 |      0.33 |      0.46 |  -1    |  -1    |   0.44 |    -1   |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.47 |   -1   |    0.44 |    0.46 |   0.1  |  0.11 |    -1    |   0.39 |      0.47 |      0.47 |  -1    |  -1    |   0.43 |     0.4 |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.36 |    0.6 |    0.42 |    0.55 |   0.46 |  0.35 |     0.39 |  -1    |      0.35 |      0.54 |   0.3  |  -1    |   0.47 |     0.6 |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.39 |   -1   |    0.39 |    0.48 |   0.29 |  0.33 |     0.47 |   0.35 |     -1    |      0.5  |   0.42 |   0.4  |   0.41 |    -1   |    -1    |   -1   |  0.17 |      -1    |
| Abishek  |     0.47 |    0.4 |    0.56 |    0.58 |   0.42 |  0.46 |     0.47 |   0.54 |      0.5  |     -1    |   0.46 |   0.8  |   0.52 |    -1   |    -1    |    0.4 |  0.5  |      -1    |
| Ruhi     |    -1    |   -1   |    0.5  |    0.56 |   0.2  | -1    |    -1    |   0.3  |      0.42 |      0.46 |  -1    |  -1    |   0.67 |    -1   |    -1    |   -1   | -1    |      -1    |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Alex     |     0.4  |   -1   |    0.29 |    0.54 |  -1    |  0.44 |     0.43 |   0.47 |      0.41 |      0.52 |   0.67 |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jeron    |     0.4  |   -1   |   -1    |    0.6  |  -1    | -1    |     0.4  |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jay      |    -1    |   -1   |    0.6  |   -1    |  -1    | -1    |    -1    |  -1    |      0.17 |      0.5  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |
|----------|--------|----------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|
| Minh     |  -1    |     -1   | -1    |   0.8  |      0.33 |      0.6  |   -1   |   -1    |    -1   |     -1   |  -1    |
| Rachel   |  -1    |     -1   |  0    |   0.6  |      0.8  |     -1    |   -1   |   -1    |    -1   |     -1   |   0.5  |
| Jai      |  -1    |      0   | -1    |   0.67 |     -1    |      0.8  |   -1   |   -1    |    -1   |     -1   |  -1    |
| Kate     |   0.8  |      0.6 |  0.67 |  -1    |      0.33 |      0.9  |   -1   |    0.8  |    -1   |     -1   |   1    |
| Sushant  |   0.33 |      0.8 | -1    |   0.33 |     -1    |      0.78 |   -1   |    0.67 |     0.7 |     -1   |   0.67 |
| Abishek  |   0.6  |     -1   |  0.8  |   0.9  |      0.78 |     -1    |    0.6 |    0.8  |     0.7 |     -1   |   0.86 |
| Ruhi     |  -1    |     -1   | -1    |  -1    |     -1    |      0.6  |   -1   |   -1    |    -1   |     -1   |   0.5  |
| Brian    |  -1    |     -1   | -1    |   0.8  |      0.67 |      0.8  |   -1   |   -1    |     1   |      0.8 |   1    |
| Peter    |  -1    |     -1   | -1    |  -1    |      0.7  |      0.7  |   -1   |    1    |    -1   |     -1   |  -1    |
| Jackie   |  -1    |     -1   | -1    |  -1    |     -1    |     -1    |   -1   |    0.8  |    -1   |     -1   |  -1    |
| Alex     |  -1    |      0.5 | -1    |   1    |      0.67 |      0.86 |    0.5 |    1    |    -1   |     -1   |  -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |
|----------|--------|----------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|
| Minh     |  -1    |     -1   | -1    |   0.8  |      0.33 |      0.6  |   -1   |   -1    |    -1   |     -1   |  -1    |
| Rachel   |  -1    |     -1   | -1    |   0.6  |     -1    |     -1    |   -1   |   -1    |    -1   |     -1   |  -1    |
| Jai      |  -1    |     -1   | -1    |   0.67 |     -1    |      0.8  |   -1   |   -1    |    -1   |     -1   |  -1    |
| Kate     |   0.8  |      0.6 |  0.67 |  -1    |      0.33 |      0.9  |   -1   |    0.8  |    -1   |     -1   |   1    |
| Sushant  |   0.33 |     -1   | -1    |   0.33 |     -1    |      0.78 |   -1   |    0.67 |     0.7 |     -1   |   0.67 |
| Abishek  |   0.6  |     -1   |  0.8  |   0.9  |      0.78 |     -1    |    0.6 |    0.89 |     0.7 |     -1   |   0.86 |
| Ruhi     |  -1    |     -1   | -1    |  -1    |     -1    |      0.6  |   -1   |   -1    |    -1   |     -1   |  -1    |
| Brian    |  -1    |     -1   | -1    |   0.8  |      0.67 |      0.89 |   -1   |   -1    |     1   |      0.8 |   1    |
| Peter    |  -1    |     -1   | -1    |  -1    |      0.7  |      0.7  |   -1   |    1    |    -1   |     -1   |  -1    |
| Jackie   |  -1    |     -1   | -1    |  -1    |     -1    |     -1    |   -1   |    0.8  |    -1   |     -1   |  -1    |
| Alex     |  -1    |     -1   | -1    |   1    |      0.67 |      0.86 |   -1   |    1    |    -1   |     -1   |  -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |   Sai |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|-------|
| Peter    |   -1    |    0.41 |   0.62 |     0.5  |    0.2 |  0.56 |     0.44 |   0.53 |      0.48 |      0.41 |   0.75 |  -1    |   0.67 |    0.4  |     -1   | -1    |       -1   |   0.8 |
| Brian    |    0.59 |   -1    |   0.59 |     0.64 |   -1   |  0.67 |     0.5  |   0.57 |      0.59 |      0.5  |   0.74 |   0.64 |   0.67 |   -1    |      0.6 |  0.5  |       -1   |  -1   |
| Minh     |    0.38 |    0.41 |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.27 |      0.33 |      0.4  |  -1    |  -1    |   0.33 |   -1    |     -1   | -1    |       -1   |  -1   |
| Rachel   |    0.5  |    0.36 |   0.5  |    -1    |   -1   |  0.5  |     0.5  |   0.39 |      0.44 |      0.36 |   0.6  |   0.6  |   0.27 |   -1    |     -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.33 |  -1    |     0.5  |   -1   | -1    |     0.38 |   0.25 |      0.38 |      0.28 |   0.38 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |  -1   |
| Jackie   |    0.56 |    0.5  |   0.5  |     0.5  |   -1   |  0.62 |    -1    |   0.5  |      0.37 |      0.46 |   0.57 |  -1    |   0.53 |   -1    |     -1   | -1    |       -1   |  -1   |
| Kate     |    0.47 |    0.43 |   0.73 |     0.61 |    0.5 |  0.75 |     0.5  |  -1    |      0.54 |      0.41 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |  0.38 |       -1   |  -1   |
| Sushant  |    0.52 |    0.41 |   0.67 |     0.56 |   -1   |  0.62 |     0.63 |   0.46 |     -1    |      0.38 |   0.54 |   0.4  |   0.43 |    0.57 |      0.6 |  0.2  |       -1   |   0.8 |
| Abishek  |    0.59 |    0.5  |   0.6  |     0.64 |   -1   |  0.72 |     0.54 |   0.59 |      0.62 |     -1    |   0.69 |   0.71 |   0.59 |    0.56 |      0.6 |  0.6  |        0.8 |  -1   |
| Ruhi     |    0.25 |    0.26 |  -1    |     0.4  |   -1   |  0.62 |     0.43 |   0.38 |      0.46 |      0.31 |  -1    |  -1    |   0.57 |    0.6  |     -1   | -1    |       -1   |  -1   |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Alex     |    0.33 |    0.33 |   0.67 |     0.73 |   -1   |  0.73 |     0.47 |   0.48 |      0.57 |      0.41 |   0.43 |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.43 |      0.44 |   0.4  |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jay      |   -1    |    0.5  |  -1    |    -1    |   -1   | -1    |    -1    |   0.62 |      0.8  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|
| Peter    |   -1    |    0.39 |   0.62 |     0.45 |    0.2 |  0.53 |     0.44 |   0.53 |      0.45 |      0.39 |   0.71 |  -1    |   0.64 |    0.4  |     -1   | -1    |       -1   |
| Brian    |    0.61 |   -1    |   0.6  |     0.61 |   -1   |  0.64 |     0.53 |   0.58 |      0.6  |      0.5  |   0.71 |   0.6  |   0.67 |   -1    |      0.6 |  0.5  |       -1   |
| Minh     |    0.38 |    0.4  |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.29 |      0.33 |      0.38 |  -1    |  -1    |   0.29 |   -1    |     -1   | -1    |       -1   |
| Rachel   |    0.55 |    0.39 |   0.5  |    -1    |   -1   |  0.56 |     0.53 |   0.42 |      0.48 |      0.39 |   0.6  |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |
| Jai      |    0.47 |    0.36 |  -1    |     0.44 |   -1   | -1    |     0.43 |   0.3  |      0.39 |      0.31 |   0.38 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |
| Jackie   |    0.56 |    0.47 |   0.5  |     0.47 |   -1   |  0.57 |    -1    |   0.5  |      0.37 |      0.43 |   0.5  |  -1    |   0.5  |   -1    |     -1   | -1    |       -1   |
| Kate     |    0.47 |    0.42 |   0.71 |     0.58 |    0.5 |  0.7  |     0.5  |  -1    |      0.54 |      0.4  |   0.62 |   0.33 |   0.48 |   -1    |     -1   |  0.38 |       -1   |
| Sushant  |    0.55 |    0.4  |   0.67 |     0.52 |   -1   |  0.61 |     0.63 |   0.46 |     -1    |      0.37 |   0.5  |  -1    |   0.38 |    0.57 |      0.6 |  0.2  |       -1   |
| Abishek  |    0.61 |    0.5  |   0.62 |     0.61 |   -1   |  0.69 |     0.57 |   0.6  |      0.63 |     -1    |   0.64 |   0.67 |   0.57 |    0.56 |      0.6 |  0.6  |        0.8 |
| Ruhi     |    0.29 |    0.29 |  -1    |     0.4  |   -1   |  0.62 |     0.5  |   0.38 |      0.5  |      0.36 |  -1    |  -1    |   0.57 |    0.6  |     -1   | -1    |       -1   |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Alex     |    0.36 |    0.33 |   0.71 |     0.73 |   -1   |  0.73 |     0.5  |   0.52 |      0.62 |      0.43 |   0.43 |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.43 |      0.44 |   0.4  |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jay      |   -1    |    0.5  |  -1    |    -1    |   -1   | -1    |    -1    |   0.62 |      0.8  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.368421 |            19 |
| 2+2        | 0.369565 |            46 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.333333 |            18 |
| 2+2        | 0.309524 |            42 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.411765 |            17 |
| Success      | 0.344262 |            61 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.411765 |            17 |
| Success      | 0.322034 |            59 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      20 | 0.434783 |     0.35     |
|         1 |      18 | 0.391304 |     0.111111 |
|         2 |       8 | 0.173913 |     0.5      |

*2 bad guys on mission 1:*

|   # Fails |   Count |   % |   Good Win % |
|-----------|---------|-----|--------------|
|         0 |       7 | 0.7 |     0.142857 |
|         1 |       3 | 0.3 |     0        |

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
|                   0 |            19 |     0.473684 |
|                   1 |            87 |     0.344828 |
|                   2 |            12 |     0.583333 |
|                   3 |             2 |     0.5      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            17 |     0.411765 |
|                   1 |            81 |     0.296296 |
|                   2 |            12 |     0.583333 |
|                   3 |             2 |     0.5      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.11667 |           120 |              14 |
| Assassin      |                 0.04505 |           111 |               5 |
| Morgana       |                 0.05    |           120 |               6 |
| Mordred       |                 0.0125  |            80 |               1 |
| Loyal Servant |                 0       |           364 |               0 |
| Oberon        |                 0       |            34 |               0 |
| Minion #1     |                 0       |            17 |               0 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Jai      |                   0.428571  |                  3 |             7 |
| Rachel   |                   0.416667  |                  5 |            12 |
| Alex     |                   0.352941  |                  6 |            17 |
| Abishek  |                   0.318182  |                  7 |            22 |
| Kate     |                   0.285714  |                  6 |            21 |
| Minh     |                   0.285714  |                  2 |             7 |
| Jackie   |                   0.266667  |                  4 |            15 |
| Sushant  |                   0.181818  |                  2 |            11 |
| Peter    |                   0.142857  |                  2 |            14 |
| Brian    |                   0.0869565 |                  2 |            23 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Minh     |          0        |                  0 |             3 |
| Sushant  |          0.142857 |                  1 |             7 |
| Brian    |          0.222222 |                  2 |             9 |
| Jai      |          0.333333 |                  1 |             3 |
| Jeron    |          0.333333 |                  1 |             3 |
| Kate     |          0.444444 |                  4 |             9 |
| Abishek  |          0.454545 |                  5 |            11 |
| Jackie   |          0.5      |                  4 |             8 |
| Rachel   |          0.6      |                  6 |            10 |
| Peter    |          0.666667 |                  8 |            12 |
| Alex     |          0.75     |                  3 |             4 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

|   # Players |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
|           5 |          0.8      |                  4 |             5 |
|           6 |          0.357143 |                  5 |            14 |
|           7 |          0.526316 |                 10 |            19 |
|           8 |          0.529412 |                  9 |            17 |
|           9 |          0.384615 |                  5 |            13 |
|          10 |          0.4      |                  6 |            15 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

|   # Players |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
|           5 |                   0 |          0.5      |                  1 |             2 |
|           5 |                   1 |          1        |                  3 |             3 |
|           6 |                   0 |          0.5      |                  3 |             6 |
|           6 |                   1 |          0.285714 |                  2 |             7 |
|           6 |                   3 |          0        |                  0 |             1 |
|           7 |                   0 |          0.555556 |                  5 |             9 |
|           7 |                   1 |          0.625    |                  5 |             8 |
|           7 |                   2 |          0        |                  0 |             2 |
|           8 |                   0 |          0.5      |                  1 |             2 |
|           8 |                   1 |          0.533333 |                  8 |            15 |
|           9 |                   1 |          0.363636 |                  4 |            11 |
|           9 |                   2 |          0.5      |                  1 |             2 |
|          10 |                   1 |          0.5      |                  6 |            12 |
|          10 |                   2 |          0        |                  0 |             3 |
