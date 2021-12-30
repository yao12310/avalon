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
29. [Mission success/fail sequence counts](#pass-fail-sequences)
## Stats

Note: The friends and memories made in this game far outweigh any statistic you will find on this page. In any case, most of these stats are super high variance: especially individual stats, which depend heavily on team composition.

### <a id="good-win"></a>Good win %

Cheesy wins included: 0.4362 (n = 243)

Cheesy wins excluded: 0.4095 (n = 232)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            32 |     0.40625  |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5X          |             6 |     0.5      |
| 6           |            27 |     0.62963  |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            35 |     0.371429 |
| 7O          |             8 |     0.5      |
| 8           |            42 |     0.309524 |
| 8O          |             3 |     0        |
| 9           |            44 |     0.363636 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

Cheesy wins excluded:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            31 |     0.387097 |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5X          |             6 |     0.5      |
| 6           |            25 |     0.6      |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            32 |     0.3125   |
| 7O          |             8 |     0.5      |
| 8           |            42 |     0.309524 |
| 8O          |             3 |     0        |
| 9           |            39 |     0.282051 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           122 |       29.4508 |     19.3933 |
| Good     |            94 |       19.8298 |     15.9533 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           122 |       29.4508 |     19.3933 |
| Good     |            87 |       20.8046 |     16.1899 |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|---------|------------|
| Kate     |          10 |
| Abishek  |           5 |
| Peter    |           4 |
| Brian    |           2 |
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
| Brian    |            220 |
| Kate     |            181 |
| Peter    |            179 |
| Jackie   |            172 |
| Abishek  |            170 |
| Rachel   |            135 |
| Sushant  |            135 |
| Alex     |             94 |
| Jai      |             94 |
| Minh     |             69 |
| Ruhi     |             47 |
| Jeron    |             32 |
| Jay      |             26 |
| Tercel   |             24 |
| Kish     |             21 |
| Daisy    |             21 |
| Jade     |             20 |
| Aman     |             20 |
| Andrew   |             16 |
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
| Daisy    | 0.761905 |       16 |       5 |
| Andrew   | 0.75     |       12 |       4 |
| Rachel   | 0.733333 |       99 |      36 |
| Karthik  | 0.714286 |        5 |       2 |
| Kate     | 0.696133 |      126 |      55 |
| Megan    | 0.666667 |        4 |       2 |
| Tercel   | 0.666667 |       16 |       8 |
| Justin   | 0.666667 |        6 |       3 |
| Jeron    | 0.65625  |       21 |      11 |
| Jackie   | 0.639535 |      110 |      62 |
| Alex     | 0.638298 |       60 |      34 |
| Brian    | 0.631818 |      139 |      81 |
| Jai      | 0.62766  |       59 |      35 |
| Sai      | 0.625    |        5 |       3 |
| Kish     | 0.619048 |       13 |       8 |
| Ewen     | 0.615385 |        8 |       5 |
| Jay      | 0.615385 |       16 |      10 |
| Peter    | 0.614525 |      110 |      69 |
| Olivia   | 0.6      |        3 |       2 |
| Selena   | 0.6      |        3 |       2 |
| Minh     | 0.57971  |       40 |      29 |
| Abishek  | 0.570588 |       97 |      73 |
| Sushant  | 0.57037  |       77 |      58 |
| Vishal   | 0.538462 |        7 |       6 |
| Ruhi     | 0.531915 |       25 |      22 |
| Aman     | 0.45     |        9 |      11 |
| Sofia    | 0.4      |        2 |       3 |
| Anthony  | 0.25     |        3 |       9 |
| Kevin    | 0        |        0 |       5 |

### <a id="kgt-stats"></a>Kate Good Theorem statistics
| Weak Success   |   Count |   Good Win % |
|---------------|--------|-------------|
| No             |       3 |            0 |
| Yes            |       7 |            0 |

| Strong Success   |   Count |   Good Win % |
|-----------------|--------|-------------|
| No               |       4 |            0 |
| Yes              |       6 |            0 |

| Weak KGT Applied   |   Sample Size |   Good Win % |
|-------------------|--------------|-------------|
| No                 |           229 |     0.454148 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|---------------------|--------------|-------------|
| N/A                  |             4 |     0.25     |
| No                   |           225 |     0.457778 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |       20 |         23 |         23 |        22 |         7 |       10 |          11 |              54 |           170 |
| Alex     |       13 |         13 |         13 |        14 |         4 |        2 |           1 |              34 |            94 |
| Aman     |        3 |          3 |          3 |         4 |         2 |        2 |           0 |               3 |            20 |
| Andrew   |        4 |          2 |          1 |         1 |         1 |        1 |           0 |               6 |            16 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       25 |         38 |         24 |        33 |        16 |        5 |           3 |              76 |           220 |
| Daisy    |        3 |          1 |          0 |         4 |         1 |        0 |           0 |              12 |            21 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       25 |         23 |         15 |        25 |        10 |        9 |           3 |              62 |           172 |
| Jade     |        5 |          3 |          1 |         1 |         1 |        1 |           0 |               8 |            20 |
| Jai      |       12 |         11 |          8 |        13 |         9 |        4 |           1 |              36 |            94 |
| Jay      |        4 |          3 |          4 |         0 |         5 |        1 |           0 |               9 |            26 |
| Jeron    |        5 |          9 |          2 |         5 |         2 |        1 |           1 |               7 |            32 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Karthik  |        2 |          0 |          0 |         1 |         0 |        0 |           1 |               3 |             7 |
| Kate     |       22 |         21 |         11 |        16 |        14 |       12 |           2 |              83 |           181 |
| Kevin    |        0 |          0 |          1 |         3 |         1 |        0 |           0 |               0 |             5 |
| Kish     |        3 |          4 |          1 |         4 |         2 |        0 |           1 |               6 |            21 |
| Megan    |        2 |          0 |          0 |         0 |         0 |        2 |           0 |               2 |             6 |
| Minh     |        9 |          8 |         12 |         7 |         6 |        2 |           2 |              23 |            69 |
| Olivia   |        1 |          0 |          1 |         0 |         1 |        0 |           0 |               2 |             5 |
| Peter    |       28 |         22 |         25 |        21 |        12 |        8 |           3 |              60 |           179 |
| Rachel   |       20 |         21 |         10 |        13 |        10 |        0 |           3 |              58 |           135 |
| Ruhi     |        2 |          5 |          7 |         7 |         7 |        1 |           0 |              18 |            47 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Selena   |        0 |          0 |          0 |         0 |         1 |        1 |           0 |               3 |             5 |
| Sofia    |        0 |          1 |          1 |         2 |         0 |        0 |           0 |               1 |             5 |
| Sushant  |       21 |         10 |         21 |        21 |         9 |        5 |           2 |              46 |           135 |
| Tercel   |        2 |          5 |          4 |         1 |         3 |        0 |           0 |               9 |            24 |
| Vishal   |        3 |          0 |          3 |         2 |         1 |        0 |           0 |               4 |            13 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.083 |      0.098 |      0.114 |     0.095 |     0.053 |    0.137 |       0.314 |           0.082 |           170 |
| Alex     |    0.054 |      0.055 |      0.065 |     0.06  |     0.031 |    0.027 |       0.029 |           0.051 |            94 |
| Aman     |    0.012 |      0.013 |      0.015 |     0.017 |     0.015 |    0.027 |       0     |           0.005 |            20 |
| Andrew   |    0.017 |      0.009 |      0.005 |     0.004 |     0.008 |    0.014 |       0     |           0.009 |            16 |
| Anthony  |    0     |      0.009 |      0.02  |     0.017 |     0     |    0.014 |       0     |           0.002 |            12 |
| Brian    |    0.104 |      0.162 |      0.119 |     0.142 |     0.122 |    0.068 |       0.086 |           0.115 |           220 |
| Daisy    |    0.012 |      0.004 |      0     |     0.017 |     0.008 |    0     |       0     |           0.018 |            21 |
| Ewen     |    0.004 |      0.009 |      0.01  |     0.004 |     0     |    0.027 |       0     |           0.008 |            13 |
| Gathenji |    0     |      0     |      0     |     0.004 |     0     |    0     |       0     |           0.009 |             7 |
| Jackie   |    0.104 |      0.098 |      0.075 |     0.108 |     0.076 |    0.123 |       0.086 |           0.094 |           172 |
| Jade     |    0.021 |      0.013 |      0.005 |     0.004 |     0.008 |    0.014 |       0     |           0.012 |            20 |
| Jai      |    0.05  |      0.047 |      0.04  |     0.056 |     0.069 |    0.055 |       0.029 |           0.054 |            94 |
| Jay      |    0.017 |      0.013 |      0.02  |     0     |     0.038 |    0.014 |       0     |           0.014 |            26 |
| Jeron    |    0.021 |      0.038 |      0.01  |     0.022 |     0.015 |    0.014 |       0.029 |           0.011 |            32 |
| Justin   |    0.008 |      0     |      0.005 |     0.004 |     0.008 |    0     |       0     |           0.006 |             9 |
| Karthik  |    0.008 |      0     |      0     |     0.004 |     0     |    0     |       0.029 |           0.005 |             7 |
| Kate     |    0.092 |      0.089 |      0.055 |     0.069 |     0.107 |    0.164 |       0.057 |           0.126 |           181 |
| Kevin    |    0     |      0     |      0.005 |     0.013 |     0.008 |    0     |       0     |           0     |             5 |
| Kish     |    0.012 |      0.017 |      0.005 |     0.017 |     0.015 |    0     |       0.029 |           0.009 |            21 |
| Megan    |    0.008 |      0     |      0     |     0     |     0     |    0.027 |       0     |           0.003 |             6 |
| Minh     |    0.038 |      0.034 |      0.06  |     0.03  |     0.046 |    0.027 |       0.057 |           0.035 |            69 |
| Olivia   |    0.004 |      0     |      0.005 |     0     |     0.008 |    0     |       0     |           0.003 |             5 |
| Peter    |    0.117 |      0.094 |      0.124 |     0.091 |     0.092 |    0.11  |       0.086 |           0.091 |           179 |
| Rachel   |    0.083 |      0.089 |      0.05  |     0.056 |     0.076 |    0     |       0.086 |           0.088 |           135 |
| Ruhi     |    0.008 |      0.021 |      0.035 |     0.03  |     0.053 |    0.014 |       0     |           0.027 |            47 |
| Sai      |    0.004 |      0.004 |      0     |     0.004 |     0.015 |    0     |       0     |           0.005 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.008 |    0.014 |       0     |           0.005 |             5 |
| Sofia    |    0     |      0.004 |      0.005 |     0.009 |     0     |    0     |       0     |           0.002 |             5 |
| Sushant  |    0.088 |      0.043 |      0.104 |     0.091 |     0.069 |    0.068 |       0.057 |           0.07  |           135 |
| Tercel   |    0.008 |      0.021 |      0.02  |     0.004 |     0.023 |    0     |       0     |           0.014 |            24 |
| Vishal   |    0.012 |      0     |      0.015 |     0.009 |     0.008 |    0     |       0     |           0.006 |            13 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.118 |      0.135 |      0.135 |     0.129 |     0.041 |    0.059 |       0.065 |           0.318 |           170 |
| Alex     |    0.138 |      0.138 |      0.138 |     0.149 |     0.043 |    0.021 |       0.011 |           0.362 |            94 |
| Aman     |    0.15  |      0.15  |      0.15  |     0.2   |     0.1   |    0.1   |       0     |           0.15  |            20 |
| Andrew   |    0.25  |      0.125 |      0.062 |     0.062 |     0.062 |    0.062 |       0     |           0.375 |            16 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.114 |      0.173 |      0.109 |     0.15  |     0.073 |    0.023 |       0.014 |           0.345 |           220 |
| Daisy    |    0.143 |      0.048 |      0     |     0.19  |     0.048 |    0     |       0     |           0.571 |            21 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.145 |      0.134 |      0.087 |     0.145 |     0.058 |    0.052 |       0.017 |           0.36  |           172 |
| Jade     |    0.25  |      0.15  |      0.05  |     0.05  |     0.05  |    0.05  |       0     |           0.4   |            20 |
| Jai      |    0.128 |      0.117 |      0.085 |     0.138 |     0.096 |    0.043 |       0.011 |           0.383 |            94 |
| Jay      |    0.154 |      0.115 |      0.154 |     0     |     0.192 |    0.038 |       0     |           0.346 |            26 |
| Jeron    |    0.156 |      0.281 |      0.062 |     0.156 |     0.062 |    0.031 |       0.031 |           0.219 |            32 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Karthik  |    0.286 |      0     |      0     |     0.143 |     0     |    0     |       0.143 |           0.429 |             7 |
| Kate     |    0.122 |      0.116 |      0.061 |     0.088 |     0.077 |    0.066 |       0.011 |           0.459 |           181 |
| Kevin    |    0     |      0     |      0.2   |     0.6   |     0.2   |    0     |       0     |           0     |             5 |
| Kish     |    0.143 |      0.19  |      0.048 |     0.19  |     0.095 |    0     |       0.048 |           0.286 |            21 |
| Megan    |    0.333 |      0     |      0     |     0     |     0     |    0.333 |       0     |           0.333 |             6 |
| Minh     |    0.13  |      0.116 |      0.174 |     0.101 |     0.087 |    0.029 |       0.029 |           0.333 |            69 |
| Olivia   |    0.2   |      0     |      0.2   |     0     |     0.2   |    0     |       0     |           0.4   |             5 |
| Peter    |    0.156 |      0.123 |      0.14  |     0.117 |     0.067 |    0.045 |       0.017 |           0.335 |           179 |
| Rachel   |    0.148 |      0.156 |      0.074 |     0.096 |     0.074 |    0     |       0.022 |           0.43  |           135 |
| Ruhi     |    0.043 |      0.106 |      0.149 |     0.149 |     0.149 |    0.021 |       0     |           0.383 |            47 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.2   |    0.2   |       0     |           0.6   |             5 |
| Sofia    |    0     |      0.2   |      0.2   |     0.4   |     0     |    0     |       0     |           0.2   |             5 |
| Sushant  |    0.156 |      0.074 |      0.156 |     0.156 |     0.067 |    0.037 |       0.015 |           0.341 |           135 |
| Tercel   |    0.083 |      0.208 |      0.167 |     0.042 |     0.125 |    0     |       0     |           0.375 |            24 |
| Vishal   |    0.231 |      0     |      0.231 |     0.154 |     0.077 |    0     |       0     |           0.308 |            13 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     1    |   0.5  |    0.47 |    0.46 |      0.33 |   0.43 |  0.55 |     0.54 |   0.47 |      0.5  |      0.36 |   0.43 |   0.6  |   0.56 |    0.73 |     0.57 |   0.73 |    -1   |  0.72 |       0.86 | -1    |     0.4  |      0.57 |     0.44 |     -1   |    1    |  -1    |   -1    |    -1    |     0   |      0.6 |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.47 |   0.17 |    1    |    0.51 |      0.43 |   0.42 |  0.5  |     0.45 |   0.42 |      0.48 |      0.45 |   0.48 |   0.55 |   0.45 |    0.45 |     0.78 |   0.53 |    -1   |  0.65 |      -1    |  0.29 |     0.55 |     -1    |    -1    |     -1   |    0.38 |   0.53 |    0.5  |     0.43 |    -1   |     -1   |
| Brian    |     0.46 |   0.83 |    0.51 |    1    |      0.25 |   0.42 |  0.54 |     0.4  |   0.52 |      0.41 |      0.5  |   0.31 |   0.38 |   0.46 |    0.5  |     0.44 |   0.6  |     0.2 |  0.3  |       0.5  |  0.62 |     0.55 |      0.43 |     0.54 |      0.6 |    0.25 |   0.5  |    0.5  |     0.56 |    -1   |     -1   |
| Anthony  |     0.33 |  -1    |    0.43 |    0.25 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.43 |   0.4  |    0.42 |    0.42 |      0.5  |   1    |  0.46 |     0.46 |   0.46 |      0.64 |      0.51 |   0.5  |   0.67 |   0.32 |    0.29 |    -1    |   0.12 |    -1   |  0.33 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.75 |   0.33 |   -1    |     0.71 |     0.2 |      0.4 |
| Jai      |     0.55 |   0.4  |    0.5  |    0.54 |      0.29 |   0.46 |  1    |     0.46 |   0.58 |      0.36 |      0.4  |   0.24 |  -1    |   0.51 |    0.5  |    -1    |   0.4  |    -1   |  0.23 |       0.8  | -1    |     0.56 |      0.67 |     0    |     -1   |    0.2  |  -1    |   -1    |     0.8  |    -1   |     -1   |
| Jackie   |     0.54 |   0.33 |    0.45 |    0.4  |      0.17 |   0.46 |  0.46 |     1    |   0.54 |      0.44 |      0.39 |   0.45 |   0.38 |   0.58 |    0.57 |    -1    |   0.43 |     0.6 |  0.6  |      -1    |  0.4  |     0.33 |      0.57 |     0.38 |     -1   |    0.79 |   0.5  |   -1    |     0.42 |    -1   |     -1   |
| Kate     |     0.47 |   0.45 |    0.42 |    0.52 |      0.33 |   0.46 |  0.58 |     0.54 |   1    |      0.41 |      0.52 |   0.45 |   0.33 |   0.45 |    0.64 |     0.83 |   0.43 |    -1   |  0.4  |       0.57 |  0.5  |     0.41 |     -1    |     0.57 |      0.2 |    0.57 |   0.3  |    0.67 |     0.67 |     0.6 |      0.4 |
| Sushant  |     0.5  |   0.43 |    0.48 |    0.41 |     -1    |   0.64 |  0.36 |     0.44 |   0.41 |      1    |      0.48 |   0.47 |   0.55 |   0.44 |    0.29 |     0.17 |   0.5  |    -1   |  0.45 |       0.5  |  0.38 |    -1    |     -1    |    -1    |     -1   |    0.83 |   0.33 |   -1    |     0.67 |    -1   |     -1   |
| Abishek  |     0.36 |   0.56 |    0.45 |    0.5  |      0.2  |   0.51 |  0.4  |     0.39 |   0.52 |      0.48 |      1    |   0.43 |   0.5  |   0.43 |    0.21 |     0.38 |   0.56 |    -1   |  0.46 |       0.29 |  0.62 |    -1    |      0.14 |     0.54 |     -1   |    0.5  |   0.29 |   -1    |     0.8  |    -1   |     -1   |
| Ruhi     |     0.43 |  -1    |    0.48 |    0.31 |     -1    |   0.5  |  0.24 |     0.45 |   0.45 |      0.47 |      0.43 |   1    |   0.71 |   0.53 |    0.44 |    -1    |  -1    |    -1   |  0.57 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.8  |  -1    |   -1    |    -1    |    -1   |     -1   |
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
| Daisy    |     1    |  -1    |    0.38 |    0.25 |     -1    |   0.75 |  0.2  |     0.79 |   0.57 |      0.83 |      0.5  |   0.8  |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.38 |     -1    |    -1    |      0.4 |    1    |   0.25 |   -1    |     0.44 |     0   |      0.6 |
| Aman     |    -1    |  -1    |    0.53 |    0.5  |     -1    |   0.33 | -1    |     0.5  |   0.3  |      0.33 |      0.29 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.71 |     -1    |    -1    |     -1   |    0.25 |   1    |   -1    |     0    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.67 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.33 |     -1    |    -1    |     -1   |   -1    |  -1    |    1    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.43 |    0.56 |     -1    |   0.71 |  0.8  |     0.42 |   0.67 |      0.67 |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.44 |   0    |   -1    |     1    |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |     1   |      0.4 |
| Selena   |     0.6  |  -1    |   -1    |   -1    |     -1    |   0.4  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.6  |  -1    |   -1    |    -1    |     0.4 |      1   |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |    -1    |   0.25 |    0.08 |    0.04 |      0.17 |   0.09 |  0.1  |     0.09 |   0.06 |      0.09 |      0.07 |   0.07 |   0.13 |   0.12 |    0.05 |     0    |   0.13 |    -1   |  0.11 |       0.14 | -1    |     0    |      0    |     0.11 |     -1   |    0    |  -1    |   -1    |    -1    |     0   |      0   |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.08 |   0    |   -1    |    0.13 |      0.29 |   0.13 |  0.14 |     0.07 |   0.05 |      0.16 |      0.17 |   0.16 |   0    |   0.06 |    0.09 |     0.11 |   0.13 |    -1   |  0.25 |      -1    |  0    |     0.05 |     -1    |    -1    |     -1   |    0.08 |   0.24 |    0.17 |     0    |    -1   |     -1   |
| Brian    |     0.04 |   0.25 |    0.13 |   -1    |      0.25 |   0.11 |  0.09 |     0.07 |   0.09 |      0.09 |      0.16 |   0.05 |   0.14 |   0.07 |    0.07 |     0    |   0    |     0.2 |  0.05 |       0    |  0.12 |     0.14 |      0    |     0.23 |      0.4 |    0    |   0.3  |    0.33 |     0.12 |    -1   |     -1   |
| Anthony  |     0.17 |  -1    |    0.29 |    0.25 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.09 |   0.2  |    0.13 |    0.11 |      0.33 |  -1    |  0.08 |     0.09 |   0.12 |      0.21 |      0.1  |   0.14 |   0.33 |   0.08 |    0.14 |    -1    |   0    |    -1   |  0.17 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.17 |   -1    |     0.14 |     0.2 |      0   |
| Jai      |     0.1  |   0    |    0.14 |    0.09 |      0.29 |   0.08 | -1    |     0.07 |   0.13 |      0.12 |      0.12 |   0.14 |  -1    |   0.15 |    0.08 |    -1    |   0    |    -1   |  0.08 |       0    | -1    |     0.22 |      0    |     0    |     -1   |    0    |  -1    |   -1    |     0.2  |    -1   |     -1   |
| Jackie   |     0.09 |   0    |    0.07 |    0.07 |      0    |   0.09 |  0.07 |    -1    |   0.09 |      0.09 |      0.09 |   0.09 |   0.25 |   0.13 |    0.17 |    -1    |   0.07 |     0.2 |  0.13 |      -1    |  0.2  |     0.06 |      0.29 |     0.23 |     -1   |    0.29 |   0.12 |   -1    |     0.08 |    -1   |     -1   |
| Kate     |     0.06 |   0.09 |    0.05 |    0.09 |      0.11 |   0.12 |  0.13 |     0.09 |  -1    |      0.09 |      0.12 |   0.08 |   0    |   0.09 |    0.14 |     0.33 |   0.07 |    -1   |  0.04 |       0    |  0.12 |     0    |     -1    |     0    |      0   |    0.05 |   0.05 |    0.17 |     0    |     0.6 |      0.2 |
| Sushant  |     0.09 |   0.14 |    0.16 |    0.09 |     -1    |   0.21 |  0.12 |     0.09 |   0.09 |     -1    |      0.18 |   0.18 |   0    |   0.1  |    0    |     0    |   0.1  |    -1   |  0.14 |       0    |  0.12 |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.17 |   -1    |     0.33 |    -1   |     -1   |
| Abishek  |     0.07 |   0.11 |    0.17 |    0.16 |      0    |   0.1  |  0.12 |     0.09 |   0.12 |      0.18 |     -1    |   0.16 |   0.14 |   0.11 |    0    |     0.25 |   0    |    -1   |  0.08 |       0    |  0.12 |    -1    |      0    |     0.23 |     -1   |    0    |   0.29 |   -1    |     0    |    -1   |     -1   |
| Ruhi     |     0.07 |  -1    |    0.16 |    0.05 |     -1    |   0.14 |  0.14 |     0.09 |   0.08 |      0.18 |      0.16 |  -1    |   0.14 |   0.35 |    0.11 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.2  |  -1    |   -1    |    -1    |    -1   |     -1   |
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
| Daisy    |     0    |  -1    |    0.08 |    0    |     -1    |   0.17 |  0    |     0.29 |   0.05 |      0.17 |      0    |   0.2  |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |      0   |   -1    |   0.08 |   -1    |     0    |     0   |      0   |
| Aman     |    -1    |  -1    |    0.24 |    0.3  |     -1    |   0.17 | -1    |     0.12 |   0.05 |      0.17 |      0.29 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.29 |     -1    |    -1    |     -1   |    0.08 |  -1    |   -1    |     0    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.17 |    0.33 |     -1    |  -1    | -1    |    -1    |   0.17 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0    |    0.12 |     -1    |   0.14 |  0.2  |     0.08 |   0    |      0.33 |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |   0    |   -1    |    -1    |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |    -1   |      0.4 |
| Selena   |     0    |  -1    |   -1    |   -1    |     -1    |   0    | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |     0.4 |     -1   |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     0    |   0.5  |    0.53 |    0.54 |      0.67 |   0.57 |  0.45 |     0.46 |   0.53 |      0.5  |      0.64 |   0.57 |   0.4  |   0.44 |    0.27 |     0.43 |   0.27 |    -1   |  0.28 |       0.14 | -1    |     0.6  |      0.43 |     0.56 |     -1   |    0    |  -1    |   -1    |    -1    |     1   |      0.4 |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.53 |   0.83 |    0    |    0.49 |      0.57 |   0.58 |  0.5  |     0.55 |   0.58 |      0.52 |      0.55 |   0.52 |   0.45 |   0.55 |    0.55 |     0.22 |   0.47 |    -1   |  0.35 |      -1    |  0.71 |     0.45 |     -1    |    -1    |     -1   |    0.62 |   0.47 |    0.5  |     0.57 |    -1   |     -1   |
| Brian    |     0.54 |   0.17 |    0.49 |    0    |      0.75 |   0.58 |  0.46 |     0.6  |   0.48 |      0.59 |      0.5  |   0.69 |   0.62 |   0.54 |    0.5  |     0.56 |   0.4  |     0.8 |  0.7  |       0.5  |  0.38 |     0.45 |      0.57 |     0.46 |      0.4 |    0.75 |   0.5  |    0.5  |     0.44 |    -1   |     -1   |
| Anthony  |     0.67 |  -1    |    0.57 |    0.75 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.57 |   0.6  |    0.58 |    0.58 |      0.5  |   0    |  0.54 |     0.54 |   0.54 |      0.36 |      0.49 |   0.5  |   0.33 |   0.68 |    0.71 |    -1    |   0.88 |    -1   |  0.67 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.25 |   0.67 |   -1    |     0.29 |     0.8 |      0.6 |
| Jai      |     0.45 |   0.6  |    0.5  |    0.46 |      0.71 |   0.54 |  0    |     0.54 |   0.42 |      0.64 |      0.6  |   0.76 |  -1    |   0.49 |    0.5  |    -1    |   0.6  |    -1   |  0.77 |       0.2  | -1    |     0.44 |      0.33 |     1    |     -1   |    0.8  |  -1    |   -1    |     0.2  |    -1   |     -1   |
| Jackie   |     0.46 |   0.67 |    0.55 |    0.6  |      0.83 |   0.54 |  0.54 |     0    |   0.46 |      0.56 |      0.61 |   0.55 |   0.62 |   0.42 |    0.43 |    -1    |   0.57 |     0.4 |  0.4  |      -1    |  0.6  |     0.67 |      0.43 |     0.62 |     -1   |    0.21 |   0.5  |   -1    |     0.58 |    -1   |     -1   |
| Kate     |     0.53 |   0.55 |    0.58 |    0.48 |      0.67 |   0.54 |  0.42 |     0.46 |   0    |      0.59 |      0.48 |   0.55 |   0.67 |   0.55 |    0.36 |     0.17 |   0.57 |    -1   |  0.6  |       0.43 |  0.5  |     0.59 |     -1    |     0.43 |      0.8 |    0.43 |   0.7  |    0.33 |     0.33 |     0.4 |      0.6 |
| Sushant  |     0.5  |   0.57 |    0.52 |    0.59 |     -1    |   0.36 |  0.64 |     0.56 |   0.59 |      0    |      0.52 |   0.53 |   0.45 |   0.56 |    0.71 |     0.83 |   0.5  |    -1   |  0.55 |       0.5  |  0.62 |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.67 |   -1    |     0.33 |    -1   |     -1   |
| Abishek  |     0.64 |   0.44 |    0.55 |    0.5  |      0.8  |   0.49 |  0.6  |     0.61 |   0.48 |      0.52 |      0    |   0.57 |   0.5  |   0.57 |    0.79 |     0.62 |   0.44 |    -1   |  0.54 |       0.71 |  0.38 |    -1    |      0.86 |     0.46 |     -1   |    0.5  |   0.71 |   -1    |     0.2  |    -1   |     -1   |
| Ruhi     |     0.57 |  -1    |    0.52 |    0.69 |     -1    |   0.5  |  0.76 |     0.55 |   0.55 |      0.53 |      0.57 |   0    |   0.29 |   0.47 |    0.56 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.2  |  -1    |   -1    |    -1    |    -1   |     -1   |
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
| Daisy    |     0    |  -1    |    0.62 |    0.75 |     -1    |   0.25 |  0.8  |     0.21 |   0.43 |      0.17 |      0.5  |   0.2  |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.62 |     -1    |    -1    |      0.6 |    0    |   0.75 |   -1    |     0.56 |     1   |      0.4 |
| Aman     |    -1    |  -1    |    0.47 |    0.5  |     -1    |   0.67 | -1    |     0.5  |   0.7  |      0.67 |      0.71 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.29 |     -1    |    -1    |     -1   |    0.75 |   0    |   -1    |     1    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.33 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.67 |     -1    |    -1    |     -1   |   -1    |  -1    |    0    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.57 |    0.44 |     -1    |   0.29 |  0.2  |     0.58 |   0.33 |      0.33 |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.56 |   1    |   -1    |     0    |    -1   |     -1   |
| Kevin    |     1    |  -1    |   -1    |   -1    |     -1    |   0.8  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    1    |  -1    |   -1    |    -1    |     0   |      0.6 |
| Selena   |     0.4  |  -1    |   -1    |   -1    |     -1    |   0.6  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.4  |  -1    |   -1    |    -1    |     0.6 |      0   |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|----------|
| Rachel   |      135 |      4 |      44 |      51 |         4 |     19 |    38 |       52 |     45 |        39 |        37 |     12 |      9 |     29 |          1 |        1 |        0 |      16 |        0 |        4 |     11 |       1 |    13 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |        2 |         4 |        4 |        0 |       0 |       5 |      1 |       0 |        2 |       0 |        3 |    0 |        1 |         0 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Peter    |       44 |      1 |     179 |      84 |         3 |     19 |    36 |       61 |     55 |        51 |        53 |     12 |      6 |     35 |          1 |        1 |        0 |      10 |        0 |        7 |      8 |       0 |    13 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |       11 |         0 |        0 |        0 |       1 |       5 |      9 |       3 |        6 |       0 |        0 |    0 |        1 |         1 |
| Brian    |       51 |     10 |      84 |     220 |         3 |     24 |    44 |       62 |     83 |        50 |        77 |     13 |      8 |     37 |          1 |        1 |        0 |      14 |        0 |        4 |      9 |       1 |     6 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |       12 |         3 |        7 |        3 |       1 |       4 |     10 |       3 |        9 |       0 |        0 |    0 |        1 |         1 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Minh     |       19 |      2 |      19 |      24 |         3 |     69 |    11 |       25 |     27 |        21 |        26 |      7 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      1 |       2 |     2 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       9 |      2 |       0 |        5 |       1 |        2 |    0 |        0 |         0 |
| Jai      |       38 |      2 |      36 |      44 |         2 |     11 |    94 |       32 |     41 |        18 |        24 |      5 |      2 |     20 |          0 |        0 |        0 |       6 |        0 |        0 |      4 |       0 |     3 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         4 |        0 |        0 |       0 |       1 |      2 |       0 |        4 |       2 |        1 |    1 |        1 |         0 |
| Jackie   |       52 |      2 |      61 |      62 |         1 |     25 |    32 |      172 |     69 |        39 |        46 |     10 |      3 |     36 |          0 |        0 |        1 |      13 |        1 |        1 |      6 |       3 |     9 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       1 |        6 |         4 |        5 |        1 |       2 |      11 |      8 |       1 |        5 |       2 |        0 |    0 |        0 |         1 |
| Kate     |       45 |      5 |      55 |      83 |         3 |     27 |    41 |       69 |    181 |        43 |        67 |     17 |      5 |     30 |          0 |        0 |        0 |       9 |        0 |        5 |      6 |       1 |    10 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |        7 |         1 |        4 |        1 |       2 |      12 |      6 |       4 |       10 |       3 |        2 |    1 |        1 |         1 |
| Sushant  |       39 |      3 |      51 |      50 |         0 |     21 |    18 |       39 |     43 |       135 |        58 |     16 |      6 |     30 |          2 |        0 |        0 |       5 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       5 |      2 |       0 |        4 |       0 |        1 |    0 |        0 |         0 |
| Abishek  |       37 |      5 |      53 |      77 |         1 |     26 |    24 |       46 |     67 |        58 |       170 |     16 |      7 |     33 |          0 |        0 |        0 |       4 |        0 |        3 |      9 |       1 |    11 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |        2 |         1 |        7 |        0 |       0 |       4 |      2 |       0 |        4 |       0 |        0 |    0 |        3 |         0 |
| Ruhi     |       12 |      2 |      12 |      13 |         2 |      7 |     5 |       10 |     17 |        16 |        16 |     47 |      5 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       4 |      0 |       0 |        1 |       1 |        4 |    0 |        0 |         1 |
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
| Daisy    |        5 |      0 |       5 |       4 |         0 |      9 |     1 |       11 |     12 |         5 |         4 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        2 |       3 |      21 |      3 |       1 |        4 |       0 |        3 |    0 |        0 |         1 |
| Aman     |        1 |      0 |       9 |      10 |         0 |      2 |     2 |        8 |      6 |         2 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         0 |        0 |        4 |       2 |       3 |     20 |       1 |        0 |       0 |        0 |    0 |        0 |         0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       1 |      1 |       6 |        0 |       0 |        0 |    0 |        0 |         0 |
| Andrew   |        2 |      0 |       6 |       9 |         0 |      5 |     4 |        5 |     10 |         4 |         4 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        0 |       0 |       4 |      0 |       0 |       16 |       0 |        0 |    0 |        0 |         1 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       5 |        2 |    1 |        0 |         0 |
| Selena   |        3 |      0 |       0 |       0 |         0 |      2 |     1 |        0 |      2 |         1 |         0 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       3 |      0 |       0 |        0 |       2 |        5 |    0 |        0 |         0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |    1 |        0 |         0 |
| Claire   |        1 |      0 |       1 |       1 |         0 |      0 |     1 |        0 |      1 |         0 |         3 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        3 |         0 |
| Timothy  |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        1 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |         2 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|----------|
| Rachel   |       -1 |      2 |       7 |       4 |         2 |      4 |     7 |        9 |      6 |         7 |         7 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      2 |       0 |     2 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        1 |        0 |       0 |       0 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |         0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Peter    |        7 |      0 |      -1 |      21 |         2 |      6 |    10 |        9 |      7 |        17 |        20 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     5 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      4 |       1 |        0 |       0 |        0 |    0 |        1 |         0 |
| Brian    |        4 |      3 |      21 |      -1 |         3 |      6 |     7 |       11 |     15 |        11 |        25 |      2 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |        3 |         0 |        3 |        2 |       0 |       0 |      6 |       2 |        2 |       0 |        0 |    0 |        1 |         0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Minh     |        4 |      1 |       6 |       6 |         2 |     -1 |     2 |        5 |      7 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      1 |       0 |        1 |       1 |        0 |    0 |        0 |         0 |
| Jai      |        7 |      0 |      10 |       7 |         2 |      2 |    -1 |        5 |      9 |         6 |         7 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        1 |       2 |        1 |    1 |        0 |         0 |
| Jackie   |        9 |      0 |       9 |      11 |         0 |      5 |     5 |       -1 |     12 |         8 |        11 |      2 |      2 |      8 |          0 |        0 |        1 |       4 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |        1 |         2 |        3 |        0 |       0 |       4 |      2 |       0 |        1 |       2 |        0 |    0 |        0 |         1 |
| Kate     |        6 |      1 |       7 |      15 |         1 |      7 |     9 |       12 |     -1 |         9 |        15 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      1 |       1 |        0 |       3 |        1 |    1 |        1 |         0 |
| Sushant  |        7 |      1 |      17 |      11 |         0 |      7 |     6 |        8 |      9 |        -1 |        21 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       1 |      1 |       0 |        2 |       0 |        0 |    0 |        0 |         0 |
| Abishek  |        7 |      1 |      20 |      25 |         0 |      5 |     7 |       11 |     15 |        21 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       1 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        3 |        0 |       0 |       0 |      2 |       0 |        0 |       0 |        0 |    0 |        2 |         0 |
| Ruhi     |        2 |      1 |       4 |       2 |         1 |      2 |     3 |        2 |      3 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       1 |        1 |    0 |        0 |         1 |
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
| Daisy    |        0 |      0 |       1 |       0 |         0 |      2 |     0 |        4 |      1 |         1 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |      -1 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |         1 |
| Aman     |        0 |      0 |       4 |       6 |         0 |      1 |     0 |        2 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        2 |       0 |       1 |     -1 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
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
| Rachel   |        0 |      4 |      49 |      61 |         8 |     25 |    31 |       44 |     50 |        39 |        65 |     16 |      6 |     23 |          1 |        0 |        1 |       6 |        1 |        3 |      4 |       3 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |        3 |         3 |        5 |        0 |       0 |       0 |      1 |       0 |        0 |       5 |        2 |    1 |        1 |         0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Peter    |       49 |      5 |       0 |      81 |         4 |     26 |    36 |       74 |     77 |        56 |        66 |     13 |      5 |     42 |          1 |        0 |        1 |      12 |        1 |        2 |      7 |       3 |     7 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       1 |        9 |         0 |        0 |        2 |       1 |       8 |      8 |       3 |        8 |       0 |        0 |    0 |        0 |         1 |
| Brian    |       61 |      2 |      81 |       0 |         9 |     33 |    37 |       93 |     78 |        71 |        76 |     29 |     13 |     44 |          1 |        0 |        1 |      14 |        1 |        5 |      6 |       4 |    14 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       1 |       10 |         4 |        6 |        2 |       3 |      12 |     10 |       3 |        7 |       0 |        0 |    0 |        1 |         1 |
| Anthony  |        8 |      0 |       4 |       9 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Minh     |       25 |      3 |      26 |      33 |         3 |      0 |    13 |       29 |     32 |        12 |        25 |      7 |      2 |     17 |          0 |        0 |        0 |       5 |        0 |        2 |      7 |       0 |     4 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |        1 |         0 |        0 |        0 |       0 |       3 |      4 |       0 |        2 |       4 |        3 |    1 |        3 |         2 |
| Jai      |       31 |      3 |      36 |      37 |         5 |     13 |     0 |       38 |     30 |        32 |        36 |     16 |      2 |     19 |          1 |        0 |        0 |       6 |        0 |        2 |      6 |       0 |    10 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       2 |        4 |         2 |        6 |        0 |       0 |       4 |      2 |       0 |        1 |       0 |        1 |    0 |        2 |         0 |
| Jackie   |       44 |      4 |      74 |      93 |         5 |     29 |    38 |        0 |     58 |        50 |        72 |     12 |      5 |     26 |          0 |        1 |        0 |      10 |        0 |        2 |      8 |       2 |     6 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |       12 |         3 |        8 |        3 |       1 |       3 |      8 |       1 |        7 |       1 |        3 |    0 |        3 |         1 |
| Kate     |       50 |      6 |      77 |      78 |         6 |     32 |    30 |       58 |      0 |        61 |        63 |     21 |     10 |     36 |          2 |        0 |        0 |       5 |        0 |        1 |      8 |       1 |    15 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |       10 |         0 |        3 |        4 |       2 |       9 |     14 |       2 |        5 |       2 |        3 |    0 |        2 |         1 |
| Sushant  |       39 |      4 |      56 |      71 |         1 |     12 |    32 |       50 |     61 |         0 |        62 |     18 |      5 |     38 |          0 |        0 |        0 |      12 |        0 |        5 |      5 |       3 |    12 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       1 |      4 |       0 |        2 |       2 |        1 |    1 |        1 |         0 |
| Abishek  |       65 |      4 |      66 |      76 |         4 |     25 |    36 |       72 |     63 |        62 |         0 |     21 |      7 |     43 |          0 |        0 |        0 |      15 |        0 |        5 |      7 |       3 |    13 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |        2 |         6 |        6 |        0 |       0 |       4 |      5 |       0 |        1 |       2 |        2 |    0 |        0 |         0 |
| Ruhi     |       16 |      1 |      13 |      29 |         1 |      7 |    16 |       12 |     21 |        18 |        21 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      1 |       0 |        2 |       3 |        0 |    1 |        0 |         0 |
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
| Daisy    |        0 |      0 |       8 |      12 |         0 |      3 |     4 |        3 |      9 |         1 |         4 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         0 |        0 |        3 |       1 |       0 |      9 |       1 |        5 |       5 |        2 |    1 |        0 |         1 |
| Aman     |        1 |      0 |       8 |      10 |         0 |      4 |     2 |        8 |     14 |         4 |         5 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       9 |      0 |       2 |       12 |       0 |        0 |    0 |        1 |         0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        2 |       1 |       1 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |         0 |
| Andrew   |        0 |      0 |       8 |       7 |         0 |      2 |     1 |        7 |      5 |         2 |         1 |      2 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       5 |     12 |       0 |        0 |       0 |        0 |    0 |        0 |         1 |
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
| 3+1        | 0.371429 |            35 |
| 2+2        | 0.381579 |            76 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|-----------|---------|--------------|
| 3+1        | 0.333333 |            33 |
| 2+2        | 0.347222 |            72 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |   Win % |   Sample Size |
|-------------|--------|--------------|
| Fail         | 0.40625 |            32 |
| Success      | 0.31405 |           121 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.40625  |            32 |
| Success      | 0.302521 |           119 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |      % |   Good Win % |
|----------|--------|-------|-------------|
|         0 |      37 | 0.4625 |     0.324324 |
|         1 |      32 | 0.4    |     0.15625  |
|         2 |      11 | 0.1375 |     0.363636 |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |      15 | 0.789474 |     0.133333 |
|         1 |       4 | 0.210526 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |      12 | 0.4      |     0.5      |
|         1 |      13 | 0.433333 |     0.153846 |
|         2 |       5 | 0.166667 |     0.2      |

*2 bad guys on mission 3:*

|   # Fails |   Count |    % |   Good Win % |
|----------|--------|-----|-------------|
|         0 |       8 | 0.32 |         0.5  |
|         1 |      12 | 0.48 |         0.25 |
|         2 |       5 | 0.2  |         0.4  |

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
|                   0 |            96 |     0.510417 |
|                   1 |           124 |     0.354839 |
|                   2 |            17 |     0.588235 |
|                   3 |             6 |     0.5      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|--------------------|--------------|-------------|
|                   0 |            91 |     0.483516 |
|                   1 |           118 |     0.322034 |
|                   2 |            17 |     0.588235 |
|                   3 |             6 |     0.5      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|--------------|------------------------|--------------|----------------|
| Merlin        |                 0.11111 |           243 |              27 |
| Assassin      |                 0.03415 |           205 |               7 |
| Morgana       |                 0.05907 |           237 |              14 |
| Mordred       |                 0.0146  |           137 |               2 |
| Loyal Servant |                 0       |           675 |               0 |
| Oberon        |                 0.0137  |            73 |               1 |
| Minion #1     |                 0.05556 |            36 |               2 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|---------|----------------------------|-------------------|--------------|
| Jeron    |                    0.5      |                  3 |             6 |
| Abishek  |                    0.459459 |                 17 |            37 |
| Minh     |                    0.4      |                  4 |            10 |
| Alex     |                    0.363636 |                  8 |            22 |
| Tercel   |                    0.333333 |                  2 |             6 |
| Jai      |                    0.3125   |                  5 |            16 |
| Rachel   |                    0.296296 |                  8 |            27 |
| Kate     |                    0.288462 |                 15 |            52 |
| Jackie   |                    0.243243 |                  9 |            37 |
| Sushant  |                    0.238095 |                  5 |            21 |
| Peter    |                    0.222222 |                  8 |            36 |
| Brian    |                    0.188679 |                 10 |            53 |
| Ruhi     |                    0.166667 |                  1 |             6 |

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
| 5X          |          0.5      |                  2 |             4 |
| 6           |          0.291667 |                  7 |            24 |
| 6M          |          0.363636 |                  4 |            11 |
| 6O          |          0.25     |                  3 |            12 |
| 7           |          0.580645 |                 18 |            31 |
| 7O          |          0.5      |                  4 |             8 |
| 8           |          0.47619  |                 10 |            21 |
| 8O          |          0.666667 |                  2 |             3 |
| 9           |          0.461538 |                 12 |            26 |
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
| 5X          |                   0 |          0.5      |                  2 |             4 |
| 6           |                   0 |          0.307692 |                  4 |            13 |
| 6           |                   1 |          0.3      |                  3 |            10 |
| 6           |                   3 |          0        |                  0 |             1 |
| 6M          |                   0 |          0.444444 |                  4 |             9 |
| 6M          |                   1 |          0        |                  0 |             2 |
| 6O          |                   0 |          0.25     |                  3 |            12 |
| 7           |                   0 |          0.615385 |                  8 |            13 |
| 7           |                   1 |          0.642857 |                  9 |            14 |
| 7           |                   2 |          0.333333 |                  1 |             3 |
| 7           |                   3 |          0        |                  0 |             1 |
| 7O          |                   0 |          0.666667 |                  4 |             6 |
| 7O          |                   2 |          0        |                  0 |             1 |
| 7O          |                   3 |          0        |                  0 |             1 |
| 8           |                   0 |          0.428571 |                  3 |             7 |
| 8           |                   1 |          0.538462 |                  7 |            13 |
| 8           |                   2 |          0        |                  0 |             1 |
| 8O          |                   1 |          0.666667 |                  2 |             3 |
| 9           |                   0 |          0.428571 |                  3 |             7 |
| 9           |                   1 |          0.470588 |                  8 |            17 |
| 9           |                   2 |          0.5      |                  1 |             2 |
| 9L          |                   0 |          1        |                  1 |             1 |
| 9L          |                   1 |          0        |                  0 |             2 |
| 9O          |                   2 |          0        |                  0 |             1 |

### <a id="pass-fail-sequences"></a>Mission success/fail sequence counts


*Lengths: 1*

| Sequence   |   Count |   Frequency |   Good Win % |
|-----------|--------|------------|-------------|
| Success    |     207 |    0.869748 |     0.444444 |
| Fail       |      31 |    0.130252 |     0.387097 |

*Lengths: 2*

| Sequence         |   Count |   Frequency |   Good Win % |
|-----------------|--------|------------|-------------|
| Success, Success |      94 |   0.394958  |     0.62766  |
| Success, Fail    |     113 |   0.47479   |     0.292035 |
| Fail, Success    |      16 |   0.0672269 |     0.625    |
| Fail, Fail       |      15 |   0.0630252 |     0.133333 |

*Lengths: 3*

| Sequence                  |   Count |   Frequency |   Good Win % |
|--------------------------|--------|------------|-------------|
| Success, Success, Success |      57 |  0.239496   |     0.701754 |
| Success, Success, Fail    |      37 |  0.155462   |     0.513514 |
| Success, Fail, Success    |      56 |  0.235294   |     0.428571 |
| Success, Fail, Fail       |      57 |  0.239496   |     0.157895 |
| Fail, Success, Success    |      15 |  0.0630252  |     0.666667 |
| Fail, Success, Fail       |       1 |  0.00420168 |     0        |
| Fail, Fail, Success       |       8 |  0.0336134  |     0.25     |
| Fail, Fail, Fail          |       7 |  0.0294118  |     0        |

*Lengths: 4*

| Sequence                        |   Count |   Frequency | Good Win %          |
|--------------------------------|--------|------------|--------------------|
| Success, Success, Fail, Success |      13 |  0.0751445  | 0.7692307692307693  |
| Success, Success, Fail, Fail    |      24 |  0.138728   | 0.375               |
| Success, Fail, Success, Success |      42 |  0.242775   | 0.47619047619047616 |
| Success, Fail, Success, Fail    |      14 |  0.0809249  | 0.2857142857142857  |
| Success, Fail, Fail, Success    |      41 |  0.236994   | 0.21951219512195122 |
| Success, Fail, Fail, Fail       |      15 |  0.0867052  | 0.0                 |
| Fail, Success, Success, Success |       8 |  0.0462428  | 0.875               |
| Fail, Success, Success, Fail    |       7 |  0.0404624  | 0.42857142857142855 |
| Fail, Success, Fail, Success    |       1 |  0.00578035 | 0.0                 |
| Fail, Success, Fail, Fail       |       0 |  0          | N/A                 |
| Fail, Fail, Success, Success    |       7 |  0.0404624  | 0.2857142857142857  |
| Fail, Fail, Success, Fail       |       1 |  0.00578035 | 0.0                 |

*Lengths: 5*

| Sequence                              |   Count |   Frequency | Good Win %          |
|--------------------------------------|--------|------------|--------------------|
| Success, Success, Fail, Fail, Success |      13 |   0.168831  | 0.46153846153846156 |
| Success, Success, Fail, Fail, Fail    |       6 |   0.0779221 | 0.0                 |
| Success, Fail, Success, Fail, Success |       6 |   0.0779221 | 0.5                 |
| Success, Fail, Success, Fail, Fail    |       2 |   0.025974  | 0.0                 |
| Success, Fail, Fail, Success, Success |      21 |   0.272727  | 0.42857142857142855 |
| Success, Fail, Fail, Success, Fail    |      19 |   0.246753  | 0.0                 |
| Fail, Success, Success, Fail, Success |       1 |   0.012987  | 0.0                 |
| Fail, Success, Success, Fail, Fail    |       1 |   0.012987  | 0.0                 |
| Fail, Success, Fail, Success, Success |       0 |   0         | N/A                 |
| Fail, Success, Fail, Success, Fail    |       1 |   0.012987  | 0.0                 |
| Fail, Fail, Success, Success, Success |       5 |   0.0649351 | 0.4                 |
| Fail, Fail, Success, Success, Fail    |       2 |   0.025974  | 0.0                 |
