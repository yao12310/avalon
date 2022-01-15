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
python -m avalon.main db_write --player_write {True/False, optional, default=True}
```

The script will prompt you to enter each column value for the data row one-by-one.

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
9. [Player/role counts/percentages](#player-role-cnts-pcts)
10. [Percentage of times two players are on the same team](#pair-teams-pct)
11. [Percentage of times two players are both bad](#pair-bad-team-pct)
12. [Percentage of times two players are on different teams](#pair-opp-teams-pct)
13. [Count of times two players are on the same team](#pair-teams-cnt)
14. [Count of times two players are both bad](#pair-bad-team-cnt)
15. [Count of times two players are on different teams](#pair-opp-teams-cnt)
16. [Percentage of times two players win, given that they are on the same team](#pair-teams-win-pct)
17. [Percentage of times two players win, given that they are both bad](#pair-bad-team-win-pct)
18. [Percentage of times two players win, given that they are on opposite teams](#pair-opp-teams-win-pct)
19. [3+1 vs 2+2 strategy success rate](#mission2)
20. [Good win rate w.r.t. R1 fail](#r1-fail)
21. [Flip statistics for different # bad guys and mission index](#flip-stats)
22. [Good win % w.r.t. # Percival claims](#good-win-num-percival)
23. [Percentage of time each role fake claims Percival](#role-fake-percival)
24. [% of time players are wrongly assassinated as non-Merlin good guy](#wrongly-assassinated)
25. [% of time players are correctly assassinated as Merlin](#correctly-assassinated)
26. [% of time Merlin is assassinated by game size](#assassination-game-size)
27. [% of time Merlin is assassinated by game size and # Percival claims](#assassination-game-size-percival)
28. [Mission success/fail sequence counts](#pass-fail-sequences)
## Stats

Note: The friends and memories made in this game far outweigh any statistic you will find on this page. In any case, most of these stats are super high variance: especially individual stats, which depend heavily on team composition.

### <a id="good-win"></a>Good win %

Cheesy wins included: 0.4462 (n = 260)

Cheesy wins excluded: 0.4217 (n = 249)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            32 |     0.40625  |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5P          |             1 |     0        |
| 5X          |             8 |     0.5      |
| 6           |            32 |     0.625    |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            35 |     0.371429 |
| 7O          |            13 |     0.538462 |
| 8           |            43 |     0.325581 |
| 8O          |             4 |     0.25     |
| 9           |            46 |     0.369565 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

Cheesy wins excluded:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            31 |     0.387097 |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5P          |             1 |     0        |
| 5X          |             8 |     0.5      |
| 6           |            30 |     0.6      |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            32 |     0.3125   |
| 7O          |            13 |     0.538462 |
| 8           |            43 |     0.325581 |
| 8O          |             4 |     0.25     |
| 9           |            41 |     0.292683 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           129 |       29.2171 |     19.1009 |
| Good     |           104 |       20.4519 |     16.6062 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           129 |       29.2171 |     19.1009 |
| Good     |            97 |       21.3711 |     16.8228 |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|---------|------------|
| Kate     |          10 |
| Abishek  |           6 |
| Peter    |           4 |
| Brian    |           3 |
| Jackie   |           2 |
| Rachel   |           2 |
| Minh     |           1 |
| Sachin   |           1 |
| Sushant  |           1 |

### <a id="win-rate-leaderboard"></a>Win rate leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Games Behind column reports # games needed to win in a row in order to pass leader.*

Cheesy wins included:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|-------------|------------|--------------|-------|---------|-----------------------|
| Abishek  | 0.589286 |     0.5      |    0.708333 |           112 |     66 |       46 |                      0 |
| Brian    | 0.571429 |     0.488095 |    0.738095 |           126 |     72 |       54 |                      6 |
| Daisy    | 0.545455 |     0.571429 |    0.5      |            11 |      6 |        5 |                      2 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      2 |
| Kate     | 0.53271  |     0.486111 |    0.628571 |           107 |     57 |       50 |                     15 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|---------|---------|-------------|------------|--------------|-------|---------|-----------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.576923 |     0.448276 |    0.73913  |           104 |     60 |       44 |                      7 |
| Brian    | 0.559322 |     0.448718 |    0.775    |           118 |     66 |       52 |                     13 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kate     | 0.51     |     0.439394 |    0.647059 |           100 |     51 |       49 |                     23 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|---------|----------------------|---------|-----------------|---------|
| Daisy    |             0.146293  | 0.545455 |         0.399161 | 0.636364 |
| Brian    |             0.0882771 | 0.571429 |         0.483151 | 0.666667 |
| Abishek  |             0.0781223 | 0.589286 |         0.511163 | 0.571429 |
| Kish     |             0.0745448 | 0.529412 |         0.454867 | 0.588235 |
| Kate     |             0.0488818 | 0.53271  |         0.483828 | 0.672897 |
| Ewen     |             0.0439332 | 0.538462 |         0.494528 | 0.615385 |
| Anthony  |             0.0347222 | 0.5      |         0.465278 | 0.166667 |
| Peter    |             0.0225268 | 0.48     |         0.457473 | 0.62     |
| Andrew   |             0.0163095 | 0.466667 |         0.450357 | 0.8      |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|---------|----------------------|---------|-----------------|---------|
| Anthony  |             0.126957  | 0.6      |         0.473043 | 0.166667 |
| Daisy    |             0.105337  | 0.5      |         0.394663 | 0.636364 |
| Brian    |             0.0891742 | 0.559322 |         0.470148 | 0.666667 |
| Abishek  |             0.0740088 | 0.576923 |         0.502914 | 0.571429 |
| Ewen     |             0.0646966 | 0.538462 |         0.473765 | 0.615385 |
| Kate     |             0.0346068 | 0.51     |         0.475393 | 0.672897 |
| Kish     |             0.02036   | 0.5      |         0.47964  | 0.588235 |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|---------|---------|--------------|-------|---------|---------------------|
| Brian    | 0.615385 |            13 |      8 |        5 |                    0 |
| Minh     | 0.571429 |             7 |      4 |        3 |                    1 |
| Kate     | 0.538462 |            13 |      7 |        6 |                    3 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Sushant |
|---------|---------|--------------|-------|---------|-----------------------|
| Sushant  | 0.714286 |             7 |      5 |        2 |                      0 |
| Kate     | 0.692308 |            13 |      9 |        4 |                      2 |
| Jackie   | 0.636364 |            11 |      7 |        4 |                      4 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Ruhi |
|---------|---------|--------------|-------|---------|--------------------|
| Ruhi     | 0.8      |             5 |      4 |        1 |                   0 |
| Abishek  | 0.692308 |            13 |      9 |        4 |                   8 |
| Brian    | 0.642857 |            14 |      9 |        5 |                  12 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.75     |            16 |     12 |        4 |                      0 |
| Brian    | 0.722222 |            18 |     13 |        5 |                      3 |
| Minh     | 0.666667 |             6 |      4 |        2 |                      3 |

*Mordred:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|---------|--------|--------------|-------|---------|--------------------|
| Kate     |    1    |            10 |     10 |        0 |                   0 |
| Brian    |    1    |             9 |      9 |        0 |                 nan |
| Sushant  |    0.75 |             8 |      6 |        2 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.606061 |            33 |     20 |       13 |                      0 |
| Ruhi     | 0.538462 |            13 |      7 |        6 |                      3 |
| Daisy    | 0.5      |             6 |      3 |        3 |                      2 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|---------|---------|--------------|-------|---------|---------------------|
| Brian    | 0.583333 |            12 |      7 |        5 |                    0 |
| Kate     | 0.538462 |            13 |      7 |        6 |                    2 |
| Peter    | 0.428571 |            14 |      6 |        8 |                    6 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Sushant |
|---------|---------|--------------|-------|---------|-----------------------|
| Sushant  | 0.714286 |             7 |      5 |        2 |                      0 |
| Kate     | 0.636364 |            11 |      7 |        4 |                      4 |
| Jackie   | 0.6      |            10 |      6 |        4 |                      5 |

*Assassin:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Ruhi |
|---------|--------|--------------|-------|---------|--------------------|
| Ruhi     |    0.8  |             5 |      4 |        1 |                   0 |
| Abishek  |    0.75 |            12 |      9 |        3 |                   4 |
| Alex     |    0.7  |            10 |      7 |        3 |                   6 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.8      |            15 |     12 |        3 |                      0 |
| Minh     | 0.8      |             5 |      4 |        1 |                      1 |
| Brian    | 0.764706 |            17 |     13 |        4 |                      4 |

*Mordred:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|---------|--------|--------------|-------|---------|--------------------|
| Kate     |    1    |            10 |     10 |        0 |                   0 |
| Brian    |    1    |             9 |      9 |        0 |                 nan |
| Sushant  |    0.75 |             8 |      6 |        2 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.535714 |            28 |     15 |       13 |                      0 |
| Ruhi     | 0.454545 |            11 |      5 |        6 |                      2 |
| Brian    | 0.4375   |            48 |     21 |       27 |                     11 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|---------|---------------|
| Brian    |            236 |
| Kate     |            198 |
| Peter    |            194 |
| Jackie   |            186 |
| Abishek  |            179 |
| Sushant  |            147 |
| Rachel   |            136 |
| Jai      |             96 |
| Alex     |             94 |
| Minh     |             72 |
| Ruhi     |             49 |
| Aman     |             37 |
| Jeron    |             32 |
| Jay      |             26 |
| Daisy    |             25 |
| Tercel   |             24 |
| Kish     |             21 |
| Jade     |             20 |
| Andrew   |             17 |
| Vishal   |             13 |
| Ewen     |             13 |
| Anthony  |             12 |
| Justin   |              9 |
| Sai      |              8 |
| Karthik  |              7 |
| Gathenji |              7 |
| Megan    |              6 |
| Olivia   |              5 |
| Sofia    |              5 |
| Kevin    |              5 |
| Selena   |              5 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|---------|---------|---------|--------|
| Gathenji | 0.857143 |        6 |       1 |
| Jade     | 0.8      |       16 |       4 |
| Andrew   | 0.764706 |       13 |       4 |
| Rachel   | 0.727941 |       99 |      37 |
| Daisy    | 0.72     |       18 |       7 |
| Karthik  | 0.714286 |        5 |       2 |
| Kate     | 0.681818 |      135 |      63 |
| Megan    | 0.666667 |        4 |       2 |
| Tercel   | 0.666667 |       16 |       8 |
| Justin   | 0.666667 |        6 |       3 |
| Jeron    | 0.65625  |       21 |      11 |
| Jackie   | 0.639785 |      119 |      67 |
| Alex     | 0.638298 |       60 |      34 |
| Peter    | 0.634021 |      123 |      71 |
| Brian    | 0.627119 |      148 |      88 |
| Sai      | 0.625    |        5 |       3 |
| Jai      | 0.625    |       60 |      36 |
| Kish     | 0.619048 |       13 |       8 |
| Ewen     | 0.615385 |        8 |       5 |
| Jay      | 0.615385 |       16 |      10 |
| Olivia   | 0.6      |        3 |       2 |
| Selena   | 0.6      |        3 |       2 |
| Aman     | 0.594595 |       22 |      15 |
| Minh     | 0.583333 |       42 |      30 |
| Sushant  | 0.571429 |       84 |      63 |
| Abishek  | 0.564246 |      101 |      78 |
| Vishal   | 0.538462 |        7 |       6 |
| Ruhi     | 0.530612 |       26 |      23 |
| Sofia    | 0.4      |        2 |       3 |
| Anthony  | 0.25     |        3 |       9 |
| Kevin    | 0        |        0 |       5 |

### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |       21 |         24 |         24 |        23 |         9 |       11 |          11 |              56 |           179 |
| Alex     |       13 |         13 |         13 |        14 |         4 |        2 |           1 |              34 |            94 |
| Aman     |        6 |          7 |          3 |         6 |         3 |        3 |           0 |               9 |            37 |
| Andrew   |        5 |          2 |          1 |         1 |         1 |        1 |           0 |               6 |            17 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       27 |         42 |         27 |        36 |        16 |        6 |           3 |              79 |           236 |
| Daisy    |        4 |          1 |          1 |         4 |         1 |        1 |           0 |              13 |            25 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       28 |         23 |         19 |        26 |        10 |        9 |           3 |              68 |           186 |
| Jade     |        5 |          3 |          1 |         1 |         1 |        1 |           0 |               8 |            20 |
| Jai      |       12 |         11 |          8 |        14 |         9 |        4 |           1 |              37 |            96 |
| Jay      |        4 |          3 |          4 |         0 |         5 |        1 |           0 |               9 |            26 |
| Jeron    |        5 |          9 |          2 |         5 |         2 |        1 |           1 |               7 |            32 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Karthik  |        2 |          0 |          0 |         1 |         0 |        0 |           1 |               3 |             7 |
| Kate     |       23 |         23 |         13 |        19 |        14 |       15 |           2 |              89 |           198 |
| Kevin    |        0 |          0 |          1 |         3 |         1 |        0 |           0 |               0 |             5 |
| Kish     |        3 |          4 |          1 |         4 |         2 |        0 |           1 |               6 |            21 |
| Megan    |        2 |          0 |          0 |         0 |         0 |        2 |           0 |               2 |             6 |
| Minh     |        9 |          8 |         12 |         7 |         7 |        2 |           2 |              25 |            72 |
| Olivia   |        1 |          0 |          1 |         0 |         1 |        0 |           0 |               2 |             5 |
| Peter    |       31 |         23 |         26 |        22 |        12 |        8 |           3 |              69 |           194 |
| Rachel   |       20 |         21 |         11 |        13 |        10 |        0 |           3 |              58 |           136 |
| Ruhi     |        2 |          6 |          8 |         7 |         7 |        1 |           0 |              18 |            49 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Selena   |        0 |          0 |          0 |         0 |         1 |        1 |           0 |               3 |             5 |
| Sofia    |        0 |          1 |          1 |         2 |         0 |        0 |           0 |               1 |             5 |
| Sushant  |       23 |         11 |         23 |        23 |         9 |        6 |           2 |              50 |           147 |
| Tercel   |        2 |          5 |          4 |         1 |         3 |        0 |           0 |               9 |            24 |
| Vishal   |        3 |          0 |          3 |         2 |         1 |        0 |           0 |               4 |            13 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.082 |      0.096 |      0.111 |     0.093 |     0.067 |    0.136 |       0.314 |           0.08  |           179 |
| Alex     |    0.051 |      0.052 |      0.06  |     0.057 |     0.03  |    0.025 |       0.029 |           0.049 |            94 |
| Aman     |    0.023 |      0.028 |      0.014 |     0.024 |     0.022 |    0.037 |       0     |           0.013 |            37 |
| Andrew   |    0.019 |      0.008 |      0.005 |     0.004 |     0.007 |    0.012 |       0     |           0.009 |            17 |
| Anthony  |    0     |      0.008 |      0.018 |     0.016 |     0     |    0.012 |       0     |           0.001 |            12 |
| Brian    |    0.105 |      0.169 |      0.124 |     0.146 |     0.119 |    0.074 |       0.086 |           0.113 |           236 |
| Daisy    |    0.016 |      0.004 |      0.005 |     0.016 |     0.007 |    0.012 |       0     |           0.019 |            25 |
| Ewen     |    0.004 |      0.008 |      0.009 |     0.004 |     0     |    0.025 |       0     |           0.007 |            13 |
| Gathenji |    0     |      0     |      0     |     0.004 |     0     |    0     |       0     |           0.009 |             7 |
| Jackie   |    0.109 |      0.092 |      0.088 |     0.106 |     0.074 |    0.111 |       0.086 |           0.097 |           186 |
| Jade     |    0.019 |      0.012 |      0.005 |     0.004 |     0.007 |    0.012 |       0     |           0.011 |            20 |
| Jai      |    0.047 |      0.044 |      0.037 |     0.057 |     0.067 |    0.049 |       0.029 |           0.053 |            96 |
| Jay      |    0.016 |      0.012 |      0.018 |     0     |     0.037 |    0.012 |       0     |           0.013 |            26 |
| Jeron    |    0.019 |      0.036 |      0.009 |     0.02  |     0.015 |    0.012 |       0.029 |           0.01  |            32 |
| Justin   |    0.008 |      0     |      0.005 |     0.004 |     0.007 |    0     |       0     |           0.006 |             9 |
| Karthik  |    0.008 |      0     |      0     |     0.004 |     0     |    0     |       0.029 |           0.004 |             7 |
| Kate     |    0.089 |      0.092 |      0.06  |     0.077 |     0.104 |    0.185 |       0.057 |           0.127 |           198 |
| Kevin    |    0     |      0     |      0.005 |     0.012 |     0.007 |    0     |       0     |           0     |             5 |
| Kish     |    0.012 |      0.016 |      0.005 |     0.016 |     0.015 |    0     |       0.029 |           0.009 |            21 |
| Megan    |    0.008 |      0     |      0     |     0     |     0     |    0.025 |       0     |           0.003 |             6 |
| Minh     |    0.035 |      0.032 |      0.055 |     0.028 |     0.052 |    0.025 |       0.057 |           0.036 |            72 |
| Olivia   |    0.004 |      0     |      0.005 |     0     |     0.007 |    0     |       0     |           0.003 |             5 |
| Peter    |    0.121 |      0.092 |      0.12  |     0.089 |     0.089 |    0.099 |       0.086 |           0.098 |           194 |
| Rachel   |    0.078 |      0.084 |      0.051 |     0.053 |     0.074 |    0     |       0.086 |           0.083 |           136 |
| Ruhi     |    0.008 |      0.024 |      0.037 |     0.028 |     0.052 |    0.012 |       0     |           0.026 |            49 |
| Sai      |    0.004 |      0.004 |      0     |     0.004 |     0.015 |    0     |       0     |           0.004 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.007 |    0.012 |       0     |           0.004 |             5 |
| Sofia    |    0     |      0.004 |      0.005 |     0.008 |     0     |    0     |       0     |           0.001 |             5 |
| Sushant  |    0.089 |      0.044 |      0.106 |     0.093 |     0.067 |    0.074 |       0.057 |           0.071 |           147 |
| Tercel   |    0.008 |      0.02  |      0.018 |     0.004 |     0.022 |    0     |       0     |           0.013 |            24 |
| Vishal   |    0.012 |      0     |      0.014 |     0.008 |     0.007 |    0     |       0     |           0.006 |            13 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.117 |      0.134 |      0.134 |     0.128 |     0.05  |    0.061 |       0.061 |           0.313 |           179 |
| Alex     |    0.138 |      0.138 |      0.138 |     0.149 |     0.043 |    0.021 |       0.011 |           0.362 |            94 |
| Aman     |    0.162 |      0.189 |      0.081 |     0.162 |     0.081 |    0.081 |       0     |           0.243 |            37 |
| Andrew   |    0.294 |      0.118 |      0.059 |     0.059 |     0.059 |    0.059 |       0     |           0.353 |            17 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.114 |      0.178 |      0.114 |     0.153 |     0.068 |    0.025 |       0.013 |           0.335 |           236 |
| Daisy    |    0.16  |      0.04  |      0.04  |     0.16  |     0.04  |    0.04  |       0     |           0.52  |            25 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.151 |      0.124 |      0.102 |     0.14  |     0.054 |    0.048 |       0.016 |           0.366 |           186 |
| Jade     |    0.25  |      0.15  |      0.05  |     0.05  |     0.05  |    0.05  |       0     |           0.4   |            20 |
| Jai      |    0.125 |      0.115 |      0.083 |     0.146 |     0.094 |    0.042 |       0.01  |           0.385 |            96 |
| Jay      |    0.154 |      0.115 |      0.154 |     0     |     0.192 |    0.038 |       0     |           0.346 |            26 |
| Jeron    |    0.156 |      0.281 |      0.062 |     0.156 |     0.062 |    0.031 |       0.031 |           0.219 |            32 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Karthik  |    0.286 |      0     |      0     |     0.143 |     0     |    0     |       0.143 |           0.429 |             7 |
| Kate     |    0.116 |      0.116 |      0.066 |     0.096 |     0.071 |    0.076 |       0.01  |           0.449 |           198 |
| Kevin    |    0     |      0     |      0.2   |     0.6   |     0.2   |    0     |       0     |           0     |             5 |
| Kish     |    0.143 |      0.19  |      0.048 |     0.19  |     0.095 |    0     |       0.048 |           0.286 |            21 |
| Megan    |    0.333 |      0     |      0     |     0     |     0     |    0.333 |       0     |           0.333 |             6 |
| Minh     |    0.125 |      0.111 |      0.167 |     0.097 |     0.097 |    0.028 |       0.028 |           0.347 |            72 |
| Olivia   |    0.2   |      0     |      0.2   |     0     |     0.2   |    0     |       0     |           0.4   |             5 |
| Peter    |    0.16  |      0.119 |      0.134 |     0.113 |     0.062 |    0.041 |       0.015 |           0.356 |           194 |
| Rachel   |    0.147 |      0.154 |      0.081 |     0.096 |     0.074 |    0     |       0.022 |           0.426 |           136 |
| Ruhi     |    0.041 |      0.122 |      0.163 |     0.143 |     0.143 |    0.02  |       0     |           0.367 |            49 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.2   |    0.2   |       0     |           0.6   |             5 |
| Sofia    |    0     |      0.2   |      0.2   |     0.4   |     0     |    0     |       0     |           0.2   |             5 |
| Sushant  |    0.156 |      0.075 |      0.156 |     0.156 |     0.061 |    0.041 |       0.014 |           0.34  |           147 |
| Tercel   |    0.083 |      0.208 |      0.167 |     0.042 |     0.125 |    0     |       0     |           0.375 |            24 |
| Vishal   |    0.231 |      0     |      0.231 |     0.154 |     0.077 |    0     |       0     |           0.308 |            13 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     1    |   0.5  |    0.47 |    0.45 |      0.33 |   0.43 |  0.55 |     0.54 |   0.48 |      0.5  |      0.36 |   0.43 |   0.6  |   0.56 |    0.73 |     0.57 |   0.73 |    -1   |  0.72 |       0.86 | -1    |     0.4  |      0.57 |     0.44 |     -1   |    1    |  -1    |   -1    |    -1    |     0   |      0.6 |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.47 |   0.17 |    1    |    0.5  |      0.43 |   0.44 |  0.5  |     0.48 |   0.42 |      0.49 |      0.44 |   0.48 |   0.55 |   0.45 |    0.45 |     0.78 |   0.53 |    -1   |  0.65 |      -1    |  0.29 |     0.55 |     -1    |    -1    |     -1   |    0.4  |   0.56 |    0.5  |     0.47 |    -1   |     -1   |
| Brian    |     0.45 |   0.83 |    0.5  |    1    |      0.25 |   0.43 |  0.54 |     0.4  |   0.5  |      0.43 |      0.5  |   0.32 |   0.38 |   0.46 |    0.5  |     0.44 |   0.6  |     0.2 |  0.3  |       0.5  |  0.62 |     0.55 |      0.43 |     0.54 |      0.6 |    0.3  |   0.53 |    0.5  |     0.53 |    -1   |     -1   |
| Anthony  |     0.33 |  -1    |    0.43 |    0.25 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.43 |   0.4  |    0.44 |    0.43 |      0.5  |   1    |  0.46 |     0.46 |   0.48 |      0.64 |      0.5  |   0.5  |   0.67 |   0.32 |    0.29 |    -1    |   0.12 |    -1   |  0.33 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.75 |   0.22 |   -1    |     0.71 |     0.2 |      0.4 |
| Jai      |     0.55 |   0.4  |    0.5  |    0.54 |      0.29 |   0.46 |  1    |     0.44 |   0.58 |      0.37 |      0.4  |   0.24 |  -1    |   0.51 |    0.5  |    -1    |   0.4  |    -1   |  0.23 |       0.8  | -1    |     0.56 |      0.67 |     0    |     -1   |    0.2  |   0.5  |   -1    |     0.8  |    -1   |     -1   |
| Jackie   |     0.54 |   0.33 |    0.48 |    0.4  |      0.17 |   0.46 |  0.44 |     1    |   0.54 |      0.43 |      0.38 |   0.46 |   0.38 |   0.58 |    0.57 |    -1    |   0.43 |     0.6 |  0.6  |      -1    |  0.4  |     0.33 |      0.57 |     0.38 |     -1   |    0.75 |   0.5  |   -1    |     0.46 |    -1   |     -1   |
| Kate     |     0.48 |   0.45 |    0.42 |    0.5  |      0.33 |   0.48 |  0.58 |     0.54 |   1    |      0.41 |      0.5  |   0.45 |   0.33 |   0.45 |    0.64 |     0.83 |   0.43 |    -1   |  0.4  |       0.57 |  0.5  |     0.41 |     -1    |     0.57 |      0.2 |    0.52 |   0.3  |    0.67 |     0.69 |     0.6 |      0.4 |
| Sushant  |     0.5  |   0.43 |    0.49 |    0.43 |     -1    |   0.64 |  0.37 |     0.43 |   0.41 |      1    |      0.48 |   0.47 |   0.55 |   0.44 |    0.29 |     0.17 |   0.5  |    -1   |  0.45 |       0.5  |  0.38 |    -1    |     -1    |    -1    |     -1   |    0.83 |   0.39 |   -1    |     0.57 |    -1   |     -1   |
| Abishek  |     0.36 |   0.56 |    0.44 |    0.5  |      0.2  |   0.5  |  0.4  |     0.38 |   0.5  |      0.48 |      1    |   0.43 |   0.5  |   0.43 |    0.21 |     0.38 |   0.56 |    -1   |  0.46 |       0.29 |  0.62 |    -1    |      0.14 |     0.54 |     -1   |    0.5  |   0.44 |   -1    |     0.67 |    -1   |     -1   |
| Ruhi     |     0.43 |  -1    |    0.48 |    0.32 |     -1    |   0.5  |  0.24 |     0.46 |   0.45 |      0.47 |      0.43 |   1    |   0.71 |   0.53 |    0.44 |    -1    |  -1    |    -1   |  0.57 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.57 |  -1    |   -1    |    -1    |    -1   |     -1   |
| Kish     |     0.6  |   0    |    0.55 |    0.38 |     -1    |   0.67 | -1    |     0.38 |   0.33 |      0.55 |      0.5  |   0.71 |   1    |  -1    |    0.2  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Alex     |     0.56 |   0.2  |    0.45 |    0.46 |     -1    |   0.32 |  0.51 |     0.58 |   0.45 |      0.44 |      0.43 |   0.53 |  -1    |   1    |    0.4  |     0.67 |   0.2  |    -1   |  0.45 |       0.4  |  0.5  |     0.38 |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jeron    |     0.73 |  -1    |    0.45 |    0.5  |      0.5  |   0.29 |  0.5  |     0.57 |   0.64 |      0.29 |      0.21 |   0.44 |   0.2  |   0.4  |    1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jade     |     0.73 |  -1    |    0.53 |    0.6  |     -1    |   0.12 |  0.4  |     0.43 |   0.43 |      0.5  |      0.56 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Sofia    |    -1    |  -1    |   -1    |    0.2  |     -1    |  -1    | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |     1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jay      |     0.72 |  -1    |    0.65 |    0.3  |     -1    |   0.33 |  0.23 |     0.6  |   0.4  |      0.45 |      0.46 |   0.57 |  -1    |   0.45 |   -1    |    -1    |  -1    |    -1   |  1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    |    -1   | -1    |       1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    |  1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Tercel   |     0.4  |  -1    |    0.55 |    0.55 |     -1    |  -1    |  0.56 |     0.33 |   0.41 |     -1    |     -1    |  -1    |  -1    |   0.38 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     1    |     -1    |    -1    |      0.6 |    0.38 |   0.71 |    0.33 |    -1    |    -1   |     -1   |
| Karthik  |     0.57 |  -1    |   -1    |    0.43 |     -1    |  -1    |  0.67 |     0.57 |  -1    |     -1    |      0.14 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      1    |     0.29 |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Vishal   |     0.44 |  -1    |   -1    |    0.54 |     -1    |  -1    |  0    |     0.38 |   0.57 |     -1    |      0.54 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0.29 |     1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Olivia   |    -1    |  -1    |   -1    |    0.6  |     -1    |  -1    | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.6  |     -1    |    -1    |      1   |    0.4  |  -1    |   -1    |    -1    |    -1   |     -1   |
| Daisy    |     1    |  -1    |    0.4  |    0.3  |     -1    |   0.75 |  0.2  |     0.75 |   0.52 |      0.83 |      0.5  |   0.57 |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.38 |     -1    |    -1    |      0.4 |    1    |   0.31 |   -1    |     0.44 |     0   |      0.6 |
| Aman     |    -1    |  -1    |    0.56 |    0.53 |     -1    |   0.22 |  0.5  |     0.5  |   0.3  |      0.39 |      0.44 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.71 |     -1    |    -1    |     -1   |    0.31 |   1    |   -1    |     0.08 |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.67 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.33 |     -1    |    -1    |     -1   |   -1    |  -1    |    1    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.47 |    0.53 |     -1    |   0.71 |  0.8  |     0.46 |   0.69 |      0.57 |      0.67 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.44 |   0.08 |   -1    |     1    |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |     1   |      0.4 |
| Selena   |     0.6  |  -1    |   -1    |   -1    |     -1    |   0.4  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.6  |  -1    |   -1    |    -1    |     0.4 |      1   |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |    -1    |   0.25 |    0.07 |    0.04 |      0.17 |   0.09 |  0.1  |     0.09 |   0.07 |      0.09 |      0.07 |   0.07 |   0.13 |   0.12 |    0.05 |     0    |   0.13 |    -1   |  0.11 |       0.14 | -1    |     0    |      0    |     0.11 |     -1   |    0    |  -1    |   -1    |    -1    |     0   |      0   |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.07 |   0    |   -1    |    0.12 |      0.29 |   0.12 |  0.14 |     0.07 |   0.05 |      0.15 |      0.16 |   0.16 |   0    |   0.06 |    0.09 |     0.11 |   0.13 |    -1   |  0.25 |      -1    |  0    |     0.05 |     -1    |    -1    |     -1   |    0.07 |   0.12 |    0.17 |     0    |    -1   |     -1   |
| Brian    |     0.04 |   0.25 |    0.12 |   -1    |      0.25 |   0.1  |  0.08 |     0.07 |   0.1  |      0.11 |      0.17 |   0.05 |   0.14 |   0.07 |    0.07 |     0    |   0    |     0.2 |  0.05 |       0    |  0.12 |     0.14 |      0    |     0.23 |      0.4 |    0.05 |   0.22 |    0.33 |     0.12 |    -1   |     -1   |
| Anthony  |     0.17 |  -1    |    0.29 |    0.25 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.09 |   0.2  |    0.12 |    0.1  |      0.33 |  -1    |  0.08 |     0.09 |   0.13 |      0.19 |      0.11 |   0.14 |   0.33 |   0.08 |    0.14 |    -1    |   0    |    -1   |  0.17 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.11 |   -1    |     0.14 |     0.2 |      0   |
| Jai      |     0.1  |   0    |    0.14 |    0.08 |      0.29 |   0.08 | -1    |     0.07 |   0.12 |      0.12 |      0.13 |   0.14 |  -1    |   0.15 |    0.08 |    -1    |   0    |    -1   |  0.08 |       0    | -1    |     0.22 |      0    |     0    |     -1   |    0    |   0.17 |   -1    |     0.2  |    -1   |     -1   |
| Jackie   |     0.09 |   0    |    0.07 |    0.07 |      0    |   0.09 |  0.07 |    -1    |   0.1  |      0.09 |      0.09 |   0.08 |   0.25 |   0.13 |    0.17 |    -1    |   0.07 |     0.2 |  0.13 |      -1    |  0.2  |     0.06 |      0.29 |     0.23 |     -1   |    0.25 |   0.1  |   -1    |     0.08 |    -1   |     -1   |
| Kate     |     0.07 |   0.09 |    0.05 |    0.1  |      0.11 |   0.13 |  0.12 |     0.1  |  -1    |      0.09 |      0.12 |   0.1  |   0    |   0.09 |    0.14 |     0.33 |   0.07 |    -1   |  0.04 |       0    |  0.12 |     0    |     -1    |     0    |      0   |    0.08 |   0.03 |    0.17 |     0    |     0.6 |      0.2 |
| Sushant  |     0.09 |   0.14 |    0.15 |    0.11 |     -1    |   0.19 |  0.12 |     0.09 |   0.09 |     -1    |      0.18 |   0.18 |   0    |   0.1  |    0    |     0    |   0.1  |    -1   |  0.14 |       0    |  0.12 |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.11 |   -1    |     0.29 |    -1   |     -1   |
| Abishek  |     0.07 |   0.11 |    0.16 |    0.17 |      0    |   0.11 |  0.13 |     0.09 |   0.12 |      0.18 |     -1    |   0.16 |   0.14 |   0.11 |    0    |     0.25 |   0    |    -1   |  0.08 |       0    |  0.12 |    -1    |      0    |     0.23 |     -1   |    0    |   0.25 |   -1    |     0    |    -1   |     -1   |
| Ruhi     |     0.07 |  -1    |    0.16 |    0.05 |     -1    |   0.14 |  0.14 |     0.08 |   0.1  |      0.18 |      0.16 |  -1    |   0.14 |   0.35 |    0.11 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.14 |  -1    |   -1    |    -1    |    -1   |     -1   |
| Kish     |     0.13 |   0    |    0    |    0.14 |     -1    |   0.33 | -1    |     0.25 |   0    |      0    |      0.14 |   0.14 |  -1    |  -1    |    0.2  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Alex     |     0.12 |   0    |    0.06 |    0.07 |     -1    |   0.08 |  0.15 |     0.13 |   0.09 |      0.1  |      0.11 |   0.35 |  -1    |  -1    |    0.1  |     0    |   0    |    -1   |  0.09 |       0    |  0.17 |     0    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jeron    |     0.05 |  -1    |    0.09 |    0.07 |      0.33 |   0.14 |  0.08 |     0.17 |   0.14 |      0    |      0    |   0.11 |   0.2  |   0.1  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jade     |     0.13 |  -1    |    0.13 |    0    |     -1    |   0    |  0    |     0.07 |   0.07 |      0.1  |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Sofia    |    -1    |  -1    |   -1    |    0.2  |     -1    |  -1    | -1    |     0.2  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jay      |     0.11 |  -1    |    0.25 |    0.05 |     -1    |   0.17 |  0.08 |     0.13 |   0.04 |      0.14 |      0.08 |   0.43 |  -1    |   0.09 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Tercel   |     0    |  -1    |    0.05 |    0.14 |     -1    |  -1    |  0.22 |     0.06 |   0    |     -1    |     -1    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |      0.2 |    0    |   0.29 |    0    |    -1    |    -1   |     -1   |
| Karthik  |     0    |  -1    |   -1    |    0    |     -1    |  -1    |  0    |     0.29 |  -1    |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |     0.14 |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Vishal   |     0.11 |  -1    |   -1    |    0.23 |     -1    |  -1    |  0    |     0.23 |   0    |     -1    |      0.23 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0.14 |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Olivia   |    -1    |  -1    |   -1    |    0.4  |     -1    |  -1    | -1    |    -1    |   0    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.2  |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Daisy    |     0    |  -1    |    0.07 |    0.05 |     -1    |   0.17 |  0    |     0.25 |   0.08 |      0.17 |      0    |   0.14 |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |      0   |   -1    |   0.06 |   -1    |     0    |     0   |      0   |
| Aman     |    -1    |  -1    |    0.12 |    0.22 |     -1    |   0.11 |  0.17 |     0.1  |   0.03 |      0.11 |      0.25 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.29 |     -1    |    -1    |     -1   |    0.06 |  -1    |   -1    |     0    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.17 |    0.33 |     -1    |  -1    | -1    |    -1    |   0.17 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0    |    0.12 |     -1    |   0.14 |  0.2  |     0.08 |   0    |      0.29 |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |   0    |   -1    |    -1    |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |    -1   |      0.4 |
| Selena   |     0    |  -1    |   -1    |   -1    |     -1    |   0    | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |     0.4 |     -1   |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     0    |   0.5  |    0.53 |    0.55 |      0.67 |   0.57 |  0.45 |     0.46 |   0.52 |      0.5  |      0.64 |   0.57 |   0.4  |   0.44 |    0.27 |     0.43 |   0.27 |    -1   |  0.28 |       0.14 | -1    |     0.6  |      0.43 |     0.56 |     -1   |    0    |  -1    |   -1    |    -1    |     1   |      0.4 |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.53 |   0.83 |    0    |    0.5  |      0.57 |   0.56 |  0.5  |     0.52 |   0.58 |      0.51 |      0.56 |   0.52 |   0.45 |   0.55 |    0.55 |     0.22 |   0.47 |    -1   |  0.35 |      -1    |  0.71 |     0.45 |     -1    |    -1    |     -1   |    0.6  |   0.44 |    0.5  |     0.53 |    -1   |     -1   |
| Brian    |     0.55 |   0.17 |    0.5  |    0    |      0.75 |   0.57 |  0.46 |     0.6  |   0.5  |      0.57 |      0.5  |   0.68 |   0.62 |   0.54 |    0.5  |     0.56 |   0.4  |     0.8 |  0.7  |       0.5  |  0.38 |     0.45 |      0.57 |     0.46 |      0.4 |    0.7  |   0.47 |    0.5  |     0.47 |    -1   |     -1   |
| Anthony  |     0.67 |  -1    |    0.57 |    0.75 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.57 |   0.6  |    0.56 |    0.57 |      0.5  |   0    |  0.54 |     0.54 |   0.52 |      0.36 |      0.5  |   0.5  |   0.33 |   0.68 |    0.71 |    -1    |   0.88 |    -1   |  0.67 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.25 |   0.78 |   -1    |     0.29 |     0.8 |      0.6 |
| Jai      |     0.45 |   0.6  |    0.5  |    0.46 |      0.71 |   0.54 |  0    |     0.56 |   0.42 |      0.63 |      0.6  |   0.76 |  -1    |   0.49 |    0.5  |    -1    |   0.6  |    -1   |  0.77 |       0.2  | -1    |     0.44 |      0.33 |     1    |     -1   |    0.8  |   0.5  |   -1    |     0.2  |    -1   |     -1   |
| Jackie   |     0.46 |   0.67 |    0.52 |    0.6  |      0.83 |   0.54 |  0.56 |     0    |   0.46 |      0.57 |      0.62 |   0.54 |   0.62 |   0.42 |    0.43 |    -1    |   0.57 |     0.4 |  0.4  |      -1    |  0.6  |     0.67 |      0.43 |     0.62 |     -1   |    0.25 |   0.5  |   -1    |     0.54 |    -1   |     -1   |
| Kate     |     0.52 |   0.55 |    0.58 |    0.5  |      0.67 |   0.52 |  0.42 |     0.46 |   0    |      0.59 |      0.5  |   0.55 |   0.67 |   0.55 |    0.36 |     0.17 |   0.57 |    -1   |  0.6  |       0.43 |  0.5  |     0.59 |     -1    |     0.43 |      0.8 |    0.48 |   0.7  |    0.33 |     0.31 |     0.4 |      0.6 |
| Sushant  |     0.5  |   0.57 |    0.51 |    0.57 |     -1    |   0.36 |  0.63 |     0.57 |   0.59 |      0    |      0.52 |   0.53 |   0.45 |   0.56 |    0.71 |     0.83 |   0.5  |    -1   |  0.55 |       0.5  |  0.62 |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.61 |   -1    |     0.43 |    -1   |     -1   |
| Abishek  |     0.64 |   0.44 |    0.56 |    0.5  |      0.8  |   0.5  |  0.6  |     0.62 |   0.5  |      0.52 |      0    |   0.57 |   0.5  |   0.57 |    0.79 |     0.62 |   0.44 |    -1   |  0.54 |       0.71 |  0.38 |    -1    |      0.86 |     0.46 |     -1   |    0.5  |   0.56 |   -1    |     0.33 |    -1   |     -1   |
| Ruhi     |     0.57 |  -1    |    0.52 |    0.68 |     -1    |   0.5  |  0.76 |     0.54 |   0.55 |      0.53 |      0.57 |   0    |   0.29 |   0.47 |    0.56 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.43 |  -1    |   -1    |    -1    |    -1   |     -1   |
| Kish     |     0.4  |   1    |    0.45 |    0.62 |     -1    |   0.33 | -1    |     0.62 |   0.67 |      0.45 |      0.5  |   0.29 |   0    |  -1    |    0.8  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Alex     |     0.44 |   0.8  |    0.55 |    0.54 |     -1    |   0.68 |  0.49 |     0.42 |   0.55 |      0.56 |      0.57 |   0.47 |  -1    |   0    |    0.6  |     0.33 |   0.8  |    -1   |  0.55 |       0.6  |  0.5  |     0.62 |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jeron    |     0.27 |  -1    |    0.55 |    0.5  |      0.5  |   0.71 |  0.5  |     0.43 |   0.36 |      0.71 |      0.79 |   0.56 |   0.8  |   0.6  |    0    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jade     |     0.27 |  -1    |    0.47 |    0.4  |     -1    |   0.88 |  0.6  |     0.57 |   0.57 |      0.5  |      0.44 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Sofia    |    -1    |  -1    |   -1    |    0.8  |     -1    |  -1    | -1    |     0.4  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |     0   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jay      |     0.28 |  -1    |    0.35 |    0.7  |     -1    |   0.67 |  0.77 |     0.4  |   0.6  |      0.55 |      0.54 |   0.43 |  -1    |   0.55 |   -1    |    -1    |  -1    |    -1   |  0    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    |    -1   | -1    |       0    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    |  0    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Tercel   |     0.6  |  -1    |    0.45 |    0.45 |     -1    |  -1    |  0.44 |     0.67 |   0.59 |     -1    |     -1    |  -1    |  -1    |   0.62 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |      0.4 |    0.62 |   0.29 |    0.67 |    -1    |    -1   |     -1   |
| Karthik  |     0.43 |  -1    |   -1    |    0.57 |     -1    |  -1    |  0.33 |     0.43 |  -1    |     -1    |      0.86 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0    |     0.71 |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Vishal   |     0.56 |  -1    |   -1    |    0.46 |     -1    |  -1    |  1    |     0.62 |   0.43 |     -1    |      0.46 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0.71 |     0    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Olivia   |    -1    |  -1    |   -1    |    0.4  |     -1    |  -1    | -1    |    -1    |   0.8  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.4  |     -1    |    -1    |      0   |    0.6  |  -1    |   -1    |    -1    |    -1   |     -1   |
| Daisy    |     0    |  -1    |    0.6  |    0.7  |     -1    |   0.25 |  0.8  |     0.25 |   0.48 |      0.17 |      0.5  |   0.43 |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.62 |     -1    |    -1    |      0.6 |    0    |   0.69 |   -1    |     0.56 |     1   |      0.4 |
| Aman     |    -1    |  -1    |    0.44 |    0.47 |     -1    |   0.78 |  0.5  |     0.5  |   0.7  |      0.61 |      0.56 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.29 |     -1    |    -1    |     -1   |    0.69 |   0    |   -1    |     0.92 |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.33 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.67 |     -1    |    -1    |     -1   |   -1    |  -1    |    0    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.53 |    0.47 |     -1    |   0.29 |  0.2  |     0.54 |   0.31 |      0.43 |      0.33 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.56 |   0.92 |   -1    |     0    |    -1   |     -1   |
| Kevin    |     1    |  -1    |   -1    |   -1    |     -1    |   0.8  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    1    |  -1    |   -1    |    -1    |     0   |      0.6 |
| Selena   |     0.4  |  -1    |   -1    |   -1    |     -1    |   0.6  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.4  |  -1    |   -1    |    -1    |     0.6 |      0   |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|----------|
| Rachel   |      136 |      4 |      44 |      51 |         4 |     19 |    38 |       52 |     46 |        39 |        37 |     12 |      9 |     29 |          1 |        1 |        0 |      16 |        0 |        4 |     11 |       1 |    13 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |        2 |         4 |        4 |        0 |       0 |       5 |      1 |       0 |        2 |       0 |        3 |    0 |        1 |         0 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Peter    |       44 |      1 |     194 |      89 |         3 |     21 |    37 |       70 |     62 |        58 |        56 |     12 |      6 |     35 |          1 |        1 |        0 |      10 |        0 |        7 |      8 |       0 |    13 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |       11 |         0 |        0 |        0 |       1 |       6 |     18 |       3 |        7 |       0 |        0 |    0 |        1 |         1 |
| Brian    |       51 |     10 |      89 |     236 |         3 |     26 |    45 |       68 |     89 |        57 |        80 |     14 |      8 |     37 |          1 |        1 |        0 |      14 |        0 |        4 |      9 |       1 |     6 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |       12 |         3 |        7 |        3 |       1 |       6 |     19 |       3 |        9 |       0 |        0 |    0 |        1 |         1 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Minh     |       19 |      2 |      21 |      26 |         3 |     72 |    12 |       26 |     30 |        23 |        27 |      7 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      1 |       2 |     2 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       9 |      2 |       0 |        5 |       1 |        2 |    0 |        0 |         0 |
| Jai      |       38 |      2 |      37 |      45 |         2 |     12 |    96 |       32 |     42 |        19 |        25 |      5 |      2 |     20 |          0 |        0 |        0 |       6 |        0 |        0 |      4 |       0 |     3 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         4 |        0 |        0 |       0 |       1 |      3 |       0 |        4 |       2 |        1 |    1 |        1 |         0 |
| Jackie   |       52 |      2 |      70 |      68 |         1 |     26 |    32 |      186 |     76 |        43 |        48 |     11 |      3 |     36 |          0 |        0 |        1 |      13 |        1 |        1 |      6 |       3 |     9 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       1 |        6 |         4 |        5 |        1 |       2 |      12 |     15 |       1 |        6 |       2 |        0 |    0 |        0 |         1 |
| Kate     |       46 |      5 |      62 |      89 |         3 |     30 |    42 |       76 |    198 |        48 |        70 |     18 |      5 |     30 |          0 |        0 |        0 |       9 |        0 |        5 |      6 |       1 |    10 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |        7 |         1 |        4 |        1 |       2 |      13 |     11 |       4 |       11 |       3 |        2 |    1 |        1 |         1 |
| Sushant  |       39 |      3 |      58 |      57 |         0 |     23 |    19 |       43 |     48 |       147 |        62 |     16 |      6 |     30 |          2 |        0 |        0 |       5 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       5 |      7 |       0 |        4 |       0 |        1 |    0 |        0 |         0 |
| Abishek  |       37 |      5 |      56 |      80 |         1 |     27 |    25 |       48 |     70 |        62 |       179 |     16 |      7 |     33 |          0 |        0 |        0 |       4 |        0 |        3 |      9 |       1 |    11 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |        2 |         1 |        7 |        0 |       0 |       4 |      7 |       0 |        4 |       0 |        0 |    0 |        3 |         0 |
| Ruhi     |       12 |      2 |      12 |      14 |         2 |      7 |     5 |       11 |     18 |        16 |        16 |     49 |      5 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       4 |      1 |       0 |        1 |       1 |        4 |    0 |        0 |         1 |
| Kish     |        9 |      0 |       6 |       8 |         2 |      4 |     2 |        3 |      5 |         6 |         7 |      5 |     21 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Alex     |       29 |      1 |      35 |      37 |         0 |      8 |    20 |       36 |     30 |        30 |        33 |      9 |      2 |     94 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       2 |     5 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jeron    |       16 |      0 |      10 |      14 |         3 |      2 |     6 |       13 |      9 |         5 |         4 |      4 |      1 |      4 |          0 |        0 |        1 |      32 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        1 |         0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jade     |       11 |      2 |       8 |       9 |         0 |      1 |     4 |        6 |      6 |         5 |         9 |      2 |      0 |      1 |          0 |        1 |        0 |       1 |        0 |        1 |     20 |       0 |     3 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        1 |         0 |
| Sofia    |        1 |      0 |       0 |       1 |         0 |      2 |     0 |        3 |      1 |         1 |         1 |      0 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       5 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jay      |       13 |      1 |      13 |       6 |         0 |      2 |     3 |        9 |     10 |        10 |        11 |      4 |      1 |      5 |          0 |        0 |        0 |       2 |        0 |        0 |      3 |       0 |    26 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Derek    |        1 |      0 |       2 |       3 |         0 |      0 |     0 |        1 |      1 |         3 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       4 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Gathenji |        6 |      0 |       1 |       3 |         0 |      0 |     4 |        2 |      4 |         3 |         2 |      2 |      1 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          7 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      2 |         1 |         1 |      2 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      3 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sai      |        2 |      1 |       2 |       5 |         0 |      2 |     2 |        2 |      4 |         3 |         5 |      0 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     8 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Nabeel   |        0 |      1 |       2 |       1 |         0 |      0 |     0 |        2 |      3 |         0 |         2 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        4 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Ronnie   |        1 |      0 |       2 |       0 |         0 |      1 |     0 |        2 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        2 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Neha     |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Kawin    |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Abrar    |        1 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       2 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Tercel   |        2 |      0 |      11 |      12 |         0 |      2 |     5 |        6 |      7 |         4 |         2 |      0 |      0 |      3 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       24 |         0 |        0 |        3 |       2 |       3 |      5 |       2 |        3 |       0 |        0 |    0 |        0 |         1 |
| Karthik  |        4 |      0 |       0 |       3 |         0 |      0 |     4 |        4 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         7 |        2 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Vishal   |        4 |      0 |       0 |       7 |         0 |      0 |     0 |        5 |      4 |         0 |         7 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         2 |       13 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Olivia   |        0 |      0 |       0 |       3 |         0 |      0 |     0 |        1 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        5 |       3 |       2 |      4 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| AlexY    |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        2 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        3 |       4 |       3 |      2 |       1 |        0 |       0 |        0 |    0 |        0 |         0 |
| Daisy    |        5 |      0 |       6 |       6 |         0 |      9 |     1 |       12 |     13 |         5 |         4 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        2 |       3 |      25 |      5 |       1 |        4 |       0 |        3 |    0 |        0 |         1 |
| Aman     |        1 |      0 |      18 |      19 |         0 |      2 |     3 |       15 |     11 |         7 |         7 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         0 |        0 |        4 |       2 |       5 |     37 |       1 |        1 |       0 |        0 |    0 |        0 |         0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       1 |      1 |       6 |        0 |       0 |        0 |    0 |        0 |         0 |
| Andrew   |        2 |      0 |       7 |       9 |         0 |      5 |     4 |        6 |     11 |         4 |         4 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        0 |       0 |       4 |      1 |       0 |       17 |       0 |        0 |    0 |        0 |         1 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       5 |        2 |    1 |        0 |         0 |
| Selena   |        3 |      0 |       0 |       0 |         0 |      2 |     1 |        0 |      2 |         1 |         0 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       3 |      0 |       0 |        0 |       2 |        5 |    0 |        0 |         0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |    1 |        0 |         0 |
| Claire   |        1 |      0 |       1 |       1 |         0 |      0 |     1 |        0 |      1 |         0 |         3 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        3 |         0 |
| Timothy  |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        1 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |         2 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|----------|
| Rachel   |       -1 |      2 |       7 |       4 |         2 |      4 |     7 |        9 |      7 |         7 |         7 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      2 |       0 |     2 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        1 |        0 |       0 |       0 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |         0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Peter    |        7 |      0 |      -1 |      21 |         2 |      6 |    10 |       11 |      7 |        18 |        20 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     5 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      4 |       1 |        0 |       0 |        0 |    0 |        1 |         0 |
| Brian    |        4 |      3 |      21 |      -1 |         3 |      6 |     7 |       12 |     17 |        14 |        27 |      2 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |        3 |         0 |        3 |        2 |       0 |       1 |      8 |       2 |        2 |       0 |        0 |    0 |        1 |         0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Minh     |        4 |      1 |       6 |       6 |         2 |     -1 |     2 |        5 |      8 |         7 |         6 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      1 |       0 |        1 |       1 |        0 |    0 |        0 |         0 |
| Jai      |        7 |      0 |      10 |       7 |         2 |      2 |    -1 |        5 |      9 |         6 |         8 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      1 |       0 |        1 |       2 |        1 |    1 |        0 |         0 |
| Jackie   |        9 |      0 |      11 |      12 |         0 |      5 |     5 |       -1 |     14 |         9 |        12 |      2 |      2 |      8 |          0 |        0 |        1 |       4 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |        1 |         2 |        3 |        0 |       0 |       4 |      3 |       0 |        1 |       2 |        0 |    0 |        0 |         1 |
| Kate     |        7 |      1 |       7 |      17 |         1 |      8 |     9 |       14 |     -1 |        10 |        16 |      4 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      1 |       1 |        0 |       3 |        1 |    1 |        1 |         0 |
| Sushant  |        7 |      1 |      18 |      14 |         0 |      7 |     6 |        9 |     10 |        -1 |        23 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       1 |      2 |       0 |        2 |       0 |        0 |    0 |        0 |         0 |
| Abishek  |        7 |      1 |      20 |      27 |         0 |      6 |     8 |       12 |     16 |        23 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       1 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        3 |        0 |       0 |       0 |      4 |       0 |        0 |       0 |        0 |    0 |        2 |         0 |
| Ruhi     |        2 |      1 |       4 |       2 |         1 |      2 |     3 |        2 |      4 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       1 |        1 |    0 |        0 |         1 |
| Kish     |        2 |      0 |       0 |       3 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     6 |        8 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jeron    |        1 |      0 |       2 |       2 |         2 |      1 |     1 |        4 |      2 |         0 |         0 |      1 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jade     |        2 |      0 |       2 |       0 |         0 |      0 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sofia    |        0 |      0 |       0 |       1 |         0 |      1 |     0 |        1 |      0 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |      -1 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jay      |        2 |      0 |       5 |       1 |         0 |      1 |     1 |        2 |      1 |         3 |         2 |      3 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |    -1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Greg     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |     -1 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Gathenji |        1 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |         -1 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        1 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |     -1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sai      |        1 |      0 |       0 |       1 |         0 |      0 |     1 |        1 |      1 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |    -1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Nabeel   |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |       -1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Ronnie   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |       -1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Neha     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |     -1 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |    -1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Kawin    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |      -1 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |      -1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Tercel   |        0 |      0 |       1 |       3 |         0 |      0 |     2 |        1 |      0 |         2 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       -1 |         0 |        0 |        1 |       0 |       0 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Karthik  |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        2 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |        -1 |        1 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Vishal   |        1 |      0 |       0 |       3 |         0 |      0 |     0 |        3 |      0 |         0 |         3 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         1 |       -1 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Olivia   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |       -1 |       0 |       0 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| AlexY    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |      -1 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Daisy    |        0 |      0 |       1 |       1 |         0 |      2 |     0 |        4 |      2 |         1 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |      -1 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |         1 |
| Aman     |        0 |      0 |       4 |       8 |         0 |      1 |     1 |        3 |      1 |         2 |         4 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        2 |       0 |       1 |     -1 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Megan    |        0 |      0 |       1 |       2 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |      -1 |        0 |       0 |        0 |    0 |        0 |         0 |
| Andrew   |        1 |      0 |       0 |       2 |         0 |      1 |     1 |        1 |      0 |         2 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |       -1 |       0 |        0 |    0 |        0 |         0 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |      -1 |        2 |    1 |        0 |         0 |
| Selena   |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       2 |       -1 |    0 |        0 |         0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |   -1 |        0 |         0 |
| Claire   |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |       -1 |         0 |
| Timothy  |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        -1 |

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|----------|
| Rachel   |        0 |      4 |      50 |      62 |         8 |     25 |    31 |       44 |     50 |        39 |        65 |     16 |      6 |     23 |          1 |        0 |        1 |       6 |        1 |        3 |      4 |       3 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |        3 |         3 |        5 |        0 |       0 |       0 |      2 |       0 |        0 |       5 |        2 |    1 |        1 |         0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Peter    |       50 |      5 |       0 |      90 |         4 |     27 |    37 |       77 |     85 |        61 |        72 |     13 |      5 |     42 |          1 |        0 |        1 |      12 |        1 |        2 |      7 |       3 |     7 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       1 |        9 |         0 |        0 |        2 |       1 |       9 |     14 |       3 |        8 |       0 |        0 |    0 |        0 |         1 |
| Brian    |       62 |      2 |      90 |       0 |         9 |     34 |    38 |      100 |     88 |        75 |        81 |     30 |     13 |     44 |          1 |        0 |        1 |      14 |        1 |        5 |      6 |       4 |    14 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       1 |       10 |         4 |        6 |        2 |       3 |      14 |     17 |       3 |        8 |       0 |        0 |    0 |        1 |         1 |
| Anthony  |        8 |      0 |       4 |       9 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Minh     |       25 |      3 |      27 |      34 |         3 |      0 |    14 |       31 |     32 |        13 |        27 |      7 |      2 |     17 |          0 |        0 |        0 |       5 |        0 |        2 |      7 |       0 |     4 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |        1 |         0 |        0 |        0 |       0 |       3 |      7 |       0 |        2 |       4 |        3 |    1 |        3 |         2 |
| Jai      |       31 |      3 |      37 |      38 |         5 |     14 |     0 |       40 |     31 |        33 |        37 |     16 |      2 |     19 |          1 |        0 |        0 |       6 |        0 |        2 |      6 |       0 |    10 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       2 |        4 |         2 |        6 |        0 |       0 |       4 |      3 |       0 |        1 |       0 |        1 |    0 |        2 |         0 |
| Jackie   |       44 |      4 |      77 |     100 |         5 |     31 |    40 |        0 |     65 |        58 |        79 |     13 |      5 |     26 |          0 |        1 |        0 |      10 |        0 |        2 |      8 |       2 |     6 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |       12 |         3 |        8 |        3 |       1 |       4 |     15 |       1 |        7 |       1 |        3 |    0 |        3 |         1 |
| Kate     |       50 |      6 |      85 |      88 |         6 |     32 |    31 |       65 |      0 |        68 |        69 |     22 |     10 |     36 |          2 |        0 |        0 |       5 |        0 |        1 |      8 |       1 |    15 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |       10 |         0 |        3 |        4 |       2 |      12 |     26 |       2 |        5 |       2 |        3 |    0 |        2 |         1 |
| Sushant  |       39 |      4 |      61 |      75 |         1 |     13 |    33 |       58 |     68 |         0 |        67 |     18 |      5 |     38 |          0 |        0 |        0 |      12 |        0 |        5 |      5 |       3 |    12 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       1 |     11 |       0 |        3 |       2 |        1 |    1 |        1 |         0 |
| Abishek  |       65 |      4 |      72 |      81 |         4 |     27 |    37 |       79 |     69 |        67 |         0 |     21 |      7 |     43 |          0 |        0 |        0 |      15 |        0 |        5 |      7 |       3 |    13 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |        2 |         6 |        6 |        0 |       0 |       4 |      9 |       0 |        2 |       2 |        2 |    0 |        0 |         0 |
| Ruhi     |       16 |      1 |      13 |      30 |         1 |      7 |    16 |       13 |     22 |        18 |        21 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       3 |      2 |       0 |        2 |       3 |        0 |    1 |        0 |         0 |
| Kish     |        6 |      5 |       5 |      13 |         2 |      2 |     2 |        5 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       4 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Alex     |       23 |      4 |      42 |      44 |         0 |     17 |    19 |       26 |     36 |        38 |        43 |      8 |      1 |      0 |          1 |        0 |        0 |       6 |        0 |        2 |      4 |       1 |     6 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |        5 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jeron    |        6 |      1 |      12 |      14 |         3 |      5 |     6 |       10 |      5 |        12 |        15 |      5 |      4 |      6 |          0 |        1 |        0 |       0 |        0 |        1 |      3 |       1 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jade     |        4 |      0 |       7 |       6 |         0 |      7 |     6 |        8 |      8 |         5 |         7 |      2 |      0 |      4 |          0 |        0 |        1 |       3 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sofia    |        3 |      0 |       3 |       4 |         0 |      0 |     0 |        2 |      1 |         3 |         3 |      0 |      0 |      1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Jay      |        5 |      1 |       7 |      14 |         0 |      4 |    10 |        6 |     15 |        12 |        13 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Derek    |        3 |      0 |       2 |       1 |         0 |      0 |     2 |        1 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Gathenji |        1 |      0 |       3 |       3 |         0 |      0 |     1 |        2 |      3 |         3 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Caro     |        1 |      0 |       0 |       3 |         0 |      1 |     0 |        1 |      1 |         2 |         2 |      1 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Sai      |        1 |      0 |       5 |       3 |         0 |      2 |     1 |        3 |      4 |         5 |         3 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Nabeel   |        2 |      3 |       0 |       3 |         0 |      0 |     1 |        2 |      1 |         0 |         2 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Ronnie   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      1 |         1 |         2 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Neha     |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Ira      |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      1 |     0 |       1 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Kawin    |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Abrar    |        0 |      0 |       1 |       1 |         0 |      0 |     2 |        1 |      0 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Tercel   |        3 |      0 |       9 |      10 |         0 |      1 |     4 |       12 |     10 |         0 |         2 |      1 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     4 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        2 |       2 |       5 |      2 |       4 |        1 |       0 |        0 |    0 |        0 |         1 |
| Karthik  |        3 |      0 |       0 |       4 |         0 |      0 |     2 |        3 |      0 |         0 |         6 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        5 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Vishal   |        5 |      0 |       0 |       6 |         0 |      0 |     6 |        8 |      3 |         0 |         6 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         5 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Olivia   |        0 |      0 |       2 |       2 |         0 |      0 |     0 |        3 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       3 |      0 |       2 |        0 |       0 |        0 |    0 |        0 |         0 |
| AlexY    |        0 |      0 |       1 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        1 |       0 |       1 |      1 |       1 |        0 |       0 |        0 |    0 |        0 |         0 |
| Daisy    |        0 |      0 |       9 |      14 |         0 |      3 |     4 |        4 |     12 |         1 |         4 |      3 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         0 |        0 |        3 |       1 |       0 |     11 |       1 |        5 |       5 |        2 |    1 |        0 |         1 |
| Aman     |        2 |      0 |      14 |      17 |         0 |      7 |     3 |       15 |     26 |        11 |         9 |      2 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |      11 |      0 |       2 |       12 |       0 |        0 |    0 |        1 |         0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        2 |       1 |       1 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Andrew   |        0 |      0 |       8 |       8 |         0 |      2 |     1 |        7 |      5 |         3 |         2 |      2 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       5 |     12 |       0 |        0 |       0 |        0 |    0 |        0 |         1 |
| Kevin    |        5 |      0 |       0 |       0 |         0 |      4 |     0 |        1 |      2 |         2 |         2 |      3 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       5 |      0 |       0 |        0 |       0 |        3 |    0 |        0 |         0 |
| Selena   |        2 |      0 |       0 |       0 |         0 |      3 |     1 |        3 |      3 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      0 |       0 |        0 |       3 |        0 |    1 |        0 |         0 |
| NA       |        1 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      0 |         1 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        1 |    0 |        0 |         0 |
| Claire   |        1 |      0 |       0 |       1 |         0 |      3 |     2 |        3 |      2 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Timothy  |        0 |      0 |       1 |       1 |         0 |      2 |     0 |        1 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |         0 |

### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |   Aman |   Andrew |   Daisy |
|---------|---------|-------|--------|--------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|------|-------|---------|--------|
| Rachel   |    -1    |   -1   |    0.28 |    0.47 |   0.44 |  0.22 |     0.42 |   0.4  |      0.35 |      0.57 |   0.14 |   0.43 |   0.38 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1   |  -1    |    -1    |   -1    |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Peter    |     0.28 |   -1   |   -1    |    0.55 |   0.5  |  0.33 |     0.44 |   0.55 |      0.41 |      0.59 |   0.4  |   0.2  |   0.3  |   -1    |     0.14 |    0.2 |  0.5  |      -1    |  -1   |   0.57 |     0.67 |   -1    |
| Brian    |     0.47 |    0.5 |    0.55 |   -1    |   0.44 |  0.41 |     0.45 |   0.6  |      0.5  |      0.63 |   0.62 |   0.83 |   0.54 |    0.5  |    -1    |    0.5 | -1    |      -1    |   0.2 |   0.67 |     0.56 |   -1    |
| Minh     |     0.44 |   -1   |    0.5  |    0.44 |  -1    |  0    |     0.31 |   0.56 |      0.38 |      0.43 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |     0.6  |    0.4  |
| Jai      |     0.22 |   -1   |    0.33 |    0.41 |   0    | -1    |     0.08 |   0.35 |      0.29 |      0.56 |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Jackie   |     0.42 |   -1   |    0.44 |    0.45 |   0.31 |  0.08 |    -1    |   0.5  |      0.42 |      0.48 |   0.14 |  -1    |   0.5  |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |   0.6  |     0.4  |    0.33 |
| Kate     |     0.4  |    0.6 |    0.55 |    0.6  |   0.56 |  0.35 |     0.5  |  -1    |      0.42 |      0.6  |   0.33 |  -1    |   0.58 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |  -1    |     0.6  |    0.67 |
| Sushant  |     0.35 |   -1   |    0.41 |    0.5  |   0.38 |  0.29 |     0.42 |   0.42 |     -1    |      0.55 |   0.43 |   0.4  |   0.44 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1   |  -1    |    -1    |   -1    |
| Abishek  |     0.57 |    0.4 |    0.59 |    0.63 |   0.43 |  0.56 |     0.48 |   0.6  |      0.55 |     -1    |   0.53 |   0.83 |   0.55 |   -1    |    -1    |    0.5 |  0.57 |      -1    |   0.2 |  -1    |    -1    |   -1    |
| Ruhi     |     0.14 |   -1   |    0.4  |    0.62 |   0.2  | -1    |     0.14 |   0.33 |      0.43 |      0.53 |  -1    |  -1    |   0.56 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Alex     |     0.38 |   -1   |    0.3  |    0.54 |   0.4  |  0.33 |     0.5  |   0.58 |      0.44 |      0.55 |   0.56 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Jade     |    -1    |   -1   |    0.2  |    0.5  |  -1    | -1    |    -1    |  -1    |     -1    |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Aman     |    -1    |   -1   |    0.57 |    0.67 |  -1    | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Andrew   |    -1    |   -1   |    0.67 |    0.56 |   0.6  | -1    |     0.4  |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |
| Daisy    |    -1    |   -1   |   -1    |   -1    |   0.4  | -1    |     0.33 |   0.67 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |  -1    |    -1    |   -1    |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Aman |   Andrew |   Daisy |
|---------|---------|-------|--------|--------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|-------|---------|--------|
| Rachel   |    -1    |   -1   |    0.28 |    0.44 |   0.44 |  0.24 |     0.42 |   0.38 |      0.37 |      0.55 |   0    |   0.33 |   0.41 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1    |    -1    |    -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Peter    |     0.28 |   -1   |   -1    |    0.53 |   0.38 |  0.29 |     0.41 |   0.48 |      0.38 |      0.56 |   0.4  |  -1    |   0.27 |   -1    |     0.14 |    0.2 |  0.5  |      -1    |   0.57 |     0.6  |    -1   |
| Brian    |     0.44 |    0.5 |    0.53 |   -1    |   0.4  |  0.38 |     0.44 |   0.58 |      0.49 |      0.62 |   0.55 |  -1    |   0.52 |    0.5  |    -1    |    0.5 | -1    |      -1    |   0.8  |     0.56 |    -1   |
| Minh     |     0.44 |   -1   |    0.38 |    0.4  |  -1    |  0    |     0.15 |   0.47 |      0.29 |      0.4  |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Jai      |     0.24 |   -1   |    0.29 |    0.38 |   0    | -1    |     0.08 |   0.35 |      0.29 |      0.53 |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Jackie   |     0.42 |   -1   |    0.41 |    0.44 |   0.15 |  0.08 |    -1    |   0.44 |      0.38 |      0.46 |   0.14 |  -1    |   0.47 |    0.33 |    -1    |   -1   | -1    |      -1    |   0.6  |    -1    |     0.2 |
| Kate     |     0.38 |    0.6 |    0.48 |    0.58 |   0.47 |  0.35 |     0.44 |  -1    |      0.37 |      0.57 |   0.33 |  -1    |   0.57 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1    |     0.56 |     0.6 |
| Sushant  |     0.37 |   -1   |    0.38 |    0.49 |   0.29 |  0.29 |     0.38 |   0.37 |     -1    |      0.52 |   0.43 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1    |    -1    |    -1   |
| Abishek  |     0.55 |    0.4 |    0.56 |    0.62 |   0.4  |  0.53 |     0.46 |   0.57 |      0.52 |     -1    |   0.5  |   0.8  |   0.54 |   -1    |    -1    |    0.5 |  0.57 |      -1    |  -1    |    -1    |    -1   |
| Ruhi     |     0    |   -1   |    0.4  |    0.55 |   0.2  | -1    |     0.14 |   0.33 |      0.43 |      0.5  |  -1    |  -1    |   0.67 |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Alex     |     0.41 |   -1   |    0.27 |    0.52 |  -1    |  0.4  |     0.47 |   0.57 |      0.42 |      0.54 |   0.67 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Jade     |    -1    |   -1   |    0.2  |    0.5  |  -1    | -1    |    -1    |  -1    |     -1    |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Aman     |    -1    |   -1   |    0.57 |    0.8  |  -1    | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Andrew   |    -1    |   -1   |    0.6  |    0.56 |  -1    | -1    |    -1    |   0.56 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |
| Daisy    |    -1    |   -1   |   -1    |   -1    |  -1    | -1    |     0.2  |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1    |    -1    |    -1   |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |   Daisy |   Aman |
|---------|-------|---------|-------|------|-------|----------|----------|-------|--------|--------|---------|-------|------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |    0.67 |   -1    |     0.33 |  -1    | -1    |   -1    |   -1   |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      0.83 |      1    |  -1    |    0.75 |    0.5  |     1    |   0.5  | -1    |   -1    |   -1   |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |   -1    |   -1   |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |   0    | -1    |   -1    |   -1   |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.83 |    0.25 |     0.25 |   1    | -1    |   -1    |   -1   |
| Sushant  |   0.33 |     0.83 |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.62 |    0.57 |     0.5  |   0.67 | -1    |   -1    |   -1   |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.73 |    0.6  |     0.5  |   0.88 | -1    |   -1    |   -1   |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.5  |  0.33 |   -1    |   -1   |
| Brian    |   0.67 |     0.75 |      1 | -1    |   0.83 |      0.62 |      0.73 |  -1    |   -1    |    0.9  |     0.8  |   0.83 | -1    |   -1    |    0.5 |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.25 |      0.57 |      0.6  |   0.75 |    0.9  |   -1    |     0.83 |   0.33 |  1    |   -1    |    0.5 |
| Jackie   |   0.33 |     1    |     -1 | -1    |   0.25 |      0.5  |      0.5  |  -1    |    0.8  |    0.83 |    -1    |  -1    | -1    |    0.33 |   -1   |
| Alex     |  -1    |     0.5  |     -1 |  0    |   1    |      0.67 |      0.88 |   0.5  |    0.83 |    0.33 |    -1    |  -1    | -1    |   -1    |   -1   |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |   -1    |   -1   |
| Daisy    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |   -1    |     0.33 |  -1    | -1    |   -1    |   -1   |
| Aman     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    0.5  |    0.5  |    -1    |  -1    | -1    |   -1    |   -1   |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |   Daisy |   Aman |
|---------|-------|---------|-------|------|-------|----------|----------|-------|--------|--------|---------|-------|------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |    0.67 |   -1    |     0.33 |  -1    | -1    |   -1    |  -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      1    |      1    |  -1    |    0.75 |    0.5  |     1    |   0.75 | -1    |   -1    |  -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |   -1    |  -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |  -1    | -1    |   -1    |  -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.83 |    0.25 |     0.25 |   1    | -1    |   -1    |  -1    |
| Sushant  |   0.33 |     1    |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.62 |    0.57 |     0.5  |   0.67 | -1    |   -1    |  -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.85 |    0.6  |     0.5  |   0.88 | -1    |   -1    |  -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.75 |  0.33 |   -1    |  -1    |
| Brian    |   0.67 |     0.75 |      1 | -1    |   0.83 |      0.62 |      0.85 |  -1    |   -1    |    0.9  |     0.8  |   0.83 | -1    |   -1    |   0.67 |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.25 |      0.57 |      0.6  |   0.75 |    0.9  |   -1    |     0.83 |   0.33 |  1    |   -1    |   0.5  |
| Jackie   |   0.33 |     1    |     -1 | -1    |   0.25 |      0.5  |      0.5  |  -1    |    0.8  |    0.83 |    -1    |  -1    | -1    |    0.33 |  -1    |
| Alex     |  -1    |     0.75 |     -1 | -1    |   1    |      0.67 |      0.88 |   0.75 |    0.83 |    0.33 |    -1    |  -1    | -1    |   -1    |  -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |   -1    |  -1    |
| Daisy    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |   -1    |     0.33 |  -1    | -1    |   -1    |  -1    |
| Aman     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    0.67 |    0.5  |    -1    |  -1    | -1    |   -1    |  -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |   Aman |   Andrew |   Daisy |
|---------|--------|--------|-------|---------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|------|-------|---------|--------|
| Peter    |   -1    |    0.42 |   0.59 |     0.48 |    0.2 |  0.58 |     0.52 |   0.5  |      0.5  |      0.39 |   0.73 |  -1    |   0.6  |    0.4  |     -1   |   -1   | -1    |       -1   |   0.8 |   0.6  |     0.71 |    0.43 |
| Brian    |    0.58 |   -1    |   0.58 |     0.64 |   -1   |  0.72 |     0.55 |   0.56 |      0.6  |      0.5  |   0.71 |   0.64 |   0.64 |   -1    |      0.6 |   -1   |  0.55 |       -1   |  -1   |   0.71 |     0.67 |    0.57 |
| Minh     |    0.41 |    0.42 |  -1    |     0.5  |   -1   |  0.67 |     0.53 |   0.32 |      0.33 |      0.41 |   0.6  |  -1    |   0.33 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Rachel   |    0.52 |    0.36 |   0.5  |    -1    |   -1   |  0.55 |     0.55 |   0.44 |      0.45 |      0.33 |   0.57 |   0.6  |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jai      |    0.42 |    0.28 |   0.33 |     0.45 |   -1   | -1    |     0.45 |   0.29 |      0.36 |      0.24 |   0.36 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jackie   |    0.48 |    0.45 |   0.47 |     0.45 |   -1   |  0.55 |    -1    |   0.47 |      0.4  |      0.39 |   0.5  |  -1    |   0.53 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |   0.4  |     0.5  |   -1    |
| Kate     |    0.5  |    0.44 |   0.68 |     0.56 |    0.5 |  0.71 |     0.53 |  -1    |      0.59 |      0.45 |   0.65 |   0.4  |   0.52 |   -1    |     -1   |    0.8 |  0.44 |       -1   |  -1   |   0.67 |    -1    |    0.6  |
| Sushant  |    0.5  |    0.4  |   0.67 |     0.55 |   -1   |  0.64 |     0.6  |   0.41 |     -1    |      0.36 |   0.56 |   0.4  |   0.42 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |   0.8 |  -1    |    -1    |   -1    |
| Abishek  |    0.61 |    0.5  |   0.59 |     0.67 |   -1   |  0.76 |     0.61 |   0.55 |      0.64 |     -1    |   0.74 |   0.71 |   0.58 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1   |  -1    |    -1    |   -1    |
| Ruhi     |    0.27 |    0.29 |   0.4  |     0.43 |   -1   |  0.64 |     0.5  |   0.35 |      0.44 |      0.26 |  -1    |  -1    |   0.62 |    0.6  |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Alex     |    0.4  |    0.36 |   0.67 |     0.75 |   -1   |  0.75 |     0.47 |   0.48 |      0.58 |      0.42 |   0.38 |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jade     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Aman     |    0.4  |    0.29 |  -1    |    -1    |   -1   | -1    |     0.6  |   0.33 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |     0.45 |    0.33 |
| Andrew   |    0.29 |    0.33 |  -1    |    -1    |   -1   | -1    |     0.5  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |   0.55 |    -1    |    0.6  |
| Daisy    |    0.57 |    0.43 |  -1    |    -1    |   -1   | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |   0.67 |     0.4  |   -1    |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Aman |   Andrew |   Daisy |
|---------|--------|--------|-------|---------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|-------|---------|--------|
| Peter    |   -1    |    0.39 |   0.59 |     0.44 |    0.2 |  0.56 |     0.52 |   0.5  |      0.49 |      0.36 |   0.7  |  -1    |   0.57 |    0.4  |     -1   |   -1   | -1    |       -1   |  -1    |     0.71 |    0.43 |
| Brian    |    0.61 |   -1    |   0.61 |     0.62 |   -1   |  0.71 |     0.58 |   0.57 |      0.6  |      0.5  |   0.68 |   0.6  |   0.63 |   -1    |      0.6 |   -1   |  0.55 |       -1   |   0.71 |     0.8  |    0.67 |
| Minh     |    0.41 |    0.39 |  -1    |     0.5  |   -1   |  0.6  |     0.53 |   0.33 |      0.33 |      0.36 |  -1    |  -1    |   0.29 |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Rachel   |    0.56 |    0.38 |   0.5  |    -1    |   -1   |  0.6  |     0.57 |   0.47 |      0.48 |      0.36 |   0.57 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Jai      |    0.44 |    0.29 |   0.4  |     0.4  |   -1   | -1    |     0.5  |   0.33 |      0.36 |      0.26 |   0.36 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Jackie   |    0.48 |    0.42 |   0.47 |     0.43 |   -1   |  0.5  |    -1    |   0.47 |      0.4  |      0.36 |   0.43 |  -1    |   0.5  |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |     0.5  |   -1    |
| Kate     |    0.5  |    0.43 |   0.67 |     0.53 |    0.5 |  0.67 |     0.53 |  -1    |      0.59 |      0.44 |   0.64 |   0.33 |   0.48 |   -1    |     -1   |    0.8 |  0.44 |       -1   |   0.62 |    -1    |    0.6  |
| Sushant  |    0.51 |    0.4  |   0.67 |     0.52 |   -1   |  0.64 |     0.6  |   0.41 |     -1    |      0.36 |   0.53 |  -1    |   0.39 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |  -1    |    -1    |   -1    |
| Abishek  |    0.64 |    0.5  |   0.64 |     0.64 |   -1   |  0.74 |     0.64 |   0.56 |      0.64 |     -1    |   0.71 |   0.67 |   0.56 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1    |    -1    |   -1    |
| Ruhi     |    0.3  |    0.32 |  -1    |     0.43 |   -1   |  0.64 |     0.57 |   0.36 |      0.47 |      0.29 |  -1    |  -1    |   0.62 |    0.6  |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Alex     |    0.43 |    0.37 |   0.71 |     0.75 |   -1   |  0.75 |     0.5  |   0.52 |      0.61 |      0.44 |   0.38 |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Jade     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |   -1    |
| Aman     |   -1    |    0.29 |  -1    |    -1    |   -1   | -1    |    -1    |   0.38 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |     0.5  |    0.4  |
| Andrew   |    0.29 |    0.2  |  -1    |    -1    |   -1   | -1    |     0.5  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |   0.5  |    -1    |    0.6  |
| Daisy    |    0.57 |    0.33 |  -1    |    -1    |   -1   | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |   0.6  |     0.4  |   -1    |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|-----------|---------|--------------|
| 3+1        | 0.388889 |            36 |
| 2+2        | 0.4      |            80 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|-----------|---------|--------------|
| 3+1        | 0.352941 |            34 |
| 2+2        | 0.368421 |            76 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.382353 |            34 |
| Success      | 0.330769 |           130 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.382353 |            34 |
| Success      | 0.320312 |           128 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |      38 | 0.447059 |     0.342105 |
|         1 |      35 | 0.411765 |     0.171429 |
|         2 |      12 | 0.141176 |     0.416667 |

*2 bad guys on mission 1:*

|   # Fails |   Count |   % |   Good Win % |
|----------|--------|----|-------------|
|         0 |      16 | 0.8 |       0.1875 |
|         1 |       4 | 0.2 |       0      |

*2 bad guys on mission 2:*

|   # Fails |   Count |       % |   Good Win % |
|----------|--------|--------|-------------|
|         0 |      12 | 0.375   |          0.5 |
|         1 |      15 | 0.46875 |          0.2 |
|         2 |       5 | 0.15625 |          0.2 |

*2 bad guys on mission 3:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |       8 | 0.296296 |     0.5      |
|         1 |      13 | 0.481481 |     0.230769 |
|         2 |       6 | 0.222222 |     0.5      |

*3 bad guys on mission 2:*

|   # Fails |   Count |   % |   Good Win % |
|----------|--------|----|-------------|
|         0 |       2 | 0.4 |            0 |
|         1 |       2 | 0.4 |            0 |
|         2 |       1 | 0.2 |            1 |

*3 bad guys on mission 3:*

|   # Fails |   Count |   % |   Good Win % |
|----------|--------|----|-------------|
|         1 |       1 |   1 |            0 |

### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|--------------------|--------------|-------------|
|                   0 |           109 |     0.522936 |
|                   1 |           128 |     0.359375 |
|                   2 |            17 |     0.588235 |
|                   3 |             6 |     0.5      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|--------------------|--------------|-------------|
|                   0 |           104 |     0.5      |
|                   1 |           122 |     0.327869 |
|                   2 |            17 |     0.588235 |
|                   3 |             6 |     0.5      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|--------------|------------------------|--------------|----------------|
| Merlin        |                 0.10769 |           260 |              28 |
| Assassin      |                 0.03167 |           221 |               7 |
| Morgana       |                 0.05976 |           251 |              15 |
| Mordred       |                 0.01418 |           141 |               2 |
| Loyal Servant |                 0       |           715 |               0 |
| Oberon        |                 0.01235 |            81 |               1 |
| Minion #1     |                 0.05556 |            36 |               2 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|---------|----------------------------|-------------------|--------------|
| Jeron    |                    0.5      |                  3 |             6 |
| Abishek  |                    0.461538 |                 18 |            39 |
| Alex     |                    0.363636 |                  8 |            22 |
| Minh     |                    0.363636 |                  4 |            11 |
| Tercel   |                    0.333333 |                  2 |             6 |
| Jai      |                    0.3125   |                  5 |            16 |
| Aman     |                    0.3      |                  3 |            10 |
| Rachel   |                    0.296296 |                  8 |            27 |
| Kate     |                    0.290909 |                 16 |            55 |
| Ruhi     |                    0.285714 |                  2 |             7 |
| Peter    |                    0.238095 |                 10 |            42 |
| Sushant  |                    0.230769 |                  6 |            26 |
| Jackie   |                    0.214286 |                  9 |            42 |
| Brian    |                    0.210526 |                 12 |            57 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)


*Competitive games only statistic.*

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|---------|------------------|-------------------|--------------|
| Minh     |          0        |                  0 |             4 |
| Brian    |          0.111111 |                  1 |             9 |
| Sushant  |          0.333333 |                  3 |             9 |
| Jeron    |          0.333333 |                  1 |             3 |
| Andrew   |          0.333333 |                  1 |             3 |
| Kate     |          0.363636 |                  4 |            11 |
| Peter    |          0.428571 |                  6 |            14 |
| Abishek  |          0.444444 |                  4 |             9 |
| Alex     |          0.5      |                  2 |             4 |
| Jai      |          0.6      |                  3 |             5 |
| Rachel   |          0.666667 |                  6 |             9 |
| Jackie   |          0.75     |                  3 |             4 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

| # Players   |   Assassination % |   # Assassinations |   Sample Size |
|------------|------------------|-------------------|--------------|
| 10          |          0.434783 |                 10 |            23 |
| 5           |          0.75     |                  6 |             8 |
| 5O          |          0.333333 |                  3 |             9 |
| 5X          |          0.4      |                  2 |             5 |
| 6           |          0.310345 |                  9 |            29 |
| 6M          |          0.363636 |                  4 |            11 |
| 6O          |          0.25     |                  3 |            12 |
| 7           |          0.580645 |                 18 |            31 |
| 7O          |          0.461538 |                  6 |            13 |
| 8           |          0.454545 |                 10 |            22 |
| 8O          |          0.5      |                  2 |             4 |
| 9           |          0.444444 |                 12 |            27 |
| 9L          |          0.333333 |                  1 |             3 |
| 9O          |          0        |                  0 |             1 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

| # Players   |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|------------|--------------------|------------------|-------------------|--------------|
| 10          |                   0 |          1        |                  1 |             1 |
| 10          |                   1 |          0.444444 |                  8 |            18 |
| 10          |                   2 |          0        |                  0 |             3 |
| 10          |                   3 |          1        |                  1 |             1 |
| 5           |                   0 |          0.5      |                  2 |             4 |
| 5           |                   1 |          1        |                  4 |             4 |
| 5O          |                   0 |          0.25     |                  2 |             8 |
| 5O          |                   1 |          1        |                  1 |             1 |
| 5X          |                   0 |          0.4      |                  2 |             5 |
| 6           |                   0 |          0.352941 |                  6 |            17 |
| 6           |                   1 |          0.272727 |                  3 |            11 |
| 6           |                   3 |          0        |                  0 |             1 |
| 6M          |                   0 |          0.444444 |                  4 |             9 |
| 6M          |                   1 |          0        |                  0 |             2 |
| 6O          |                   0 |          0.25     |                  3 |            12 |
| 7           |                   0 |          0.615385 |                  8 |            13 |
| 7           |                   1 |          0.642857 |                  9 |            14 |
| 7           |                   2 |          0.333333 |                  1 |             3 |
| 7           |                   3 |          0        |                  0 |             1 |
| 7O          |                   0 |          0.5      |                  5 |            10 |
| 7O          |                   1 |          1        |                  1 |             1 |
| 7O          |                   2 |          0        |                  0 |             1 |
| 7O          |                   3 |          0        |                  0 |             1 |
| 8           |                   0 |          0.428571 |                  3 |             7 |
| 8           |                   1 |          0.5      |                  7 |            14 |
| 8           |                   2 |          0        |                  0 |             1 |
| 8O          |                   0 |          0        |                  0 |             1 |
| 8O          |                   1 |          0.666667 |                  2 |             3 |
| 9           |                   0 |          0.375    |                  3 |             8 |
| 9           |                   1 |          0.470588 |                  8 |            17 |
| 9           |                   2 |          0.5      |                  1 |             2 |
| 9L          |                   0 |          1        |                  1 |             1 |
| 9L          |                   1 |          0        |                  0 |             2 |
| 9O          |                   2 |          0        |                  0 |             1 |

### <a id="pass-fail-sequences"></a>Mission success/fail sequence counts


*Lengths: 1*

| Sequence   |   Count |   Frequency |   Good Win % |
|-----------|--------|------------|-------------|
| Success    |     222 |    0.870588 |     0.459459 |
| Fail       |      33 |    0.129412 |     0.363636 |

*Lengths: 2*

| Sequence         |   Count |   Frequency |   Good Win % |
|-----------------|--------|------------|-------------|
| Success, Success |     100 |   0.392157  |     0.63     |
| Success, Fail    |     122 |   0.478431  |     0.319672 |
| Fail, Success    |      16 |   0.0627451 |     0.625    |
| Fail, Fail       |      17 |   0.0666667 |     0.117647 |

*Lengths: 3*

| Sequence                  |   Count |   Frequency |   Good Win % |
|--------------------------|--------|------------|-------------|
| Success, Success, Success |      61 |  0.239216   |     0.704918 |
| Success, Success, Fail    |      39 |  0.152941   |     0.512821 |
| Success, Fail, Success    |      62 |  0.243137   |     0.467742 |
| Success, Fail, Fail       |      60 |  0.235294   |     0.166667 |
| Fail, Success, Success    |      15 |  0.0588235  |     0.666667 |
| Fail, Success, Fail       |       1 |  0.00392157 |     0        |
| Fail, Fail, Success       |      10 |  0.0392157  |     0.2      |
| Fail, Fail, Fail          |       7 |  0.027451   |     0        |

*Lengths: 4*

| Sequence                        |   Count |   Frequency | Good Win %          |
|--------------------------------|--------|------------|--------------------|
| Success, Success, Fail, Success |      13 |  0.0698925  | 0.7692307692307693  |
| Success, Success, Fail, Fail    |      26 |  0.139785   | 0.38461538461538464 |
| Success, Fail, Success, Success |      45 |  0.241935   | 0.4888888888888889  |
| Success, Fail, Success, Fail    |      17 |  0.0913978  | 0.4117647058823529  |
| Success, Fail, Fail, Success    |      44 |  0.236559   | 0.22727272727272727 |
| Success, Fail, Fail, Fail       |      15 |  0.0806452  | 0.0                 |
| Fail, Success, Success, Success |       8 |  0.0430108  | 0.875               |
| Fail, Success, Success, Fail    |       7 |  0.0376344  | 0.42857142857142855 |
| Fail, Success, Fail, Success    |       1 |  0.00537634 | 0.0                 |
| Fail, Success, Fail, Fail       |       0 |  0          | N/A                 |
| Fail, Fail, Success, Success    |       8 |  0.0430108  | 0.25                |
| Fail, Fail, Success, Fail       |       2 |  0.0107527  | 0.0                 |

*Lengths: 5*

| Sequence                              |   Count |   Frequency | Good Win %          |
|--------------------------------------|--------|------------|--------------------|
| Success, Success, Fail, Fail, Success |      14 |   0.166667  | 0.5                 |
| Success, Success, Fail, Fail, Fail    |       7 |   0.0833333 | 0.0                 |
| Success, Fail, Success, Fail, Success |       7 |   0.0833333 | 0.5714285714285714  |
| Success, Fail, Success, Fail, Fail    |       2 |   0.0238095 | 0.0                 |
| Success, Fail, Fail, Success, Success |      23 |   0.27381   | 0.43478260869565216 |
| Success, Fail, Fail, Success, Fail    |      20 |   0.238095  | 0.0                 |
| Fail, Success, Success, Fail, Success |       1 |   0.0119048 | 0.0                 |
| Fail, Success, Success, Fail, Fail    |       1 |   0.0119048 | 0.0                 |
| Fail, Success, Fail, Success, Success |       0 |   0         | N/A                 |
| Fail, Success, Fail, Success, Fail    |       1 |   0.0119048 | 0.0                 |
| Fail, Fail, Success, Success, Success |       6 |   0.0714286 | 0.3333333333333333  |
| Fail, Fail, Success, Success, Fail    |       2 |   0.0238095 | 0.0                 |
