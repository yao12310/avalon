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

Cheesy wins included: 0.4322 (n = 236)

Cheesy wins excluded: 0.4044 (n = 225)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            32 |     0.40625  |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5X          |             6 |     0.5      |
| 6           |            26 |     0.653846 |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            35 |     0.371429 |
| 7O          |             5 |     0.4      |
| 8           |            39 |     0.282051 |
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
| 6           |            24 |     0.625    |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            32 |     0.3125   |
| 7O          |             5 |     0.4      |
| 8           |            39 |     0.282051 |
| 8O          |             3 |     0        |
| 9           |            39 |     0.282051 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           119 |       29.1681 |     19.4432 |
| Good     |            90 |       19.5222 |     15.4732 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           119 |       29.1681 |     19.4432 |
| Good     |            83 |       20.5181 |     15.708  |

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

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Andrew |
|---------|---------|-------------|------------|--------------|-------|---------|----------------------|
| Andrew   | 0.666667 |        0.625 |    1        |             9 |      6 |        3 |                     0 |
| Abishek  | 0.59633  |        0.5   |    0.723404 |           109 |     65 |       44 |                    24 |
| Brian    | 0.563025 |        0.475 |    0.74359  |           119 |     67 |       52 |                    38 |
| Ewen     | 0.538462 |        0.375 |    0.8      |            13 |      7 |        6 |                     6 |
| Kish     | 0.529412 |        0.5   |    0.571429 |            17 |      9 |        8 |                     8 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Andrew |
|---------|---------|-------------|------------|--------------|-------|---------|----------------------|
| Andrew   | 0.625    |     0.571429 |    1        |             8 |      5 |        3 |                     0 |
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                     1 |
| Abishek  | 0.584158 |     0.446429 |    0.755556 |           101 |     59 |       42 |                    12 |
| Brian    | 0.54955  |     0.432432 |    0.783784 |           111 |     61 |       50 |                    23 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                     4 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|---------|----------------------|---------|-----------------|---------|
| Andrew   |             0.200794  | 0.666667 |         0.465873 | 0.888889 |
| Brian    |             0.080397  | 0.563025 |         0.482628 | 0.672269 |
| Kish     |             0.0784748 | 0.529412 |         0.450937 | 0.588235 |
| Abishek  |             0.0777647 | 0.59633  |         0.518566 | 0.568807 |
| Anthony  |             0.0486111 | 0.5      |         0.451389 | 0.166667 |
| Ewen     |             0.0413635 | 0.538462 |         0.497098 | 0.615385 |
| Kate     |             0.041209  | 0.524752 |         0.483543 | 0.653465 |
| Peter    |             0.0229291 | 0.468085 |         0.445156 | 0.638298 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|---------|----------------------|---------|-----------------|---------|
| Andrew   |             0.174138  | 0.625    |         0.450862 | 0.888889 |
| Anthony  |             0.144099  | 0.6      |         0.455901 | 0.166667 |
| Brian    |             0.0813404 | 0.54955  |         0.468209 | 0.672269 |
| Abishek  |             0.0738071 | 0.584158 |         0.510351 | 0.568807 |
| Ewen     |             0.062127  | 0.538462 |         0.476335 | 0.615385 |
| Kate     |             0.025806  | 0.5      |         0.474194 | 0.653465 |
| Kish     |             0.0251322 | 0.5      |         0.474868 | 0.588235 |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|---------|---------|--------------|-------|---------|---------------------|
| Brian    | 0.615385 |            13 |      8 |        5 |                    0 |
| Kate     | 0.583333 |            12 |      7 |        5 |                    2 |
| Minh     | 0.571429 |             7 |      4 |        3 |                    1 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|---------|---------|--------------|-------|---------|----------------------|
| Jackie   | 0.7      |            10 |      7 |        3 |                     0 |
| Sushant  | 0.666667 |             6 |      4 |        2 |                     1 |
| Kate     | 0.636364 |            11 |      7 |        4 |                     3 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.692308 |            13 |      9 |        4 |                      0 |
| Sushant  | 0.666667 |            12 |      8 |        4 |                      2 |
| Brian    | 0.642857 |            14 |      9 |        5 |                      3 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.8      |            15 |     12 |        3 |                      0 |
| Brian    | 0.75     |            16 |     12 |        4 |                      5 |
| Minh     | 0.666667 |             6 |      4 |        2 |                      5 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|---------|---------|--------------|-------|---------|--------------------|
| Kate     | 1        |            10 |     10 |        0 |                   0 |
| Brian    | 1        |             8 |      8 |        0 |                 nan |
| Peter    | 0.857143 |             7 |      6 |        1 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.612903 |            31 |     19 |       12 |                      0 |
| Andrew   | 0.6      |             5 |      3 |        2 |                      1 |
| Ruhi     | 0.538462 |            13 |      7 |        6 |                      3 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|---------|---------|--------------|-------|---------|---------------------|
| Brian    | 0.583333 |            12 |      7 |        5 |                    0 |
| Kate     | 0.583333 |            12 |      7 |        5 |                    1 |
| Minh     | 0.4      |             5 |      2 |        3 |                    3 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|---------|---------|--------------|-------|---------|----------------------|
| Jackie   | 0.666667 |             9 |      6 |        3 |                     0 |
| Sushant  | 0.666667 |             6 |      4 |        2 |                     1 |
| Kate     | 0.555556 |             9 |      5 |        4 |                     4 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.75     |            12 |      9 |        3 |                      0 |
| Sushant  | 0.727273 |            11 |      8 |        3 |                      2 |
| Alex     | 0.7      |            10 |      7 |        3 |                      3 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Brian    | 0.8      |            15 |     12 |        3 |                      7 |
| Minh     | 0.8      |             5 |      4 |        1 |                      3 |

*Mordred:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|---------|---------|--------------|-------|---------|--------------------|
| Kate     | 1        |            10 |     10 |        0 |                   0 |
| Brian    | 1        |             8 |      8 |        0 |                 nan |
| Peter    | 0.857143 |             7 |      6 |        1 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.538462 |            26 |     14 |       12 |                      0 |
| Ruhi     | 0.454545 |            11 |      5 |        6 |                      3 |
| Brian    | 0.422222 |            45 |     19 |       26 |                     12 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|---------|---------------|
| Brian    |            213 |
| Kate     |            175 |
| Peter    |            173 |
| Jackie   |            169 |
| Abishek  |            166 |
| Rachel   |            134 |
| Sushant  |            128 |
| Alex     |             94 |
| Jai      |             92 |
| Minh     |             69 |
| Ruhi     |             46 |
| Jeron    |             32 |
| Jay      |             26 |
| Tercel   |             24 |
| Kish     |             21 |
| Jade     |             20 |
| Daisy    |             17 |
| Aman     |             15 |
| Vishal   |             13 |
| Ewen     |             13 |
| Anthony  |             12 |
| Andrew   |             10 |
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
| Andrew   | 0.8      |        8 |       2 |
| Daisy    | 0.764706 |       13 |       4 |
| Rachel   | 0.731343 |       98 |      36 |
| Karthik  | 0.714286 |        5 |       2 |
| Kate     | 0.685714 |      120 |      55 |
| Megan    | 0.666667 |        4 |       2 |
| Tercel   | 0.666667 |       16 |       8 |
| Justin   | 0.666667 |        6 |       3 |
| Jeron    | 0.65625  |       21 |      11 |
| Jackie   | 0.639053 |      108 |      61 |
| Alex     | 0.638298 |       60 |      34 |
| Brian    | 0.633803 |      135 |      78 |
| Sai      | 0.625    |        5 |       3 |
| Peter    | 0.624277 |      108 |      65 |
| Jai      | 0.619565 |       57 |      35 |
| Kish     | 0.619048 |       13 |       8 |
| Ewen     | 0.615385 |        8 |       5 |
| Jay      | 0.615385 |       16 |      10 |
| Olivia   | 0.6      |        3 |       2 |
| Selena   | 0.6      |        3 |       2 |
| Minh     | 0.57971  |       40 |      29 |
| Sushant  | 0.578125 |       74 |      54 |
| Abishek  | 0.566265 |       94 |      72 |
| Ruhi     | 0.543478 |       25 |      21 |
| Vishal   | 0.538462 |        7 |       6 |
| Aman     | 0.466667 |        7 |       8 |
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
| No                 |           222 |      0.45045 |
| Yes                |            10 |      0       |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|---------------------|--------------|-------------|
| N/A                  |             4 |     0.25     |
| No                   |           218 |     0.454128 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |       20 |         23 |         23 |        21 |         7 |       10 |          11 |              51 |           166 |
| Alex     |       13 |         13 |         13 |        14 |         4 |        2 |           1 |              34 |            94 |
| Aman     |        3 |          3 |          1 |         3 |         2 |        2 |           0 |               1 |            15 |
| Andrew   |        1 |          2 |          1 |         0 |         1 |        0 |           0 |               5 |            10 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       25 |         37 |         24 |        31 |        15 |        5 |           3 |              73 |           213 |
| Daisy    |        2 |          1 |          0 |         3 |         1 |        0 |           0 |              10 |            17 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       25 |         22 |         15 |        25 |        10 |        8 |           3 |              61 |           169 |
| Jade     |        5 |          3 |          1 |         1 |         1 |        1 |           0 |               8 |            20 |
| Jai      |       12 |         10 |          8 |        13 |         9 |        4 |           1 |              35 |            92 |
| Jay      |        4 |          3 |          4 |         0 |         5 |        1 |           0 |               9 |            26 |
| Jeron    |        5 |          9 |          2 |         5 |         2 |        1 |           1 |               7 |            32 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Karthik  |        2 |          0 |          0 |         1 |         0 |        0 |           1 |               3 |             7 |
| Kate     |       21 |         19 |         11 |        16 |        14 |       12 |           2 |              80 |           175 |
| Kevin    |        0 |          0 |          1 |         3 |         1 |        0 |           0 |               0 |             5 |
| Kish     |        3 |          4 |          1 |         4 |         2 |        0 |           1 |               6 |            21 |
| Megan    |        2 |          0 |          0 |         0 |         0 |        2 |           0 |               2 |             6 |
| Minh     |        9 |          8 |         12 |         7 |         6 |        2 |           2 |              23 |            69 |
| Olivia   |        1 |          0 |          1 |         0 |         1 |        0 |           0 |               2 |             5 |
| Peter    |       26 |         22 |         24 |        20 |        10 |        8 |           3 |              60 |           173 |
| Rachel   |       20 |         20 |         10 |        13 |        10 |        0 |           3 |              58 |           134 |
| Ruhi     |        2 |          5 |          6 |         7 |         7 |        1 |           0 |              18 |            46 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Selena   |        0 |          0 |          0 |         0 |         1 |        1 |           0 |               3 |             5 |
| Sofia    |        0 |          1 |          1 |         2 |         0 |        0 |           0 |               1 |             5 |
| Sushant  |       21 |          9 |         18 |        21 |         9 |        4 |           2 |              44 |           128 |
| Tercel   |        2 |          5 |          4 |         1 |         3 |        0 |           0 |               9 |            24 |
| Vishal   |        3 |          0 |          3 |         2 |         1 |        0 |           0 |               4 |            13 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.086 |      0.101 |      0.119 |     0.093 |     0.055 |    0.143 |       0.314 |           0.079 |           166 |
| Alex     |    0.056 |      0.057 |      0.067 |     0.062 |     0.031 |    0.029 |       0.029 |           0.053 |            94 |
| Aman     |    0.013 |      0.013 |      0.005 |     0.013 |     0.016 |    0.029 |       0     |           0.002 |            15 |
| Andrew   |    0.004 |      0.009 |      0.005 |     0     |     0.008 |    0     |       0     |           0.008 |            10 |
| Anthony  |    0     |      0.009 |      0.021 |     0.018 |     0     |    0.014 |       0     |           0.002 |            12 |
| Brian    |    0.107 |      0.162 |      0.124 |     0.138 |     0.117 |    0.071 |       0.086 |           0.113 |           213 |
| Daisy    |    0.009 |      0.004 |      0     |     0.013 |     0.008 |    0     |       0     |           0.016 |            17 |
| Ewen     |    0.004 |      0.009 |      0.01  |     0.004 |     0     |    0.029 |       0     |           0.008 |            13 |
| Gathenji |    0     |      0     |      0     |     0.004 |     0     |    0     |       0     |           0.009 |             7 |
| Jackie   |    0.107 |      0.096 |      0.077 |     0.111 |     0.078 |    0.114 |       0.086 |           0.095 |           169 |
| Jade     |    0.021 |      0.013 |      0.005 |     0.004 |     0.008 |    0.014 |       0     |           0.012 |            20 |
| Jai      |    0.052 |      0.044 |      0.041 |     0.058 |     0.07  |    0.057 |       0.029 |           0.054 |            92 |
| Jay      |    0.017 |      0.013 |      0.021 |     0     |     0.039 |    0.014 |       0     |           0.014 |            26 |
| Jeron    |    0.021 |      0.039 |      0.01  |     0.022 |     0.016 |    0.014 |       0.029 |           0.011 |            32 |
| Justin   |    0.009 |      0     |      0.005 |     0.004 |     0.008 |    0     |       0     |           0.006 |             9 |
| Karthik  |    0.009 |      0     |      0     |     0.004 |     0     |    0     |       0.029 |           0.005 |             7 |
| Kate     |    0.09  |      0.083 |      0.057 |     0.071 |     0.109 |    0.171 |       0.057 |           0.124 |           175 |
| Kevin    |    0     |      0     |      0.005 |     0.013 |     0.008 |    0     |       0     |           0     |             5 |
| Kish     |    0.013 |      0.018 |      0.005 |     0.018 |     0.016 |    0     |       0.029 |           0.009 |            21 |
| Megan    |    0.009 |      0     |      0     |     0     |     0     |    0.029 |       0     |           0.003 |             6 |
| Minh     |    0.039 |      0.035 |      0.062 |     0.031 |     0.047 |    0.029 |       0.057 |           0.036 |            69 |
| Olivia   |    0.004 |      0     |      0.005 |     0     |     0.008 |    0     |       0     |           0.003 |             5 |
| Peter    |    0.112 |      0.096 |      0.124 |     0.089 |     0.078 |    0.114 |       0.086 |           0.093 |           173 |
| Rachel   |    0.086 |      0.088 |      0.052 |     0.058 |     0.078 |    0     |       0.086 |           0.09  |           134 |
| Ruhi     |    0.009 |      0.022 |      0.031 |     0.031 |     0.055 |    0.014 |       0     |           0.028 |            46 |
| Sai      |    0.004 |      0.004 |      0     |     0.004 |     0.016 |    0     |       0     |           0.005 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.008 |    0.014 |       0     |           0.005 |             5 |
| Sofia    |    0     |      0.004 |      0.005 |     0.009 |     0     |    0     |       0     |           0.002 |             5 |
| Sushant  |    0.09  |      0.039 |      0.093 |     0.093 |     0.07  |    0.057 |       0.057 |           0.068 |           128 |
| Tercel   |    0.009 |      0.022 |      0.021 |     0.004 |     0.023 |    0     |       0     |           0.014 |            24 |
| Vishal   |    0.013 |      0     |      0.015 |     0.009 |     0.008 |    0     |       0     |           0.006 |            13 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.12  |      0.139 |      0.139 |     0.127 |     0.042 |    0.06  |       0.066 |           0.307 |           166 |
| Alex     |    0.138 |      0.138 |      0.138 |     0.149 |     0.043 |    0.021 |       0.011 |           0.362 |            94 |
| Aman     |    0.2   |      0.2   |      0.067 |     0.2   |     0.133 |    0.133 |       0     |           0.067 |            15 |
| Andrew   |    0.1   |      0.2   |      0.1   |     0     |     0.1   |    0     |       0     |           0.5   |            10 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.117 |      0.174 |      0.113 |     0.146 |     0.07  |    0.023 |       0.014 |           0.343 |           213 |
| Daisy    |    0.118 |      0.059 |      0     |     0.176 |     0.059 |    0     |       0     |           0.588 |            17 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.148 |      0.13  |      0.089 |     0.148 |     0.059 |    0.047 |       0.018 |           0.361 |           169 |
| Jade     |    0.25  |      0.15  |      0.05  |     0.05  |     0.05  |    0.05  |       0     |           0.4   |            20 |
| Jai      |    0.13  |      0.109 |      0.087 |     0.141 |     0.098 |    0.043 |       0.011 |           0.38  |            92 |
| Jay      |    0.154 |      0.115 |      0.154 |     0     |     0.192 |    0.038 |       0     |           0.346 |            26 |
| Jeron    |    0.156 |      0.281 |      0.062 |     0.156 |     0.062 |    0.031 |       0.031 |           0.219 |            32 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Karthik  |    0.286 |      0     |      0     |     0.143 |     0     |    0     |       0.143 |           0.429 |             7 |
| Kate     |    0.12  |      0.109 |      0.063 |     0.091 |     0.08  |    0.069 |       0.011 |           0.457 |           175 |
| Kevin    |    0     |      0     |      0.2   |     0.6   |     0.2   |    0     |       0     |           0     |             5 |
| Kish     |    0.143 |      0.19  |      0.048 |     0.19  |     0.095 |    0     |       0.048 |           0.286 |            21 |
| Megan    |    0.333 |      0     |      0     |     0     |     0     |    0.333 |       0     |           0.333 |             6 |
| Minh     |    0.13  |      0.116 |      0.174 |     0.101 |     0.087 |    0.029 |       0.029 |           0.333 |            69 |
| Olivia   |    0.2   |      0     |      0.2   |     0     |     0.2   |    0     |       0     |           0.4   |             5 |
| Peter    |    0.15  |      0.127 |      0.139 |     0.116 |     0.058 |    0.046 |       0.017 |           0.347 |           173 |
| Rachel   |    0.149 |      0.149 |      0.075 |     0.097 |     0.075 |    0     |       0.022 |           0.433 |           134 |
| Ruhi     |    0.043 |      0.109 |      0.13  |     0.152 |     0.152 |    0.022 |       0     |           0.391 |            46 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.2   |    0.2   |       0     |           0.6   |             5 |
| Sofia    |    0     |      0.2   |      0.2   |     0.4   |     0     |    0     |       0     |           0.2   |             5 |
| Sushant  |    0.164 |      0.07  |      0.141 |     0.164 |     0.07  |    0.031 |       0.016 |           0.344 |           128 |
| Tercel   |    0.083 |      0.208 |      0.167 |     0.042 |     0.125 |    0     |       0     |           0.375 |            24 |
| Vishal   |    0.231 |      0     |      0.231 |     0.154 |     0.077 |    0     |       0     |           0.308 |            13 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     1    |   0.5  |    0.47 |    0.46 |      0.33 |   0.43 |  0.54 |     0.54 |   0.47 |      0.49 |      0.36 |   0.44 |   0.6  |   0.56 |    0.73 |     0.57 |   0.73 |    -1   |  0.72 |       0.86 | -1    |     0.4  |      0.57 |     0.44 |     -1   |    1    |  -1    |   -1    |    -1    |     0   |      0.6 |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.47 |   0.17 |    1    |    0.52 |      0.43 |   0.42 |  0.51 |     0.45 |   0.42 |      0.49 |      0.45 |   0.48 |   0.55 |   0.45 |    0.45 |     0.78 |   0.53 |    -1   |  0.65 |      -1    |  0.29 |     0.55 |     -1    |    -1    |     -1   |    0.44 |   0.33 |    0.5  |     0.67 |    -1   |     -1   |
| Brian    |     0.46 |   0.83 |    0.52 |    1    |      0.25 |   0.42 |  0.54 |     0.41 |   0.51 |      0.42 |      0.51 |   0.29 |   0.38 |   0.46 |    0.5  |     0.44 |   0.6  |     0.2 |  0.3  |       0.5  |  0.62 |     0.55 |      0.43 |     0.54 |      0.6 |    0.08 |   0.53 |    0.5  |     0.6  |    -1   |     -1   |
| Anthony  |     0.33 |  -1    |    0.43 |    0.25 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.43 |   0.4  |    0.42 |    0.42 |      0.5  |   1    |  0.46 |     0.46 |   0.46 |      0.64 |      0.5  |   0.5  |   0.67 |   0.32 |    0.29 |    -1    |   0.12 |    -1   |  0.33 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.75 |   0.33 |   -1    |     0.71 |     0.2 |      0.4 |
| Jai      |     0.54 |   0.4  |    0.51 |    0.54 |      0.29 |   0.46 |  1    |     0.46 |   0.57 |      0.35 |      0.41 |   0.25 |  -1    |   0.51 |    0.5  |    -1    |   0.4  |    -1   |  0.23 |       0.8  | -1    |     0.56 |      0.67 |     0    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jackie   |     0.54 |   0.33 |    0.45 |    0.41 |      0.17 |   0.46 |  0.46 |     1    |   0.54 |      0.43 |      0.38 |   0.45 |   0.38 |   0.58 |    0.57 |    -1    |   0.43 |     0.6 |  0.6  |      -1    |  0.4  |     0.33 |      0.57 |     0.38 |     -1   |    0.79 |   0.54 |   -1    |     0.33 |    -1   |     -1   |
| Kate     |     0.47 |   0.45 |    0.42 |    0.51 |      0.33 |   0.46 |  0.57 |     0.54 |   1    |      0.42 |      0.51 |   0.45 |   0.33 |   0.45 |    0.64 |     0.83 |   0.43 |    -1   |  0.4  |       0.57 |  0.5  |     0.41 |     -1    |     0.57 |      0.2 |    0.53 |   0.27 |    0.67 |     0.7  |     0.6 |      0.4 |
| Sushant  |     0.49 |   0.43 |    0.49 |    0.42 |     -1    |   0.64 |  0.35 |     0.43 |   0.42 |      1    |      0.48 |   0.48 |   0.55 |   0.44 |    0.29 |     0.17 |   0.5  |    -1   |  0.45 |       0.5  |  0.38 |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Abishek  |     0.36 |   0.56 |    0.45 |    0.51 |      0.2  |   0.5  |  0.41 |     0.38 |   0.51 |      0.48 |      1    |   0.44 |   0.5  |   0.43 |    0.21 |     0.38 |   0.56 |    -1   |  0.46 |       0.29 |  0.62 |    -1    |      0.14 |     0.54 |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Ruhi     |     0.44 |  -1    |    0.48 |    0.29 |     -1    |   0.5  |  0.25 |     0.45 |   0.45 |      0.48 |      0.44 |   1    |   0.71 |   0.53 |    0.44 |    -1    |  -1    |    -1   |  0.57 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.8  |  -1    |   -1    |    -1    |    -1   |     -1   |
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
| Daisy    |     1    |  -1    |    0.44 |    0.08 |     -1    |   0.75 | -1    |     0.79 |   0.53 |     -1    |     -1    |   0.8  |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.38 |     -1    |    -1    |      0.4 |    1    |   0.33 |   -1    |     0.43 |     0   |      0.6 |
| Aman     |    -1    |  -1    |    0.33 |    0.53 |     -1    |   0.33 | -1    |     0.54 |   0.27 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.71 |     -1    |    -1    |     -1   |    0.33 |   1    |   -1    |     0    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.67 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.33 |     -1    |    -1    |     -1   |   -1    |  -1    |    1    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.67 |    0.6  |     -1    |   0.71 | -1    |     0.33 |   0.7  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.43 |   0    |   -1    |     1    |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |     1   |      0.4 |
| Selena   |     0.6  |  -1    |   -1    |   -1    |     -1    |   0.4  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.6  |  -1    |   -1    |    -1    |     0.4 |      1   |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |    -1    |   0.25 |    0.08 |    0.04 |      0.17 |   0.09 |  0.1  |     0.09 |   0.06 |      0.09 |      0.07 |   0.07 |   0.13 |   0.12 |    0.05 |     0    |   0.13 |    -1   |  0.11 |       0.14 | -1    |     0    |      0    |     0.11 |     -1   |    0    |  -1    |   -1    |    -1    |     0   |      0   |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.08 |   0    |   -1    |    0.13 |      0.29 |   0.13 |  0.14 |     0.07 |   0.06 |      0.15 |      0.16 |   0.16 |   0    |   0.06 |    0.09 |     0.11 |   0.13 |    -1   |  0.25 |      -1    |  0    |     0.05 |     -1    |    -1    |     -1   |    0    |   0.08 |    0.17 |     0    |    -1   |     -1   |
| Brian    |     0.04 |   0.25 |    0.13 |   -1    |      0.25 |   0.11 |  0.09 |     0.07 |   0.1  |      0.09 |      0.17 |   0.02 |   0.14 |   0.07 |    0.07 |     0    |   0    |     0.2 |  0.05 |       0    |  0.12 |     0.14 |      0    |     0.23 |      0.4 |    0    |   0.33 |    0.33 |     0.1  |    -1   |     -1   |
| Anthony  |     0.17 |  -1    |    0.29 |    0.25 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.09 |   0.2  |    0.13 |    0.11 |      0.33 |  -1    |  0.08 |     0.09 |   0.12 |      0.21 |      0.1  |   0.14 |   0.33 |   0.08 |    0.14 |    -1    |   0    |    -1   |  0.17 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.17 |   0.17 |   -1    |     0.14 |     0.2 |      0   |
| Jai      |     0.1  |   0    |    0.14 |    0.09 |      0.29 |   0.08 | -1    |     0.07 |   0.13 |      0.12 |      0.12 |   0.15 |  -1    |   0.15 |    0.08 |    -1    |   0    |    -1   |  0.08 |       0    | -1    |     0.22 |      0    |     0    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jackie   |     0.09 |   0    |    0.07 |    0.07 |      0    |   0.09 |  0.07 |    -1    |   0.1  |      0.08 |      0.09 |   0.09 |   0.25 |   0.13 |    0.17 |    -1    |   0.07 |     0.2 |  0.13 |      -1    |  0.2  |     0.06 |      0.29 |     0.23 |     -1   |    0.29 |   0.15 |   -1    |     0    |    -1   |     -1   |
| Kate     |     0.06 |   0.09 |    0.06 |    0.1  |      0.11 |   0.12 |  0.13 |     0.1  |  -1    |      0.09 |      0.12 |   0.08 |   0    |   0.09 |    0.14 |     0.33 |   0.07 |    -1   |  0.04 |       0    |  0.12 |     0    |     -1    |     0    |      0   |    0.06 |   0.07 |    0.17 |     0    |     0.6 |      0.2 |
| Sushant  |     0.09 |   0.14 |    0.15 |    0.09 |     -1    |   0.21 |  0.12 |     0.08 |   0.09 |     -1    |      0.18 |   0.18 |   0    |   0.1  |    0    |     0    |   0.1  |    -1   |  0.14 |       0    |  0.12 |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Abishek  |     0.07 |   0.11 |    0.16 |    0.17 |      0    |   0.1  |  0.12 |     0.09 |   0.12 |      0.18 |     -1    |   0.17 |   0.14 |   0.11 |    0    |     0.25 |   0    |    -1   |  0.08 |       0    |  0.12 |    -1    |      0    |     0.23 |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Ruhi     |     0.07 |  -1    |    0.16 |    0.02 |     -1    |   0.14 |  0.15 |     0.09 |   0.08 |      0.18 |      0.17 |  -1    |   0.14 |   0.35 |    0.11 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.2  |  -1    |   -1    |    -1    |    -1   |     -1   |
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
| Daisy    |     0    |  -1    |    0    |    0    |     -1    |   0.17 | -1    |     0.29 |   0.06 |     -1    |     -1    |   0.2  |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |      0   |   -1    |   0.11 |   -1    |     0    |     0   |      0   |
| Aman     |    -1    |  -1    |    0.08 |    0.33 |     -1    |   0.17 | -1    |     0.15 |   0.07 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.29 |     -1    |    -1    |     -1   |    0.11 |  -1    |   -1    |     0    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.17 |    0.33 |     -1    |  -1    | -1    |    -1    |   0.17 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0    |    0.1  |     -1    |   0.14 | -1    |     0    |   0    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |   0    |   -1    |    -1    |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |    -1   |      0.4 |
| Selena   |     0    |  -1    |   -1    |   -1    |     -1    |   0    | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |    -1    |     0.4 |     -1   |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     0    |   0.5  |    0.53 |    0.54 |      0.67 |   0.57 |  0.46 |     0.46 |   0.53 |      0.51 |      0.64 |   0.56 |   0.4  |   0.44 |    0.27 |     0.43 |   0.27 |    -1   |  0.28 |       0.14 | -1    |     0.6  |      0.43 |     0.56 |     -1   |    0    |  -1    |   -1    |    -1    |     1   |      0.4 |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Peter    |     0.53 |   0.83 |    0    |    0.48 |      0.57 |   0.58 |  0.49 |     0.55 |   0.58 |      0.51 |      0.55 |   0.52 |   0.45 |   0.55 |    0.55 |     0.22 |   0.47 |    -1   |  0.35 |      -1    |  0.71 |     0.45 |     -1    |    -1    |     -1   |    0.56 |   0.67 |    0.5  |     0.33 |    -1   |     -1   |
| Brian    |     0.54 |   0.17 |    0.48 |    0    |      0.75 |   0.58 |  0.46 |     0.59 |   0.49 |      0.58 |      0.49 |   0.71 |   0.62 |   0.54 |    0.5  |     0.56 |   0.4  |     0.8 |  0.7  |       0.5  |  0.38 |     0.45 |      0.57 |     0.46 |      0.4 |    0.92 |   0.47 |    0.5  |     0.4  |    -1   |     -1   |
| Anthony  |     0.67 |  -1    |    0.57 |    0.75 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Minh     |     0.57 |   0.6  |    0.58 |    0.58 |      0.5  |   0    |  0.54 |     0.54 |   0.54 |      0.36 |      0.5  |   0.5  |   0.33 |   0.68 |    0.71 |    -1    |   0.88 |    -1   |  0.67 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.25 |   0.67 |   -1    |     0.29 |     0.8 |      0.6 |
| Jai      |     0.46 |   0.6  |    0.49 |    0.46 |      0.71 |   0.54 |  0    |     0.54 |   0.43 |      0.65 |      0.59 |   0.75 |  -1    |   0.49 |    0.5  |    -1    |   0.6  |    -1   |  0.77 |       0.2  | -1    |     0.44 |      0.33 |     1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Jackie   |     0.46 |   0.67 |    0.55 |    0.59 |      0.83 |   0.54 |  0.54 |     0    |   0.46 |      0.57 |      0.62 |   0.55 |   0.62 |   0.42 |    0.43 |    -1    |   0.57 |     0.4 |  0.4  |      -1    |  0.6  |     0.67 |      0.43 |     0.62 |     -1   |    0.21 |   0.46 |   -1    |     0.67 |    -1   |     -1   |
| Kate     |     0.53 |   0.55 |    0.58 |    0.49 |      0.67 |   0.54 |  0.43 |     0.46 |   0    |      0.58 |      0.49 |   0.55 |   0.67 |   0.55 |    0.36 |     0.17 |   0.57 |    -1   |  0.6  |       0.43 |  0.5  |     0.59 |     -1    |     0.43 |      0.8 |    0.47 |   0.73 |    0.33 |     0.3  |     0.4 |      0.6 |
| Sushant  |     0.51 |   0.57 |    0.51 |    0.58 |     -1    |   0.36 |  0.65 |     0.57 |   0.58 |      0    |      0.52 |   0.52 |   0.45 |   0.56 |    0.71 |     0.83 |   0.5  |    -1   |  0.55 |       0.5  |  0.62 |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Abishek  |     0.64 |   0.44 |    0.55 |    0.49 |      0.8  |   0.5  |  0.59 |     0.62 |   0.49 |      0.52 |      0    |   0.56 |   0.5  |   0.57 |    0.79 |     0.62 |   0.44 |    -1   |  0.54 |       0.71 |  0.38 |    -1    |      0.86 |     0.46 |     -1   |   -1    |  -1    |   -1    |    -1    |    -1   |     -1   |
| Ruhi     |     0.56 |  -1    |    0.52 |    0.71 |     -1    |   0.5  |  0.75 |     0.55 |   0.55 |      0.52 |      0.56 |   0    |   0.29 |   0.47 |    0.56 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.2  |  -1    |   -1    |    -1    |    -1   |     -1   |
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
| Daisy    |     0    |  -1    |    0.56 |    0.92 |     -1    |   0.25 | -1    |     0.21 |   0.47 |     -1    |     -1    |   0.2  |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.62 |     -1    |    -1    |      0.6 |    0    |   0.67 |   -1    |     0.57 |     1   |      0.4 |
| Aman     |    -1    |  -1    |    0.67 |    0.47 |     -1    |   0.67 | -1    |     0.46 |   0.73 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.29 |     -1    |    -1    |     -1   |    0.67 |   0    |   -1    |     1    |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.33 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.67 |     -1    |    -1    |     -1   |   -1    |  -1    |    0    |    -1    |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.33 |    0.4  |     -1    |   0.29 | -1    |     0.67 |   0.3  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.57 |   1    |   -1    |     0    |    -1   |     -1   |
| Kevin    |     1    |  -1    |   -1    |   -1    |     -1    |   0.8  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    1    |  -1    |   -1    |    -1    |     0   |      0.6 |
| Selena   |     0.4  |  -1    |   -1    |   -1    |     -1    |   0.6  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.4  |  -1    |   -1    |    -1    |     0.6 |      0   |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Abishe |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|---------|----------|
| Rachel   |      134 |      4 |      44 |      51 |         4 |     19 |    37 |       52 |     45 |        38 |        36 |     12 |      9 |     29 |          1 |        1 |        0 |      16 |        0 |        4 |     11 |       1 |    13 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |        2 |         4 |        4 |        0 |       0 |       5 |      1 |       0 |        1 |       0 |        3 |    0 |        1 |        1 |         0 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Peter    |       44 |      1 |     173 |      82 |         3 |     19 |    36 |       60 |     53 |        49 |        52 |     12 |      6 |     35 |          1 |        1 |        0 |      10 |        0 |        7 |      8 |       0 |    13 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |       11 |         0 |        0 |        0 |       1 |       4 |      4 |       3 |        6 |       0 |        0 |    0 |        0 |        1 |         1 |
| Brian    |       51 |     10 |      82 |     213 |         3 |     24 |    43 |       62 |     79 |        48 |        76 |     12 |      8 |     37 |          1 |        1 |        0 |      14 |        0 |        4 |      9 |       1 |     6 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |       12 |         3 |        7 |        3 |       1 |       1 |      8 |       3 |        6 |       0 |        0 |    0 |        0 |        1 |         1 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Minh     |       19 |      2 |      19 |      24 |         3 |     69 |    11 |       25 |     27 |        21 |        25 |      7 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      1 |       2 |     2 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       9 |      2 |       0 |        5 |       1 |        2 |    0 |        1 |        0 |         0 |
| Jai      |       37 |      2 |      36 |      43 |         2 |     11 |    92 |       32 |     40 |        17 |        24 |      5 |      2 |     20 |          0 |        0 |        0 |       6 |        0 |        0 |      4 |       0 |     3 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         4 |        0 |        0 |       0 |       1 |      2 |       0 |        2 |       2 |        1 |    1 |        0 |        1 |         0 |
| Jackie   |       52 |      2 |      60 |      62 |         1 |     25 |    32 |      169 |     67 |        37 |        45 |     10 |      3 |     36 |          0 |        0 |        1 |      13 |        1 |        1 |      6 |       3 |     9 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       1 |        6 |         4 |        5 |        1 |       2 |      11 |      7 |       1 |        3 |       2 |        0 |    0 |        0 |        0 |         1 |
| Kate     |       45 |      5 |      53 |      79 |         3 |     27 |    40 |       67 |    175 |        41 |        64 |     17 |      5 |     30 |          0 |        0 |        0 |       9 |        0 |        5 |      6 |       1 |    10 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |        7 |         1 |        4 |        1 |       2 |       9 |      4 |       4 |        7 |       3 |        2 |    1 |        1 |        1 |         1 |
| Sushant  |       38 |      3 |      49 |      48 |         0 |     21 |    17 |       37 |     41 |       128 |        56 |     16 |      6 |     30 |          2 |        0 |        0 |       5 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       2 |      1 |       0 |        0 |       0 |        1 |    0 |        1 |        0 |         0 |
| Abishek  |       36 |      5 |      52 |      76 |         1 |     25 |    24 |       45 |     64 |        56 |       166 |     16 |      7 |     33 |          0 |        0 |        0 |       4 |        0 |        3 |      9 |       1 |    11 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |        2 |         1 |        7 |        0 |       0 |       2 |      1 |       0 |        2 |       0 |        0 |    0 |        0 |        3 |         0 |
| Ruhi     |       12 |      2 |      12 |      12 |         2 |      7 |     5 |       10 |     17 |        16 |        16 |     46 |      5 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       4 |      0 |       0 |        1 |       1 |        4 |    0 |        0 |        0 |         1 |
| Kish     |        9 |      0 |       6 |       8 |         2 |      4 |     2 |        3 |      5 |         6 |         7 |      5 |     21 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Alex     |       29 |      1 |      35 |      37 |         0 |      8 |    20 |       36 |     30 |        30 |        33 |      9 |      2 |     94 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       2 |     5 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jeron    |       16 |      0 |      10 |      14 |         3 |      2 |     6 |       13 |      9 |         5 |         4 |      4 |      1 |      4 |          0 |        0 |        1 |      32 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        1 |         0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jade     |       11 |      2 |       8 |       9 |         0 |      1 |     4 |        6 |      6 |         5 |         9 |      2 |      0 |      1 |          0 |        1 |        0 |       1 |        0 |        1 |     20 |       0 |     3 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        1 |         0 |
| Sofia    |        1 |      0 |       0 |       1 |         0 |      2 |     0 |        3 |      1 |         1 |         1 |      0 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       5 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jay      |       13 |      1 |      13 |       6 |         0 |      2 |     3 |        9 |     10 |        10 |        11 |      4 |      1 |      5 |          0 |        0 |        0 |       2 |        0 |        0 |      3 |       0 |    26 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Derek    |        1 |      0 |       2 |       3 |         0 |      0 |     0 |        1 |      1 |         3 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       4 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Gathenji |        6 |      0 |       1 |       3 |         0 |      0 |     4 |        2 |      4 |         3 |         2 |      2 |      1 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          7 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      2 |         1 |         1 |      2 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      3 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sai      |        2 |      1 |       2 |       5 |         0 |      2 |     2 |        2 |      4 |         3 |         5 |      0 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     8 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Nabeel   |        0 |      1 |       2 |       1 |         0 |      0 |     0 |        2 |      3 |         0 |         2 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        4 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ronnie   |        1 |      0 |       2 |       0 |         0 |      1 |     0 |        2 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        2 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Neha     |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Kawin    |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Abrar    |        1 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       2 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Tercel   |        2 |      0 |      11 |      12 |         0 |      2 |     5 |        6 |      7 |         4 |         2 |      0 |      0 |      3 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       24 |         0 |        0 |        3 |       2 |       3 |      5 |       2 |        3 |       0 |        0 |    0 |        0 |        0 |         1 |
| Karthik  |        4 |      0 |       0 |       3 |         0 |      0 |     4 |        4 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         7 |        2 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Vishal   |        4 |      0 |       0 |       7 |         0 |      0 |     0 |        5 |      4 |         0 |         7 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         2 |       13 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Olivia   |        0 |      0 |       0 |       3 |         0 |      0 |     0 |        1 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        5 |       3 |       2 |      4 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| AlexY    |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        2 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        3 |       4 |       3 |      2 |       1 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Daisy    |        5 |      0 |       4 |       1 |         0 |      9 |     1 |       11 |      9 |         2 |         2 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        2 |       3 |      17 |      3 |       1 |        3 |       0 |        3 |    0 |        1 |        0 |         1 |
| Aman     |        1 |      0 |       4 |       8 |         0 |      2 |     2 |        7 |      4 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         0 |        0 |        4 |       2 |       3 |     15 |       1 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       1 |      1 |       6 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Andrew   |        1 |      0 |       6 |       6 |         0 |      5 |     2 |        3 |      7 |         0 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        0 |       0 |       3 |      0 |       0 |       10 |       0 |        0 |    0 |        0 |        0 |         1 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       5 |        2 |    1 |        0 |        0 |         0 |
| Selena   |        3 |      0 |       0 |       0 |         0 |      2 |     1 |        0 |      2 |         1 |         0 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       3 |      0 |       0 |        0 |       2 |        5 |    0 |        0 |        0 |         0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |    1 |        0 |        0 |         0 |
| Abishe   |        1 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        0 |    0 |        1 |        0 |         0 |
| Claire   |        1 |      0 |       1 |       1 |         0 |      0 |     1 |        0 |      1 |         0 |         3 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        3 |         0 |
| Timothy  |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        1 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |        0 |         2 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Abishe |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|---------|----------|
| Rachel   |       -1 |      2 |       7 |       4 |         2 |      4 |     7 |        9 |      6 |         7 |         7 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      2 |       0 |     2 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        1 |        0 |       0 |       0 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Peter    |        7 |      0 |      -1 |      20 |         2 |      6 |    10 |        9 |      7 |        15 |        19 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     5 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      1 |       1 |        0 |       0 |        0 |    0 |        0 |        1 |         0 |
| Brian    |        4 |      3 |      20 |      -1 |         3 |      6 |     7 |       11 |     15 |        10 |        25 |      1 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |        3 |         0 |        3 |        2 |       0 |       0 |      5 |       2 |        1 |       0 |        0 |    0 |        0 |        1 |         0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Minh     |        4 |      1 |       6 |       6 |         2 |     -1 |     2 |        5 |      7 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      1 |       0 |        1 |       1 |        0 |    0 |        0 |        0 |         0 |
| Jai      |        7 |      0 |      10 |       7 |         2 |      2 |    -1 |        5 |      9 |         6 |         7 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        1 |       2 |        1 |    1 |        0 |        0 |         0 |
| Jackie   |        9 |      0 |       9 |      11 |         0 |      5 |     5 |       -1 |     12 |         7 |        11 |      2 |      2 |      8 |          0 |        0 |        1 |       4 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |        1 |         2 |        3 |        0 |       0 |       4 |      2 |       0 |        0 |       2 |        0 |    0 |        0 |        0 |         1 |
| Kate     |        6 |      1 |       7 |      15 |         1 |      7 |     9 |       12 |     -1 |         9 |        15 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      1 |       1 |        0 |       3 |        1 |    1 |        0 |        1 |         0 |
| Sushant  |        7 |      1 |      15 |      10 |         0 |      7 |     6 |        7 |      9 |        -1 |        21 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Abishek  |        7 |      1 |      19 |      25 |         0 |      5 |     7 |       11 |     15 |        21 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       1 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        3 |        0 |       0 |       0 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |        2 |         0 |
| Ruhi     |        2 |      1 |       4 |       1 |         1 |      2 |     3 |        2 |      3 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       1 |        1 |    0 |        0 |        0 |         1 |
| Kish     |        2 |      0 |       0 |       3 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     6 |        8 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jeron    |        1 |      0 |       2 |       2 |         2 |      1 |     1 |        4 |      2 |         0 |         0 |      1 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jade     |        2 |      0 |       2 |       0 |         0 |      0 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sofia    |        0 |      0 |       0 |       1 |         0 |      1 |     0 |        1 |      0 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |      -1 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jay      |        2 |      0 |       5 |       1 |         0 |      1 |     1 |        2 |      1 |         3 |         2 |      3 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |    -1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Greg     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |     -1 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Gathenji |        1 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |         -1 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        1 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |     -1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sai      |        1 |      0 |       0 |       1 |         0 |      0 |     1 |        1 |      1 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |    -1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Nabeel   |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |       -1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ronnie   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |       -1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Neha     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |     -1 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |    -1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Kawin    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |      -1 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |      -1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Tercel   |        0 |      0 |       1 |       3 |         0 |      0 |     2 |        1 |      0 |         2 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       -1 |         0 |        0 |        1 |       0 |       0 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Karthik  |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        2 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |        -1 |        1 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Vishal   |        1 |      0 |       0 |       3 |         0 |      0 |     0 |        3 |      0 |         0 |         3 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         1 |       -1 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Olivia   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |       -1 |       0 |       0 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| AlexY    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |      -1 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Daisy    |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        4 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |      -1 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         1 |
| Aman     |        0 |      0 |       1 |       5 |         0 |      1 |     0 |        2 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        2 |       0 |       1 |     -1 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Megan    |        0 |      0 |       1 |       2 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |      -1 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Andrew   |        1 |      0 |       0 |       1 |         0 |      1 |     1 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |       -1 |       0 |        0 |    0 |        0 |        0 |         0 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |      -1 |        2 |    1 |        0 |        0 |         0 |
| Selena   |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       2 |       -1 |    0 |        0 |        0 |         0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |   -1 |        0 |        0 |         0 |
| Abishe   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |       -1 |        0 |         0 |
| Claire   |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |       -1 |         0 |
| Timothy  |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |        -1 |

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Abishe |   Claire |   Timothy |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|---------|----------|
| Rachel   |        0 |      4 |      49 |      60 |         8 |     25 |    31 |       44 |     50 |        39 |        65 |     15 |      6 |     23 |          1 |        0 |        1 |       6 |        1 |        3 |      4 |       3 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |        3 |         3 |        5 |        0 |       0 |       0 |      1 |       0 |        0 |       5 |        2 |    1 |        0 |        1 |         0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Peter    |       49 |      5 |       0 |      77 |         4 |     26 |    35 |       72 |     73 |        52 |        64 |     13 |      5 |     42 |          1 |        0 |        1 |      12 |        1 |        2 |      7 |       3 |     7 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       1 |        9 |         0 |        0 |        2 |       1 |       5 |      8 |       3 |        3 |       0 |        0 |    0 |        0 |        0 |         1 |
| Brian    |       60 |      2 |      77 |       0 |         9 |     33 |    36 |       90 |     76 |        66 |        74 |     29 |     13 |     44 |          1 |        0 |        1 |      14 |        1 |        5 |      6 |       4 |    14 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       1 |       10 |         4 |        6 |        2 |       3 |      11 |      7 |       3 |        4 |       0 |        0 |    0 |        0 |        1 |         1 |
| Anthony  |        8 |      0 |       4 |       9 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Minh     |       25 |      3 |      26 |      33 |         3 |      0 |    13 |       29 |     32 |        12 |        25 |      7 |      2 |     17 |          0 |        0 |        0 |       5 |        0 |        2 |      7 |       0 |     4 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |        1 |         0 |        0 |        0 |       0 |       3 |      4 |       0 |        2 |       4 |        3 |    1 |        0 |        3 |         2 |
| Jai      |       31 |      3 |      35 |      36 |         5 |     13 |     0 |       38 |     30 |        31 |        35 |     15 |      2 |     19 |          1 |        0 |        0 |       6 |        0 |        2 |      6 |       0 |    10 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       2 |        4 |         2 |        6 |        0 |       0 |       3 |      2 |       0 |        1 |       0 |        1 |    0 |        1 |        2 |         0 |
| Jackie   |       44 |      4 |      72 |      90 |         5 |     29 |    38 |        0 |     57 |        49 |        72 |     12 |      5 |     26 |          0 |        1 |        0 |      10 |        0 |        2 |      8 |       2 |     6 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |       12 |         3 |        8 |        3 |       1 |       3 |      6 |       1 |        6 |       1 |        3 |    0 |        0 |        3 |         1 |
| Kate     |       50 |      6 |      73 |      76 |         6 |     32 |    30 |       57 |      0 |        57 |        62 |     21 |     10 |     36 |          2 |        0 |        0 |       5 |        0 |        1 |      8 |       1 |    15 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |       10 |         0 |        3 |        4 |       2 |       8 |     11 |       2 |        3 |       2 |        3 |    0 |        0 |        2 |         1 |
| Sushant  |       39 |      4 |      52 |      66 |         1 |     12 |    31 |       49 |     57 |         0 |        60 |     17 |      5 |     38 |          0 |        0 |        0 |      12 |        0 |        5 |      5 |       3 |    12 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       2 |        1 |    1 |        0 |        1 |         0 |
| Abishek  |       65 |      4 |      64 |      74 |         4 |     25 |    35 |       72 |     62 |        60 |         0 |     20 |      7 |     43 |          0 |        0 |        0 |      15 |        0 |        5 |      7 |       3 |    13 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |        2 |         6 |        6 |        0 |       0 |       2 |      3 |       0 |        1 |       1 |        1 |    0 |        0 |        0 |         0 |
| Ruhi     |       15 |      1 |      13 |      29 |         1 |      7 |    15 |       12 |     21 |        17 |        20 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      1 |       0 |        1 |       3 |        0 |    1 |        1 |        0 |         0 |
| Kish     |        6 |      5 |       5 |      13 |         2 |      2 |     2 |        5 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       4 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Alex     |       23 |      4 |      42 |      44 |         0 |     17 |    19 |       26 |     36 |        38 |        43 |      8 |      1 |      0 |          1 |        0 |        0 |       6 |        0 |        2 |      4 |       1 |     6 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |        5 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jeron    |        6 |      1 |      12 |      14 |         3 |      5 |     6 |       10 |      5 |        12 |        15 |      5 |      4 |      6 |          0 |        1 |        0 |       0 |        0 |        1 |      3 |       1 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jade     |        4 |      0 |       7 |       6 |         0 |      7 |     6 |        8 |      8 |         5 |         7 |      2 |      0 |      4 |          0 |        0 |        1 |       3 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sofia    |        3 |      0 |       3 |       4 |         0 |      0 |     0 |        2 |      1 |         3 |         3 |      0 |      0 |      1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Jay      |        5 |      1 |       7 |      14 |         0 |      4 |    10 |        6 |     15 |        12 |        13 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Derek    |        3 |      0 |       2 |       1 |         0 |      0 |     2 |        1 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Gathenji |        1 |      0 |       3 |       3 |         0 |      0 |     1 |        2 |      3 |         3 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Caro     |        1 |      0 |       0 |       3 |         0 |      1 |     0 |        1 |      1 |         2 |         2 |      1 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Sai      |        1 |      0 |       5 |       3 |         0 |      2 |     1 |        3 |      4 |         5 |         3 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Nabeel   |        2 |      3 |       0 |       3 |         0 |      0 |     1 |        2 |      1 |         0 |         2 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ronnie   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      1 |         1 |         2 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Neha     |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Ira      |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      1 |     0 |       1 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Kawin    |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Abrar    |        0 |      0 |       1 |       1 |         0 |      0 |     2 |        1 |      0 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Tercel   |        3 |      0 |       9 |      10 |         0 |      1 |     4 |       12 |     10 |         0 |         2 |      1 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     4 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        2 |       2 |       5 |      2 |       4 |        1 |       0 |        0 |    0 |        0 |        0 |         1 |
| Karthik  |        3 |      0 |       0 |       4 |         0 |      0 |     2 |        3 |      0 |         0 |         6 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        5 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Vishal   |        5 |      0 |       0 |       6 |         0 |      0 |     6 |        8 |      3 |         0 |         6 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         5 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Olivia   |        0 |      0 |       2 |       2 |         0 |      0 |     0 |        3 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       3 |      0 |       2 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| AlexY    |        0 |      0 |       1 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        1 |       0 |       1 |      1 |       1 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Daisy    |        0 |      0 |       5 |      11 |         0 |      3 |     3 |        3 |      8 |         0 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         0 |        0 |        3 |       1 |       0 |      6 |       1 |        4 |       5 |        2 |    1 |        0 |        0 |         1 |
| Aman     |        1 |      0 |       8 |       7 |         0 |      4 |     2 |        6 |     11 |         0 |         3 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       6 |      0 |       2 |        8 |       0 |        0 |    0 |        0 |        1 |         0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        2 |       1 |       1 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Andrew   |        0 |      0 |       3 |       4 |         0 |      2 |     1 |        6 |      3 |         0 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       4 |      8 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         1 |
| Kevin    |        5 |      0 |       0 |       0 |         0 |      4 |     0 |        1 |      2 |         2 |         1 |      3 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       5 |      0 |       0 |        0 |       0 |        3 |    0 |        1 |        0 |         0 |
| Selena   |        2 |      0 |       0 |       0 |         0 |      3 |     1 |        3 |      3 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      0 |       0 |        0 |       3 |        0 |    1 |        1 |        0 |         0 |
| NA       |        1 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      0 |         1 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        1 |    0 |        0 |        0 |         0 |
| Abishe   |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        1 |    0 |        0 |        0 |         0 |
| Claire   |        1 |      0 |       0 |       1 |         0 |      3 |     2 |        3 |      2 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |        0 |         0 |
| Timothy  |        0 |      0 |       1 |       1 |         0 |      2 |     0 |        1 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |        0 |         0 |

### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |   Andrew |   Daisy |
|---------|---------|-------|--------|--------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|------|---------|--------|
| Rachel   |    -1    |   -1   |    0.28 |    0.47 |   0.44 |  0.23 |     0.42 |   0.4  |      0.37 |      0.57 |   0.14 |   0.43 |   0.38 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1   |    -1    |   -1    |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Peter    |     0.28 |   -1   |   -1    |    0.53 |   0.5  |  0.33 |     0.42 |   0.52 |      0.41 |      0.61 |   0.4  |   0.2  |   0.3  |   -1    |     0.14 |    0.2 |  0.5  |      -1    |  -1   |     0.67 |   -1    |
| Brian    |     0.47 |    0.5 |    0.53 |   -1    |   0.44 |  0.43 |     0.45 |   0.59 |      0.5  |      0.62 |   0.58 |   0.83 |   0.54 |    0.5  |    -1    |    0.5 | -1    |      -1    |   0.2 |     0.67 |   -1    |
| Minh     |     0.44 |   -1   |    0.5  |    0.44 |  -1    |  0    |     0.31 |   0.56 |      0.38 |      0.43 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |     0.6  |    0.4  |
| Jai      |     0.23 |   -1   |    0.33 |    0.43 |   0    | -1    |     0.08 |   0.36 |      0.31 |      0.56 |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Jackie   |     0.42 |   -1   |    0.42 |    0.45 |   0.31 |  0.08 |    -1    |   0.5  |      0.46 |      0.5  |   0.14 |  -1    |   0.5  |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |    0.33 |
| Kate     |     0.4  |    0.6 |    0.52 |    0.59 |   0.56 |  0.36 |     0.5  |  -1    |      0.42 |      0.61 |   0.33 |  -1    |   0.58 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |     0.71 |   -1    |
| Sushant  |     0.37 |   -1   |    0.41 |    0.5  |   0.38 |  0.31 |     0.46 |   0.42 |     -1    |      0.56 |   0.43 |   0.4  |   0.44 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1   |    -1    |   -1    |
| Abishek  |     0.57 |    0.4 |    0.61 |    0.62 |   0.43 |  0.56 |     0.5  |   0.61 |      0.56 |     -1    |   0.53 |   0.83 |   0.55 |   -1    |    -1    |    0.5 |  0.57 |      -1    |   0.2 |    -1    |   -1    |
| Ruhi     |     0.14 |   -1   |    0.4  |    0.58 |   0.2  | -1    |     0.14 |   0.33 |      0.43 |      0.53 |  -1    |  -1    |   0.56 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Alex     |     0.38 |   -1   |    0.3  |    0.54 |   0.4  |  0.33 |     0.5  |   0.58 |      0.44 |      0.55 |   0.56 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Jade     |    -1    |   -1   |    0.2  |    0.5  |  -1    | -1    |    -1    |  -1    |     -1    |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Andrew   |    -1    |   -1   |    0.67 |    0.67 |   0.6  | -1    |    -1    |   0.71 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |
| Daisy    |    -1    |   -1   |   -1    |   -1    |   0.4  | -1    |     0.33 |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |    -1    |   -1    |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Andrew |   Daisy |
|---------|---------|-------|--------|--------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|---------|--------|
| Rachel   |    -1    |   -1   |    0.28 |    0.44 |   0.44 |  0.25 |     0.42 |   0.38 |      0.38 |      0.55 |   0    |   0.33 |   0.41 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |    -1    |    -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Peter    |     0.28 |   -1   |   -1    |    0.51 |   0.38 |  0.29 |     0.39 |   0.44 |      0.38 |      0.57 |   0.4  |  -1    |   0.27 |   -1    |     0.14 |    0.2 |  0.5  |      -1    |     0.6  |    -1   |
| Brian    |     0.44 |    0.5 |    0.51 |   -1    |   0.4  |  0.4  |     0.44 |   0.57 |      0.49 |      0.61 |   0.5  |  -1    |   0.52 |    0.5  |    -1    |    0.5 | -1    |      -1    |     0.67 |    -1   |
| Minh     |     0.44 |   -1   |    0.38 |    0.4  |  -1    |  0    |     0.15 |   0.47 |      0.29 |      0.4  |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Jai      |     0.25 |   -1   |    0.29 |    0.4  |   0    | -1    |     0.08 |   0.36 |      0.31 |      0.53 |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Jackie   |     0.42 |   -1   |    0.39 |    0.44 |   0.15 |  0.08 |    -1    |   0.44 |      0.41 |      0.48 |   0.14 |  -1    |   0.47 |    0.33 |    -1    |   -1   | -1    |      -1    |    -1    |     0.2 |
| Kate     |     0.38 |    0.6 |    0.44 |    0.57 |   0.47 |  0.36 |     0.44 |  -1    |      0.36 |      0.57 |   0.33 |  -1    |   0.57 |    0.6  |     0.6  |   -1   | -1    |      -1    |     0.67 |    -1   |
| Sushant  |     0.38 |   -1   |    0.38 |    0.49 |   0.29 |  0.31 |     0.41 |   0.36 |     -1    |      0.54 |   0.43 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.12 |      -1    |    -1    |    -1   |
| Abishek  |     0.55 |    0.4 |    0.57 |    0.61 |   0.4  |  0.53 |     0.48 |   0.57 |      0.54 |     -1    |   0.5  |   0.8  |   0.54 |   -1    |    -1    |    0.5 |  0.57 |      -1    |    -1    |    -1   |
| Ruhi     |     0    |   -1   |    0.4  |    0.5  |   0.2  | -1    |     0.14 |   0.33 |      0.43 |      0.5  |  -1    |  -1    |   0.67 |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Alex     |     0.41 |   -1   |    0.27 |    0.52 |  -1    |  0.4  |     0.47 |   0.57 |      0.42 |      0.54 |   0.67 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Jade     |    -1    |   -1   |    0.2  |    0.5  |  -1    | -1    |    -1    |  -1    |     -1    |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Andrew   |    -1    |   -1   |    0.6  |    0.67 |  -1    | -1    |    -1    |   0.67 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |
| Daisy    |    -1    |   -1   |   -1    |   -1    |  -1    | -1    |     0.2  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |    -1    |    -1   |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |   Daisy |   Aman |
|---------|-------|---------|-------|------|-------|----------|----------|-------|--------|--------|---------|-------|------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |    0.67 |   -1    |     0.33 |  -1    | -1    |   -1    |  -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      0.83 |      1    |  -1    |    0.75 |    0.5  |     1    |   0.5  | -1    |   -1    |  -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |   -1    |  -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |   0    | -1    |   -1    |  -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.83 |    0.25 |     0.25 |   1    | -1    |   -1    |  -1    |
| Sushant  |   0.33 |     0.83 |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |   -1    |  -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.73 |    0.64 |     0.5  |   0.88 | -1    |   -1    |  -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.5  |  0.33 |   -1    |  -1    |
| Brian    |   0.67 |     0.75 |      1 | -1    |   0.83 |      0.71 |      0.73 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |   -1    |   0.33 |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.25 |      0.58 |      0.64 |   0.75 |    0.89 |   -1    |     0.83 |   0.33 |  1    |   -1    |  -1    |
| Jackie   |   0.33 |     1    |     -1 | -1    |   0.25 |      0.67 |      0.5  |  -1    |    0.8  |    0.83 |    -1    |  -1    | -1    |    0.33 |  -1    |
| Alex     |  -1    |     0.5  |     -1 |  0    |   1    |      0.67 |      0.88 |   0.5  |    0.83 |    0.33 |    -1    |  -1    | -1    |   -1    |  -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |   -1    |  -1    |
| Daisy    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |   -1    |     0.33 |  -1    | -1    |   -1    |  -1    |
| Aman     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    0.33 |   -1    |    -1    |  -1    | -1    |   -1    |  -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |   Daisy |
|---------|-------|---------|-------|------|-------|----------|----------|-------|--------|--------|---------|-------|------|--------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |    0.67 |   -1    |     0.33 |  -1    | -1    |   -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      1    |      1    |  -1    |    0.75 |    0.5  |     1    |   0.75 | -1    |   -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |   -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |  -1    | -1    |   -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.83 |    0.25 |     0.25 |   1    | -1    |   -1    |
| Sushant  |   0.33 |     1    |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |   -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.85 |    0.64 |     0.5  |   0.88 | -1    |   -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.75 |  0.33 |   -1    |
| Brian    |   0.67 |     0.75 |      1 | -1    |   0.83 |      0.71 |      0.85 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |   -1    |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.25 |      0.58 |      0.64 |   0.75 |    0.89 |   -1    |     0.83 |   0.33 |  1    |   -1    |
| Jackie   |   0.33 |     1    |     -1 | -1    |   0.25 |      0.67 |      0.5  |  -1    |    0.8  |    0.83 |    -1    |  -1    | -1    |    0.33 |
| Alex     |  -1    |     0.75 |     -1 | -1    |   1    |      0.67 |      0.88 |   0.75 |    0.83 |    0.33 |    -1    |  -1    | -1    |   -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |   -1    |
| Daisy    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |   -1    |     0.33 |  -1    | -1    |   -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |   Aman |   Andrew |   Daisy |
|---------|--------|--------|-------|---------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|------|-------|---------|--------|
| Peter    |   -1    |    0.41 |   0.59 |     0.48 |    0.2 |  0.56 |     0.48 |   0.5  |      0.47 |      0.39 |   0.73 |  -1    |   0.6  |    0.4  |     -1   |   -1   | -1    |       -1   |   0.8 |   0.6  |    -1    |   -1    |
| Brian    |    0.59 |   -1    |   0.58 |     0.63 |   -1   |  0.71 |     0.54 |   0.56 |      0.57 |      0.48 |   0.71 |   0.64 |   0.64 |   -1    |      0.6 |   -1   |  0.55 |       -1   |  -1   |  -1    |    -1    |    0.67 |
| Minh     |    0.41 |    0.42 |  -1    |     0.5  |   -1   |  0.67 |     0.53 |   0.32 |      0.33 |      0.41 |   0.6  |  -1    |   0.33 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Rachel   |    0.52 |    0.37 |   0.5  |    -1    |   -1   |  0.55 |     0.55 |   0.44 |      0.45 |      0.33 |   0.62 |   0.6  |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jai      |    0.44 |    0.29 |   0.33 |     0.45 |   -1   | -1    |     0.45 |   0.29 |      0.38 |      0.24 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jackie   |    0.52 |    0.46 |   0.47 |     0.45 |   -1   |  0.55 |    -1    |   0.48 |      0.38 |      0.39 |   0.5  |  -1    |   0.53 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |     0.4  |   -1    |
| Kate     |    0.5  |    0.44 |   0.68 |     0.56 |    0.5 |  0.71 |     0.52 |  -1    |      0.57 |      0.44 |   0.65 |   0.4  |   0.52 |   -1    |     -1   |    0.8 |  0.44 |       -1   |  -1   |   0.67 |    -1    |   -1    |
| Sushant  |    0.53 |    0.43 |   0.67 |     0.55 |   -1   |  0.62 |     0.62 |   0.42 |     -1    |      0.36 |   0.6  |   0.4  |   0.42 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |   0.8 |  -1    |    -1    |   -1    |
| Abishek  |    0.61 |    0.52 |   0.59 |     0.67 |   -1   |  0.76 |     0.61 |   0.56 |      0.64 |     -1    |   0.74 |   0.71 |   0.58 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1   |  -1    |    -1    |   -1    |
| Ruhi     |    0.27 |    0.29 |   0.4  |     0.38 |   -1   |  0.6  |     0.5  |   0.35 |      0.4  |      0.26 |  -1    |  -1    |   0.62 |    0.6  |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Alex     |    0.4  |    0.36 |   0.67 |     0.75 |   -1   |  0.75 |     0.47 |   0.48 |      0.58 |      0.42 |   0.38 |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jade     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |
| Aman     |    0.4  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.33 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |     0.29 |   -1    |
| Andrew   |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |   0.71 |    -1    |   -1    |
| Daisy    |   -1    |    0.33 |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |  -1    |    -1    |   -1    |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Aman |   Andrew |   Daisy |
|---------|--------|--------|-------|---------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|-------|---------|--------|
| Peter    |   -1    |    0.38 |   0.59 |     0.44 |    0.2 |  0.53 |     0.48 |   0.5  |      0.45 |      0.36 |   0.7  |  -1    |   0.57 |    0.4  |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Brian    |    0.62 |   -1    |   0.61 |     0.61 |   -1   |  0.69 |     0.58 |   0.57 |      0.58 |      0.48 |   0.68 |   0.6  |   0.63 |   -1    |      0.6 |   -1   |  0.55 |       -1   |  -1    |    -1    |     0.8 |
| Minh     |    0.41 |    0.39 |  -1    |     0.5  |   -1   |  0.6  |     0.53 |   0.33 |      0.33 |      0.36 |  -1    |  -1    |   0.29 |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Rachel   |    0.56 |    0.39 |   0.5  |    -1    |   -1   |  0.6  |     0.57 |   0.47 |      0.48 |      0.36 |   0.62 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Jai      |    0.47 |    0.31 |   0.4  |     0.4  |   -1   | -1    |     0.5  |   0.33 |      0.38 |      0.26 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Jackie   |    0.52 |    0.42 |   0.47 |     0.43 |   -1   |  0.5  |    -1    |   0.48 |      0.38 |      0.36 |   0.43 |  -1    |   0.5  |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |     0.4  |    -1   |
| Kate     |    0.5  |    0.42 |   0.67 |     0.53 |    0.5 |  0.67 |     0.52 |  -1    |      0.57 |      0.42 |   0.64 |   0.33 |   0.48 |   -1    |     -1   |    0.8 |  0.44 |       -1   |   0.6  |    -1    |    -1   |
| Sushant  |    0.55 |    0.42 |   0.67 |     0.52 |   -1   |  0.62 |     0.62 |   0.42 |     -1    |      0.35 |   0.57 |  -1    |   0.39 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |  -1    |    -1    |    -1   |
| Abishek  |    0.64 |    0.52 |   0.64 |     0.64 |   -1   |  0.74 |     0.64 |   0.57 |      0.65 |     -1    |   0.71 |   0.67 |   0.56 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1    |    -1    |    -1   |
| Ruhi     |    0.3  |    0.32 |  -1    |     0.38 |   -1   |  0.6  |     0.57 |   0.36 |      0.43 |      0.29 |  -1    |  -1    |   0.62 |    0.6  |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Alex     |    0.43 |    0.37 |   0.71 |     0.75 |   -1   |  0.75 |     0.5  |   0.52 |      0.61 |      0.44 |   0.38 |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Jade     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |
| Aman     |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |     0.33 |    -1   |
| Andrew   |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |   0.67 |    -1    |    -1   |
| Daisy    |   -1    |    0.2  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1    |    -1    |    -1   |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|-----------|---------|--------------|
| 3+1        | 0.352941 |            34 |
| 2+2        | 0.373333 |            75 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|-----------|---------|--------------|
| 3+1        | 0.3125   |            32 |
| 2+2        | 0.338028 |            71 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.419355 |            31 |
| Success      | 0.313559 |           118 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.419355 |            31 |
| Success      | 0.301724 |           116 |

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |      37 | 0.468354 |     0.324324 |
|         1 |      31 | 0.392405 |     0.129032 |
|         2 |      11 | 0.139241 |     0.363636 |

*2 bad guys on mission 1:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |      15 | 0.789474 |     0.133333 |
|         1 |       4 | 0.210526 |     0        |

*2 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|----------|--------|---------|-------------|
|         0 |      12 | 0.413793 |    0.5       |
|         1 |      12 | 0.413793 |    0.0833333 |
|         2 |       5 | 0.172414 |    0.2       |

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
|                   0 |            91 |     0.516484 |
|                   1 |           124 |     0.354839 |
|                   2 |            16 |     0.5625   |
|                   3 |             5 |     0.4      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|--------------------|--------------|-------------|
|                   0 |            86 |     0.488372 |
|                   1 |           118 |     0.322034 |
|                   2 |            16 |     0.5625   |
|                   3 |             5 |     0.4      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|--------------|------------------------|--------------|----------------|
| Merlin        |                 0.11017 |           236 |              26 |
| Assassin      |                 0.03535 |           198 |               7 |
| Morgana       |                 0.05652 |           230 |              13 |
| Mordred       |                 0.00746 |           134 |               1 |
| Loyal Servant |                 0       |           658 |               0 |
| Oberon        |                 0.01429 |            70 |               1 |
| Minion #1     |                 0.05556 |            36 |               2 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|---------|----------------------------|-------------------|--------------|
| Jeron    |                    0.5      |                  3 |             6 |
| Abishek  |                    0.444444 |                 16 |            36 |
| Minh     |                    0.4      |                  4 |            10 |
| Alex     |                    0.363636 |                  8 |            22 |
| Tercel   |                    0.333333 |                  2 |             6 |
| Jai      |                    0.3125   |                  5 |            16 |
| Rachel   |                    0.296296 |                  8 |            27 |
| Kate     |                    0.291667 |                 14 |            48 |
| Jackie   |                    0.25     |                  9 |            36 |
| Peter    |                    0.222222 |                  8 |            36 |
| Sushant  |                    0.2      |                  4 |            20 |
| Brian    |                    0.18     |                  9 |            50 |
| Ruhi     |                    0.166667 |                  1 |             6 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)


*Competitive games only statistic.*

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|---------|------------------|-------------------|--------------|
| Minh     |          0        |                  0 |             4 |
| Brian    |          0.111111 |                  1 |             9 |
| Sushant  |          0.333333 |                  3 |             9 |
| Jeron    |          0.333333 |                  1 |             3 |
| Kate     |          0.363636 |                  4 |            11 |
| Abishek  |          0.444444 |                  4 |             9 |
| Peter    |          0.5      |                  6 |            12 |
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
| 7O          |          0.6      |                  3 |             5 |
| 8           |          0.526316 |                 10 |            19 |
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
| 7O          |                   0 |          0.75     |                  3 |             4 |
| 7O          |                   2 |          0        |                  0 |             1 |
| 8           |                   0 |          0.5      |                  3 |             6 |
| 8           |                   1 |          0.538462 |                  7 |            13 |
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
| Success    |     201 |     0.87013 |     0.437811 |
| Fail       |      30 |     0.12987 |     0.4      |

*Lengths: 2*

| Sequence         |   Count |   Frequency |   Good Win % |
|-----------------|--------|------------|-------------|
| Success, Success |      90 |   0.38961   |     0.622222 |
| Success, Fail    |     111 |   0.480519  |     0.288288 |
| Fail, Success    |      16 |   0.0692641 |     0.625    |
| Fail, Fail       |      14 |   0.0606061 |     0.142857 |

*Lengths: 3*

| Sequence                  |   Count |   Frequency |   Good Win % |
|--------------------------|--------|------------|-------------|
| Success, Success, Success |      54 |   0.233766  |     0.685185 |
| Success, Success, Fail    |      36 |   0.155844  |     0.527778 |
| Success, Fail, Success    |      56 |   0.242424  |     0.428571 |
| Success, Fail, Fail       |      55 |   0.238095  |     0.145455 |
| Fail, Success, Success    |      15 |   0.0649351 |     0.666667 |
| Fail, Success, Fail       |       1 |   0.004329  |     0        |
| Fail, Fail, Success       |       7 |   0.030303  |     0.285714 |
| Fail, Fail, Fail          |       7 |   0.030303  |     0        |

*Lengths: 4*

| Sequence                        |   Count |   Frequency | Good Win %          |
|--------------------------------|--------|------------|--------------------|
| Success, Success, Fail, Success |      13 |  0.0769231  | 0.7692307692307693  |
| Success, Success, Fail, Fail    |      23 |  0.136095   | 0.391304347826087   |
| Success, Fail, Success, Success |      42 |  0.248521   | 0.47619047619047616 |
| Success, Fail, Success, Fail    |      14 |  0.0828402  | 0.2857142857142857  |
| Success, Fail, Fail, Success    |      40 |  0.236686   | 0.2                 |
| Success, Fail, Fail, Fail       |      14 |  0.0828402  | 0.0                 |
| Fail, Success, Success, Success |       8 |  0.0473373  | 0.875               |
| Fail, Success, Success, Fail    |       7 |  0.0414201  | 0.42857142857142855 |
| Fail, Success, Fail, Success    |       1 |  0.00591716 | 0.0                 |
| Fail, Success, Fail, Fail       |       0 |  0          | N/A                 |
| Fail, Fail, Success, Success    |       7 |  0.0414201  | 0.2857142857142857  |
| Fail, Fail, Success, Fail       |       0 |  0          | N/A                 |

*Lengths: 5*

| Sequence                              |   Count |   Frequency | Good Win %          |
|--------------------------------------|--------|------------|--------------------|
| Success, Success, Fail, Fail, Success |      13 |   0.173333  | 0.46153846153846156 |
| Success, Success, Fail, Fail, Fail    |       5 |   0.0666667 | 0.0                 |
| Success, Fail, Success, Fail, Success |       6 |   0.08      | 0.5                 |
| Success, Fail, Success, Fail, Fail    |       2 |   0.0266667 | 0.0                 |
| Success, Fail, Fail, Success, Success |      20 |   0.266667  | 0.4                 |
| Success, Fail, Fail, Success, Fail    |      19 |   0.253333  | 0.0                 |
| Fail, Success, Success, Fail, Success |       1 |   0.0133333 | 0.0                 |
| Fail, Success, Success, Fail, Fail    |       1 |   0.0133333 | 0.0                 |
| Fail, Success, Fail, Success, Success |       0 |   0         | N/A                 |
| Fail, Success, Fail, Success, Fail    |       1 |   0.0133333 | 0.0                 |
| Fail, Fail, Success, Success, Success |       5 |   0.0666667 | 0.4                 |
| Fail, Fail, Success, Success, Fail    |       2 |   0.0266667 | 0.0                 |
