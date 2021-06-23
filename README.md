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

Cheesy wins included: 0.4059 (n = 101)

Cheesy wins excluded: 0.3548 (n = 93)

**Good win % w.r.t. # players:**

Cheesy wins included:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           6 |            14 |     0.642857 |
|           7 |            15 |     0.466667 |
|           8 |            24 |     0.333333 |
|           9 |            27 |     0.333333 |
|          10 |            21 |     0.380952 |

Cheesy wins excluded:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           6 |            13 |     0.615385 |
|           7 |            12 |     0.333333 |
|           8 |            24 |     0.333333 |
|           9 |            24 |     0.25     |
|          10 |            20 |     0.35     |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            45 |       37.0889 |     22.1809 |
| Good     |            29 |       22.5862 |     14.1004 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            45 |       37.0889 |     22.1809 |
| Good     |            25 |       24.8    |     13.9583 |

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

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Jeron |
|----------|----------|--------------|-------------|---------------|--------|----------|----------------------|
| Jeron    | 0.714286 |     0.666667 |    0.75     |             7 |      5 |        2 |                    0 |
| Brian    | 0.593023 |     0.5      |    0.785714 |            86 |     51 |       35 |                   37 |
| Abishek  | 0.5875   |     0.5      |    0.71875  |            80 |     47 |       33 |                   36 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                    9 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                   12 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Jeron |
|----------|----------|--------------|-------------|---------------|--------|----------|----------------------|
| Jeron    | 0.714286 |     0.666667 |    0.75     |             7 |      5 |        2 |                    0 |
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                    3 |
| Brian    | 0.56962  |     0.442308 |    0.814815 |            79 |     45 |       34 |                   41 |
| Abishek  | 0.561644 |     0.428571 |    0.741935 |            73 |     41 |       32 |                   40 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                    9 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Jeron    |             0.192308  | 0.714286 |         0.521978 | 0.428571 |
| Brian    |             0.115278  | 0.593023 |         0.477745 | 0.674419 |
| Kish     |             0.0823098 | 0.529412 |         0.447102 | 0.588235 |
| Abishek  |             0.0799451 | 0.5875   |         0.507555 | 0.6      |
| Ewen     |             0.0443787 | 0.538462 |         0.494083 | 0.615385 |
| Anthony  |             0.0421245 | 0.5      |         0.457875 | 0.166667 |
| Jackie   |             0.0369588 | 0.487179 |         0.450221 | 0.717949 |
| Peter    |             0.0221332 | 0.491525 |         0.469392 | 0.644068 |
| Kate     |             0.0206666 | 0.506173 |         0.485506 | 0.641975 |
| Alex     |             0.0151548 | 0.490196 |         0.475041 | 0.627451 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Jeron    |             0.180124  | 0.714286 |         0.534161 | 0.428571 |
| Anthony  |             0.12      | 0.6      |         0.48     | 0.166667 |
| Brian    |             0.107734  | 0.56962  |         0.461886 | 0.674419 |
| Ewen     |             0.0746218 | 0.538462 |         0.46384  | 0.615385 |
| Abishek  |             0.0725857 | 0.561644 |         0.489058 | 0.6      |
| Alex     |             0.0385318 | 0.5      |         0.461468 | 0.627451 |
| Kish     |             0.0241497 | 0.5      |         0.47585  | 0.588235 |
| Jackie   |             0.0152342 | 0.459459 |         0.444225 | 0.717949 |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.6      |            10 |      6 |        4 |                    0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                    2 |
| Sushant  | 0.545455 |            11 |      6 |        5 |                    2 |
| Abishek  | 0.444444 |             9 |      4 |        5 |                    4 |
| Minh     | 0.4      |             5 |      2 |        3 |                    3 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|----------|---------------|--------|----------|-----------------------|
| Jackie   | 0.625    |             8 |      5 |        3 |                     0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                     2 |
| Brian    | 0.538462 |            13 |      7 |        6 |                     4 |
| Alex     | 0.375    |             8 |      3 |        5 |                     6 |
| Peter    | 0.333333 |             9 |      3 |        6 |                     8 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.8      |             5 |      4 |        1 |                    0 |
| Abishek  | 0.75     |             8 |      6 |        2 |                    3 |
| Alex     | 0.666667 |             9 |      6 |        3 |                    7 |
| Sushant  | 0.625    |             8 |      5 |        3 |                    8 |
| Jackie   | 0.6      |             5 |      3 |        2 |                    6 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.8      |            10 |      8 |        2 |                      0 |
| Brian    | 0.733333 |            15 |     11 |        4 |                      6 |
| Kate     | 0.666667 |             9 |      6 |        3 |                      7 |
| Sushant  | 0.5      |             8 |      4 |        4 |                     13 |
| Alex     | 0.5      |             6 |      3 |        3 |                     10 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 1        |             8 |      8 |        0 |                   0 |
| Brian    | 1        |             7 |      7 |        0 |                 nan |
| Peter    | 1        |             6 |      6 |        0 |                 nan |
| Rachel   | 0.714286 |             7 |      5 |        2 |                 nan |
| Sushant  | 0.666667 |             6 |      4 |        2 |                 nan |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.555556 |             9 |      5 |        4 |                    0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                    1 |
| Sushant  | 0.545455 |            11 |      6 |        5 |                    1 |
| Abishek  | 0.375    |             8 |      3 |        5 |                    4 |
| Rachel   | 0.222222 |             9 |      2 |        7 |                    7 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|----------|---------------|--------|----------|-----------------------|
| Jackie   | 0.625    |             8 |      5 |        3 |                     0 |
| Kate     | 0.428571 |             7 |      3 |        4 |                     4 |
| Brian    | 0.4      |            10 |      4 |        6 |                     7 |
| Alex     | 0.285714 |             7 |      2 |        5 |                     7 |
| Abishek  | 0.25     |            12 |      3 |        9 |                    13 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |             7 |      6 |        1 |                      0 |
| Alex     | 0.857143 |             7 |      6 |        1 |                      1 |
| Brian    | 0.8      |             5 |      4 |        1 |                      3 |
| Sushant  | 0.714286 |             7 |      5 |        2 |                      8 |
| Jackie   | 0.6      |             5 |      3 |        2 |                     10 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.8      |            10 |      8 |        2 |                      0 |
| Brian    | 0.785714 |            14 |     11 |        3 |                      2 |
| Kate     | 0.666667 |             9 |      6 |        3 |                      7 |
| Sushant  | 0.5      |             8 |      4 |        4 |                     13 |
| Ruhi     | 0.5      |             6 |      3 |        3 |                     10 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|----------|---------------|--------|----------|---------------------|
| Kate     | 1        |             8 |      8 |        0 |                   0 |
| Brian    | 1        |             7 |      7 |        0 |                 nan |
| Peter    | 1        |             6 |      6 |        0 |                 nan |
| Rachel   | 0.833333 |             6 |      5 |        1 |                 nan |
| Sushant  | 0.666667 |             6 |      4 |        2 |                 nan |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|----------|----------------|
| Brian    |             97 |
| Kate     |             92 |
| Abishek  |             82 |
| Peter    |             69 |
| Sushant  |             67 |
| Rachel   |             64 |
| Alex     |             55 |
| Jackie   |             50 |
| Jai      |             43 |
| Minh     |             36 |
| Ruhi     |             28 |
| Kish     |             17 |
| Ewen     |             13 |
| Jay      |             13 |
| Jeron    |             10 |
| Justin   |              9 |
| Sai      |              8 |
| Jade     |              7 |
| Gathenji |              7 |
| Anthony  |              6 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|----------|----------|----------|---------|
| Jade     | 1        |        7 |       0 |
| Gathenji | 0.857143 |        6 |       1 |
| Rachel   | 0.703125 |       45 |      19 |
| Jackie   | 0.7      |       35 |      15 |
| Justin   | 0.666667 |        6 |       3 |
| Kate     | 0.652174 |       60 |      32 |
| Jai      | 0.651163 |       28 |      15 |
| Brian    | 0.649485 |       63 |      34 |
| Alex     | 0.636364 |       35 |      20 |
| Sushant  | 0.626866 |       42 |      25 |
| Sai      | 0.625    |        5 |       3 |
| Peter    | 0.623188 |       43 |      26 |
| Ewen     | 0.615385 |        8 |       5 |
| Jeron    | 0.6      |        6 |       4 |
| Abishek  | 0.597561 |       49 |      33 |
| Kish     | 0.588235 |       10 |       7 |
| Jay      | 0.538462 |        7 |       6 |
| Ruhi     | 0.5      |       14 |      14 |
| Minh     | 0.5      |       18 |      18 |
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
| No                 |            87 |     0.448276 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |            87 |     0.448276 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       10 |         12 |          8 |        10 |         6 |        6 |           3 |              27 |            82 |
| Alex     |        4 |         10 |          9 |         6 |         3 |        1 |           1 |              21 |            55 |
| Anthony  |        0 |          1 |          3 |         2 |         0 |        0 |           0 |               0 |             6 |
| Brian    |       11 |         14 |          6 |        18 |         9 |        0 |           1 |              38 |            97 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |        7 |          9 |          5 |         5 |         1 |        3 |           1 |              19 |            50 |
| Jade     |        3 |          0 |          0 |         0 |         0 |        0 |           0 |               4 |             7 |
| Jai      |        4 |          4 |          4 |         5 |         3 |        3 |           0 |              20 |            43 |
| Jay      |        2 |          2 |          3 |         0 |         2 |        1 |           0 |               3 |            13 |
| Jeron    |        2 |          3 |          1 |         1 |         1 |        1 |           0 |               1 |            10 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       10 |          9 |          8 |        10 |         8 |        4 |           2 |              41 |            92 |
| Kish     |        1 |          3 |          1 |         3 |         2 |        0 |           1 |               6 |            17 |
| Minh     |        5 |          4 |          8 |         4 |         4 |        0 |           2 |               9 |            36 |
| Peter    |       11 |          9 |         10 |         6 |         6 |        3 |           1 |              23 |            69 |
| Rachel   |       11 |          8 |          7 |         4 |         7 |        0 |           1 |              26 |            64 |
| Ruhi     |        1 |          2 |          2 |         7 |         4 |        1 |           0 |              11 |            28 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       11 |          4 |          8 |         9 |         6 |        1 |           1 |              27 |            67 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.102 |      0.121 |      0.089 |     0.104 |     0.091 |    0.214 |       0.214 |           0.088 |            82 |
| Alex     |    0.041 |      0.101 |      0.1   |     0.062 |     0.045 |    0.036 |       0.071 |           0.068 |            55 |
| Anthony  |    0     |      0.01  |      0.033 |     0.021 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.112 |      0.141 |      0.067 |     0.188 |     0.136 |    0     |       0.071 |           0.124 |            97 |
| Ewen     |    0.01  |      0.02  |      0.022 |     0.01  |     0     |    0.071 |       0     |           0.016 |            13 |
| Gathenji |    0     |      0     |      0     |     0.01  |     0     |    0     |       0     |           0.02  |             7 |
| Jackie   |    0.071 |      0.091 |      0.056 |     0.052 |     0.015 |    0.107 |       0.071 |           0.062 |            50 |
| Jade     |    0.031 |      0     |      0     |     0     |     0     |    0     |       0     |           0.013 |             7 |
| Jai      |    0.041 |      0.04  |      0.044 |     0.052 |     0.045 |    0.107 |       0     |           0.065 |            43 |
| Jay      |    0.02  |      0.02  |      0.033 |     0     |     0.03  |    0.036 |       0     |           0.01  |            13 |
| Jeron    |    0.02  |      0.03  |      0.011 |     0.01  |     0.015 |    0.036 |       0     |           0.003 |            10 |
| Justin   |    0.02  |      0     |      0.011 |     0.01  |     0.015 |    0     |       0     |           0.013 |             9 |
| Kate     |    0.102 |      0.091 |      0.089 |     0.104 |     0.121 |    0.143 |       0.143 |           0.134 |            92 |
| Kish     |    0.01  |      0.03  |      0.011 |     0.031 |     0.03  |    0     |       0.071 |           0.02  |            17 |
| Minh     |    0.051 |      0.04  |      0.089 |     0.042 |     0.061 |    0     |       0.143 |           0.029 |            36 |
| Peter    |    0.112 |      0.091 |      0.111 |     0.062 |     0.091 |    0.107 |       0.071 |           0.075 |            69 |
| Rachel   |    0.112 |      0.081 |      0.078 |     0.042 |     0.106 |    0     |       0.071 |           0.085 |            64 |
| Ruhi     |    0.01  |      0.02  |      0.022 |     0.073 |     0.061 |    0.036 |       0     |           0.036 |            28 |
| Sai      |    0.01  |      0.01  |      0     |     0.01  |     0.03  |    0     |       0     |           0.01  |             8 |
| Sushant  |    0.112 |      0.04  |      0.089 |     0.094 |     0.091 |    0.036 |       0.071 |           0.088 |            67 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.122 |      0.146 |      0.098 |     0.122 |     0.073 |    0.073 |       0.037 |           0.329 |            82 |
| Alex     |    0.073 |      0.182 |      0.164 |     0.109 |     0.055 |    0.018 |       0.018 |           0.382 |            55 |
| Anthony  |    0     |      0.167 |      0.5   |     0.333 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.113 |      0.144 |      0.062 |     0.186 |     0.093 |    0     |       0.01  |           0.392 |            97 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.14  |      0.18  |      0.1   |     0.1   |     0.02  |    0.06  |       0.02  |           0.38  |            50 |
| Jade     |    0.429 |      0     |      0     |     0     |     0     |    0     |       0     |           0.571 |             7 |
| Jai      |    0.093 |      0.093 |      0.093 |     0.116 |     0.07  |    0.07  |       0     |           0.465 |            43 |
| Jay      |    0.154 |      0.154 |      0.231 |     0     |     0.154 |    0.077 |       0     |           0.231 |            13 |
| Jeron    |    0.2   |      0.3   |      0.1   |     0.1   |     0.1   |    0.1   |       0     |           0.1   |            10 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.109 |      0.098 |      0.087 |     0.109 |     0.087 |    0.043 |       0.022 |           0.446 |            92 |
| Kish     |    0.059 |      0.176 |      0.059 |     0.176 |     0.118 |    0     |       0.059 |           0.353 |            17 |
| Minh     |    0.139 |      0.111 |      0.222 |     0.111 |     0.111 |    0     |       0.056 |           0.25  |            36 |
| Peter    |    0.159 |      0.13  |      0.145 |     0.087 |     0.087 |    0.043 |       0.014 |           0.333 |            69 |
| Rachel   |    0.172 |      0.125 |      0.109 |     0.062 |     0.109 |    0     |       0.016 |           0.406 |            64 |
| Ruhi     |    0.036 |      0.071 |      0.071 |     0.25  |     0.143 |    0.036 |       0     |           0.393 |            28 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.164 |      0.06  |      0.119 |     0.134 |     0.09  |    0.015 |       0.015 |           0.403 |            67 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.43 |    0.45 |      0.33 |   0.43 |  0.65 |     0.42 |   0.47 |      0.49 |      0.36 |   0.38 |   0.58 |   0.62 |    0.86 |     0.57 |  -1    |  0.57 |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.43 |   0.17 |    1    |    0.51 |     -1    |   0.37 |  0.38 |     0.51 |   0.39 |      0.56 |      0.52 |   0.54 |   0.62 |   0.49 |    0.17 |     0.78 |  -1    |  0.71 |      -1    |  0.29 |
| Brian    |     0.45 |   0.83 |    0.51 |    1    |      0.33 |   0.36 |  0.5  |     0.58 |   0.53 |      0.47 |      0.53 |   0.37 |   0.35 |   0.44 |    0.4  |     0.44 |   0.71 |  0.15 |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |      1    |   0.5  | -1    |    -1    |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.43 |   0.4  |    0.37 |    0.36 |      0.5  |   1    |  0.54 |     0.43 |   0.46 |      0.55 |      0.48 |   0.56 |   0.67 |   0.13 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jai      |     0.65 |   0.4  |    0.38 |    0.5  |     -1    |   0.54 |  1    |     0.46 |   0.67 |      0.36 |      0.44 |   0.2  |  -1    |   0.46 |   -1    |    -1    |  -1    | -1    |       0.8  | -1    |
| Jackie   |     0.42 |   0.33 |    0.51 |    0.58 |     -1    |   0.43 |  0.46 |     1    |   0.53 |      0.53 |      0.42 |   0.22 |   0.43 |   0.54 |    0.62 |    -1    |  -1    | -1    |      -1    |  0.4  |
| Kate     |     0.47 |   0.45 |    0.39 |    0.53 |      0.33 |   0.46 |  0.67 |     0.53 |   1    |      0.44 |      0.5  |   0.38 |   0.29 |   0.42 |    0.78 |     0.83 |   0.33 |  0.31 |       0.57 |  0.5  |
| Sushant  |     0.49 |   0.43 |    0.56 |    0.47 |     -1    |   0.55 |  0.36 |     0.53 |   0.44 |      1    |      0.42 |   0.5  |   0.5  |   0.48 |    0.38 |     0.17 |   0.67 |  0.54 |       0.5  |  0.38 |
| Abishek  |     0.36 |   0.56 |    0.52 |    0.53 |      0.2  |   0.48 |  0.44 |     0.42 |   0.5  |      0.42 |      1    |   0.44 |   0.46 |   0.45 |    0.12 |     0.38 |   0.83 |  0.54 |       0.29 |  0.62 |
| Ruhi     |     0.38 |  -1    |    0.54 |    0.37 |     -1    |   0.56 |  0.2  |     0.22 |   0.38 |      0.5  |      0.44 |   1    |   0.67 |   0.69 |   -1    |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.58 |   0    |    0.62 |    0.35 |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.62 |   0.2  |    0.49 |    0.44 |     -1    |   0.13 |  0.46 |     0.54 |   0.42 |      0.48 |      0.45 |   0.69 |  -1    |   1    |   -1    |     0.67 |  -1    | -1    |       0.4  |  0.5  |
| Jeron    |     0.86 |  -1    |    0.17 |    0.4  |     -1    |  -1    | -1    |     0.62 |   0.78 |      0.38 |      0.12 |  -1    |  -1    |  -1    |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |    -1    |  -1    |   -1    |    0.71 |     -1    |  -1    | -1    |    -1    |   0.33 |      0.67 |      0.83 |  -1    |  -1    |  -1    |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.57 |  -1    |    0.71 |    0.15 |     -1    |  -1    | -1    |    -1    |   0.31 |      0.54 |      0.54 |   0.57 |  -1    |  -1    |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.05 |    0.05 |      0.33 |   0.13 |  0.16 |     0.03 |   0.09 |      0.09 |      0.06 |   0.12 |   0.17 |   0.12 |    0    |     0    |     -1 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Peter    |     0.05 |   0    |   -1    |    0.13 |     -1    |   0.21 |  0.12 |     0.08 |   0.05 |      0.17 |      0.2  |   0.23 |   0    |   0.05 |    0    |     0.11 |     -1 |  0.43 |      -1    |  0    |
| Brian    |     0.05 |   0.25 |    0.13 |   -1    |      0.33 |   0.11 |  0.05 |     0.12 |   0.12 |      0.09 |      0.14 |   0.04 |   0.12 |   0.1  |    0.1  |     0    |      0 |  0    |       0    |  0.12 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |     -1    |   0.33 | -1    |    -1    |   0.17 |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Minh     |     0.13 |   0.2  |    0.21 |    0.11 |      0.33 |  -1    |  0.15 |     0.04 |   0.14 |      0.23 |      0.1  |   0.22 |   0.33 |   0    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Jai      |     0.16 |   0    |    0.12 |    0.05 |     -1    |   0.15 | -1    |     0    |   0.18 |      0.06 |      0.16 |   0.2  |  -1    |   0.12 |   -1    |    -1    |     -1 | -1    |       0    | -1    |
| Jackie   |     0.03 |   0    |    0.08 |    0.12 |     -1    |   0.04 |  0    |    -1    |   0.06 |      0.09 |      0.11 |   0    |   0.29 |   0.07 |    0.25 |    -1    |     -1 | -1    |      -1    |  0.2  |
| Kate     |     0.09 |   0.09 |    0.05 |    0.12 |      0.17 |   0.14 |  0.18 |     0.06 |  -1    |      0.11 |      0.13 |   0.08 |   0    |   0.09 |    0.22 |     0.33 |      0 |  0.08 |       0    |  0.12 |
| Sushant  |     0.09 |   0.14 |    0.17 |    0.09 |     -1    |   0.23 |  0.06 |     0.09 |   0.11 |     -1    |      0.11 |   0.14 |   0    |   0.12 |    0    |     0    |      0 |  0.15 |       0    |  0.12 |
| Abishek  |     0.06 |   0.11 |    0.2  |    0.14 |      0    |   0.1  |  0.16 |     0.11 |   0.13 |      0.11 |     -1    |   0.15 |   0.15 |   0.12 |    0    |     0.25 |      0 |  0.15 |       0    |  0.12 |
| Ruhi     |     0.12 |  -1    |    0.23 |    0.04 |     -1    |   0.22 |  0.2  |     0    |   0.08 |      0.14 |      0.15 |  -1    |   0.17 |   0.46 |   -1    |    -1    |     -1 |  0.43 |      -1    | -1    |
| Kish     |     0.17 |   0    |    0    |    0.12 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Alex     |     0.12 |   0    |    0.05 |    0.1  |     -1    |   0    |  0.12 |     0.07 |   0.09 |      0.12 |      0.12 |   0.46 |  -1    |  -1    |   -1    |     0    |     -1 | -1    |       0    |  0.17 |
| Jeron    |     0    |  -1    |    0    |    0.1  |     -1    |  -1    | -1    |     0.25 |   0.22 |      0    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Jade     |    -1    |  -1    |   -1    |    0    |     -1    |  -1    | -1    |    -1    |   0    |      0    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Jay      |     0    |  -1    |    0.43 |    0    |     -1    |  -1    | -1    |    -1    |   0.08 |      0.15 |      0.15 |   0.43 |  -1    |  -1    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |     -1 | -1    |      -1    | -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |     -1 | -1    |      -1    | -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     0    |   0.5  |    0.57 |    0.55 |      0.67 |   0.57 |  0.35 |     0.58 |   0.53 |      0.51 |      0.64 |   0.62 |   0.42 |   0.38 |    0.14 |     0.43 |  -1    |  0.43 |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.57 |   0.83 |    0    |    0.49 |     -1    |   0.63 |  0.62 |     0.49 |   0.61 |      0.44 |      0.48 |   0.46 |   0.38 |   0.51 |    0.83 |     0.22 |  -1    |  0.29 |      -1    |  0.71 |
| Brian    |     0.55 |   0.17 |    0.49 |    0    |      0.67 |   0.64 |  0.5  |     0.42 |   0.47 |      0.53 |      0.47 |   0.63 |   0.65 |   0.56 |    0.6  |     0.56 |   0.29 |  0.85 |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |   -1    |    0.67 |      0    |   0.5  | -1    |    -1    |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.57 |   0.6  |    0.63 |    0.64 |      0.5  |   0    |  0.46 |     0.57 |   0.54 |      0.45 |      0.52 |   0.44 |   0.33 |   0.87 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jai      |     0.35 |   0.6  |    0.62 |    0.5  |     -1    |   0.46 |  0    |     0.54 |   0.33 |      0.64 |      0.56 |   0.8  |  -1    |   0.54 |   -1    |    -1    |  -1    | -1    |       0.2  | -1    |
| Jackie   |     0.58 |   0.67 |    0.49 |    0.42 |     -1    |   0.57 |  0.54 |     0    |   0.47 |      0.47 |      0.58 |   0.78 |   0.57 |   0.46 |    0.38 |    -1    |  -1    | -1    |      -1    |  0.6  |
| Kate     |     0.53 |   0.55 |    0.61 |    0.47 |      0.67 |   0.54 |  0.33 |     0.47 |   0    |      0.56 |      0.5  |   0.62 |   0.71 |   0.58 |    0.22 |     0.17 |   0.67 |  0.69 |       0.43 |  0.5  |
| Sushant  |     0.51 |   0.57 |    0.44 |    0.53 |     -1    |   0.45 |  0.64 |     0.47 |   0.56 |      0    |      0.58 |   0.5  |   0.5  |   0.52 |    0.62 |     0.83 |   0.33 |  0.46 |       0.5  |  0.62 |
| Abishek  |     0.64 |   0.44 |    0.48 |    0.47 |      0.8  |   0.52 |  0.56 |     0.58 |   0.5  |      0.58 |      0    |   0.56 |   0.54 |   0.55 |    0.88 |     0.62 |   0.17 |  0.46 |       0.71 |  0.38 |
| Ruhi     |     0.62 |  -1    |    0.46 |    0.63 |     -1    |   0.44 |  0.8  |     0.78 |   0.62 |      0.5  |      0.56 |   0    |   0.33 |   0.31 |   -1    |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.42 |   1    |    0.38 |    0.65 |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.38 |   0.8  |    0.51 |    0.56 |     -1    |   0.87 |  0.54 |     0.46 |   0.58 |      0.52 |      0.55 |   0.31 |  -1    |   0    |   -1    |     0.33 |  -1    | -1    |       0.6  |  0.5  |
| Jeron    |     0.14 |  -1    |    0.83 |    0.6  |     -1    |  -1    | -1    |     0.38 |   0.22 |      0.62 |      0.88 |  -1    |  -1    |  -1    |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |    -1    |  -1    |   -1    |    0.29 |     -1    |  -1    | -1    |    -1    |   0.67 |      0.33 |      0.17 |  -1    |  -1    |  -1    |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.43 |  -1    |    0.29 |    0.85 |     -1    |  -1    | -1    |    -1    |   0.69 |      0.46 |      0.46 |   0.43 |  -1    |  -1    |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|
| Rachel   |       64 |      4 |      18 |      27 |         2 |     10 |    20 |       13 |     26 |        23 |        19 |      6 |      7 |     20 |          1 |        1 |        0 |       6 |        0 |        4 |      2 |       0 |     4 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Peter    |       18 |      1 |      69 |      34 |         0 |      7 |    13 |       20 |     25 |        27 |        28 |      7 |      5 |     20 |          1 |        1 |        0 |       1 |        0 |        7 |      3 |       0 |     5 |      0 |       1 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |
| Brian    |       27 |     10 |      34 |      97 |         2 |     13 |    20 |       29 |     47 |        30 |        42 |     10 |      6 |     23 |          1 |        1 |        0 |       4 |        0 |        4 |      5 |       0 |     2 |      2 |       2 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |         6 |      3 |     0 |        0 |      2 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |       10 |      2 |       7 |      13 |         3 |     36 |     7 |       10 |     16 |        12 |        14 |      5 |      4 |      2 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |
| Jai      |       20 |      2 |      13 |      20 |         0 |      7 |    43 |       11 |     26 |        12 |        14 |      2 |      2 |     12 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     1 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |
| Jackie   |       13 |      2 |      20 |      29 |         0 |     10 |    11 |       50 |     26 |        17 |        16 |      2 |      3 |     15 |          0 |        0 |        1 |       5 |        1 |        1 |      0 |       1 |     1 |      0 |       0 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |
| Kate     |       26 |      5 |      25 |      47 |         2 |     16 |    26 |       26 |     92 |        28 |        39 |     10 |      4 |     22 |          0 |        0 |        0 |       7 |        0 |        5 |      2 |       1 |     4 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |
| Sushant  |       23 |      3 |      27 |      30 |         0 |     12 |    12 |       17 |     28 |        67 |        26 |     11 |      5 |     20 |          2 |        0 |        0 |       3 |        0 |        1 |      4 |       1 |     7 |      2 |       2 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |
| Abishek  |       19 |      5 |      28 |      42 |         1 |     14 |    14 |       16 |     39 |        26 |        82 |     12 |      6 |     22 |          0 |        0 |        0 |       1 |        0 |        3 |      5 |       0 |     7 |      1 |       1 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |
| Ruhi     |        6 |      2 |       7 |      10 |         0 |      5 |     2 |        2 |     10 |        11 |        12 |     28 |      4 |      9 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     4 |      1 |       0 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        7 |      0 |       5 |       6 |         1 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     17 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |
| Alex     |       20 |      1 |      20 |      23 |         0 |      2 |    12 |       15 |     22 |        20 |        22 |      9 |      2 |     55 |          1 |        0 |        0 |       0 |        0 |        4 |      1 |       1 |     2 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        6 |      0 |       1 |       4 |         0 |      2 |     3 |        5 |      7 |         3 |         1 |      0 |      1 |      0 |          0 |        0 |        1 |      10 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |
| Jade     |        2 |      2 |       3 |       5 |         0 |      0 |     0 |        0 |      2 |         4 |         5 |      1 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |      7 |       0 |     1 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        4 |      1 |       5 |       2 |         0 |      1 |     1 |        1 |      4 |         7 |         7 |      4 |      1 |      2 |          0 |        0 |        0 |       2 |        0 |        0 |      1 |       0 |    13 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
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
| Rachel   |       -1 |      2 |       2 |       3 |         2 |      3 |     5 |        1 |      5 |         4 |         3 |      2 |      2 |      4 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Peter    |        2 |      0 |      -1 |       9 |         0 |      4 |     4 |        3 |      3 |         8 |        11 |      3 |      0 |      2 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     3 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |
| Brian    |        3 |      3 |       9 |      -1 |         2 |      4 |     2 |        6 |     11 |         6 |        11 |      1 |      2 |      5 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |        -1 |      2 |     0 |        0 |      1 |         0 |         0 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |        3 |      1 |       4 |       4 |         2 |     -1 |     2 |        1 |      5 |         5 |         3 |      2 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jai      |        5 |      0 |       4 |       2 |         0 |      2 |    -1 |        0 |      7 |         2 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Jackie   |        1 |      0 |       3 |       6 |         0 |      1 |     0 |       -1 |      3 |         3 |         4 |      0 |      2 |      2 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |
| Kate     |        5 |      1 |       3 |      11 |         1 |      5 |     7 |        3 |     -1 |         7 |        10 |      2 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        2 |      0 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |
| Sushant  |        4 |      1 |       8 |       6 |         0 |      5 |     2 |        3 |      7 |        -1 |         7 |      3 |      0 |      5 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       1 |     2 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Abishek  |        3 |      1 |      11 |      11 |         0 |      3 |     5 |        4 |     10 |         7 |        -1 |      4 |      2 |      6 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Ruhi     |        2 |      1 |       3 |       1 |         0 |      2 |     2 |        0 |      2 |         3 |         4 |     -1 |      1 |      6 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        2 |      0 |       0 |       2 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |
| Alex     |        4 |      0 |       2 |       5 |         0 |      0 |     3 |        2 |      5 |         5 |         6 |      6 |      0 |     -1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        0 |      0 |       0 |       1 |         0 |      1 |     0 |        2 |      2 |         0 |         0 |      0 |      1 |      0 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jade     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
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
| Rachel   |        0 |      4 |      24 |      33 |         4 |     13 |    11 |       18 |     29 |        24 |        34 |     10 |      5 |     12 |          1 |        0 |        1 |       1 |        1 |        3 |      1 |       1 |     3 |      0 |       1 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |
| Peter    |       24 |      5 |       0 |      33 |         1 |     12 |    21 |       19 |     39 |        21 |        26 |      6 |      3 |     21 |          1 |        0 |        1 |       5 |        1 |        2 |      1 |       2 |     2 |      2 |       1 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |
| Brian    |       33 |      2 |      33 |       0 |         4 |     23 |    20 |       21 |     42 |        34 |        37 |     17 |     11 |     29 |          1 |        0 |        1 |       6 |        1 |        5 |      2 |       2 |    11 |      0 |       0 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |
| Anthony  |        4 |      0 |       1 |       4 |         0 |      3 |     1 |        1 |      4 |         1 |         4 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |       13 |      3 |      12 |      23 |         3 |      0 |     6 |       13 |     19 |        10 |        15 |      4 |      2 |     13 |          0 |        0 |        0 |       2 |        0 |        2 |      2 |       0 |     2 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |
| Jai      |       11 |      3 |      21 |      20 |         1 |      6 |     0 |       13 |     13 |        21 |        18 |      8 |      0 |     14 |          1 |        0 |        0 |       1 |        0 |        2 |      3 |       0 |     2 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Jackie   |       18 |      4 |      19 |      21 |         1 |     13 |    13 |        0 |     23 |        15 |        22 |      7 |      4 |     13 |          0 |        1 |        0 |       3 |        0 |        2 |      1 |       1 |     1 |      0 |       0 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |
| Kate     |       29 |      6 |      39 |      42 |         4 |     19 |    13 |       23 |      0 |        35 |        39 |     16 |     10 |     31 |          2 |        0 |        0 |       2 |        0 |        1 |      4 |       1 |     9 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |
| Sushant  |       24 |      4 |      21 |      34 |         1 |     10 |    21 |       15 |     35 |         0 |        36 |     11 |      5 |     22 |          0 |        0 |        0 |       5 |        0 |        5 |      2 |       0 |     6 |      0 |       0 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |
| Abishek  |       34 |      4 |      26 |      37 |         4 |     15 |    18 |       22 |     39 |        36 |         0 |     15 |      7 |     27 |          0 |        0 |        0 |       7 |        0 |        5 |      1 |       1 |     6 |      1 |       1 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |
| Ruhi     |       10 |      1 |       6 |      17 |         0 |      4 |     8 |        7 |     16 |        11 |        15 |      0 |      2 |      4 |          0 |        0 |        0 |       4 |        0 |        0 |      1 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        5 |      5 |       3 |      11 |         2 |      2 |     0 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |
| Alex     |       12 |      4 |      21 |      29 |         0 |     13 |    14 |       13 |     31 |        22 |        27 |      4 |      1 |      0 |          1 |        0 |        0 |       0 |        0 |        2 |      1 |       0 |     2 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        1 |      1 |       5 |       6 |         0 |      2 |     1 |        3 |      2 |         5 |         7 |      4 |      1 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Jade     |        1 |      0 |       1 |       2 |         0 |      2 |     3 |        1 |      4 |         2 |         1 |      1 |      0 |      1 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        1 |      0 |       2 |       2 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        3 |      1 |       2 |      11 |         0 |      2 |     2 |        1 |      9 |         6 |         6 |      3 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |
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
| Rachel   |    -1    |   -1   |    0.22 |    0.48 |   0.44 |  0.21 |     0.45 |   0.39 |      0.36 |      0.5  |   0.17 |   0.43 |   0.37 |    -1   |    -1    |   -1   | -1    |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.22 |   -1   |   -1    |    0.59 |  -1    |  0.33 |     0.5  |   0.5  |      0.44 |      0.63 |   0.43 |   0.2  |   0.39 |    -1   |     0.14 |   -1   |  0.6  |      -1    |  -1   |
| Brian    |     0.48 |    0.5 |    0.59 |   -1    |   0.45 |  0.39 |     0.5  |   0.58 |      0.53 |      0.65 |   0.6  |   0.83 |   0.67 |    -1   |    -1    |    0.4 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |   -1    |    0.45 |  -1    |  0    |     0.2  |   0.53 |      0.33 |      0.43 |   0.2  |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.21 |   -1   |    0.33 |    0.39 |   0    | -1    |     0.11 |   0.35 |      0.33 |      0.5  |  -1    |  -1    |   0.36 |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.45 |   -1   |    0.5  |    0.5  |   0.2  |  0.11 |    -1    |   0.45 |      0.53 |      0.5  |  -1    |  -1    |   0.5  |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.39 |    0.6 |    0.5  |    0.58 |   0.53 |  0.35 |     0.45 |  -1    |      0.42 |      0.59 |   0.3  |  -1    |   0.5  |     0.6 |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.36 |   -1   |    0.44 |    0.53 |   0.33 |  0.33 |     0.53 |   0.42 |     -1    |      0.54 |   0.36 |   0.4  |   0.5  |    -1   |    -1    |   -1   |  0.17 |      -1    |  -1   |
| Abishek  |     0.5  |    0.4 |    0.63 |    0.65 |   0.43 |  0.5  |     0.5  |   0.59 |      0.54 |     -1    |   0.42 |   0.83 |   0.59 |    -1   |    -1    |    0.4 |  0.5  |      -1    |   0.2 |
| Ruhi     |     0.17 |   -1   |    0.43 |    0.6  |   0.2  | -1    |    -1    |   0.3  |      0.36 |      0.42 |  -1    |  -1    |   0.56 |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Alex     |     0.37 |   -1   |    0.39 |    0.67 |  -1    |  0.36 |     0.5  |   0.5  |      0.5  |      0.59 |   0.56 |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jeron    |    -1    |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Jay      |    -1    |   -1   |    0.6  |   -1    |  -1    | -1    |    -1    |  -1    |      0.17 |      0.5  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |  -1   |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|
| Rachel   |    -1    |   -1   |    0.22 |    0.43 |   0.44 |  0.24 |     0.45 |   0.36 |      0.38 |      0.47 |  -1    |   0.33 |   0.41 |    -1   |    -1    |   -1   | -1    |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.22 |   -1   |   -1    |    0.56 |  -1    |  0.25 |     0.47 |   0.42 |      0.4  |      0.58 |   0.43 |  -1    |   0.35 |    -1   |     0.14 |   -1   |  0.6  |      -1    |
| Brian    |     0.43 |    0.5 |    0.56 |   -1    |   0.4  |  0.35 |     0.48 |   0.55 |      0.52 |      0.62 |   0.5  |  -1    |   0.65 |    -1   |    -1    |    0.4 | -1    |      -1    |
| Minh     |     0.44 |   -1   |   -1    |    0.4  |  -1    |  0    |     0    |   0.46 |      0.2  |      0.38 |   0.2  |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.24 |   -1   |    0.25 |    0.35 |   0    | -1    |     0.11 |   0.35 |      0.33 |      0.46 |  -1    |  -1    |   0.44 |    -1   |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.45 |   -1   |    0.47 |    0.48 |   0    |  0.11 |    -1    |   0.39 |      0.46 |      0.47 |  -1    |  -1    |   0.45 |    -1   |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.36 |    0.6 |    0.42 |    0.55 |   0.46 |  0.35 |     0.39 |  -1    |      0.35 |      0.54 |   0.3  |  -1    |   0.47 |     0.6 |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.38 |   -1   |    0.4  |    0.52 |   0.2  |  0.33 |     0.46 |   0.35 |     -1    |      0.5  |   0.36 |   0.4  |   0.47 |    -1   |    -1    |   -1   |  0.17 |      -1    |
| Abishek  |     0.47 |    0.4 |    0.58 |    0.62 |   0.38 |  0.46 |     0.47 |   0.54 |      0.5  |     -1    |   0.36 |   0.8  |   0.57 |    -1   |    -1    |    0.4 |  0.5  |      -1    |
| Ruhi     |    -1    |   -1   |    0.43 |    0.5  |   0.2  | -1    |    -1    |   0.3  |      0.36 |      0.36 |  -1    |  -1    |   0.67 |    -1   |    -1    |   -1   | -1    |      -1    |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Alex     |     0.41 |   -1   |    0.35 |    0.65 |  -1    |  0.44 |     0.45 |   0.47 |      0.47 |      0.57 |   0.67 |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jeron    |    -1    |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Jay      |    -1    |   -1   |    0.6  |   -1    |  -1    | -1    |    -1    |  -1    |      0.17 |      0.5  |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |    -1   |    -1    |   -1   | -1    |      -1    |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Alex |
|----------|--------|----------|-------|--------|-----------|-----------|--------|---------|---------|--------|
| Minh     |   -1   |     -1   | -1    |   0.8  |      0.2  |     -1    |   -1   |   -1    |   -1    |  -1    |
| Rachel   |   -1   |     -1   |  0    |   0.6  |     -1    |     -1    |   -1   |   -1    |   -1    |  -1    |
| Jai      |   -1   |      0   | -1    |   0.67 |     -1    |      0.8  |   -1   |   -1    |   -1    |  -1    |
| Kate     |    0.8 |      0.6 |  0.67 |  -1    |      0.33 |      0.9  |   -1   |    0.8  |   -1    |   1    |
| Sushant  |    0.2 |     -1   | -1    |   0.33 |     -1    |      0.71 |   -1   |    0.67 |    0.75 |   0.8  |
| Abishek  |   -1   |     -1   |  0.8  |   0.9  |      0.71 |     -1    |   -1   |    0.8  |    0.7  |   0.83 |
| Ruhi     |   -1   |     -1   | -1    |  -1    |     -1    |     -1    |   -1   |   -1    |   -1    |   0.5  |
| Brian    |   -1   |     -1   | -1    |   0.8  |      0.67 |      0.8  |   -1   |   -1    |    1    |   1    |
| Peter    |   -1   |     -1   | -1    |  -1    |      0.75 |      0.7  |   -1   |    1    |   -1    |  -1    |
| Alex     |   -1   |     -1   | -1    |   1    |      0.8  |      0.83 |    0.5 |    1    |   -1    |  -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Jai |   Kate |   Sushant |   Abishek |   Brian |   Peter |   Alex |
|----------|--------|----------|-------|--------|-----------|-----------|---------|---------|--------|
| Minh     |   -1   |     -1   | -1    |   0.8  |      0.2  |     -1    |   -1    |   -1    |  -1    |
| Rachel   |   -1   |     -1   | -1    |   0.6  |     -1    |     -1    |   -1    |   -1    |  -1    |
| Jai      |   -1   |     -1   | -1    |   0.67 |     -1    |      0.8  |   -1    |   -1    |  -1    |
| Kate     |    0.8 |      0.6 |  0.67 |  -1    |      0.33 |      0.9  |    0.8  |   -1    |   1    |
| Sushant  |    0.2 |     -1   | -1    |   0.33 |     -1    |      0.71 |    0.67 |    0.75 |   0.8  |
| Abishek  |   -1   |     -1   |  0.8  |   0.9  |      0.71 |     -1    |    0.89 |    0.7  |   0.83 |
| Brian    |   -1   |     -1   | -1    |   0.8  |      0.67 |      0.89 |   -1    |    1    |   1    |
| Peter    |   -1   |     -1   | -1    |  -1    |      0.75 |      0.7  |    1    |   -1    |  -1    |
| Alex     |   -1   |     -1   | -1    |   1    |      0.8  |      0.83 |    1    |   -1    |  -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |   Sai |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|-------|
| Peter    |   -1    |    0.39 |   0.7  |     0.52 |    0.2 |  0.56 |     0.46 |   0.53 |      0.5  |      0.42 |   1    |  -1    |   0.68 |   -1    |     -1   | -1    |       -1   |   0.8 |
| Brian    |    0.61 |   -1    |   0.6  |     0.68 |   -1   |  0.67 |     0.53 |   0.57 |      0.62 |      0.51 |   0.82 |   0.64 |   0.67 |   -1    |      0.6 |  0.5  |       -1   |  -1   |
| Minh     |    0.3  |    0.4  |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.27 |      0.3  |      0.4  |  -1    |  -1    |   0.25 |   -1    |     -1   | -1    |       -1   |  -1   |
| Rachel   |    0.48 |    0.32 |   0.5  |    -1    |   -1   |  0.5  |     0.5  |   0.39 |      0.43 |      0.33 |   0.6  |   0.6  |   0.17 |   -1    |     -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.33 |  -1    |     0.5  |   -1   | -1    |     0.38 |   0.25 |      0.38 |      0.28 |   0.38 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |  -1   |
| Jackie   |    0.54 |    0.47 |   0.5  |     0.5  |   -1   |  0.62 |    -1    |   0.5  |      0.33 |      0.45 |   0.57 |  -1    |   0.5  |   -1    |     -1   | -1    |       -1   |  -1   |
| Kate     |    0.47 |    0.43 |   0.73 |     0.61 |    0.5 |  0.75 |     0.5  |  -1    |      0.54 |      0.41 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |  0.38 |       -1   |  -1   |
| Sushant  |    0.5  |    0.38 |   0.7  |     0.57 |   -1   |  0.62 |     0.67 |   0.46 |     -1    |      0.38 |   0.64 |   0.4  |   0.36 |   -1    |      0.6 |  0.2  |       -1   |   0.8 |
| Abishek  |    0.58 |    0.49 |   0.6  |     0.67 |   -1   |  0.72 |     0.55 |   0.59 |      0.62 |     -1    |   0.73 |   0.71 |   0.56 |    0.33 |      0.6 |  0.6  |        0.8 |  -1   |
| Ruhi     |    0    |    0.18 |  -1    |     0.4  |   -1   |  0.62 |     0.43 |   0.38 |      0.36 |      0.27 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Alex     |    0.32 |    0.33 |   0.75 |     0.83 |   -1   |  0.73 |     0.5  |   0.48 |      0.64 |      0.44 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jeron    |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.67 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jay      |   -1    |    0.5  |  -1    |    -1    |   -1   | -1    |    -1    |   0.62 |      0.8  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|
| Peter    |   -1    |    0.37 |   0.7  |     0.47 |    0.2 |  0.53 |     0.46 |   0.53 |      0.47 |      0.4  |   1    |  -1    |   0.65 |   -1    |     -1   | -1    |       -1   |
| Brian    |    0.63 |   -1    |   0.61 |     0.66 |   -1   |  0.64 |     0.57 |   0.58 |      0.63 |      0.51 |   0.8  |   0.6  |   0.67 |   -1    |      0.6 |  0.5  |       -1   |
| Minh     |    0.3  |    0.39 |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.29 |      0.3  |      0.38 |  -1    |  -1    |   0.18 |   -1    |     -1   | -1    |       -1   |
| Rachel   |    0.53 |    0.34 |   0.5  |    -1    |   -1   |  0.56 |     0.53 |   0.42 |      0.48 |      0.37 |   0.6  |  -1    |   0.17 |   -1    |     -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |
| Jai      |    0.47 |    0.36 |  -1    |     0.44 |   -1   | -1    |     0.43 |   0.3  |      0.39 |      0.31 |   0.38 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |
| Jackie   |    0.54 |    0.43 |   0.5  |     0.47 |   -1   |  0.57 |    -1    |   0.5  |      0.33 |      0.42 |   0.5  |  -1    |   0.45 |   -1    |     -1   | -1    |       -1   |
| Kate     |    0.47 |    0.42 |   0.71 |     0.58 |    0.5 |  0.7  |     0.5  |  -1    |      0.54 |      0.4  |   0.62 |   0.33 |   0.48 |   -1    |     -1   |  0.38 |       -1   |
| Sushant  |    0.53 |    0.37 |   0.7  |     0.52 |   -1   |  0.61 |     0.67 |   0.46 |     -1    |      0.38 |   0.6  |  -1    |   0.3  |   -1    |      0.6 |  0.2  |       -1   |
| Abishek  |    0.6  |    0.49 |   0.62 |     0.63 |   -1   |  0.69 |     0.58 |   0.6  |      0.62 |     -1    |   0.69 |   0.67 |   0.52 |    0.33 |      0.6 |  0.6  |        0.8 |
| Ruhi     |    0    |    0.2  |  -1    |     0.4  |   -1   |  0.62 |     0.5  |   0.38 |      0.4  |      0.31 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Alex     |    0.35 |    0.33 |   0.82 |     0.83 |   -1   |  0.73 |     0.55 |   0.52 |      0.7  |      0.48 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jeron    |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.67 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jay      |   -1    |    0.5  |  -1    |    -1    |   -1   | -1    |    -1    |   0.62 |      0.8  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.352941 |            17 |
| 2+2        | 0.394737 |            38 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.3125   |            16 |
| 2+2        | 0.323529 |            34 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.4375   |            16 |
| Success      | 0.352941 |            51 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.4375   |            16 |
| Success      | 0.326531 |            49 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |      17 | 0.414634 |     0.411765 |
|         1 |      16 | 0.390244 |     0.125    |
|         2 |       8 | 0.195122 |     0.5      |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       6 | 0.666667 |     0.166667 |
|         1 |       3 | 0.333333 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |      % |   Good Win % |
|-----------|---------|--------|--------------|
|         0 |       7 | 0.4375 |     0.571429 |
|         1 |       6 | 0.375  |     0.166667 |
|         2 |       3 | 0.1875 |     0.333333 |

*2 bad guys on mission 3:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       4 | 0.285714 |     0.5      |
|         1 |       6 | 0.428571 |     0.166667 |
|         2 |       4 | 0.285714 |     0.5      |

*3 bad guys on mission 2:*

|   # Fails |   Count |   % |   Good Win % |
|-----------|---------|-----|--------------|
|         1 |       1 | 0.5 |            0 |
|         2 |       1 | 0.5 |            1 |

### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            11 |     0.545455 |
|                   1 |            78 |     0.371795 |
|                   2 |            10 |     0.5      |
|                   3 |             2 |     0.5      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |             9 |     0.444444 |
|                   1 |            72 |     0.319444 |
|                   2 |            10 |     0.5      |
|                   3 |             2 |     0.5      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

|   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|-------------------------|---------------|-----------------|
|                 0.11881 |           101 |              12 |
|                 0.04255 |            94 |               4 |
|                 0.0297  |           101 |               3 |
|                 0.01389 |            72 |               1 |
|                 0       |           321 |               0 |
|                 0       |            28 |               0 |
|                 0       |            15 |               0 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Jai      |                   0.5       |                  3 |             6 |
| Rachel   |                   0.363636  |                  4 |            11 |
| Alex     |                   0.357143  |                  5 |            14 |
| Jackie   |                   0.333333  |                  4 |            12 |
| Abishek  |                   0.315789  |                  6 |            19 |
| Kate     |                   0.25      |                  5 |            20 |
| Sushant  |                   0.222222  |                  2 |             9 |
| Peter    |                   0.166667  |                  2 |            12 |
| Brian    |                   0.0909091 |                  2 |            22 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Jade     |         0         |                  0 |             3 |
| Minh     |         0         |                  0 |             5 |
| Sushant  |         0.0909091 |                  1 |            11 |
| Brian    |         0.0909091 |                  1 |            11 |
| Jai      |         0.25      |                  1 |             4 |
| Jackie   |         0.285714  |                  2 |             7 |
| Rachel   |         0.363636  |                  4 |            11 |
| Kate     |         0.4       |                  4 |            10 |
| Abishek  |         0.4       |                  4 |            10 |
| Alex     |         0.5       |                  2 |             4 |
| Peter    |         0.545455  |                  6 |            11 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

|   # Players |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
|           6 |          0.307692 |                  4 |            13 |
|           7 |          0.5      |                  7 |            14 |
|           8 |          0.533333 |                  8 |            15 |
|           9 |          0.416667 |                  5 |            12 |
|          10 |          0.428571 |                  6 |            14 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

|   # Players |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
|           6 |                   0 |          0.4      |                  2 |             5 |
|           6 |                   1 |          0.285714 |                  2 |             7 |
|           6 |                   3 |          0        |                  0 |             1 |
|           7 |                   0 |          0.5      |                  3 |             6 |
|           7 |                   1 |          0.571429 |                  4 |             7 |
|           7 |                   2 |          0        |                  0 |             1 |
|           8 |                   1 |          0.533333 |                  8 |            15 |
|           9 |                   1 |          0.363636 |                  4 |            11 |
|           9 |                   2 |          1        |                  1 |             1 |
|          10 |                   1 |          0.545455 |                  6 |            11 |
|          10 |                   2 |          0        |                  0 |             3 |
