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

Cheesy wins included: 0.4136 (n = 162)

Cheesy wins excluded: 0.3831 (n = 154)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            24 |     0.416667 |
| 5           |             8 |     0.25     |
| 5O          |             5 |     0.6      |
| 6           |            15 |     0.6      |
| 6M          |             6 |     0.666667 |
| 6O          |             6 |     0.666667 |
| 7           |            25 |     0.44     |
| 7O          |             5 |     0.4      |
| 8           |            29 |     0.310345 |
| 8O          |             3 |     0        |
| 9           |            31 |     0.322581 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

Cheesy wins excluded:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            23 |     0.391304 |
| 5           |             8 |     0.25     |
| 5O          |             5 |     0.6      |
| 6           |            14 |     0.571429 |
| 6M          |             6 |     0.666667 |
| 6O          |             6 |     0.666667 |
| 7           |            22 |     0.363636 |
| 7O          |             5 |     0.4      |
| 8           |            29 |     0.310345 |
| 8O          |             3 |     0        |
| 9           |            28 |     0.25     |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            80 |       30.05   |     20.6648 |
| Good     |            55 |       21.0727 |     16.829  |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            80 |       30.05   |     20.6648 |
| Good     |            51 |       22.0392 |     17.109  |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|----------|-------------|
| Kate     |           6 |
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
| Abishek  | 0.603774 |     0.5      |    0.73913  |           106 |     64 |       42 |                      0 |
| Brian    | 0.559633 |     0.459459 |    0.771429 |           109 |     61 |       48 |                     13 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                      4 |
| Kate     | 0.516484 |     0.448276 |    0.636364 |            91 |     47 |       44 |                     21 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|----------|----------|--------------|-------------|---------------|--------|----------|------------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.585859 |     0.444444 |    0.755556 |            99 |     58 |       41 |                      4 |
| Brian    | 0.539216 |     0.411765 |    0.794118 |           102 |     55 |       47 |                     16 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kish     | 0.5      |     0.375    |    0.666667 |            14 |      7 |        7 |                      4 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Abishek  |             0.0924666 | 0.603774 |         0.511307 | 0.566038 |
| Brian    |             0.0881482 | 0.559633 |         0.471485 | 0.678899 |
| Kish     |             0.0820272 | 0.529412 |         0.447385 | 0.588235 |
| Ewen     |             0.0436862 | 0.538462 |         0.494775 | 0.615385 |
| Kate     |             0.0348186 | 0.516484 |         0.481665 | 0.637363 |
| Anthony  |             0.0126263 | 0.5      |         0.487374 | 0.166667 |
| Jackie   |             0.0116375 | 0.451613 |         0.439975 | 0.709677 |
| Peter    |             0.010185  | 0.458824 |         0.448639 | 0.623529 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Anthony  |             0.0943723 | 0.6      |         0.505628 | 0.166667 |
| Brian    |             0.0803076 | 0.539216 |         0.458908 | 0.678899 |
| Abishek  |             0.0797846 | 0.585859 |         0.506074 | 0.566038 |
| Ewen     |             0.0636945 | 0.538462 |         0.474767 | 0.615385 |
| Kish     |             0.0328222 | 0.5      |         0.467178 | 0.588235 |
| Kate     |             0.0204711 | 0.494118 |         0.473647 | 0.637363 |
| Jade     |             0.0143121 | 0.333333 |         0.319021 | 1        |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.636364 |            11 |      7 |        4 |                    0 |
| Kate     | 0.6      |            10 |      6 |        4 |                    2 |
| Minh     | 0.5      |             6 |      3 |        3 |                    3 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Sushant |
|----------|----------|---------------|--------|----------|------------------------|
| Sushant  | 0.666667 |             6 |      4 |        2 |                      0 |
| Jackie   | 0.625    |             8 |      5 |        3 |                      2 |
| Kate     | 0.6      |            10 |      6 |        4 |                      3 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.727273 |            11 |      8 |        3 |                    0 |
| Abishek  | 0.692308 |            13 |      9 |        4 |                    2 |
| Sushant  | 0.666667 |            12 |      8 |        4 |                    3 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Brian    | 0.733333 |            15 |     11 |        4 |                     14 |
| Kate     | 0.636364 |            11 |      7 |        4 |                     18 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 1        |             9 |      9 |        0 |                   0 |
| Brian    | 1        |             8 |      8 |        0 |                 nan |
| Peter    | 0.857143 |             7 |      6 |        1 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.612903 |            31 |     19 |       12 |                      0 |
| Ruhi     | 0.5      |            12 |      6 |        6 |                      4 |
| Rachel   | 0.4375   |            32 |     14 |       18 |                     15 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|---------|---------------|--------|----------|----------------------|
| Brian    |     0.6 |            10 |      6 |        4 |                    0 |
| Kate     |     0.6 |            10 |      6 |        4 |                    1 |
| Abishek  |     0.4 |            10 |      4 |        6 |                    6 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Sushant |
|----------|----------|---------------|--------|----------|------------------------|
| Sushant  | 0.666667 |             6 |      4 |        2 |                      0 |
| Jackie   | 0.625    |             8 |      5 |        3 |                      2 |
| Kate     | 0.5      |             8 |      4 |        4 |                      5 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.75     |            12 |      9 |        3 |                      0 |
| Sushant  | 0.727273 |            11 |      8 |        3 |                      2 |
| Brian    | 0.727273 |            11 |      8 |        3 |                      2 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Brian    | 0.785714 |            14 |     11 |        3 |                      8 |
| Rachel   | 0.666667 |             6 |      4 |        2 |                      9 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 1        |             9 |      9 |        0 |                   0 |
| Brian    | 1        |             8 |      8 |        0 |                 nan |
| Peter    | 0.857143 |             7 |      6 |        1 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.538462 |            26 |     14 |       12 |                      0 |
| Rachel   | 0.4      |            30 |     12 |       18 |                     10 |
| Ruhi     | 0.4      |            10 |      4 |        6 |                      4 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|----------|----------------|
| Brian    |            148 |
| Peter    |            128 |
| Abishek  |            125 |
| Kate     |            121 |
| Sushant  |            108 |
| Jackie   |            103 |
| Rachel   |            102 |
| Alex     |             83 |
| Jai      |             60 |
| Minh     |             51 |
| Ruhi     |             38 |
| Jeron    |             25 |
| Kish     |             20 |
| Jay      |             19 |
| Ewen     |             13 |
| Jade     |             13 |
| Anthony  |             12 |
| Justin   |              9 |
| Sai      |              8 |
| Gathenji |              7 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|----------|----------|----------|---------|
| Gathenji | 0.857143 |        6 |       1 |
| Jade     | 0.769231 |       10 |       3 |
| Rachel   | 0.72549  |       74 |      28 |
| Jackie   | 0.708738 |       73 |      30 |
| Justin   | 0.666667 |        6 |       3 |
| Brian    | 0.662162 |       98 |      50 |
| Alex     | 0.650602 |       54 |      29 |
| Kate     | 0.644628 |       78 |      43 |
| Jeron    | 0.64     |       16 |       9 |
| Jay      | 0.631579 |       12 |       7 |
| Sai      | 0.625    |        5 |       3 |
| Jai      | 0.616667 |       37 |      23 |
| Ewen     | 0.615385 |        8 |       5 |
| Kish     | 0.6      |       12 |       8 |
| Peter    | 0.59375  |       76 |      52 |
| Sushant  | 0.583333 |       63 |      45 |
| Abishek  | 0.576    |       72 |      53 |
| Minh     | 0.529412 |       27 |      24 |
| Ruhi     | 0.5      |       19 |      19 |
| Anthony  | 0.25     |        3 |       9 |

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
| No                 |           148 |     0.439189 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           148 |     0.439189 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       15 |         20 |         15 |        16 |         6 |        8 |           8 |              37 |           125 |
| Alex     |        9 |         13 |         12 |        11 |         4 |        1 |           1 |              32 |            83 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       16 |         28 |         16 |        22 |        11 |        0 |           1 |              54 |           148 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       19 |         13 |          6 |        12 |         5 |        5 |           2 |              41 |           103 |
| Jade     |        3 |          1 |          0 |         1 |         1 |        1 |           0 |               6 |            13 |
| Jai      |        9 |          4 |          6 |         8 |         6 |        3 |           0 |              24 |            60 |
| Jay      |        3 |          3 |          3 |         0 |         3 |        1 |           0 |               6 |            19 |
| Jeron    |        4 |          8 |          1 |         4 |         2 |        1 |           1 |               4 |            25 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       12 |         12 |          8 |        13 |        10 |       10 |           2 |              54 |           121 |
| Kish     |        3 |          3 |          1 |         4 |         2 |        0 |           1 |               6 |            20 |
| Minh     |        6 |          5 |         10 |         5 |         5 |        2 |           2 |              16 |            51 |
| Peter    |       20 |         14 |         20 |        17 |         8 |        5 |           2 |              42 |           128 |
| Rachel   |       15 |         15 |          8 |         9 |         9 |        0 |           2 |              44 |           102 |
| Ruhi     |        1 |          5 |          5 |         7 |         6 |        1 |           0 |              13 |            38 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       19 |          8 |         14 |        18 |         8 |        3 |           2 |              36 |           108 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.094 |      0.125 |      0.11  |     0.102 |     0.066 |    0.174 |       0.333 |           0.083 |           125 |
| Alex     |    0.057 |      0.081 |      0.088 |     0.07  |     0.044 |    0.022 |       0.042 |           0.071 |            83 |
| Anthony  |    0     |      0.012 |      0.029 |     0.025 |     0     |    0.022 |       0     |           0.002 |            12 |
| Brian    |    0.101 |      0.175 |      0.118 |     0.14  |     0.121 |    0     |       0.042 |           0.121 |           148 |
| Ewen     |    0.006 |      0.012 |      0.015 |     0.006 |     0     |    0.043 |       0     |           0.011 |            13 |
| Gathenji |    0     |      0     |      0     |     0.006 |     0     |    0     |       0     |           0.013 |             7 |
| Jackie   |    0.119 |      0.081 |      0.044 |     0.076 |     0.055 |    0.109 |       0.083 |           0.092 |           103 |
| Jade     |    0.019 |      0.006 |      0     |     0.006 |     0.011 |    0.022 |       0     |           0.013 |            13 |
| Jai      |    0.057 |      0.025 |      0.044 |     0.051 |     0.066 |    0.065 |       0     |           0.054 |            60 |
| Jay      |    0.019 |      0.019 |      0.022 |     0     |     0.033 |    0.022 |       0     |           0.013 |            19 |
| Jeron    |    0.025 |      0.05  |      0.007 |     0.025 |     0.022 |    0.022 |       0.042 |           0.009 |            25 |
| Justin   |    0.013 |      0     |      0.007 |     0.006 |     0.011 |    0     |       0     |           0.009 |             9 |
| Kate     |    0.075 |      0.075 |      0.059 |     0.083 |     0.11  |    0.217 |       0.083 |           0.121 |           121 |
| Kish     |    0.019 |      0.019 |      0.007 |     0.025 |     0.022 |    0     |       0.042 |           0.013 |            20 |
| Minh     |    0.038 |      0.031 |      0.074 |     0.032 |     0.055 |    0.043 |       0.083 |           0.036 |            51 |
| Peter    |    0.126 |      0.088 |      0.147 |     0.108 |     0.088 |    0.109 |       0.083 |           0.094 |           128 |
| Rachel   |    0.094 |      0.094 |      0.059 |     0.057 |     0.099 |    0     |       0.083 |           0.098 |           102 |
| Ruhi     |    0.006 |      0.031 |      0.037 |     0.045 |     0.066 |    0.022 |       0     |           0.029 |            38 |
| Sai      |    0.006 |      0.006 |      0     |     0.006 |     0.022 |    0     |       0     |           0.007 |             8 |
| Sushant  |    0.119 |      0.05  |      0.103 |     0.115 |     0.088 |    0.065 |       0.083 |           0.08  |           108 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.12  |      0.16  |      0.12  |     0.128 |     0.048 |    0.064 |       0.064 |           0.296 |           125 |
| Alex     |    0.108 |      0.157 |      0.145 |     0.133 |     0.048 |    0.012 |       0.012 |           0.386 |            83 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.108 |      0.189 |      0.108 |     0.149 |     0.074 |    0     |       0.007 |           0.365 |           148 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.184 |      0.126 |      0.058 |     0.117 |     0.049 |    0.049 |       0.019 |           0.398 |           103 |
| Jade     |    0.231 |      0.077 |      0     |     0.077 |     0.077 |    0.077 |       0     |           0.462 |            13 |
| Jai      |    0.15  |      0.067 |      0.1   |     0.133 |     0.1   |    0.05  |       0     |           0.4   |            60 |
| Jay      |    0.158 |      0.158 |      0.158 |     0     |     0.158 |    0.053 |       0     |           0.316 |            19 |
| Jeron    |    0.16  |      0.32  |      0.04  |     0.16  |     0.08  |    0.04  |       0.04  |           0.16  |            25 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.099 |      0.099 |      0.066 |     0.107 |     0.083 |    0.083 |       0.017 |           0.446 |           121 |
| Kish     |    0.15  |      0.15  |      0.05  |     0.2   |     0.1   |    0     |       0.05  |           0.3   |            20 |
| Minh     |    0.118 |      0.098 |      0.196 |     0.098 |     0.098 |    0.039 |       0.039 |           0.314 |            51 |
| Peter    |    0.156 |      0.109 |      0.156 |     0.133 |     0.062 |    0.039 |       0.016 |           0.328 |           128 |
| Rachel   |    0.147 |      0.147 |      0.078 |     0.088 |     0.088 |    0     |       0.02  |           0.431 |           102 |
| Ruhi     |    0.026 |      0.132 |      0.132 |     0.184 |     0.158 |    0.026 |       0     |           0.342 |            38 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.176 |      0.074 |      0.13  |     0.167 |     0.074 |    0.028 |       0.019 |           0.333 |           108 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.46 |    0.48 |      0.33 |   0.36 |  0.56 |     0.56 |   0.48 |      0.49 |      0.34 |   0.39 |   0.6  |   0.57 |    0.72 |     0.57 |   0.75 |  0.62 |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.46 |   0.17 |    1    |    0.51 |      0.43 |   0.41 |  0.45 |     0.47 |   0.34 |      0.52 |      0.44 |   0.48 |   0.55 |   0.43 |    0.42 |     0.78 |   0.7  |  0.69 |      -1    |  0.29 |
| Brian    |     0.48 |   0.83 |    0.51 |    1    |      0.25 |   0.38 |  0.56 |     0.52 |   0.52 |      0.42 |      0.5  |   0.32 |   0.4  |   0.49 |    0.48 |     0.44 |   0.6  |  0.2  |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |    0.43 |    0.25 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.36 |   0.4  |    0.41 |    0.38 |      0.5  |   1    |  0.5  |     0.42 |   0.44 |      0.6  |      0.55 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.56 |   0.4  |    0.45 |    0.56 |      0.29 |   0.5  |  1    |     0.48 |   0.59 |      0.35 |      0.42 |   0.19 |  -1    |   0.53 |    0.4  |    -1    |   0.4  |  0.29 |       0.8  | -1    |
| Jackie   |     0.56 |   0.33 |    0.47 |    0.52 |      0.17 |   0.42 |  0.48 |     1    |   0.56 |      0.43 |      0.42 |   0.44 |   0.43 |   0.57 |    0.62 |    -1    |   0.29 |  0.62 |      -1    |  0.4  |
| Kate     |     0.48 |   0.45 |    0.34 |    0.52 |      0.33 |   0.44 |  0.59 |     0.56 |   1    |      0.42 |      0.51 |   0.43 |   0.29 |   0.44 |    0.75 |     0.83 |   0.4  |  0.33 |       0.57 |  0.5  |
| Sushant  |     0.49 |   0.43 |    0.52 |    0.42 |     -1    |   0.6  |  0.35 |     0.43 |   0.42 |      1    |      0.49 |   0.48 |   0.5  |   0.44 |    0.27 |     0.17 |   0.5  |  0.53 |       0.5  |  0.38 |
| Abishek  |     0.34 |   0.56 |    0.44 |    0.5  |      0.2  |   0.55 |  0.42 |     0.42 |   0.51 |      0.49 |      1    |   0.44 |   0.46 |   0.45 |    0.13 |     0.38 |   0.67 |  0.53 |       0.29 |  0.62 |
| Ruhi     |     0.39 |  -1    |    0.48 |    0.32 |     -1    |   0.56 |  0.19 |     0.44 |   0.43 |      0.48 |      0.44 |   1    |   0.67 |   0.53 |    0.44 |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.6  |   0    |    0.55 |    0.4  |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |    0.2  |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.57 |   0.2  |    0.43 |    0.49 |     -1    |   0.32 |  0.53 |     0.57 |   0.44 |      0.44 |      0.45 |   0.53 |  -1    |   1    |    0.67 |     0.67 |   0.2  |  0.44 |       0.4  |  0.5  |
| Jeron    |     0.72 |  -1    |    0.42 |    0.48 |      0.5  |   0.33 |  0.4  |     0.62 |   0.75 |      0.27 |      0.13 |   0.44 |   0.2  |   0.67 |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.75 |  -1    |    0.7  |    0.6  |     -1    |   0    |  0.4  |     0.29 |   0.4  |      0.5  |      0.67 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.62 |  -1    |    0.69 |    0.2  |     -1    |  -1    |  0.29 |     0.62 |   0.33 |      0.53 |      0.53 |   0.57 |  -1    |   0.44 |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.06 |    0.05 |      0.17 |   0.12 |  0.1  |     0.08 |   0.08 |      0.1  |      0.05 |   0.09 |   0.13 |   0.12 |    0.06 |     0    |   0.12 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.06 |   0    |   -1    |    0.13 |      0.29 |   0.18 |  0.16 |     0.08 |   0.05 |      0.16 |      0.16 |   0.17 |   0    |   0.07 |    0.11 |     0.11 |   0.2  |  0.31 |      -1    |  0    |
| Brian    |     0.05 |   0.25 |    0.13 |   -1    |      0.25 |   0.11 |  0.1  |     0.09 |   0.11 |      0.07 |      0.14 |   0.03 |   0.15 |   0.09 |    0.09 |     0    |   0    |  0    |       0    |  0.12 |
| Anthony  |     0.17 |  -1    |    0.29 |    0.25 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.12 |   0.2  |    0.18 |    0.11 |      0.33 |  -1    |  0.14 |     0.03 |   0.15 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.1  |   0    |    0.16 |    0.1  |      0.29 |   0.14 | -1    |     0.02 |   0.16 |      0.1  |      0.12 |   0.12 |  -1    |   0.16 |    0.1  |    -1    |   0    |  0.14 |       0    | -1    |
| Jackie   |     0.08 |   0    |    0.08 |    0.09 |      0    |   0.03 |  0.02 |    -1    |   0.1  |      0.07 |      0.09 |   0.06 |   0.29 |   0.08 |    0.12 |    -1    |   0    |  0    |      -1    |  0.2  |
| Kate     |     0.08 |   0.09 |    0.05 |    0.11 |      0.11 |   0.15 |  0.16 |     0.1  |  -1    |      0.11 |      0.13 |   0.1  |   0    |   0.09 |    0.17 |     0.33 |   0.1  |  0.06 |       0    |  0.12 |
| Sushant  |     0.1  |   0.14 |    0.16 |    0.07 |     -1    |   0.23 |  0.1  |     0.07 |   0.11 |     -1    |      0.18 |   0.21 |   0    |   0.11 |    0    |     0    |   0.1  |  0.16 |       0    |  0.12 |
| Abishek  |     0.05 |   0.11 |    0.16 |    0.14 |      0    |   0.12 |  0.12 |     0.09 |   0.13 |      0.18 |     -1    |   0.18 |   0.15 |   0.11 |    0    |     0.25 |   0    |  0.11 |       0    |  0.12 |
| Ruhi     |     0.09 |  -1    |    0.17 |    0.03 |     -1    |   0.22 |  0.12 |     0.06 |   0.1  |      0.21 |      0.18 |  -1    |   0.17 |   0.35 |    0.11 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.13 |   0    |    0    |    0.15 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |    0.2  |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.12 |   0    |    0.07 |    0.09 |     -1    |   0.08 |  0.16 |     0.08 |   0.09 |      0.11 |      0.11 |   0.35 |  -1    |  -1    |    0.17 |     0    |   0    |  0.11 |       0    |  0.17 |
| Jeron    |     0.06 |  -1    |    0.11 |    0.09 |      0.33 |   0.17 |  0.1  |     0.12 |   0.17 |      0    |      0    |   0.11 |   0.2  |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.12 |  -1    |    0.2  |    0    |     -1    |   0    |  0    |     0    |   0.1  |      0.1  |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jay      |     0    |  -1    |    0.31 |    0    |     -1    |  -1    |  0.14 |     0    |   0.06 |      0.16 |      0.11 |   0.43 |  -1    |   0.11 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     0    |   0.5  |    0.54 |    0.52 |      0.67 |   0.64 |  0.44 |     0.44 |   0.52 |      0.51 |      0.66 |   0.61 |   0.4  |   0.43 |    0.28 |     0.43 |   0.25 |  0.38 |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.54 |   0.83 |    0    |    0.49 |      0.57 |   0.59 |  0.55 |     0.53 |   0.66 |      0.48 |      0.56 |   0.52 |   0.45 |   0.57 |    0.58 |     0.22 |   0.3  |  0.31 |      -1    |  0.71 |
| Brian    |     0.52 |   0.17 |    0.49 |    0    |      0.75 |   0.62 |  0.44 |     0.48 |   0.48 |      0.58 |      0.5  |   0.68 |   0.6  |   0.51 |    0.52 |     0.56 |   0.4  |  0.8  |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |    0.57 |    0.75 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.64 |   0.6  |    0.59 |    0.62 |      0.5  |   0    |  0.5  |     0.58 |   0.56 |      0.4  |      0.45 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   1    | -1    |      -1    | -1    |
| Jai      |     0.44 |   0.6  |    0.55 |    0.44 |      0.71 |   0.5  |  0    |     0.52 |   0.41 |      0.65 |      0.57 |   0.81 |  -1    |   0.47 |    0.6  |    -1    |   0.6  |  0.71 |       0.2  | -1    |
| Jackie   |     0.44 |   0.67 |    0.53 |    0.48 |      0.83 |   0.58 |  0.52 |     0    |   0.44 |      0.57 |      0.58 |   0.56 |   0.57 |   0.43 |    0.38 |    -1    |   0.71 |  0.38 |      -1    |  0.6  |
| Kate     |     0.52 |   0.55 |    0.66 |    0.48 |      0.67 |   0.56 |  0.41 |     0.44 |   0    |      0.58 |      0.49 |   0.57 |   0.71 |   0.56 |    0.25 |     0.17 |   0.6  |  0.67 |       0.43 |  0.5  |
| Sushant  |     0.51 |   0.57 |    0.48 |    0.58 |     -1    |   0.4  |  0.65 |     0.57 |   0.58 |      0    |      0.51 |   0.52 |   0.5  |   0.56 |    0.73 |     0.83 |   0.5  |  0.47 |       0.5  |  0.62 |
| Abishek  |     0.66 |   0.44 |    0.56 |    0.5  |      0.8  |   0.45 |  0.57 |     0.58 |   0.49 |      0.51 |      0    |   0.56 |   0.54 |   0.55 |    0.87 |     0.62 |   0.33 |  0.47 |       0.71 |  0.38 |
| Ruhi     |     0.61 |  -1    |    0.52 |    0.68 |     -1    |   0.44 |  0.81 |     0.56 |   0.57 |      0.52 |      0.56 |   0    |   0.33 |   0.47 |    0.56 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.4  |   1    |    0.45 |    0.6  |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |    0.8  |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.43 |   0.8  |    0.57 |    0.51 |     -1    |   0.68 |  0.47 |     0.43 |   0.56 |      0.56 |      0.55 |   0.47 |  -1    |   0    |    0.33 |     0.33 |   0.8  |  0.56 |       0.6  |  0.5  |
| Jeron    |     0.28 |  -1    |    0.58 |    0.52 |      0.5  |   0.67 |  0.6  |     0.38 |   0.25 |      0.73 |      0.87 |   0.56 |   0.8  |   0.33 |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.25 |  -1    |    0.3  |    0.4  |     -1    |   1    |  0.6  |     0.71 |   0.6  |      0.5  |      0.33 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.38 |  -1    |    0.31 |    0.8  |     -1    |  -1    |  0.71 |     0.38 |   0.67 |      0.47 |      0.47 |   0.43 |  -1    |   0.56 |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|
| Rachel   |      102 |      4 |      37 |      42 |         4 |     12 |    27 |       37 |     36 |        34 |        26 |      9 |      9 |     28 |          1 |        1 |        0 |      13 |        0 |        4 |      6 |       0 |     8 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       37 |      1 |     128 |      59 |         3 |     14 |    23 |       43 |     32 |        45 |        42 |     11 |      6 |     29 |          1 |        1 |        0 |       8 |        0 |        7 |      7 |       0 |     9 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |
| Brian    |       42 |     10 |      59 |     148 |         3 |     17 |    29 |       48 |     57 |        41 |        57 |     12 |      8 |     34 |          1 |        1 |        0 |      11 |        0 |        4 |      6 |       0 |     3 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       12 |      2 |      14 |      17 |         3 |     51 |     7 |       16 |     18 |        18 |        22 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |
| Jai      |       27 |      2 |      23 |      29 |         2 |      7 |    60 |       19 |     30 |        14 |        17 |      3 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     2 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |       37 |      2 |      43 |      48 |         1 |     16 |    19 |      103 |     44 |        29 |        32 |      7 |      3 |     29 |          0 |        0 |        1 |      10 |        1 |        1 |      2 |       1 |     5 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       0 |
| Kate     |       36 |      5 |      32 |      57 |         3 |     18 |    30 |       44 |    121 |        34 |        49 |     13 |      4 |     28 |          0 |        0 |        0 |       9 |        0 |        5 |      4 |       1 |     6 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |
| Sushant  |       34 |      3 |      45 |      41 |         0 |     18 |    14 |       29 |     34 |       108 |        49 |     14 |      5 |     29 |          2 |        0 |        0 |       4 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Abishek  |       26 |      5 |      42 |      57 |         1 |     22 |    17 |       32 |     49 |        49 |       125 |     15 |      6 |     33 |          0 |        0 |        0 |       2 |        0 |        3 |      6 |       0 |    10 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |
| Ruhi     |        9 |      2 |      11 |      12 |         2 |      5 |     3 |        7 |     13 |        14 |        15 |     38 |      4 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        9 |      0 |       6 |       8 |         2 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     20 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       28 |      1 |      29 |      34 |         0 |      8 |    17 |       29 |     28 |        29 |        33 |      9 |      2 |     83 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       1 |     4 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |       13 |      0 |       8 |      11 |         3 |      2 |     4 |       10 |      9 |         4 |         2 |      4 |      1 |      4 |          0 |        0 |        1 |      25 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |       -1 |      2 |       5 |       4 |         2 |      4 |     5 |        5 |      6 |         7 |         4 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Peter    |        5 |      0 |      -1 |      15 |         2 |      6 |     8 |        7 |      5 |        14 |        15 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     4 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Brian    |        4 |      3 |      15 |      -1 |         3 |      5 |     5 |        8 |     12 |         7 |        16 |      1 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |        4 |      1 |       6 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jai      |        5 |      0 |       8 |       5 |         2 |      2 |    -1 |        1 |      8 |         4 |         5 |      2 |      0 |      5 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |        5 |      0 |       7 |       8 |         0 |      1 |     1 |       -1 |      8 |         5 |         7 |      1 |      2 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Kate     |        6 |      1 |       5 |      12 |         1 |      6 |     8 |        8 |     -1 |         9 |        13 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |
| Sushant  |        7 |      1 |      14 |       7 |         0 |      7 |     4 |        5 |      9 |        -1 |        18 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Abishek  |        4 |      1 |      15 |      16 |         0 |      5 |     5 |        7 |     13 |        18 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Ruhi     |        2 |      1 |       4 |       1 |         1 |      2 |     2 |        1 |      3 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        2 |      0 |       0 |       3 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     5 |        4 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        1 |      0 |       2 |       2 |         2 |      1 |     1 |        2 |      2 |         0 |         0 |      1 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |        0 |      4 |      43 |      46 |         8 |     21 |    21 |       29 |     39 |        36 |        50 |     14 |      6 |     21 |          1 |        0 |        1 |       5 |        1 |        3 |      2 |       1 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       43 |      5 |       0 |      57 |         4 |     20 |    28 |       49 |     61 |        42 |        53 |     12 |      5 |     38 |          1 |        0 |        1 |      11 |        1 |        2 |      3 |       2 |     4 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       0 |
| Brian    |       46 |      2 |      57 |       0 |         9 |     28 |    23 |       45 |     53 |        57 |        57 |     25 |     12 |     36 |          1 |        0 |        1 |      12 |        1 |        5 |      4 |       2 |    12 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       0 |
| Anthony  |        8 |      0 |       4 |       9 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       21 |      3 |      20 |      28 |         3 |      0 |     7 |       22 |     23 |        12 |        18 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      5 |       0 |     3 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |
| Jai      |       21 |      3 |      28 |      23 |         5 |      7 |     0 |       21 |     21 |        26 |        23 |     13 |      1 |     15 |          1 |        0 |        0 |       6 |        0 |        2 |      3 |       0 |     5 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |
| Jackie   |       29 |      4 |      49 |      45 |         5 |     22 |    21 |        0 |     34 |        39 |        44 |      9 |      4 |     22 |          0 |        1 |        0 |       6 |        0 |        2 |      5 |       1 |     3 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |
| Kate     |       39 |      6 |      61 |      53 |         6 |     23 |    21 |       34 |      0 |        47 |        48 |     17 |     10 |     36 |          2 |        0 |        0 |       3 |        0 |        1 |      6 |       1 |    12 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |
| Sushant  |       36 |      4 |      42 |      57 |         1 |     12 |    26 |       39 |     47 |         0 |        52 |     15 |      5 |     37 |          0 |        0 |        0 |      11 |        0 |        5 |      5 |       0 |     9 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |
| Abishek  |       50 |      4 |      53 |      57 |         4 |     18 |    23 |       44 |     48 |        52 |         0 |     19 |      7 |     41 |          0 |        0 |        0 |      13 |        0 |        5 |      3 |       1 |     9 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |
| Ruhi     |       14 |      1 |      12 |      25 |         1 |      4 |    13 |        9 |     17 |        15 |        19 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        6 |      5 |       5 |      12 |         2 |      2 |     1 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       4 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       21 |      4 |      38 |      36 |         0 |     17 |    15 |       22 |     36 |        37 |        41 |      8 |      1 |      0 |          1 |        0 |        0 |       2 |        0 |        2 |      4 |       0 |     5 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        5 |      1 |      11 |      12 |         3 |      4 |     6 |        6 |      3 |        11 |        13 |      5 |      4 |      2 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |    -1    |   -1   |    0.28 |    0.45 |   0.44 |  0.23 |     0.39 |   0.4  |      0.37 |      0.57 |   0.14 |   0.43 |   0.38 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.28 |   -1   |   -1    |    0.51 |   0.43 |  0.31 |     0.41 |   0.5  |      0.41 |      0.61 |   0.4  |   0.2  |   0.3  |   -1    |     0.14 |    0.2 |  0.5  |      -1    |  -1   |
| Brian    |     0.45 |    0.5 |    0.51 |   -1    |   0.38 |  0.4  |     0.44 |   0.58 |      0.5  |      0.63 |   0.58 |   0.83 |   0.54 |    0.5  |    -1    |    0.5 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |    0.43 |    0.38 |  -1    |  0    |     0.25 |   0.53 |      0.38 |      0.45 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.23 |   -1   |    0.31 |    0.4  |   0    | -1    |     0.09 |   0.35 |      0.31 |      0.53 |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.39 |   -1   |    0.41 |    0.44 |   0.25 |  0.09 |    -1    |   0.48 |      0.46 |      0.52 |   0    |  -1    |   0.5  |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.4  |    0.6 |    0.5  |    0.58 |   0.53 |  0.35 |     0.48 |  -1    |      0.42 |      0.6  |   0.27 |  -1    |   0.58 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.37 |   -1   |    0.41 |    0.5  |   0.38 |  0.31 |     0.46 |   0.42 |     -1    |      0.56 |   0.43 |   0.4  |   0.44 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1   |
| Abishek  |     0.57 |    0.4 |    0.61 |    0.63 |   0.45 |  0.53 |     0.52 |   0.6  |      0.56 |     -1    |   0.53 |   0.83 |   0.55 |   -1    |    -1    |    0.5 |  0.57 |      -1    |   0.2 |
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
| Rachel   |    -1    |   -1   |    0.28 |    0.42 |   0.44 |  0.25 |     0.39 |   0.38 |      0.38 |      0.55 |   0    |   0.33 |   0.41 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.28 |   -1   |   -1    |    0.49 |   0.33 |  0.25 |     0.39 |   0.42 |      0.38 |      0.58 |   0.4  |  -1    |   0.27 |   -1    |     0.14 |    0.2 |  0.5  |      -1    |
| Brian    |     0.42 |    0.5 |    0.49 |   -1    |   0.33 |  0.37 |     0.42 |   0.56 |      0.49 |      0.6  |   0.5  |  -1    |   0.52 |    0.5  |    -1    |    0.5 | -1    |      -1    |
| Minh     |     0.44 |   -1   |    0.33 |    0.33 |  -1    |  0    |     0.1  |   0.46 |      0.29 |      0.42 |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.25 |   -1   |    0.25 |    0.37 |   0    | -1    |     0.09 |   0.35 |      0.31 |      0.5  |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.39 |   -1   |    0.39 |    0.42 |   0.1  |  0.09 |    -1    |   0.43 |      0.41 |      0.5  |   0    |  -1    |   0.47 |    0.33 |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.38 |    0.6 |    0.42 |    0.56 |   0.46 |  0.35 |     0.43 |  -1    |      0.36 |      0.56 |   0.27 |  -1    |   0.57 |    0.6  |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.38 |   -1   |    0.38 |    0.49 |   0.29 |  0.31 |     0.41 |   0.36 |     -1    |      0.54 |   0.43 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.12 |      -1    |
| Abishek  |     0.55 |    0.4 |    0.58 |    0.6  |   0.42 |  0.5  |     0.5  |   0.56 |      0.54 |     -1    |   0.5  |   0.8  |   0.54 |   -1    |    -1    |    0.5 |  0.57 |      -1    |
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
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      0.83 |      1    |  -1    |    0.75 |    0.5  |     1    |   0.5  | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |   0    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.82 |    0.33 |     0.25 |   1    | -1    |
| Sushant  |   0.33 |     0.83 |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.79 |    0.64 |     0.5  |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.5  |  0.33 |
| Brian    |  -1    |     0.75 |      1 | -1    |   0.82 |      0.71 |      0.79 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.33 |      0.58 |      0.64 |   0.75 |    0.89 |   -1    |     0.8  |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |   0.25 |      0.67 |      0.5  |  -1    |    0.8  |    0.8  |    -1    |  -1    | -1    |
| Alex     |  -1    |     0.5  |     -1 |  0    |   1    |      0.67 |      0.88 |   0.5  |    0.83 |    0.33 |    -1    |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |
|----------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |   -1    |    -1    |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      1    |      1    |  -1    |    0.75 |    0.5  |     1    |   0.75 | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |  -1    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.82 |    0.33 |     0.25 |   1    | -1    |
| Sushant  |   0.33 |     1    |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.85 |    0.64 |     0.5  |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.75 |  0.33 |
| Brian    |  -1    |     0.75 |      1 | -1    |   0.82 |      0.71 |      0.85 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.33 |      0.58 |      0.64 |   0.75 |    0.89 |   -1    |     0.8  |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |   0.25 |      0.67 |      0.5  |  -1    |    0.8  |    0.8  |    -1    |  -1    | -1    |
| Alex     |  -1    |     0.75 |     -1 | -1    |   1    |      0.67 |      0.88 |   0.75 |    0.83 |    0.33 |    -1    |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Peter    |   -1    |    0.41 |   0.62 |     0.5  |    0.2 |  0.56 |     0.48 |   0.5  |      0.47 |      0.37 |   0.7  |  -1    |   0.6  |    0.4  |     -1   |   -1   | -1    |       -1   |   0.8 |
| Brian    |    0.59 |   -1    |   0.59 |     0.63 |   -1   |  0.69 |     0.56 |   0.56 |      0.57 |      0.47 |   0.73 |   0.64 |   0.64 |   -1    |      0.6 |   -1   |  0.55 |       -1   |  -1   |
| Minh     |    0.38 |    0.41 |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.27 |      0.33 |      0.4  |  -1    |  -1    |   0.33 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Rachel   |    0.5  |    0.37 |   0.5  |    -1    |   -1   |  0.55 |     0.55 |   0.42 |      0.45 |      0.33 |   0.62 |   0.6  |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.31 |  -1    |     0.45 |   -1   | -1    |     0.4  |   0.29 |      0.38 |      0.24 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jackie   |    0.52 |    0.44 |   0.5  |     0.45 |   -1   |  0.6  |    -1    |   0.48 |      0.38 |      0.39 |   0.5  |  -1    |   0.53 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Kate     |    0.5  |    0.44 |   0.73 |     0.58 |    0.5 |  0.71 |     0.52 |  -1    |      0.57 |      0.41 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |    0.8 |  0.44 |       -1   |  -1   |
| Sushant  |    0.53 |    0.43 |   0.67 |     0.55 |   -1   |  0.62 |     0.62 |   0.42 |     -1    |      0.36 |   0.6  |   0.4  |   0.42 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |   0.8 |
| Abishek  |    0.63 |    0.53 |   0.6  |     0.67 |   -1   |  0.76 |     0.61 |   0.59 |      0.64 |     -1    |   0.74 |   0.71 |   0.58 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1   |
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
| Peter    |   -1    |    0.39 |   0.62 |     0.46 |    0.2 |  0.53 |     0.48 |   0.5  |      0.45 |      0.36 |   0.67 |  -1    |   0.57 |    0.4  |     -1   |   -1   | -1    |       -1   |
| Brian    |    0.61 |   -1    |   0.6  |     0.61 |   -1   |  0.67 |     0.58 |   0.57 |      0.58 |      0.47 |   0.7  |   0.6  |   0.63 |   -1    |      0.6 |   -1   |  0.55 |       -1   |
| Minh     |    0.38 |    0.4  |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.29 |      0.33 |      0.38 |  -1    |  -1    |   0.29 |   -1    |     -1   |   -1   | -1    |       -1   |
| Rachel   |    0.54 |    0.39 |   0.5  |    -1    |   -1   |  0.6  |     0.57 |   0.45 |      0.48 |      0.36 |   0.62 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Jai      |    0.47 |    0.33 |  -1    |     0.4  |   -1   | -1    |     0.44 |   0.33 |      0.38 |      0.26 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |
| Jackie   |    0.52 |    0.42 |   0.5  |     0.43 |   -1   |  0.56 |    -1    |   0.48 |      0.38 |      0.37 |   0.43 |  -1    |   0.5  |   -1    |     -1   |   -1   | -1    |       -1   |
| Kate     |    0.5  |    0.43 |   0.71 |     0.55 |    0.5 |  0.67 |     0.52 |  -1    |      0.57 |      0.41 |   0.62 |   0.33 |   0.48 |   -1    |     -1   |    0.8 |  0.44 |       -1   |
| Sushant  |    0.55 |    0.42 |   0.67 |     0.52 |   -1   |  0.62 |     0.62 |   0.42 |     -1    |      0.35 |   0.57 |  -1    |   0.39 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |
| Abishek  |    0.64 |    0.53 |   0.62 |     0.64 |   -1   |  0.74 |     0.63 |   0.59 |      0.65 |     -1    |   0.71 |   0.67 |   0.56 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |
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
| 3+1        | 0.346154 |            26 |
| 2+2        | 0.381818 |            55 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.32     |            25 |
| 2+2        | 0.333333 |            51 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.444444 |            27 |
| Success      | 0.337662 |            77 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.444444 |            27 |
| Success      | 0.32     |            75 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      23 | 0.433962 |    0.304348  |
|         1 |      21 | 0.396226 |    0.0952381 |
|         2 |       9 | 0.169811 |    0.444444  |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       9 | 0.692308 |     0.111111 |
|         1 |       4 | 0.307692 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       9 | 0.428571 |     0.444444 |
|         1 |       8 | 0.380952 |     0.125    |
|         2 |       4 | 0.190476 |     0.25     |

*2 bad guys on mission 3:*

|   # Fails |   Count |      % |   Good Win % |
|-----------|---------|--------|--------------|
|         0 |       5 | 0.3125 |     0.4      |
|         1 |       7 | 0.4375 |     0.142857 |
|         2 |       4 | 0.25   |     0.5      |

*3 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         1 |       2 | 0.666667 |            0 |
|         2 |       1 | 0.333333 |            1 |

### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            40 |     0.475    |
|                   1 |           102 |     0.372549 |
|                   2 |            15 |     0.533333 |
|                   3 |             5 |     0.4      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            38 |     0.447368 |
|                   1 |            96 |     0.333333 |
|                   2 |            15 |     0.533333 |
|                   3 |             5 |     0.4      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.1358  |           162 |              22 |
| Assassin      |                 0.05    |           140 |               7 |
| Morgana       |                 0.07407 |           162 |              12 |
| Mordred       |                 0.01031 |            97 |               1 |
| Loyal Servant |                 0       |           462 |               0 |
| Oberon        |                 0.02174 |            46 |               1 |
| Minion #1     |                 0.04    |            25 |               1 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Alex     |                    0.4      |                  8 |            20 |
| Abishek  |                    0.392857 |                 11 |            28 |
| Minh     |                    0.375    |                  3 |             8 |
| Jai      |                    0.333333 |                  3 |             9 |
| Jackie   |                    0.291667 |                  7 |            24 |
| Kate     |                    0.285714 |                  8 |            28 |
| Rachel   |                    0.25     |                  5 |            20 |
| Ruhi     |                    0.2      |                  1 |             5 |
| Sushant  |                    0.1875   |                  3 |            16 |
| Peter    |                    0.181818 |                  4 |            22 |
| Brian    |                    0.176471 |                  6 |            34 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Minh     |          0        |                  0 |             3 |
| Brian    |          0.230769 |                  3 |            13 |
| Jeron    |          0.25     |                  1 |             4 |
| Sushant  |          0.272727 |                  3 |            11 |
| Kate     |          0.363636 |                  4 |            11 |
| Abishek  |          0.461538 |                  6 |            13 |
| Jackie   |          0.466667 |                  7 |            15 |
| Peter    |          0.555556 |                 10 |            18 |
| Alex     |          0.571429 |                  4 |             7 |
| Rachel   |          0.636364 |                  7 |            11 |
| Kish     |          0.666667 |                  2 |             3 |
| Jai      |          0.714286 |                  5 |             7 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

| # Players   |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
| 10          |          0.411765 |                  7 |            17 |
| 5           |          0.75     |                  6 |             8 |
| 5O          |          0.4      |                  2 |             5 |
| 6           |          0.307692 |                  4 |            13 |
| 6M          |          0.2      |                  1 |             5 |
| 6O          |          0.333333 |                  2 |             6 |
| 7           |          0.541667 |                 13 |            24 |
| 7O          |          0.6      |                  3 |             5 |
| 8           |          0.5      |                  7 |            14 |
| 8O          |          0.666667 |                  2 |             3 |
| 9           |          0.5      |                  8 |            16 |
| 9L          |          0.333333 |                  1 |             3 |
| 9O          |          0        |                  0 |             1 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

| # Players   |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
| 10          |                   1 |          0.461538 |                  6 |            13 |
| 10          |                   2 |          0        |                  0 |             3 |
| 10          |                   3 |          1        |                  1 |             1 |
| 5           |                   0 |          0.5      |                  2 |             4 |
| 5           |                   1 |          1        |                  4 |             4 |
| 5O          |                   0 |          0.25     |                  1 |             4 |
| 5O          |                   1 |          1        |                  1 |             1 |
| 6           |                   0 |          0.5      |                  2 |             4 |
| 6           |                   1 |          0.25     |                  2 |             8 |
| 6           |                   3 |          0        |                  0 |             1 |
| 6M          |                   0 |          0.333333 |                  1 |             3 |
| 6M          |                   1 |          0        |                  0 |             2 |
| 6O          |                   0 |          0.333333 |                  2 |             6 |
| 7           |                   0 |          0.5      |                  4 |             8 |
| 7           |                   1 |          0.615385 |                  8 |            13 |
| 7           |                   2 |          0.5      |                  1 |             2 |
| 7           |                   3 |          0        |                  0 |             1 |
| 7O          |                   0 |          0.75     |                  3 |             4 |
| 7O          |                   2 |          0        |                  0 |             1 |
| 8           |                   0 |          0.5      |                  1 |             2 |
| 8           |                   1 |          0.5      |                  6 |            12 |
| 8O          |                   1 |          0.666667 |                  2 |             3 |
| 9           |                   0 |          1        |                  2 |             2 |
| 9           |                   1 |          0.416667 |                  5 |            12 |
| 9           |                   2 |          0.5      |                  1 |             2 |
| 9L          |                   0 |          1        |                  1 |             1 |
| 9L          |                   1 |          0        |                  0 |             2 |
| 9O          |                   2 |          0        |                  0 |             1 |
