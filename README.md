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

Cheesy wins included: 0.4378 (n = 185)

Cheesy wins excluded: 0.4091 (n = 176)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            26 |     0.423077 |
| 5           |             8 |     0.25     |
| 5O          |             7 |     0.571429 |
| 6           |            17 |     0.588235 |
| 6M          |             8 |     0.75     |
| 6O          |            10 |     0.7      |
| 7           |            29 |     0.413793 |
| 7O          |             5 |     0.4      |
| 8           |            30 |     0.333333 |
| 8O          |             3 |     0        |
| 9           |            37 |     0.378378 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

Cheesy wins excluded:

| # Players   |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
| 10          |            25 |     0.4      |
| 5           |             8 |     0.25     |
| 5O          |             7 |     0.571429 |
| 6           |            16 |     0.5625   |
| 6M          |             8 |     0.75     |
| 6O          |            10 |     0.7      |
| 7           |            26 |     0.346154 |
| 7O          |             5 |     0.4      |
| 8           |            30 |     0.333333 |
| 8O          |             3 |     0        |
| 9           |            33 |     0.30303  |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            89 |       28.7865 |     20.0513 |
| Good     |            69 |       20.5797 |     16.5302 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            89 |       28.7865 |     20.0513 |
| Good     |            64 |       21.5625 |     16.7681 |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|----------|-------------|
| Kate     |           6 |
| Abishek  |           4 |
| Peter    |           4 |
| Brian    |           2 |
| Rachel   |           2 |
| Minh     |           1 |
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
| Brian    |            169 |
| Peter    |            149 |
| Abishek  |            143 |
| Kate     |            136 |
| Jackie   |            126 |
| Sushant  |            122 |
| Rachel   |            115 |
| Alex     |             89 |
| Jai      |             69 |
| Minh     |             54 |
| Ruhi     |             38 |
| Jeron    |             29 |
| Jay      |             26 |
| Kish     |             20 |
| Jade     |             18 |
| Ewen     |             13 |
| Anthony  |             12 |
| Justin   |              9 |
| Sai      |              8 |
| Gathenji |              7 |
| Tercel   |              6 |
| Sofia    |              5 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|----------|----------|----------|---------|
| Gathenji | 0.857143 |        6 |       1 |
| Jade     | 0.777778 |       14 |       4 |
| Rachel   | 0.713043 |       82 |      33 |
| Jackie   | 0.68254  |       86 |      40 |
| Kate     | 0.676471 |       92 |      44 |
| Brian    | 0.668639 |      113 |      56 |
| Justin   | 0.666667 |        6 |       3 |
| Jeron    | 0.655172 |       19 |      10 |
| Alex     | 0.651685 |       58 |      31 |
| Sai      | 0.625    |        5 |       3 |
| Jay      | 0.615385 |       16 |      10 |
| Ewen     | 0.615385 |        8 |       5 |
| Jai      | 0.608696 |       42 |      27 |
| Peter    | 0.604027 |       90 |      59 |
| Kish     | 0.6      |       12 |       8 |
| Sushant  | 0.57377  |       70 |      52 |
| Abishek  | 0.566434 |       81 |      62 |
| Minh     | 0.555556 |       30 |      24 |
| Ruhi     | 0.5      |       19 |      19 |
| Tercel   | 0.5      |        3 |       3 |
| Sofia    | 0.4      |        2 |       3 |
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
| No                 |           171 |     0.461988 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           171 |     0.461988 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       16 |         21 |         19 |        18 |         6 |       10 |           9 |              44 |           143 |
| Alex     |       11 |         13 |         13 |        11 |         4 |        2 |           1 |              34 |            89 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       19 |         32 |         16 |        27 |        12 |        0 |           1 |              62 |           169 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       21 |         17 |          6 |        18 |         7 |        7 |           2 |              48 |           126 |
| Jade     |        5 |          3 |          1 |         1 |         1 |        1 |           0 |               6 |            18 |
| Jai      |       10 |          6 |          7 |         9 |         7 |        3 |           1 |              26 |            69 |
| Jay      |        4 |          3 |          4 |         0 |         5 |        1 |           0 |               9 |            26 |
| Jeron    |        5 |          8 |          1 |         5 |         2 |        1 |           1 |               6 |            29 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       14 |         14 |          8 |        13 |        10 |       11 |           2 |              64 |           136 |
| Kish     |        3 |          3 |          1 |         4 |         2 |        0 |           1 |               6 |            20 |
| Minh     |        7 |          6 |         10 |         5 |         5 |        2 |           2 |              17 |            54 |
| Peter    |       24 |         18 |         21 |        19 |        10 |        6 |           3 |              48 |           149 |
| Rachel   |       16 |         15 |         10 |        11 |         9 |        0 |           3 |              51 |           115 |
| Ruhi     |        1 |          5 |          5 |         7 |         6 |        1 |           0 |              13 |            38 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sofia    |        0 |          1 |          1 |         2 |         0 |        0 |           0 |               1 |             5 |
| Sushant  |       21 |          9 |         17 |        20 |         9 |        4 |           2 |              40 |           122 |
| Tercel   |        0 |          1 |          1 |         0 |         2 |        0 |           0 |               2 |             6 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.088 |      0.115 |      0.126 |     0.1   |     0.059 |    0.185 |       0.321 |           0.086 |           143 |
| Alex     |    0.06  |      0.071 |      0.086 |     0.061 |     0.039 |    0.037 |       0.036 |           0.067 |            89 |
| Anthony  |    0     |      0.011 |      0.026 |     0.022 |     0     |    0.019 |       0     |           0.002 |            12 |
| Brian    |    0.104 |      0.175 |      0.106 |     0.15  |     0.118 |    0     |       0.036 |           0.122 |           169 |
| Ewen     |    0.005 |      0.011 |      0.013 |     0.006 |     0     |    0.037 |       0     |           0.01  |            13 |
| Gathenji |    0     |      0     |      0     |     0.006 |     0     |    0     |       0     |           0.012 |             7 |
| Jackie   |    0.115 |      0.093 |      0.04  |     0.1   |     0.069 |    0.13  |       0.071 |           0.094 |           126 |
| Jade     |    0.027 |      0.016 |      0.007 |     0.006 |     0.01  |    0.019 |       0     |           0.012 |            18 |
| Jai      |    0.055 |      0.033 |      0.046 |     0.05  |     0.069 |    0.056 |       0.036 |           0.051 |            69 |
| Jay      |    0.022 |      0.016 |      0.026 |     0     |     0.049 |    0.019 |       0     |           0.018 |            26 |
| Jeron    |    0.027 |      0.044 |      0.007 |     0.028 |     0.02  |    0.019 |       0.036 |           0.012 |            29 |
| Justin   |    0.011 |      0     |      0.007 |     0.006 |     0.01  |    0     |       0     |           0.008 |             9 |
| Kate     |    0.077 |      0.077 |      0.053 |     0.072 |     0.098 |    0.204 |       0.071 |           0.126 |           136 |
| Kish     |    0.016 |      0.016 |      0.007 |     0.022 |     0.02  |    0     |       0.036 |           0.012 |            20 |
| Minh     |    0.038 |      0.033 |      0.066 |     0.028 |     0.049 |    0.037 |       0.071 |           0.033 |            54 |
| Peter    |    0.132 |      0.098 |      0.139 |     0.106 |     0.098 |    0.111 |       0.107 |           0.094 |           149 |
| Rachel   |    0.088 |      0.082 |      0.066 |     0.061 |     0.088 |    0     |       0.107 |           0.1   |           115 |
| Ruhi     |    0.005 |      0.027 |      0.033 |     0.039 |     0.059 |    0.019 |       0     |           0.026 |            38 |
| Sai      |    0.005 |      0.005 |      0     |     0.006 |     0.02  |    0     |       0     |           0.006 |             8 |
| Sofia    |    0     |      0.005 |      0.007 |     0.011 |     0     |    0     |       0     |           0.002 |             5 |
| Sushant  |    0.115 |      0.049 |      0.113 |     0.111 |     0.088 |    0.074 |       0.071 |           0.079 |           122 |
| Tercel   |    0     |      0.005 |      0.007 |     0     |     0.02  |    0     |       0     |           0.004 |             6 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.112 |      0.147 |      0.133 |     0.126 |     0.042 |    0.07  |       0.063 |           0.308 |           143 |
| Alex     |    0.124 |      0.146 |      0.146 |     0.124 |     0.045 |    0.022 |       0.011 |           0.382 |            89 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.112 |      0.189 |      0.095 |     0.16  |     0.071 |    0     |       0.006 |           0.367 |           169 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.167 |      0.135 |      0.048 |     0.143 |     0.056 |    0.056 |       0.016 |           0.381 |           126 |
| Jade     |    0.278 |      0.167 |      0.056 |     0.056 |     0.056 |    0.056 |       0     |           0.333 |            18 |
| Jai      |    0.145 |      0.087 |      0.101 |     0.13  |     0.101 |    0.043 |       0.014 |           0.377 |            69 |
| Jay      |    0.154 |      0.115 |      0.154 |     0     |     0.192 |    0.038 |       0     |           0.346 |            26 |
| Jeron    |    0.172 |      0.276 |      0.034 |     0.172 |     0.069 |    0.034 |       0.034 |           0.207 |            29 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.103 |      0.103 |      0.059 |     0.096 |     0.074 |    0.081 |       0.015 |           0.471 |           136 |
| Kish     |    0.15  |      0.15  |      0.05  |     0.2   |     0.1   |    0     |       0.05  |           0.3   |            20 |
| Minh     |    0.13  |      0.111 |      0.185 |     0.093 |     0.093 |    0.037 |       0.037 |           0.315 |            54 |
| Peter    |    0.161 |      0.121 |      0.141 |     0.128 |     0.067 |    0.04  |       0.02  |           0.322 |           149 |
| Rachel   |    0.139 |      0.13  |      0.087 |     0.096 |     0.078 |    0     |       0.026 |           0.443 |           115 |
| Ruhi     |    0.026 |      0.132 |      0.132 |     0.184 |     0.158 |    0.026 |       0     |           0.342 |            38 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sofia    |    0     |      0.2   |      0.2   |     0.4   |     0     |    0     |       0     |           0.2   |             5 |
| Sushant  |    0.172 |      0.074 |      0.139 |     0.164 |     0.074 |    0.033 |       0.016 |           0.328 |           122 |
| Tercel   |    0     |      0.167 |      0.167 |     0     |     0.333 |    0     |       0     |           0.333 |             6 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|---------|-------|------------|-------|----------|
| Rachel   |     1    |   0.5  |    0.48 |    0.45 |      0.33 |   0.38 |  0.53 |     0.57 |   0.49 |      0.48 |      0.34 |   0.39 |   0.6  |   0.56 |    0.75 |     0.57 |   0.69 |    -1   |  0.72 |       0.86 | -1    |     0.4  |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Peter    |     0.48 |   0.17 |    1    |    0.52 |      0.43 |   0.43 |  0.48 |     0.44 |   0.38 |      0.49 |      0.44 |   0.48 |   0.55 |   0.46 |    0.43 |     0.78 |   0.53 |    -1   |  0.65 |      -1    |  0.29 |     0.4  |
| Brian    |     0.45 |   0.83 |    0.52 |    1    |      0.25 |   0.42 |  0.56 |     0.46 |   0.54 |      0.43 |      0.5  |   0.32 |   0.4  |   0.49 |    0.48 |     0.44 |   0.6  |     0.2 |  0.3  |       0.5  |  0.62 |    -1    |
| Anthony  |     0.33 |  -1    |    0.43 |    0.25 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Minh     |     0.38 |   0.4  |    0.43 |    0.42 |      0.5  |   1    |  0.53 |     0.39 |   0.48 |      0.6  |      0.53 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0.14 |    -1   |  0.33 |      -1    | -1    |    -1    |
| Jai      |     0.53 |   0.4  |    0.48 |    0.56 |      0.29 |   0.53 |  1    |     0.47 |   0.59 |      0.36 |      0.4  |   0.19 |  -1    |   0.53 |    0.4  |    -1    |   0.33 |    -1   |  0.23 |       0.8  | -1    |    -1    |
| Jackie   |     0.57 |   0.33 |    0.44 |    0.46 |      0.17 |   0.39 |  0.47 |     1    |   0.55 |      0.44 |      0.43 |   0.44 |   0.43 |   0.56 |    0.6  |    -1    |   0.5  |     0.6 |  0.6  |      -1    |  0.4  |     0.33 |
| Kate     |     0.49 |   0.45 |    0.38 |    0.54 |      0.33 |   0.48 |  0.59 |     0.55 |   1    |      0.41 |      0.52 |   0.43 |   0.29 |   0.45 |    0.75 |     0.83 |   0.42 |    -1   |  0.4  |       0.57 |  0.5  |    -1    |
| Sushant  |     0.48 |   0.43 |    0.49 |    0.43 |     -1    |   0.6  |  0.36 |     0.44 |   0.41 |      1    |      0.48 |   0.48 |   0.5  |   0.44 |    0.29 |     0.17 |   0.5  |    -1   |  0.45 |       0.5  |  0.38 |    -1    |
| Abishek  |     0.34 |   0.56 |    0.44 |    0.5  |      0.2  |   0.53 |  0.4  |     0.43 |   0.52 |      0.48 |      1    |   0.44 |   0.46 |   0.43 |    0.18 |     0.38 |   0.5  |    -1   |  0.46 |       0.29 |  0.62 |    -1    |
| Ruhi     |     0.39 |  -1    |    0.48 |    0.32 |     -1    |   0.56 |  0.19 |     0.44 |   0.43 |      0.48 |      0.44 |   1    |   0.67 |   0.53 |    0.44 |    -1    |  -1    |    -1   |  0.57 |      -1    | -1    |    -1    |
| Kish     |     0.6  |   0    |    0.55 |    0.4  |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |    0.2  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Alex     |     0.56 |   0.2  |    0.46 |    0.49 |     -1    |   0.32 |  0.53 |     0.56 |   0.45 |      0.44 |      0.43 |   0.53 |  -1    |   1    |    0.44 |     0.67 |   0.2  |    -1   |  0.45 |       0.4  |  0.5  |    -1    |
| Jeron    |     0.75 |  -1    |    0.43 |    0.48 |      0.5  |   0.33 |  0.4  |     0.6  |   0.75 |      0.29 |      0.18 |   0.44 |   0.2  |   0.44 |    1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Jade     |     0.69 |  -1    |    0.53 |    0.6  |     -1    |   0.14 |  0.33 |     0.5  |   0.42 |      0.5  |      0.5  |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    |    -1   | -1    |      -1    | -1    |    -1    |
| Sofia    |    -1    |  -1    |   -1    |    0.2  |     -1    |  -1    | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |     1   | -1    |      -1    | -1    |    -1    |
| Jay      |     0.72 |  -1    |    0.65 |    0.3  |     -1    |   0.33 |  0.23 |     0.6  |   0.4  |      0.45 |      0.46 |   0.57 |  -1    |   0.45 |   -1    |    -1    |  -1    |    -1   |  1    |      -1    | -1    |    -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    |    -1   | -1    |       1    | -1    |    -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    |  1    |    -1    |
| Tercel   |     0.4  |  -1    |    0.4  |   -1    |     -1    |  -1    | -1    |     0.33 |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|---------|-------|------------|-------|----------|
| Rachel   |    -1    |   0.25 |    0.08 |    0.04 |      0.17 |   0.11 |  0.11 |     0.1  |   0.07 |      0.09 |      0.07 |   0.09 |   0.13 |   0.12 |    0.05 |     0    |   0.15 |    -1   |  0.11 |       0.14 | -1    |     0    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Peter    |     0.08 |   0    |   -1    |    0.13 |      0.29 |   0.16 |  0.17 |     0.07 |   0.05 |      0.15 |      0.16 |   0.17 |   0    |   0.07 |    0.1  |     0.11 |   0.13 |    -1   |  0.25 |      -1    |  0    |     0    |
| Brian    |     0.04 |   0.25 |    0.13 |   -1    |      0.25 |   0.1  |  0.08 |     0.07 |   0.1  |      0.08 |      0.15 |   0.03 |   0.15 |   0.08 |    0.07 |     0    |   0    |     0.2 |  0.05 |       0    |  0.12 |    -1    |
| Anthony  |     0.17 |  -1    |    0.29 |    0.25 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Minh     |     0.11 |   0.2  |    0.16 |    0.1  |      0.33 |  -1    |  0.12 |     0.02 |   0.14 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    |    -1   |  0.17 |      -1    | -1    |    -1    |
| Jai      |     0.11 |   0    |    0.17 |    0.08 |      0.29 |   0.12 | -1    |     0.06 |   0.14 |      0.12 |      0.13 |   0.12 |  -1    |   0.15 |    0.1  |    -1    |   0    |    -1   |  0.08 |       0    | -1    |    -1    |
| Jackie   |     0.1  |   0    |    0.07 |    0.07 |      0    |   0.02 |  0.06 |    -1    |   0.09 |      0.09 |      0.1  |   0.06 |   0.29 |   0.11 |    0.15 |    -1    |   0.08 |     0.2 |  0.13 |      -1    |  0.2  |     0.17 |
| Kate     |     0.07 |   0.09 |    0.05 |    0.1  |      0.11 |   0.14 |  0.14 |     0.09 |  -1    |      0.1  |      0.13 |   0.1  |   0    |   0.09 |    0.17 |     0.33 |   0.08 |    -1   |  0.04 |       0    |  0.12 |    -1    |
| Sushant  |     0.09 |   0.14 |    0.15 |    0.08 |     -1    |   0.23 |  0.12 |     0.09 |   0.1  |     -1    |      0.18 |   0.21 |   0    |   0.1  |    0    |     0    |   0.1  |    -1   |  0.14 |       0    |  0.12 |    -1    |
| Abishek  |     0.07 |   0.11 |    0.16 |    0.15 |      0    |   0.12 |  0.13 |     0.1  |   0.13 |      0.18 |     -1    |   0.18 |   0.15 |   0.11 |    0    |     0.25 |   0    |    -1   |  0.08 |       0    |  0.12 |    -1    |
| Ruhi     |     0.09 |  -1    |    0.17 |    0.03 |     -1    |   0.22 |  0.12 |     0.06 |   0.1  |      0.21 |      0.18 |  -1    |   0.17 |   0.35 |    0.11 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |
| Kish     |     0.13 |   0    |    0    |    0.15 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |    0.2  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Alex     |     0.12 |   0    |    0.07 |    0.08 |     -1    |   0.08 |  0.15 |     0.11 |   0.09 |      0.1  |      0.11 |   0.35 |  -1    |  -1    |    0.11 |     0    |   0    |    -1   |  0.09 |       0    |  0.17 |    -1    |
| Jeron    |     0.05 |  -1    |    0.1  |    0.07 |      0.33 |   0.17 |  0.1  |     0.15 |   0.17 |      0    |      0    |   0.11 |   0.2  |   0.11 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Jade     |     0.15 |  -1    |    0.13 |    0    |     -1    |   0    |  0    |     0.08 |   0.08 |      0.1  |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Sofia    |    -1    |  -1    |   -1    |    0.2  |     -1    |  -1    | -1    |     0.2  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Jay      |     0.11 |  -1    |    0.25 |    0.05 |     -1    |   0.17 |  0.08 |     0.13 |   0.04 |      0.14 |      0.08 |   0.43 |  -1    |   0.09 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Tercel   |     0    |  -1    |    0    |   -1    |     -1    |  -1    | -1    |     0.17 |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|---------|-------|------------|-------|----------|
| Rachel   |     0    |   0.5  |    0.52 |    0.55 |      0.67 |   0.62 |  0.47 |     0.43 |   0.51 |      0.52 |      0.66 |   0.61 |   0.4  |   0.44 |    0.25 |     0.43 |   0.31 |    -1   |  0.28 |       0.14 | -1    |     0.6  |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Peter    |     0.52 |   0.83 |    0    |    0.48 |      0.57 |   0.57 |  0.52 |     0.56 |   0.62 |      0.51 |      0.56 |   0.52 |   0.45 |   0.54 |    0.57 |     0.22 |   0.47 |    -1   |  0.35 |      -1    |  0.71 |     0.6  |
| Brian    |     0.55 |   0.17 |    0.48 |    0    |      0.75 |   0.58 |  0.44 |     0.54 |   0.46 |      0.57 |      0.5  |   0.68 |   0.6  |   0.51 |    0.52 |     0.56 |   0.4  |     0.8 |  0.7  |       0.5  |  0.38 |    -1    |
| Anthony  |     0.67 |  -1    |    0.57 |    0.75 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Minh     |     0.62 |   0.6  |    0.57 |    0.58 |      0.5  |   0    |  0.47 |     0.61 |   0.52 |      0.4  |      0.47 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   0.86 |    -1   |  0.67 |      -1    | -1    |    -1    |
| Jai      |     0.47 |   0.6  |    0.52 |    0.44 |      0.71 |   0.47 |  0    |     0.53 |   0.41 |      0.64 |      0.6  |   0.81 |  -1    |   0.47 |    0.6  |    -1    |   0.67 |    -1   |  0.77 |       0.2  | -1    |    -1    |
| Jackie   |     0.43 |   0.67 |    0.56 |    0.54 |      0.83 |   0.61 |  0.53 |     0    |   0.45 |      0.56 |      0.57 |   0.56 |   0.57 |   0.44 |    0.4  |    -1    |   0.5  |     0.4 |  0.4  |      -1    |  0.6  |     0.67 |
| Kate     |     0.51 |   0.55 |    0.62 |    0.46 |      0.67 |   0.52 |  0.41 |     0.45 |   0    |      0.59 |      0.48 |   0.57 |   0.71 |   0.55 |    0.25 |     0.17 |   0.58 |    -1   |  0.6  |       0.43 |  0.5  |    -1    |
| Sushant  |     0.52 |   0.57 |    0.51 |    0.57 |     -1    |   0.4  |  0.64 |     0.56 |   0.59 |      0    |      0.52 |   0.52 |   0.5  |   0.56 |    0.71 |     0.83 |   0.5  |    -1   |  0.55 |       0.5  |  0.62 |    -1    |
| Abishek  |     0.66 |   0.44 |    0.56 |    0.5  |      0.8  |   0.47 |  0.6  |     0.57 |   0.48 |      0.52 |      0    |   0.56 |   0.54 |   0.57 |    0.82 |     0.62 |   0.5  |    -1   |  0.54 |       0.71 |  0.38 |    -1    |
| Ruhi     |     0.61 |  -1    |    0.52 |    0.68 |     -1    |   0.44 |  0.81 |     0.56 |   0.57 |      0.52 |      0.56 |   0    |   0.33 |   0.47 |    0.56 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |
| Kish     |     0.4  |   1    |    0.45 |    0.6  |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |    0.8  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Alex     |     0.44 |   0.8  |    0.54 |    0.51 |     -1    |   0.68 |  0.47 |     0.44 |   0.55 |      0.56 |      0.57 |   0.47 |  -1    |   0    |    0.56 |     0.33 |   0.8  |    -1   |  0.55 |       0.6  |  0.5  |    -1    |
| Jeron    |     0.25 |  -1    |    0.57 |    0.52 |      0.5  |   0.67 |  0.6  |     0.4  |   0.25 |      0.71 |      0.82 |   0.56 |   0.8  |   0.56 |    0    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |
| Jade     |     0.31 |  -1    |    0.47 |    0.4  |     -1    |   0.86 |  0.67 |     0.5  |   0.58 |      0.5  |      0.5  |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    |    -1   | -1    |      -1    | -1    |    -1    |
| Sofia    |    -1    |  -1    |   -1    |    0.8  |     -1    |  -1    | -1    |     0.4  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |     0   | -1    |      -1    | -1    |    -1    |
| Jay      |     0.28 |  -1    |    0.35 |    0.7  |     -1    |   0.67 |  0.77 |     0.4  |   0.6  |      0.55 |      0.54 |   0.43 |  -1    |   0.55 |   -1    |    -1    |  -1    |    -1   |  0    |      -1    | -1    |    -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    |    -1   | -1    |       0    | -1    |    -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    |  0    |    -1    |
| Tercel   |     0.6  |  -1    |    0.6  |   -1    |     -1    |  -1    | -1    |     0.67 |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|----------|
| Rachel   |      115 |      4 |      44 |      45 |         4 |     14 |    30 |       45 |     40 |        36 |        30 |      9 |      9 |     29 |          1 |        1 |        0 |      15 |        0 |        4 |      9 |       1 |    13 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |        2 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |
| Peter    |       44 |      1 |     149 |      70 |         3 |     16 |    29 |       50 |     41 |        49 |        49 |     11 |      6 |     33 |          1 |        1 |        0 |       9 |        0 |        7 |      8 |       0 |    13 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |        2 |
| Brian    |       45 |     10 |      70 |     169 |         3 |     20 |    33 |       53 |     66 |        47 |        65 |     12 |      8 |     37 |          1 |        1 |        0 |      13 |        0 |        4 |      9 |       1 |     6 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |        2 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Minh     |       14 |      2 |      16 |      20 |         3 |     54 |     9 |       16 |     21 |        18 |        23 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      1 |       2 |     2 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |        0 |
| Jai      |       30 |      2 |      29 |      33 |         2 |      9 |    69 |       23 |     34 |        15 |        19 |      3 |      2 |     18 |          0 |        0 |        0 |       4 |        0 |        0 |      3 |       0 |     3 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |
| Jackie   |       45 |      2 |      50 |      53 |         1 |     16 |    23 |      126 |     51 |        36 |        40 |      7 |      3 |     32 |          0 |        0 |        1 |      12 |        1 |        1 |      6 |       3 |     9 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       0 |        2 |
| Kate     |       40 |      5 |      41 |      66 |         3 |     21 |    34 |       51 |    136 |        38 |        57 |     13 |      4 |     30 |          0 |        0 |        0 |       9 |        0 |        5 |      5 |       1 |    10 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |        1 |
| Sushant  |       36 |      3 |      49 |      47 |         0 |     18 |    15 |       36 |     38 |       122 |        54 |     14 |      5 |     30 |          2 |        0 |        0 |       5 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        4 |
| Abishek  |       30 |      5 |      49 |      65 |         1 |     23 |    19 |       40 |     57 |        54 |       143 |     15 |      6 |     33 |          0 |        0 |        0 |       3 |        0 |        3 |      7 |       1 |    11 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |        2 |
| Ruhi     |        9 |      2 |      11 |      12 |         2 |      5 |     3 |        7 |     13 |        14 |        15 |     38 |      4 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Kish     |        9 |      0 |       6 |       8 |         2 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     20 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |        0 |
| Alex     |       29 |      1 |      33 |      37 |         0 |      8 |    18 |       32 |     30 |        30 |        33 |      9 |      2 |     89 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       2 |     5 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        2 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jeron    |       15 |      0 |       9 |      13 |         3 |      2 |     4 |       12 |      9 |         5 |         3 |      4 |      1 |      4 |          0 |        0 |        1 |      29 |        1 |        0 |      0 |       1 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |       0 |        0 |
| Jade     |        9 |      2 |       8 |       9 |         0 |      1 |     3 |        6 |      5 |         5 |         7 |      2 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |     18 |       0 |     3 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sofia    |        1 |      0 |       0 |       1 |         0 |      2 |     0 |        3 |      1 |         1 |         1 |      0 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       5 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jay      |       13 |      1 |      13 |       6 |         0 |      2 |     3 |        9 |     10 |        10 |        11 |      4 |      1 |      5 |          0 |        0 |        0 |       2 |        0 |        0 |      3 |       0 |    26 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Derek    |        1 |      0 |       2 |       3 |         0 |      0 |     0 |        1 |      1 |         3 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       4 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Gathenji |        6 |      0 |       1 |       3 |         0 |      0 |     4 |        2 |      4 |         3 |         2 |      2 |      1 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          7 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      2 |         1 |         1 |      2 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      3 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sai      |        2 |      1 |       2 |       5 |         0 |      2 |     2 |        2 |      4 |         3 |         5 |      0 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     8 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Nabeel   |        0 |      1 |       2 |       1 |         0 |      0 |     0 |        2 |      3 |         0 |         2 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        4 |        0 |      0 |     0 |       0 |       0 |        0 |
| Ronnie   |        1 |      0 |       2 |       0 |         0 |      1 |     0 |        2 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        2 |      0 |     0 |       0 |       0 |        0 |
| Neha     |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |
| Kawin    |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |
| Abrar    |        1 |      0 |       1 |       0 |         0 |      0 |     0 |        0 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |
| Tercel   |        2 |      0 |       2 |       2 |         0 |      0 |     3 |        2 |      1 |         4 |         2 |      0 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        6 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|----------|
| Rachel   |       -1 |      2 |       7 |       4 |         2 |      4 |     6 |        8 |      6 |         7 |         6 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      2 |       0 |     2 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Peter    |        7 |      0 |      -1 |      17 |         2 |      6 |    10 |        8 |      5 |        15 |        18 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     5 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |
| Brian    |        4 |      3 |      17 |      -1 |         3 |      5 |     5 |        8 |     12 |         9 |        19 |      1 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Minh     |        4 |      1 |       6 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jai      |        6 |      0 |      10 |       5 |         2 |      2 |    -1 |        3 |      8 |         5 |         6 |      2 |      0 |      5 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |
| Jackie   |        8 |      0 |       8 |       8 |         0 |      1 |     3 |       -1 |      8 |         7 |         9 |      1 |      2 |      6 |          0 |        0 |        1 |       3 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |
| Kate     |        6 |      1 |       5 |      12 |         1 |      6 |     8 |        8 |     -1 |         9 |        14 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |        0 |
| Sushant  |        7 |      1 |      15 |       9 |         0 |      7 |     5 |        7 |      9 |        -1 |        20 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |
| Abishek  |        6 |      1 |      18 |      19 |         0 |      5 |     6 |        9 |     14 |        20 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       1 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |
| Ruhi     |        2 |      1 |       4 |       1 |         1 |      2 |     2 |        1 |      3 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Kish     |        2 |      0 |       0 |       3 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     5 |        6 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jeron    |        1 |      0 |       2 |       2 |         2 |      1 |     1 |        3 |      2 |         0 |         0 |      1 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jade     |        2 |      0 |       2 |       0 |         0 |      0 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sofia    |        0 |      0 |       0 |       1 |         0 |      1 |     0 |        1 |      0 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |      -1 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jay      |        2 |      0 |       5 |       1 |         0 |      1 |     1 |        2 |      1 |         3 |         2 |      3 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |    -1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Greg     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |     -1 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Gathenji |        1 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |         -1 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        1 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |     -1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sai      |        1 |      0 |       0 |       1 |         0 |      0 |     1 |        1 |      1 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |    -1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Nabeel   |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |       -1 |        0 |      0 |     0 |       0 |       0 |        0 |
| Ronnie   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |       -1 |      0 |     0 |       0 |       0 |        0 |
| Neha     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |     -1 |     0 |       0 |       0 |        0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |    -1 |       0 |       0 |        0 |
| Kawin    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |      -1 |       0 |        0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |      -1 |        0 |
| Tercel   |        0 |      0 |       0 |       0 |         0 |      0 |     2 |        1 |      0 |         2 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       -1 |

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|----------|
| Rachel   |        0 |      4 |      47 |      54 |         8 |     23 |    27 |       34 |     42 |        39 |        58 |     14 |      6 |     23 |          1 |        0 |        1 |       5 |        1 |        3 |      4 |       3 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |        3 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |        0 |
| Peter    |       47 |      5 |       0 |      65 |         4 |     21 |    31 |       63 |     67 |        50 |        62 |     12 |      5 |     39 |          1 |        0 |        1 |      12 |        1 |        2 |      7 |       3 |     7 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       0 |        3 |
| Brian    |       54 |      2 |      65 |       0 |         9 |     28 |    26 |       61 |     57 |        63 |        65 |     25 |     12 |     39 |          1 |        0 |        1 |      14 |        1 |        5 |      6 |       4 |    14 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       0 |        2 |
| Anthony  |        8 |      0 |       4 |       9 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Minh     |       23 |      3 |      21 |      28 |         3 |      0 |     8 |       25 |     23 |        12 |        20 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      6 |       0 |     4 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |        0 |
| Jai      |       27 |      3 |      31 |      26 |         5 |      8 |     0 |       26 |     24 |        27 |        28 |     13 |      1 |     16 |          1 |        0 |        0 |       6 |        0 |        2 |      6 |       0 |    10 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |        1 |
| Jackie   |       34 |      4 |      63 |      61 |         5 |     25 |    26 |        0 |     42 |        46 |        54 |      9 |      4 |     25 |          0 |        1 |        0 |       8 |        0 |        2 |      6 |       2 |     6 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |        4 |
| Kate     |       42 |      6 |      67 |      57 |         6 |     23 |    24 |       42 |      0 |        54 |        52 |     17 |     10 |     36 |          2 |        0 |        0 |       3 |        0 |        1 |      7 |       1 |    15 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |        3 |
| Sushant  |       39 |      4 |      50 |      63 |         1 |     12 |    27 |       46 |     54 |         0 |        59 |     15 |      5 |     38 |          0 |        0 |        0 |      12 |        0 |        5 |      5 |       3 |    12 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |        0 |
| Abishek  |       58 |      4 |      62 |      65 |         4 |     20 |    28 |       54 |     52 |        59 |         0 |     19 |      7 |     43 |          0 |        0 |        0 |      14 |        0 |        5 |      7 |       3 |    13 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |        2 |
| Ruhi     |       14 |      1 |      12 |      25 |         1 |      4 |    13 |        9 |     17 |        15 |        19 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Kish     |        6 |      5 |       5 |      12 |         2 |      2 |     1 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       4 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |
| Alex     |       23 |      4 |      39 |      39 |         0 |     17 |    16 |       25 |     36 |        38 |        43 |      8 |      1 |      0 |          1 |        0 |        0 |       5 |        0 |        2 |      4 |       1 |     6 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |        2 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jeron    |        5 |      1 |      12 |      14 |         3 |      4 |     6 |        8 |      3 |        12 |        14 |      5 |      4 |      5 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       1 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Jade     |        4 |      0 |       7 |       6 |         0 |      6 |     6 |        6 |      7 |         5 |         7 |      2 |      0 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sofia    |        3 |      0 |       3 |       4 |         0 |      0 |     0 |        2 |      1 |         3 |         3 |      0 |      0 |      1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |
| Jay      |        5 |      1 |       7 |      14 |         0 |      4 |    10 |        6 |     15 |        12 |        13 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Derek    |        3 |      0 |       2 |       1 |         0 |      0 |     2 |        1 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Gathenji |        1 |      0 |       3 |       3 |         0 |      0 |     1 |        2 |      3 |         3 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Caro     |        1 |      0 |       0 |       3 |         0 |      1 |     0 |        1 |      1 |         2 |         2 |      1 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Sai      |        1 |      0 |       5 |       3 |         0 |      2 |     1 |        3 |      4 |         5 |         3 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Nabeel   |        2 |      3 |       0 |       3 |         0 |      0 |     1 |        2 |      1 |         0 |         2 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Ronnie   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      1 |         1 |         2 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Neha     |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |
| Ira      |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      1 |     0 |       1 |       0 |        0 |
| Kawin    |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        1 |      0 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |
| Tercel   |        3 |      0 |       3 |       2 |         0 |      0 |     1 |        4 |      3 |         0 |         2 |      0 |      0 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     4 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |

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
| 3+1        | 0.357143 |            28 |
| 2+2        | 0.396825 |            63 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.333333 |            27 |
| 2+2        | 0.355932 |            59 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.433333 |            30 |
| Success      | 0.321429 |            84 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.433333 |            30 |
| Success      | 0.304878 |            82 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      26 | 0.448276 |    0.384615  |
|         1 |      23 | 0.396552 |    0.0869565 |
|         2 |       9 | 0.155172 |    0.444444  |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       9 | 0.692308 |     0.111111 |
|         1 |       4 | 0.307692 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      10 | 0.434783 |     0.5      |
|         1 |       9 | 0.391304 |     0.111111 |
|         2 |       4 | 0.173913 |     0.25     |

*2 bad guys on mission 3:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       7 | 0.368421 |     0.571429 |
|         1 |       8 | 0.421053 |     0.125    |
|         2 |       4 | 0.210526 |     0.5      |

*3 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         1 |       2 | 0.666667 |            0 |
|         2 |       1 | 0.333333 |            1 |

### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            58 |     0.5      |
|                   1 |           106 |     0.386792 |
|                   2 |            16 |     0.5625   |
|                   3 |             5 |     0.4      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            55 |     0.472727 |
|                   1 |           100 |     0.35     |
|                   2 |            16 |     0.5625   |
|                   3 |             5 |     0.4      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.12973 |           185 |              24 |
| Assassin      |                 0.04516 |           155 |               7 |
| Morgana       |                 0.07027 |           185 |              13 |
| Mordred       |                 0.00926 |           108 |               1 |
| Loyal Servant |                 0       |           523 |               0 |
| Oberon        |                 0.01852 |            54 |               1 |
| Minion #1     |                 0.06897 |            29 |               2 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Abishek  |                    0.454545 |                 15 |            33 |
| Minh     |                    0.444444 |                  4 |             9 |
| Alex     |                    0.363636 |                  8 |            22 |
| Jai      |                    0.272727 |                  3 |            11 |
| Kate     |                    0.27027  |                 10 |            37 |
| Rachel   |                    0.26087  |                  6 |            23 |
| Jackie   |                    0.258065 |                  8 |            31 |
| Peter    |                    0.206897 |                  6 |            29 |
| Sushant  |                    0.2      |                  4 |            20 |
| Ruhi     |                    0.2      |                  1 |             5 |
| Brian    |                    0.170732 |                  7 |            41 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Jay      |          0        |                  0 |             3 |
| Brian    |          0.2      |                  3 |            15 |
| Sushant  |          0.230769 |                  3 |            13 |
| Minh     |          0.25     |                  1 |             4 |
| Kate     |          0.307692 |                  4 |            13 |
| Jeron    |          0.4      |                  2 |             5 |
| Abishek  |          0.428571 |                  6 |            14 |
| Jackie   |          0.4375   |                  7 |            16 |
| Peter    |          0.5      |                 11 |            22 |
| Alex     |          0.555556 |                  5 |             9 |
| Jai      |          0.625    |                  5 |             8 |
| Rachel   |          0.666667 |                  8 |            12 |
| Kish     |          0.666667 |                  2 |             3 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

| # Players   |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
| 10          |          0.388889 |                  7 |            18 |
| 5           |          0.75     |                  6 |             8 |
| 5O          |          0.428571 |                  3 |             7 |
| 6           |          0.333333 |                  5 |            15 |
| 6M          |          0.142857 |                  1 |             7 |
| 6O          |          0.3      |                  3 |            10 |
| 7           |          0.538462 |                 14 |            26 |
| 7O          |          0.6      |                  3 |             5 |
| 8           |          0.466667 |                  7 |            15 |
| 8O          |          0.666667 |                  2 |             3 |
| 9           |          0.454545 |                 10 |            22 |
| 9L          |          0.333333 |                  1 |             3 |
| 9O          |          0        |                  0 |             1 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

| # Players   |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
| 10          |                   1 |          0.428571 |                  6 |            14 |
| 10          |                   2 |          0        |                  0 |             3 |
| 10          |                   3 |          1        |                  1 |             1 |
| 5           |                   0 |          0.5      |                  2 |             4 |
| 5           |                   1 |          1        |                  4 |             4 |
| 5O          |                   0 |          0.333333 |                  2 |             6 |
| 5O          |                   1 |          1        |                  1 |             1 |
| 6           |                   0 |          0.5      |                  3 |             6 |
| 6           |                   1 |          0.25     |                  2 |             8 |
| 6           |                   3 |          0        |                  0 |             1 |
| 6M          |                   0 |          0.2      |                  1 |             5 |
| 6M          |                   1 |          0        |                  0 |             2 |
| 6O          |                   0 |          0.3      |                  3 |            10 |
| 7           |                   0 |          0.555556 |                  5 |             9 |
| 7           |                   1 |          0.615385 |                  8 |            13 |
| 7           |                   2 |          0.333333 |                  1 |             3 |
| 7           |                   3 |          0        |                  0 |             1 |
| 7O          |                   0 |          0.75     |                  3 |             4 |
| 7O          |                   2 |          0        |                  0 |             1 |
| 8           |                   0 |          0.333333 |                  1 |             3 |
| 8           |                   1 |          0.5      |                  6 |            12 |
| 8O          |                   1 |          0.666667 |                  2 |             3 |
| 9           |                   0 |          0.6      |                  3 |             5 |
| 9           |                   1 |          0.4      |                  6 |            15 |
| 9           |                   2 |          0.5      |                  1 |             2 |
| 9L          |                   0 |          1        |                  1 |             1 |
| 9L          |                   1 |          0        |                  0 |             2 |
| 9O          |                   2 |          0        |                  0 |             1 |
