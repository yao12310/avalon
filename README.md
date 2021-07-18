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

Cheesy wins included: 0.4133 (n = 150)

Cheesy wins excluded: 0.3803 (n = 142)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            24 |     0.416667 |
| 5           |             6 |     0.333333 |
| 5O          |             3 |     0.333333 |
| 6           |            14 |     0.571429 |
| 6M          |             4 |     1        |
| 6O          |             5 |     0.6      |
| 7           |            21 |     0.47619  |
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
| 5           |             6 |     0.333333 |
| 5O          |             3 |     0.333333 |
| 6           |            13 |     0.538462 |
| 6M          |             4 |     1        |
| 6O          |             5 |     0.6      |
| 7           |            18 |     0.388889 |
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
| Bad      |            74 |       30.7297 |     21.2534 |
| Good     |            49 |       22.1224 |     17.2163 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            74 |       30.7297 |     21.2534 |
| Good     |            45 |       23.3111 |     17.4809 |

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
| Brian    |            135 |
| Abishek  |            117 |
| Peter    |            115 |
| Kate     |            111 |
| Sushant  |             99 |
| Rachel   |             96 |
| Jackie   |             91 |
| Alex     |             82 |
| Jai      |             60 |
| Minh     |             49 |
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
| Jackie   | 0.758242 |       69 |      22 |
| Rachel   | 0.71875  |       69 |      27 |
| Justin   | 0.666667 |        6 |       3 |
| Kate     | 0.657658 |       73 |      38 |
| Alex     | 0.646341 |       53 |      29 |
| Brian    | 0.644444 |       87 |      48 |
| Jeron    | 0.64     |       16 |       9 |
| Jay      | 0.631579 |       12 |       7 |
| Sai      | 0.625    |        5 |       3 |
| Jai      | 0.616667 |       37 |      23 |
| Ewen     | 0.615385 |        8 |       5 |
| Kish     | 0.6      |       12 |       8 |
| Peter    | 0.591304 |       68 |      47 |
| Abishek  | 0.581197 |       68 |      49 |
| Sushant  | 0.565657 |       56 |      43 |
| Minh     | 0.530612 |       26 |      23 |
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
| No                 |           136 |     0.441176 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           136 |     0.441176 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       15 |         19 |         14 |        15 |         6 |        8 |           6 |              34 |           117 |
| Alex     |        8 |         13 |         12 |        11 |         4 |        1 |           1 |              32 |            82 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       13 |         24 |         14 |        22 |        11 |        0 |           1 |              50 |           135 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       17 |         12 |          5 |         7 |         4 |        5 |           1 |              40 |            91 |
| Jade     |        3 |          1 |          0 |         1 |         1 |        1 |           0 |               6 |            13 |
| Jai      |        9 |          4 |          6 |         8 |         6 |        3 |           0 |              24 |            60 |
| Jay      |        3 |          3 |          3 |         0 |         3 |        1 |           0 |               6 |            19 |
| Jeron    |        4 |          8 |          1 |         4 |         2 |        1 |           1 |               4 |            25 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       11 |         12 |          8 |        10 |        10 |        8 |           2 |              50 |           111 |
| Kish     |        3 |          3 |          1 |         4 |         2 |        0 |           1 |               6 |            20 |
| Minh     |        6 |          4 |         10 |         5 |         5 |        1 |           2 |              16 |            49 |
| Peter    |       19 |         12 |         18 |        14 |         8 |        5 |           2 |              37 |           115 |
| Rachel   |       15 |         14 |          8 |         9 |         9 |        0 |           1 |              40 |            96 |
| Ruhi     |        1 |          5 |          5 |         7 |         6 |        1 |           0 |              13 |            38 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       15 |          6 |         13 |        18 |         8 |        2 |           2 |              35 |            99 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.102 |      0.128 |      0.109 |     0.103 |     0.067 |    0.19  |        0.3  |           0.08  |           117 |
| Alex     |    0.054 |      0.088 |      0.093 |     0.076 |     0.044 |    0.024 |        0.05 |           0.075 |            82 |
| Anthony  |    0     |      0.014 |      0.031 |     0.028 |     0     |    0.024 |        0    |           0.002 |            12 |
| Brian    |    0.088 |      0.162 |      0.109 |     0.152 |     0.122 |    0     |        0.05 |           0.117 |           135 |
| Ewen     |    0.007 |      0.014 |      0.016 |     0.007 |     0     |    0.048 |        0    |           0.012 |            13 |
| Gathenji |    0     |      0     |      0     |     0.007 |     0     |    0     |        0    |           0.014 |             7 |
| Jackie   |    0.116 |      0.081 |      0.039 |     0.048 |     0.044 |    0.119 |        0.05 |           0.094 |            91 |
| Jade     |    0.02  |      0.007 |      0     |     0.007 |     0.011 |    0.024 |        0    |           0.014 |            13 |
| Jai      |    0.061 |      0.027 |      0.047 |     0.055 |     0.067 |    0.071 |        0    |           0.056 |            60 |
| Jay      |    0.02  |      0.02  |      0.023 |     0     |     0.033 |    0.024 |        0    |           0.014 |            19 |
| Jeron    |    0.027 |      0.054 |      0.008 |     0.028 |     0.022 |    0.024 |        0.05 |           0.009 |            25 |
| Justin   |    0.014 |      0     |      0.008 |     0.007 |     0.011 |    0     |        0    |           0.009 |             9 |
| Kate     |    0.075 |      0.081 |      0.062 |     0.069 |     0.111 |    0.19  |        0.1  |           0.117 |           111 |
| Kish     |    0.02  |      0.02  |      0.008 |     0.028 |     0.022 |    0     |        0.05 |           0.014 |            20 |
| Minh     |    0.041 |      0.027 |      0.078 |     0.034 |     0.056 |    0.024 |        0.1  |           0.038 |            49 |
| Peter    |    0.129 |      0.081 |      0.14  |     0.097 |     0.089 |    0.119 |        0.1  |           0.087 |           115 |
| Rachel   |    0.102 |      0.095 |      0.062 |     0.062 |     0.1   |    0     |        0.05 |           0.094 |            96 |
| Ruhi     |    0.007 |      0.034 |      0.039 |     0.048 |     0.067 |    0.024 |        0    |           0.031 |            38 |
| Sai      |    0.007 |      0.007 |      0     |     0.007 |     0.022 |    0     |        0    |           0.007 |             8 |
| Sushant  |    0.102 |      0.041 |      0.101 |     0.124 |     0.089 |    0.048 |        0.1  |           0.082 |            99 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.128 |      0.162 |      0.12  |     0.128 |     0.051 |    0.068 |       0.051 |           0.291 |           117 |
| Alex     |    0.098 |      0.159 |      0.146 |     0.134 |     0.049 |    0.012 |       0.012 |           0.39  |            82 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.096 |      0.178 |      0.104 |     0.163 |     0.081 |    0     |       0.007 |           0.37  |           135 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.187 |      0.132 |      0.055 |     0.077 |     0.044 |    0.055 |       0.011 |           0.44  |            91 |
| Jade     |    0.231 |      0.077 |      0     |     0.077 |     0.077 |    0.077 |       0     |           0.462 |            13 |
| Jai      |    0.15  |      0.067 |      0.1   |     0.133 |     0.1   |    0.05  |       0     |           0.4   |            60 |
| Jay      |    0.158 |      0.158 |      0.158 |     0     |     0.158 |    0.053 |       0     |           0.316 |            19 |
| Jeron    |    0.16  |      0.32  |      0.04  |     0.16  |     0.08  |    0.04  |       0.04  |           0.16  |            25 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.099 |      0.108 |      0.072 |     0.09  |     0.09  |    0.072 |       0.018 |           0.45  |           111 |
| Kish     |    0.15  |      0.15  |      0.05  |     0.2   |     0.1   |    0     |       0.05  |           0.3   |            20 |
| Minh     |    0.122 |      0.082 |      0.204 |     0.102 |     0.102 |    0.02  |       0.041 |           0.327 |            49 |
| Peter    |    0.165 |      0.104 |      0.157 |     0.122 |     0.07  |    0.043 |       0.017 |           0.322 |           115 |
| Rachel   |    0.156 |      0.146 |      0.083 |     0.094 |     0.094 |    0     |       0.01  |           0.417 |            96 |
| Ruhi     |    0.026 |      0.132 |      0.132 |     0.184 |     0.158 |    0.026 |       0     |           0.342 |            38 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.152 |      0.061 |      0.131 |     0.182 |     0.081 |    0.02  |       0.02  |           0.354 |            99 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.44 |    0.47 |      0.33 |   0.36 |  0.56 |     0.58 |   0.49 |      0.46 |      0.36 |   0.39 |   0.6  |   0.56 |    0.72 |     0.57 |   0.75 |  0.62 |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.44 |   0.17 |    1    |    0.52 |      0.5  |   0.38 |  0.46 |     0.47 |   0.37 |      0.5  |      0.45 |   0.45 |   0.55 |   0.44 |    0.39 |     0.78 |   0.7  |  0.69 |      -1    |  0.29 |
| Brian    |     0.47 |   0.83 |    0.52 |    1    |      0.27 |   0.37 |  0.55 |     0.54 |   0.51 |      0.4  |      0.49 |   0.33 |   0.4  |   0.48 |    0.5  |     0.44 |   0.6  |  0.2  |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |    0.5  |    0.27 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.36 |   0.4  |    0.38 |    0.37 |      0.5  |   1    |  0.5  |     0.44 |   0.46 |      0.6  |      0.55 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.56 |   0.4  |    0.46 |    0.55 |      0.29 |   0.5  |  1    |     0.48 |   0.59 |      0.35 |      0.42 |   0.19 |  -1    |   0.53 |    0.4  |    -1    |   0.4  |  0.29 |       0.8  | -1    |
| Jackie   |     0.58 |   0.33 |    0.47 |    0.54 |      0.17 |   0.44 |  0.48 |     1    |   0.54 |      0.47 |      0.43 |   0.44 |   0.43 |   0.58 |    0.62 |    -1    |   0.29 |  0.62 |      -1    |  0.4  |
| Kate     |     0.49 |   0.45 |    0.37 |    0.51 |      0.33 |   0.46 |  0.59 |     0.54 |   1    |      0.44 |      0.51 |   0.43 |   0.29 |   0.44 |    0.75 |     0.83 |   0.4  |  0.33 |       0.57 |  0.5  |
| Sushant  |     0.46 |   0.43 |    0.5  |    0.4  |     -1    |   0.6  |  0.35 |     0.47 |   0.44 |      1    |      0.48 |   0.48 |   0.5  |   0.44 |    0.27 |     0.17 |   0.5  |  0.53 |       0.5  |  0.38 |
| Abishek  |     0.36 |   0.56 |    0.45 |    0.49 |      0.2  |   0.55 |  0.42 |     0.43 |   0.51 |      0.48 |      1    |   0.44 |   0.46 |   0.45 |    0.13 |     0.38 |   0.67 |  0.53 |       0.29 |  0.62 |
| Ruhi     |     0.39 |  -1    |    0.45 |    0.33 |     -1    |   0.56 |  0.19 |     0.44 |   0.43 |      0.48 |      0.44 |   1    |   0.67 |   0.53 |    0.44 |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.6  |   0    |    0.55 |    0.4  |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |    0.2  |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.56 |   0.2  |    0.44 |    0.48 |     -1    |   0.32 |  0.53 |     0.58 |   0.44 |      0.44 |      0.45 |   0.53 |  -1    |   1    |    0.67 |     0.67 |   0.2  |  0.44 |       0.4  |  0.5  |
| Jeron    |     0.72 |  -1    |    0.39 |    0.5  |      0.5  |   0.33 |  0.4  |     0.62 |   0.75 |      0.27 |      0.13 |   0.44 |   0.2  |   0.67 |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.75 |  -1    |    0.7  |    0.6  |     -1    |   0    |  0.4  |     0.29 |   0.4  |      0.5  |      0.67 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.62 |  -1    |    0.69 |    0.2  |     -1    |  -1    |  0.29 |     0.62 |   0.33 |      0.53 |      0.53 |   0.57 |  -1    |   0.44 |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.05 |    0.05 |      0.17 |   0.12 |  0.1  |     0.07 |   0.08 |      0.11 |      0.06 |   0.09 |   0.13 |   0.12 |    0.06 |     0    |   0.12 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.05 |   0    |   -1    |    0.15 |      0.33 |   0.16 |  0.16 |     0.05 |   0.06 |      0.17 |      0.16 |   0.18 |   0    |   0.08 |    0.11 |     0.11 |   0.2  |  0.31 |      -1    |  0    |
| Brian    |     0.05 |   0.25 |    0.15 |   -1    |      0.27 |   0.12 |  0.1  |     0.09 |   0.11 |      0.08 |      0.14 |   0.03 |   0.15 |   0.09 |    0.09 |     0    |   0    |  0    |       0    |  0.12 |
| Anthony  |     0.17 |  -1    |    0.33 |    0.27 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.12 |   0.2  |    0.16 |    0.12 |      0.33 |  -1    |  0.14 |     0.03 |   0.15 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.1  |   0    |    0.16 |    0.1  |      0.29 |   0.14 | -1    |     0.02 |   0.16 |      0.1  |      0.12 |   0.12 |  -1    |   0.16 |    0.1  |    -1    |   0    |  0.14 |       0    | -1    |
| Jackie   |     0.07 |   0    |    0.05 |    0.09 |      0    |   0.03 |  0.02 |    -1    |   0.06 |      0.08 |      0.07 |   0.06 |   0.29 |   0.08 |    0.12 |    -1    |   0    |  0    |      -1    |  0.2  |
| Kate     |     0.08 |   0.09 |    0.06 |    0.11 |      0.11 |   0.15 |  0.16 |     0.06 |  -1    |      0.12 |      0.12 |   0.1  |   0    |   0.09 |    0.17 |     0.33 |   0.1  |  0.06 |       0    |  0.12 |
| Sushant  |     0.11 |   0.14 |    0.17 |    0.08 |     -1    |   0.23 |  0.1  |     0.08 |   0.12 |     -1    |      0.18 |   0.21 |   0    |   0.11 |    0    |     0    |   0.1  |  0.16 |       0    |  0.12 |
| Abishek  |     0.06 |   0.11 |    0.16 |    0.14 |      0    |   0.12 |  0.12 |     0.07 |   0.12 |      0.18 |     -1    |   0.18 |   0.15 |   0.11 |    0    |     0.25 |   0    |  0.11 |       0    |  0.12 |
| Ruhi     |     0.09 |  -1    |    0.18 |    0.03 |     -1    |   0.22 |  0.12 |     0.06 |   0.1  |      0.21 |      0.18 |  -1    |   0.17 |   0.35 |    0.11 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.13 |   0    |    0    |    0.15 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |    0.2  |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.12 |   0    |    0.08 |    0.09 |     -1    |   0.08 |  0.16 |     0.08 |   0.09 |      0.11 |      0.11 |   0.35 |  -1    |  -1    |    0.17 |     0    |   0    |  0.11 |       0    |  0.17 |
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
| Rachel   |     0    |   0.5  |    0.56 |    0.53 |      0.67 |   0.64 |  0.44 |     0.42 |   0.51 |      0.54 |      0.64 |   0.61 |   0.4  |   0.44 |    0.28 |     0.43 |   0.25 |  0.38 |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.56 |   0.83 |    0    |    0.48 |      0.5  |   0.62 |  0.54 |     0.53 |   0.63 |      0.5  |      0.55 |   0.55 |   0.45 |   0.56 |    0.61 |     0.22 |   0.3  |  0.31 |      -1    |  0.71 |
| Brian    |     0.53 |   0.17 |    0.48 |    0    |      0.73 |   0.63 |  0.45 |     0.46 |   0.49 |      0.6  |      0.51 |   0.67 |   0.6  |   0.52 |    0.5  |     0.56 |   0.4  |  0.8  |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |    0.5  |    0.73 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.64 |   0.6  |    0.62 |    0.63 |      0.5  |   0    |  0.5  |     0.56 |   0.54 |      0.4  |      0.45 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   1    | -1    |      -1    | -1    |
| Jai      |     0.44 |   0.6  |    0.54 |    0.45 |      0.71 |   0.5  |  0    |     0.52 |   0.41 |      0.65 |      0.57 |   0.81 |  -1    |   0.47 |    0.6  |    -1    |   0.6  |  0.71 |       0.2  | -1    |
| Jackie   |     0.42 |   0.67 |    0.53 |    0.46 |      0.83 |   0.56 |  0.52 |     0    |   0.46 |      0.53 |      0.57 |   0.56 |   0.57 |   0.42 |    0.38 |    -1    |   0.71 |  0.38 |      -1    |  0.6  |
| Kate     |     0.51 |   0.55 |    0.63 |    0.49 |      0.67 |   0.54 |  0.41 |     0.46 |   0    |      0.56 |      0.49 |   0.57 |   0.71 |   0.56 |    0.25 |     0.17 |   0.6  |  0.67 |       0.43 |  0.5  |
| Sushant  |     0.54 |   0.57 |    0.5  |    0.6  |     -1    |   0.4  |  0.65 |     0.53 |   0.56 |      0    |      0.52 |   0.52 |   0.5  |   0.56 |    0.73 |     0.83 |   0.5  |  0.47 |       0.5  |  0.62 |
| Abishek  |     0.64 |   0.44 |    0.55 |    0.51 |      0.8  |   0.45 |  0.57 |     0.57 |   0.49 |      0.52 |      0    |   0.56 |   0.54 |   0.55 |    0.87 |     0.62 |   0.33 |  0.47 |       0.71 |  0.38 |
| Ruhi     |     0.61 |  -1    |    0.55 |    0.67 |     -1    |   0.44 |  0.81 |     0.56 |   0.57 |      0.52 |      0.56 |   0    |   0.33 |   0.47 |    0.56 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.4  |   1    |    0.45 |    0.6  |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |    0.8  |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.44 |   0.8  |    0.56 |    0.52 |     -1    |   0.68 |  0.47 |     0.42 |   0.56 |      0.56 |      0.55 |   0.47 |  -1    |   0    |    0.33 |     0.33 |   0.8  |  0.56 |       0.6  |  0.5  |
| Jeron    |     0.28 |  -1    |    0.61 |    0.5  |      0.5  |   0.67 |  0.6  |     0.38 |   0.25 |      0.73 |      0.87 |   0.56 |   0.8  |   0.33 |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.25 |  -1    |    0.3  |    0.4  |     -1    |   1    |  0.6  |     0.71 |   0.6  |      0.5  |      0.33 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.38 |  -1    |    0.31 |    0.8  |     -1    |  -1    |  0.71 |     0.38 |   0.67 |      0.47 |      0.47 |   0.43 |  -1    |   0.56 |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|
| Rachel   |       96 |      4 |      32 |      38 |         4 |     12 |    27 |       35 |     35 |        30 |        26 |      9 |      9 |     27 |          1 |        1 |        0 |      13 |        0 |        4 |      6 |       0 |     8 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       32 |      1 |     115 |      53 |         3 |     12 |    23 |       37 |     30 |        39 |        39 |     10 |      6 |     29 |          1 |        1 |        0 |       7 |        0 |        7 |      7 |       0 |     9 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |
| Brian    |       38 |     10 |      53 |     135 |         3 |     16 |    28 |       43 |     50 |        36 |        52 |     12 |      8 |     33 |          1 |        1 |        0 |      11 |        0 |        4 |      6 |       0 |     3 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       12 |      2 |      12 |      16 |         3 |     49 |     7 |       16 |     18 |        18 |        22 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |
| Jai      |       27 |      2 |      23 |      28 |         2 |      7 |    60 |       19 |     30 |        14 |        17 |      3 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     2 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |       35 |      2 |      37 |      43 |         1 |     16 |    19 |       91 |     37 |        28 |        29 |      7 |      3 |     29 |          0 |        0 |        1 |      10 |        1 |        1 |      2 |       1 |     5 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       0 |
| Kate     |       35 |      5 |      30 |      50 |         3 |     18 |    30 |       37 |    111 |        32 |        45 |     13 |      4 |     28 |          0 |        0 |        0 |       9 |        0 |        5 |      4 |       1 |     6 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |
| Sushant  |       30 |      3 |      39 |      36 |         0 |     18 |    14 |       28 |     32 |        99 |        45 |     14 |      5 |     29 |          2 |        0 |        0 |       4 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Abishek  |       26 |      5 |      39 |      52 |         1 |     22 |    17 |       29 |     45 |        45 |       117 |     15 |      6 |     33 |          0 |        0 |        0 |       2 |        0 |        3 |      6 |       0 |    10 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |
| Ruhi     |        9 |      2 |      10 |      12 |         2 |      5 |     3 |        7 |     13 |        14 |        15 |     38 |      4 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        9 |      0 |       6 |       8 |         2 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     20 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       27 |      1 |      29 |      33 |         0 |      8 |    17 |       29 |     28 |        29 |        33 |      9 |      2 |     82 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       1 |     4 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |       13 |      0 |       7 |      11 |         3 |      2 |     4 |       10 |      9 |         4 |         2 |      4 |      1 |      4 |          0 |        0 |        1 |      25 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |       -1 |      2 |       4 |       4 |         2 |      4 |     5 |        4 |      6 |         7 |         4 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Peter    |        4 |      0 |      -1 |      15 |         2 |      5 |     8 |        4 |      5 |        13 |        14 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     4 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Brian    |        4 |      3 |      15 |      -1 |         3 |      5 |     5 |        7 |     11 |         7 |        15 |      1 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |        4 |      1 |       5 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jai      |        5 |      0 |       8 |       5 |         2 |      2 |    -1 |        1 |      8 |         4 |         5 |      2 |      0 |      5 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |        4 |      0 |       4 |       7 |         0 |      1 |     1 |       -1 |      4 |         5 |         5 |      1 |      2 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Kate     |        6 |      1 |       5 |      11 |         1 |      6 |     8 |        4 |     -1 |         9 |        11 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |
| Sushant  |        7 |      1 |      13 |       7 |         0 |      7 |     4 |        5 |      9 |        -1 |        17 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Abishek  |        4 |      1 |      14 |      15 |         0 |      5 |     5 |        5 |     11 |        17 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |        0 |      4 |      41 |      43 |         8 |     21 |    21 |       25 |     36 |        35 |        46 |     14 |      6 |     21 |          1 |        0 |        1 |       5 |        1 |        3 |      2 |       1 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       41 |      5 |       0 |      49 |         3 |     20 |    27 |       42 |     52 |        39 |        48 |     12 |      5 |     37 |          1 |        0 |        1 |      11 |        1 |        2 |      3 |       2 |     4 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       0 |
| Brian    |       43 |      2 |      49 |       0 |         8 |     27 |    23 |       37 |     49 |        53 |        54 |     24 |     12 |     36 |          1 |        0 |        1 |      11 |        1 |        5 |      4 |       2 |    12 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       0 |
| Anthony  |        8 |      0 |       3 |       8 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       21 |      3 |      20 |      27 |         3 |      0 |     7 |       20 |     21 |        12 |        18 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      5 |       0 |     3 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |
| Jai      |       21 |      3 |      27 |      23 |         5 |      7 |     0 |       21 |     21 |        26 |        23 |     13 |      1 |     15 |          1 |        0 |        0 |       6 |        0 |        2 |      3 |       0 |     5 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |
| Jackie   |       25 |      4 |      42 |      37 |         5 |     20 |    21 |        0 |     31 |        31 |        39 |      9 |      4 |     21 |          0 |        1 |        0 |       6 |        0 |        2 |      5 |       1 |     3 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |
| Kate     |       36 |      6 |      52 |      49 |         6 |     21 |    21 |       31 |      0 |        41 |        44 |     17 |     10 |     36 |          2 |        0 |        0 |       3 |        0 |        1 |      6 |       1 |    12 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |
| Sushant  |       35 |      4 |      39 |      53 |         1 |     12 |    26 |       31 |     41 |         0 |        48 |     15 |      5 |     37 |          0 |        0 |        0 |      11 |        0 |        5 |      5 |       0 |     9 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |
| Abishek  |       46 |      4 |      48 |      54 |         4 |     18 |    23 |       39 |     44 |        48 |         0 |     19 |      7 |     41 |          0 |        0 |        0 |      13 |        0 |        5 |      3 |       1 |     9 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |
| Ruhi     |       14 |      1 |      12 |      24 |         1 |      4 |    13 |        9 |     17 |        15 |        19 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        6 |      5 |       5 |      12 |         2 |      2 |     1 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       4 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       21 |      4 |      37 |      36 |         0 |     17 |    15 |       21 |     36 |        37 |        41 |      8 |      1 |      0 |          1 |        0 |        0 |       2 |        0 |        2 |      4 |       0 |     5 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        5 |      1 |      11 |      11 |         3 |      4 |     6 |        6 |      3 |        11 |        13 |      5 |      4 |      2 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| 3+1        | 0.346154 |            26 |
| 2+2        | 0.392157 |            51 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.32     |            25 |
| 2+2        | 0.340426 |            47 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.391304 |            23 |
| Success      | 0.347222 |            72 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.391304 |            23 |
| Success      | 0.328571 |            70 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      20 | 0.408163 |     0.35     |
|         1 |      20 | 0.408163 |     0.1      |
|         2 |       9 | 0.183673 |     0.444444 |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       7 | 0.636364 |     0.142857 |
|         1 |       4 | 0.363636 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |   % |   Good Win % |
|-----------|---------|-----|--------------|
|         0 |       8 | 0.4 |        0.5   |
|         1 |       8 | 0.4 |        0.125 |
|         2 |       4 | 0.2 |        0.25  |

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
|                   0 |            36 |     0.472222 |
|                   1 |            95 |     0.368421 |
|                   2 |            14 |     0.571429 |
|                   3 |             5 |     0.4      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            34 |     0.441176 |
|                   1 |            89 |     0.325843 |
|                   2 |            14 |     0.571429 |
|                   3 |             5 |     0.4      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.12667 |           150 |              19 |
| Assassin      |                 0.05263 |           133 |               7 |
| Morgana       |                 0.06667 |           150 |              10 |
| Mordred       |                 0.01042 |            96 |               1 |
| Loyal Servant |                 0       |           440 |               0 |
| Oberon        |                 0.02381 |            42 |               1 |
| Minion #1     |                 0.04762 |            21 |               1 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Alex     |                    0.4      |                  8 |            20 |
| Abishek  |                    0.346154 |                  9 |            26 |
| Jai      |                    0.333333 |                  3 |             9 |
| Minh     |                    0.285714 |                  2 |             7 |
| Jackie   |                    0.272727 |                  6 |            22 |
| Kate     |                    0.269231 |                  7 |            26 |
| Rachel   |                    0.263158 |                  5 |            19 |
| Brian    |                    0.2      |                  6 |            30 |
| Sushant  |                    0.2      |                  3 |            15 |
| Ruhi     |                    0.2      |                  1 |             5 |
| Peter    |                    0.176471 |                  3 |            17 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Minh     |          0        |                  0 |             3 |
| Sushant  |          0.125    |                  1 |             8 |
| Jeron    |          0.25     |                  1 |             4 |
| Brian    |          0.3      |                  3 |            10 |
| Kate     |          0.4      |                  4 |            10 |
| Abishek  |          0.461538 |                  6 |            13 |
| Jackie   |          0.461538 |                  6 |            13 |
| Alex     |          0.5      |                  3 |             6 |
| Peter    |          0.529412 |                  9 |            17 |
| Rachel   |          0.636364 |                  7 |            11 |
| Kish     |          0.666667 |                  2 |             3 |
| Jai      |          0.714286 |                  5 |             7 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

| # Players   |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
| 10          |          0.411765 |                  7 |            17 |
| 5           |          0.666667 |                  4 |             6 |
| 5O          |          0.666667 |                  2 |             3 |
| 6           |          0.333333 |                  4 |            12 |
| 6M          |          0.25     |                  1 |             4 |
| 6O          |          0.4      |                  2 |             5 |
| 7           |          0.5      |                 10 |            20 |
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
| 5           |                   1 |          1        |                  2 |             2 |
| 5O          |                   0 |          0.5      |                  1 |             2 |
| 5O          |                   1 |          1        |                  1 |             1 |
| 6           |                   0 |          0.5      |                  2 |             4 |
| 6           |                   1 |          0.285714 |                  2 |             7 |
| 6           |                   3 |          0        |                  0 |             1 |
| 6M          |                   0 |          0.333333 |                  1 |             3 |
| 6M          |                   1 |          0        |                  0 |             1 |
| 6O          |                   0 |          0.4      |                  2 |             5 |
| 7           |                   0 |          0.5      |                  4 |             8 |
| 7           |                   1 |          0.6      |                  6 |            10 |
| 7           |                   2 |          0        |                  0 |             1 |
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
