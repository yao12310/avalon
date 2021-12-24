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

Cheesy wins included: 0.4317 (n = 227)

Cheesy wins excluded: 0.4028 (n = 216)

**Good win % w.r.t. # players:**

Cheesy wins included:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            30 |     0.4      |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5X          |             6 |     0.5      |
| 6           |            23 |     0.652174 |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            35 |     0.371429 |
| 7O          |             5 |     0.4      |
| 8           |            38 |     0.289474 |
| 8O          |             3 |     0        |
| 9           |            41 |     0.365854 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

Cheesy wins excluded:

| # Players   |   Sample Size |   Good Win % |
|------------|--------------|-------------|
| 10          |            29 |     0.37931  |
| 5           |             8 |     0.25     |
| 5O          |             9 |     0.666667 |
| 5X          |             6 |     0.5      |
| 6           |            21 |     0.619048 |
| 6M          |            12 |     0.583333 |
| 6O          |            12 |     0.75     |
| 7           |            32 |     0.3125   |
| 7O          |             5 |     0.4      |
| 8           |            38 |     0.289474 |
| 8O          |             3 |     0        |
| 9           |            36 |     0.277778 |
| 9L          |             3 |     0.666667 |
| 9O          |             2 |     0.5      |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           114 |       28.7193 |     19.6449 |
| Good     |            86 |       19.0698 |     15.4948 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|---------|--------------|--------------|------------|
| Bad      |           114 |       28.7193 |     19.6449 |
| Good     |            79 |       20.0759 |     15.7739 |

### <a id="carries"></a>Number of carries by player

| Player   |   # Carries |
|---------|------------|
| Kate     |           9 |
| Abishek  |           5 |
| Peter    |           4 |
| Brian    |           2 |
| Rachel   |           2 |
| Jackie   |           1 |
| Minh     |           1 |
| Sachin   |           1 |
| Sushant  |           1 |

### <a id="win-rate-leaderboard"></a>Win rate leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Games Behind column reports # games needed to win in a row in order to pass leader.*

Cheesy wins included:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|-------------|------------|--------------|-------|---------|-----------------------|
| Abishek  | 0.59633  |     0.5      |    0.723404 |           109 |     65 |       44 |                      0 |
| Brian    | 0.570175 |     0.473684 |    0.763158 |           114 |     65 |       49 |                      8 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      2 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                      3 |
| Kate     | 0.520833 |     0.459016 |    0.628571 |            96 |     50 |       46 |                     18 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|---------|---------|-------------|------------|--------------|-------|---------|-----------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.584158 |     0.446429 |    0.755556 |           101 |     59 |       42 |                      5 |
| Brian    | 0.556604 |     0.428571 |    0.805556 |           106 |     59 |       47 |                     12 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kish     | 0.5      |     0.375    |    0.666667 |            14 |      7 |        7 |                      4 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|---------|----------------------|---------|-----------------|---------|
| Brian    |             0.0887849 | 0.570175 |         0.481391 | 0.666667 |
| Abishek  |             0.0822853 | 0.59633  |         0.514045 | 0.568807 |
| Kish     |             0.0790046 | 0.529412 |         0.450407 | 0.588235 |
| Ewen     |             0.0417099 | 0.538462 |         0.496752 | 0.615385 |
| Kate     |             0.0392262 | 0.520833 |         0.481607 | 0.635417 |
| Anthony  |             0.027592  | 0.5      |         0.472408 | 0.166667 |
| Peter    |             0.0110549 | 0.455556 |         0.444501 | 0.633333 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|---------|----------------------|---------|-----------------|---------|
| Anthony  |             0.115152  | 0.6      |         0.484848 | 0.166667 |
| Brian    |             0.0885256 | 0.556604 |         0.468078 | 0.666667 |
| Abishek  |             0.078795  | 0.584158 |         0.505363 | 0.568807 |
| Ewen     |             0.0629053 | 0.538462 |         0.475556 | 0.615385 |
| Kish     |             0.0288024 | 0.5      |         0.471198 | 0.588235 |
| Kate     |             0.0203615 | 0.494382 |         0.474021 | 0.635417 |

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|---------|---------|--------------|-------|---------|---------------------|
| Brian    | 0.636364 |            11 |      7 |        4 |                    0 |
| Kate     | 0.636364 |            11 |      7 |        4 |                    1 |
| Minh     | 0.571429 |             7 |      4 |        3 |                    2 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|---------|---------|--------------|-------|---------|----------------------|
| Jackie   | 0.666667 |             9 |      6 |        3 |                     0 |
| Sushant  | 0.666667 |             6 |      4 |        2 |                     1 |
| Kate     | 0.6      |            10 |      6 |        4 |                     3 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.692308 |            13 |      9 |        4 |                      0 |
| Brian    | 0.692308 |            13 |      9 |        4 |                      1 |
| Sushant  | 0.666667 |            12 |      8 |        4 |                      2 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.8      |            15 |     12 |        3 |                      0 |
| Brian    | 0.75     |            16 |     12 |        4 |                      5 |
| Kate     | 0.636364 |            11 |      7 |        4 |                     10 |

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
| Ruhi     | 0.5      |            12 |      6 |        6 |                      4 |
| Brian    | 0.444444 |            45 |     20 |       25 |                     20 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|---------|---------|--------------|-------|---------|--------------------|
| Kate     | 0.636364 |            11 |      7 |        4 |                   0 |
| Brian    | 0.6      |            10 |      6 |        4 |                   2 |
| Minh     | 0.4      |             5 |      2 |        3 |                   4 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Sushant |
|---------|---------|--------------|-------|---------|-----------------------|
| Sushant  | 0.666667 |             6 |      4 |        2 |                      0 |
| Jackie   | 0.625    |             8 |      5 |        3 |                      2 |
| Kate     | 0.5      |             8 |      4 |        4 |                      5 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.75     |            12 |      9 |        3 |                      0 |
| Brian    | 0.75     |            12 |      9 |        3 |                      1 |
| Sushant  | 0.727273 |            11 |      8 |        3 |                      2 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|---------|---------|--------------|-------|---------|-----------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Brian    | 0.8      |            15 |     12 |        3 |                      7 |
| Rachel   | 0.666667 |             6 |      4 |        2 |                      9 |

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
| Brian    | 0.418605 |            43 |     18 |       25 |                     12 |
| Rachel   | 0.4      |            30 |     12 |       18 |                     10 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|---------|---------------|
| Brian    |            206 |
| Peter    |            168 |
| Kate     |            166 |
| Abishek  |            162 |
| Jackie   |            161 |
| Rachel   |            131 |
| Sushant  |            127 |
| Alex     |             94 |
| Jai      |             89 |
| Minh     |             63 |
| Ruhi     |             44 |
| Jeron    |             30 |
| Jay      |             26 |
| Kish     |             21 |
| Tercel   |             20 |
| Jade     |             18 |
| Daisy    |             14 |
| Ewen     |             13 |
| Vishal   |             13 |
| Anthony  |             12 |
| Aman     |             11 |
| Justin   |              9 |
| Sai      |              8 |
| Karthik  |              7 |
| Gathenji |              7 |
| Megan    |              6 |
| Olivia   |              5 |
| Sofia    |              5 |
| Andrew   |              5 |
| Kevin    |              5 |
| Selena   |              5 |

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

| Player   |   Good % |   # Good |   # Bad |
|---------|---------|---------|--------|
| Daisy    | 0.857143 |       12 |       2 |
| Gathenji | 0.857143 |        6 |       1 |
| Jade     | 0.777778 |       14 |       4 |
| Rachel   | 0.725191 |       95 |      36 |
| Karthik  | 0.714286 |        5 |       2 |
| Kate     | 0.680723 |      113 |      53 |
| Megan    | 0.666667 |        4 |       2 |
| Jeron    | 0.666667 |       20 |      10 |
| Justin   | 0.666667 |        6 |       3 |
| Jackie   | 0.652174 |      105 |      56 |
| Tercel   | 0.65     |       13 |       7 |
| Alex     | 0.638298 |       60 |      34 |
| Brian    | 0.631068 |      130 |      76 |
| Sai      | 0.625    |        5 |       3 |
| Peter    | 0.625    |      105 |      63 |
| Kish     | 0.619048 |       13 |       8 |
| Ewen     | 0.615385 |        8 |       5 |
| Jay      | 0.615385 |       16 |      10 |
| Jai      | 0.606742 |       54 |      35 |
| Andrew   | 0.6      |        3 |       2 |
| Olivia   | 0.6      |        3 |       2 |
| Selena   | 0.6      |        3 |       2 |
| Sushant  | 0.574803 |       73 |      54 |
| Minh     | 0.571429 |       36 |      27 |
| Abishek  | 0.567901 |       92 |      70 |
| Aman     | 0.545455 |        6 |       5 |
| Ruhi     | 0.545455 |       24 |      20 |
| Vishal   | 0.538462 |        7 |       6 |
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
| No                 |           213 |     0.450704 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|---------------------|--------------|-------------|
| No                   |           213 |     0.450704 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |       20 |         22 |         21 |        21 |         7 |       10 |          11 |              50 |           162 |
| Alex     |       13 |         13 |         13 |        14 |         4 |        2 |           1 |              34 |            94 |
| Aman     |        3 |          2 |          1 |         1 |         1 |        2 |           0 |               1 |            11 |
| Andrew   |        0 |          0 |          1 |         0 |         1 |        0 |           0 |               3 |             5 |
| Anthony  |        0 |          2 |          4 |         4 |         0 |        1 |           0 |               1 |            12 |
| Brian    |       23 |         37 |         23 |        31 |        14 |        5 |           3 |              70 |           206 |
| Daisy    |        2 |          1 |          0 |         2 |         0 |        0 |           0 |               9 |            14 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       25 |         21 |         13 |        22 |        10 |        8 |           3 |              59 |           161 |
| Jade     |        5 |          3 |          1 |         1 |         1 |        1 |           0 |               6 |            18 |
| Jai      |       10 |          9 |          8 |        13 |         9 |        4 |           1 |              35 |            89 |
| Jay      |        4 |          3 |          4 |         0 |         5 |        1 |           0 |               9 |            26 |
| Jeron    |        5 |          9 |          1 |         5 |         2 |        1 |           1 |               6 |            30 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Karthik  |        2 |          0 |          0 |         1 |         0 |        0 |           1 |               3 |             7 |
| Kate     |       20 |         17 |         11 |        15 |        13 |       12 |           2 |              76 |           166 |
| Kevin    |        0 |          0 |          1 |         3 |         1 |        0 |           0 |               0 |             5 |
| Kish     |        3 |          4 |          1 |         4 |         2 |        0 |           1 |               6 |            21 |
| Megan    |        2 |          0 |          0 |         0 |         0 |        2 |           0 |               2 |             6 |
| Minh     |        9 |          7 |         11 |         6 |         6 |        2 |           2 |              20 |            63 |
| Olivia   |        1 |          0 |          1 |         0 |         1 |        0 |           0 |               2 |             5 |
| Peter    |       25 |         22 |         23 |        20 |        10 |        7 |           3 |              58 |           168 |
| Rachel   |       18 |         20 |         10 |        13 |        10 |        0 |           3 |              57 |           131 |
| Ruhi     |        2 |          5 |          6 |         7 |         6 |        1 |           0 |              17 |            44 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Selena   |        0 |          0 |          0 |         0 |         1 |        1 |           0 |               3 |             5 |
| Sofia    |        0 |          1 |          1 |         2 |         0 |        0 |           0 |               1 |             5 |
| Sushant  |       21 |          9 |         18 |        21 |         9 |        4 |           2 |              43 |           127 |
| Tercel   |        2 |          5 |          3 |         1 |         3 |        0 |           0 |               6 |            20 |
| Vishal   |        3 |          0 |          3 |         2 |         1 |        0 |           0 |               4 |            13 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.089 |      0.1   |      0.114 |     0.097 |     0.057 |    0.147 |       0.314 |           0.081 |           162 |
| Alex     |    0.058 |      0.059 |      0.07  |     0.065 |     0.033 |    0.029 |       0.029 |           0.055 |            94 |
| Aman     |    0.013 |      0.009 |      0.005 |     0.005 |     0.008 |    0.029 |       0     |           0.002 |            11 |
| Andrew   |    0     |      0     |      0.005 |     0     |     0.008 |    0     |       0     |           0.005 |             5 |
| Anthony  |    0     |      0.009 |      0.022 |     0.019 |     0     |    0.015 |       0     |           0.002 |            12 |
| Brian    |    0.103 |      0.169 |      0.124 |     0.144 |     0.115 |    0.074 |       0.086 |           0.114 |           206 |
| Daisy    |    0.009 |      0.005 |      0     |     0.009 |     0     |    0     |       0     |           0.015 |            14 |
| Ewen     |    0.004 |      0.009 |      0.011 |     0.005 |     0     |    0.029 |       0     |           0.008 |            13 |
| Gathenji |    0     |      0     |      0     |     0.005 |     0     |    0     |       0     |           0.01  |             7 |
| Jackie   |    0.112 |      0.096 |      0.07  |     0.102 |     0.082 |    0.118 |       0.086 |           0.096 |           161 |
| Jade     |    0.022 |      0.014 |      0.005 |     0.005 |     0.008 |    0.015 |       0     |           0.01  |            18 |
| Jai      |    0.045 |      0.041 |      0.043 |     0.06  |     0.074 |    0.059 |       0.029 |           0.057 |            89 |
| Jay      |    0.018 |      0.014 |      0.022 |     0     |     0.041 |    0.015 |       0     |           0.015 |            26 |
| Jeron    |    0.022 |      0.041 |      0.005 |     0.023 |     0.016 |    0.015 |       0.029 |           0.01  |            30 |
| Justin   |    0.009 |      0     |      0.005 |     0.005 |     0.008 |    0     |       0     |           0.007 |             9 |
| Karthik  |    0.009 |      0     |      0     |     0.005 |     0     |    0     |       0.029 |           0.005 |             7 |
| Kate     |    0.089 |      0.078 |      0.059 |     0.069 |     0.107 |    0.176 |       0.057 |           0.124 |           166 |
| Kevin    |    0     |      0     |      0.005 |     0.014 |     0.008 |    0     |       0     |           0     |             5 |
| Kish     |    0.013 |      0.018 |      0.005 |     0.019 |     0.016 |    0     |       0.029 |           0.01  |            21 |
| Megan    |    0.009 |      0     |      0     |     0     |     0     |    0.029 |       0     |           0.003 |             6 |
| Minh     |    0.04  |      0.032 |      0.059 |     0.028 |     0.049 |    0.029 |       0.057 |           0.033 |            63 |
| Olivia   |    0.004 |      0     |      0.005 |     0     |     0.008 |    0     |       0     |           0.003 |             5 |
| Peter    |    0.112 |      0.1   |      0.124 |     0.093 |     0.082 |    0.103 |       0.086 |           0.094 |           168 |
| Rachel   |    0.08  |      0.091 |      0.054 |     0.06  |     0.082 |    0     |       0.086 |           0.093 |           131 |
| Ruhi     |    0.009 |      0.023 |      0.032 |     0.032 |     0.049 |    0.015 |       0     |           0.028 |            44 |
| Sai      |    0.004 |      0.005 |      0     |     0.005 |     0.016 |    0     |       0     |           0.005 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.008 |    0.015 |       0     |           0.005 |             5 |
| Sofia    |    0     |      0.005 |      0.005 |     0.009 |     0     |    0     |       0     |           0.002 |             5 |
| Sushant  |    0.094 |      0.041 |      0.097 |     0.097 |     0.074 |    0.059 |       0.057 |           0.07  |           127 |
| Tercel   |    0.009 |      0.023 |      0.016 |     0.005 |     0.025 |    0     |       0     |           0.01  |            20 |
| Vishal   |    0.013 |      0     |      0.016 |     0.009 |     0.008 |    0     |       0     |           0.007 |            13 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|---------|-----------|-----------|----------|----------|---------|------------|----------------|--------------|
| Abishek  |    0.123 |      0.136 |      0.13  |     0.13  |     0.043 |    0.062 |       0.068 |           0.309 |           162 |
| Alex     |    0.138 |      0.138 |      0.138 |     0.149 |     0.043 |    0.021 |       0.011 |           0.362 |            94 |
| Aman     |    0.273 |      0.182 |      0.091 |     0.091 |     0.091 |    0.182 |       0     |           0.091 |            11 |
| Andrew   |    0     |      0     |      0.2   |     0     |     0.2   |    0     |       0     |           0.6   |             5 |
| Anthony  |    0     |      0.167 |      0.333 |     0.333 |     0     |    0.083 |       0     |           0.083 |            12 |
| Brian    |    0.112 |      0.18  |      0.112 |     0.15  |     0.068 |    0.024 |       0.015 |           0.34  |           206 |
| Daisy    |    0.143 |      0.071 |      0     |     0.143 |     0     |    0     |       0     |           0.643 |            14 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.155 |      0.13  |      0.081 |     0.137 |     0.062 |    0.05  |       0.019 |           0.366 |           161 |
| Jade     |    0.278 |      0.167 |      0.056 |     0.056 |     0.056 |    0.056 |       0     |           0.333 |            18 |
| Jai      |    0.112 |      0.101 |      0.09  |     0.146 |     0.101 |    0.045 |       0.011 |           0.393 |            89 |
| Jay      |    0.154 |      0.115 |      0.154 |     0     |     0.192 |    0.038 |       0     |           0.346 |            26 |
| Jeron    |    0.167 |      0.3   |      0.033 |     0.167 |     0.067 |    0.033 |       0.033 |           0.2   |            30 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Karthik  |    0.286 |      0     |      0     |     0.143 |     0     |    0     |       0.143 |           0.429 |             7 |
| Kate     |    0.12  |      0.102 |      0.066 |     0.09  |     0.078 |    0.072 |       0.012 |           0.458 |           166 |
| Kevin    |    0     |      0     |      0.2   |     0.6   |     0.2   |    0     |       0     |           0     |             5 |
| Kish     |    0.143 |      0.19  |      0.048 |     0.19  |     0.095 |    0     |       0.048 |           0.286 |            21 |
| Megan    |    0.333 |      0     |      0     |     0     |     0     |    0.333 |       0     |           0.333 |             6 |
| Minh     |    0.143 |      0.111 |      0.175 |     0.095 |     0.095 |    0.032 |       0.032 |           0.317 |            63 |
| Olivia   |    0.2   |      0     |      0.2   |     0     |     0.2   |    0     |       0     |           0.4   |             5 |
| Peter    |    0.149 |      0.131 |      0.137 |     0.119 |     0.06  |    0.042 |       0.018 |           0.345 |           168 |
| Rachel   |    0.137 |      0.153 |      0.076 |     0.099 |     0.076 |    0     |       0.023 |           0.435 |           131 |
| Ruhi     |    0.045 |      0.114 |      0.136 |     0.159 |     0.136 |    0.023 |       0     |           0.386 |            44 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Selena   |    0     |      0     |      0     |     0     |     0.2   |    0.2   |       0     |           0.6   |             5 |
| Sofia    |    0     |      0.2   |      0.2   |     0.4   |     0     |    0     |       0     |           0.2   |             5 |
| Sushant  |    0.165 |      0.071 |      0.142 |     0.165 |     0.071 |    0.031 |       0.016 |           0.339 |           127 |
| Tercel   |    0.1   |      0.25  |      0.15  |     0.05  |     0.15  |    0     |       0     |           0.3   |            20 |
| Vishal   |    0.231 |      0     |      0.231 |     0.154 |     0.077 |    0     |       0     |           0.308 |            13 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     1    |   0.5  |    0.47 |    0.45 |      0.33 |   0.43 |  0.53 |     0.55 |   0.48 |      0.49 |      0.35 |   0.44 |   0.6  |   0.56 |    0.75 |     0.57 |   0.69 |    -1   |  0.72 |       0.86 | -1    |     0.4  |      0.57 |     0.44 |     -1   |    1    |  -1    |   -1    |     -1   |     0   |      0.6 |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Peter    |     0.47 |   0.17 |    1    |    0.51 |      0.43 |   0.44 |  0.51 |     0.46 |   0.41 |      0.49 |      0.44 |   0.5  |   0.55 |   0.45 |    0.45 |     0.78 |   0.53 |    -1   |  0.65 |      -1    |  0.29 |     0.56 |     -1    |    -1    |     -1   |    0.67 |   0.33 |    0.5  |      0.6 |    -1   |     -1   |
| Brian    |     0.45 |   0.83 |    0.51 |    1    |      0.25 |   0.4  |  0.55 |     0.42 |   0.51 |      0.42 |      0.51 |   0.31 |   0.38 |   0.46 |    0.5  |     0.44 |   0.6  |     0.2 |  0.3  |       0.5  |  0.62 |     0.5  |      0.43 |     0.54 |      0.6 |    0    |   0.64 |    0.5  |      0.4 |    -1   |     -1   |
| Anthony  |     0.33 |  -1    |    0.43 |    0.25 |      1    |   0.5  |  0.29 |     0.17 |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Minh     |     0.43 |   0.4  |    0.44 |    0.4  |      0.5  |   1    |  0.43 |     0.44 |   0.43 |      0.62 |      0.53 |   0.54 |   0.67 |   0.32 |    0.33 |    -1    |   0.14 |    -1   |  0.33 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.78 |  -1    |   -1    |     -1   |     0.2 |      0.4 |
| Jai      |     0.53 |   0.4  |    0.51 |    0.55 |      0.29 |   0.43 |  1    |     0.45 |   0.58 |      0.34 |      0.41 |   0.25 |  -1    |   0.51 |    0.45 |    -1    |   0.33 |    -1   |  0.23 |       0.8  | -1    |     0.56 |      0.67 |     0    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jackie   |     0.55 |   0.33 |    0.46 |    0.42 |      0.17 |   0.44 |  0.45 |     1    |   0.55 |      0.42 |      0.4  |   0.4  |   0.38 |   0.58 |    0.57 |    -1    |   0.5  |     0.6 |  0.6  |      -1    |  0.4  |     0.4  |      0.57 |     0.38 |     -1   |    0.82 |   0.5  |   -1    |      0.4 |    -1   |     -1   |
| Kate     |     0.48 |   0.45 |    0.41 |    0.51 |      0.33 |   0.43 |  0.58 |     0.55 |   1    |      0.41 |      0.51 |   0.44 |   0.33 |   0.45 |    0.75 |     0.83 |   0.42 |    -1   |  0.4  |       0.57 |  0.5  |     0.31 |     -1    |     0.57 |      0.2 |    0.57 |   0.27 |    0.67 |      0.4 |     0.6 |      0.4 |
| Sushant  |     0.49 |   0.43 |    0.49 |    0.42 |     -1    |   0.62 |  0.34 |     0.42 |   0.41 |      1    |      0.49 |   0.48 |   0.55 |   0.44 |    0.29 |     0.17 |   0.5  |    -1   |  0.45 |       0.5  |  0.38 |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Abishek  |     0.35 |   0.56 |    0.44 |    0.51 |      0.2  |   0.53 |  0.41 |     0.4  |   0.51 |      0.49 |      1    |   0.44 |   0.5  |   0.43 |    0.18 |     0.38 |   0.5  |    -1   |  0.46 |       0.29 |  0.62 |    -1    |      0.14 |     0.54 |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Ruhi     |     0.44 |  -1    |    0.5  |    0.31 |     -1    |   0.54 |  0.25 |     0.4  |   0.44 |      0.48 |      0.44 |   1    |   0.71 |   0.53 |    0.44 |    -1    |  -1    |    -1   |  0.57 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Kish     |     0.6  |   0    |    0.55 |    0.38 |     -1    |   0.67 | -1    |     0.38 |   0.33 |      0.55 |      0.5  |   0.71 |   1    |  -1    |    0.2  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Alex     |     0.56 |   0.2  |    0.45 |    0.46 |     -1    |   0.32 |  0.51 |     0.58 |   0.45 |      0.44 |      0.43 |   0.53 |  -1    |   1    |    0.4  |     0.67 |   0.2  |    -1   |  0.45 |       0.4  |  0.5  |     0.38 |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jeron    |     0.75 |  -1    |    0.45 |    0.5  |      0.5  |   0.33 |  0.45 |     0.57 |   0.75 |      0.29 |      0.18 |   0.44 |   0.2  |   0.4  |    1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jade     |     0.69 |  -1    |    0.53 |    0.6  |     -1    |   0.14 |  0.33 |     0.5  |   0.42 |      0.5  |      0.5  |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Sofia    |    -1    |  -1    |   -1    |    0.2  |     -1    |  -1    | -1    |     0.6  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |     1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jay      |     0.72 |  -1    |    0.65 |    0.3  |     -1    |   0.33 |  0.23 |     0.6  |   0.4  |      0.45 |      0.46 |   0.57 |  -1    |   0.45 |   -1    |    -1    |  -1    |    -1   |  1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    |    -1   | -1    |       1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    |  1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Tercel   |     0.4  |  -1    |    0.56 |    0.5  |     -1    |  -1    |  0.56 |     0.4  |   0.31 |     -1    |     -1    |  -1    |  -1    |   0.38 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     1    |     -1    |    -1    |      0.6 |    0.4  |   0.8  |    0.33 |     -1   |    -1   |     -1   |
| Karthik  |     0.57 |  -1    |   -1    |    0.43 |     -1    |  -1    |  0.67 |     0.57 |  -1    |     -1    |      0.14 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      1    |     0.29 |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Vishal   |     0.44 |  -1    |   -1    |    0.54 |     -1    |  -1    |  0    |     0.38 |   0.57 |     -1    |      0.54 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0.29 |     1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Olivia   |    -1    |  -1    |   -1    |    0.6  |     -1    |  -1    | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.6  |     -1    |    -1    |      1   |    0.4  |  -1    |   -1    |     -1   |    -1   |     -1   |
| Daisy    |     1    |  -1    |    0.67 |    0    |     -1    |   0.78 | -1    |     0.82 |   0.57 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.4  |     -1    |    -1    |      0.4 |    1    |   0.38 |   -1    |     -1   |     0   |      0.6 |
| Aman     |    -1    |  -1    |    0.33 |    0.64 |     -1    |  -1    | -1    |     0.5  |   0.27 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.8  |     -1    |    -1    |     -1   |    0.38 |   1    |   -1    |      0   |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.67 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.33 |     -1    |    -1    |     -1   |   -1    |  -1    |    1    |     -1   |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.6  |    0.4  |     -1    |  -1    | -1    |     0.4  |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |   0    |   -1    |      1   |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |     -1   |     1   |      0.4 |
| Selena   |     0.6  |  -1    |   -1    |   -1    |     -1    |   0.4  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.6  |  -1    |   -1    |     -1   |     0.4 |      1   |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |    -1    |   0.25 |    0.08 |    0.04 |      0.17 |   0.1  |  0.11 |     0.1  |   0.07 |      0.09 |      0.07 |   0.07 |   0.13 |   0.12 |    0.05 |     0    |   0.15 |    -1   |  0.11 |       0.14 | -1    |     0    |      0    |     0.11 |     -1   |    0    |  -1    |   -1    |     -1   |     0   |      0   |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Peter    |     0.08 |   0    |   -1    |    0.12 |      0.29 |   0.15 |  0.14 |     0.06 |   0.06 |      0.15 |      0.16 |   0.17 |   0    |   0.06 |    0.09 |     0.11 |   0.13 |    -1   |  0.25 |      -1    |  0    |     0.06 |     -1    |    -1    |     -1   |    0    |   0    |    0.17 |      0   |    -1   |     -1   |
| Brian    |     0.04 |   0.25 |    0.12 |   -1    |      0.25 |   0.12 |  0.09 |     0.08 |   0.1  |      0.09 |      0.16 |   0.03 |   0.14 |   0.07 |    0.07 |     0    |   0    |     0.2 |  0.05 |       0    |  0.12 |     0.17 |      0    |     0.23 |      0.4 |    0    |   0.36 |    0.33 |      0.2 |    -1   |     -1   |
| Anthony  |     0.17 |  -1    |    0.29 |    0.25 |     -1    |   0.33 |  0.29 |     0    |   0.11 |     -1    |      0    |  -1    |  -1    |  -1    |    0.33 |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Minh     |     0.1  |   0.2  |    0.15 |    0.12 |      0.33 |  -1    |  0.1  |     0.06 |   0.11 |      0.22 |      0.11 |   0.15 |   0.33 |   0.08 |    0.17 |    -1    |   0    |    -1   |  0.17 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.11 |  -1    |   -1    |     -1   |     0.2 |      0   |
| Jai      |     0.11 |   0    |    0.14 |    0.09 |      0.29 |   0.1  | -1    |     0.07 |   0.13 |      0.13 |      0.12 |   0.15 |  -1    |   0.15 |    0.09 |    -1    |   0    |    -1   |  0.08 |       0    | -1    |     0.22 |      0    |     0    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jackie   |     0.1  |   0    |    0.06 |    0.08 |      0    |   0.06 |  0.07 |    -1    |   0.09 |      0.08 |      0.1  |   0.05 |   0.25 |   0.13 |    0.14 |    -1    |   0.08 |     0.2 |  0.13 |      -1    |  0.2  |     0.07 |      0.29 |     0.23 |     -1   |    0.18 |   0.1  |   -1    |      0   |    -1   |     -1   |
| Kate     |     0.07 |   0.09 |    0.06 |    0.1  |      0.11 |   0.11 |  0.13 |     0.09 |  -1    |      0.09 |      0.11 |   0.08 |   0    |   0.09 |    0.17 |     0.33 |   0.08 |    -1   |  0.04 |       0    |  0.12 |     0    |     -1    |     0    |      0   |    0.07 |   0.09 |    0.17 |      0   |     0.6 |      0.2 |
| Sushant  |     0.09 |   0.14 |    0.15 |    0.09 |     -1    |   0.22 |  0.13 |     0.08 |   0.09 |     -1    |      0.18 |   0.18 |   0    |   0.1  |    0    |     0    |   0.1  |    -1   |  0.14 |       0    |  0.12 |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Abishek  |     0.07 |   0.11 |    0.16 |    0.16 |      0    |   0.11 |  0.12 |     0.1  |   0.11 |      0.18 |     -1    |   0.17 |   0.14 |   0.11 |    0    |     0.25 |   0    |    -1   |  0.08 |       0    |  0.12 |    -1    |      0    |     0.23 |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Ruhi     |     0.07 |  -1    |    0.17 |    0.03 |     -1    |   0.15 |  0.15 |     0.05 |   0.08 |      0.18 |      0.17 |  -1    |   0.14 |   0.35 |    0.11 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Kish     |     0.13 |   0    |    0    |    0.14 |     -1    |   0.33 | -1    |     0.25 |   0    |      0    |      0.14 |   0.14 |  -1    |  -1    |    0.2  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Alex     |     0.12 |   0    |    0.06 |    0.07 |     -1    |   0.08 |  0.15 |     0.13 |   0.09 |      0.1  |      0.11 |   0.35 |  -1    |  -1    |    0.1  |     0    |   0    |    -1   |  0.09 |       0    |  0.17 |     0    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jeron    |     0.05 |  -1    |    0.09 |    0.07 |      0.33 |   0.17 |  0.09 |     0.14 |   0.17 |      0    |      0    |   0.11 |   0.2  |   0.1  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jade     |     0.15 |  -1    |    0.13 |    0    |     -1    |   0    |  0    |     0.08 |   0.08 |      0.1  |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Sofia    |    -1    |  -1    |   -1    |    0.2  |     -1    |  -1    | -1    |     0.2  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jay      |     0.11 |  -1    |    0.25 |    0.05 |     -1    |   0.17 |  0.08 |     0.13 |   0.04 |      0.14 |      0.08 |   0.43 |  -1    |   0.09 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Tercel   |     0    |  -1    |    0.06 |    0.17 |     -1    |  -1    |  0.22 |     0.07 |   0    |     -1    |     -1    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |      0.2 |    0    |   0.2  |    0    |     -1   |    -1   |     -1   |
| Karthik  |     0    |  -1    |   -1    |    0    |     -1    |  -1    |  0    |     0.29 |  -1    |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |     0.14 |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Vishal   |     0.11 |  -1    |   -1    |    0.23 |     -1    |  -1    |  0    |     0.23 |   0    |     -1    |      0.23 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0.14 |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Olivia   |    -1    |  -1    |   -1    |    0.4  |     -1    |  -1    | -1    |    -1    |   0    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.2  |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Daisy    |     0    |  -1    |    0    |    0    |     -1    |   0.11 | -1    |     0.18 |   0.07 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |      0   |   -1    |   0.12 |   -1    |     -1   |     0   |      0   |
| Aman     |    -1    |  -1    |    0    |    0.36 |     -1    |  -1    | -1    |     0.1  |   0.09 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.2  |     -1    |    -1    |     -1   |    0.12 |  -1    |   -1    |      0   |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.17 |    0.33 |     -1    |  -1    | -1    |    -1    |   0.17 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0    |    0.2  |     -1    |  -1    | -1    |     0    |   0    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |   0    |   -1    |     -1   |    -1   |     -1   |
| Kevin    |     0    |  -1    |   -1    |   -1    |     -1    |   0.2  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |     -1   |    -1   |      0.4 |
| Selena   |     0    |  -1    |   -1    |   -1    |     -1    |   0    | -1    |    -1    |   0.2  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0    |  -1    |   -1    |     -1   |     0.4 |     -1   |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Sofia |   Jay |   Gathenji |   Sai |   Tercel |   Karthik |   Vishal |   Olivia |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|--------|------|-----------|------|---------|----------|---------|---------|--------|-------|--------|---------|--------|---------|
| Rachel   |     0    |   0.5  |    0.53 |    0.55 |      0.67 |   0.57 |  0.47 |     0.45 |   0.52 |      0.51 |      0.65 |   0.56 |   0.4  |   0.44 |    0.25 |     0.43 |   0.31 |    -1   |  0.28 |       0.14 | -1    |     0.6  |      0.43 |     0.56 |     -1   |    0    |  -1    |   -1    |     -1   |     1   |      0.4 |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Peter    |     0.53 |   0.83 |    0    |    0.49 |      0.57 |   0.56 |  0.49 |     0.54 |   0.59 |      0.51 |      0.56 |   0.5  |   0.45 |   0.55 |    0.55 |     0.22 |   0.47 |    -1   |  0.35 |      -1    |  0.71 |     0.44 |     -1    |    -1    |     -1   |    0.33 |   0.67 |    0.5  |      0.4 |    -1   |     -1   |
| Brian    |     0.55 |   0.17 |    0.49 |    0    |      0.75 |   0.6  |  0.45 |     0.58 |   0.49 |      0.58 |      0.49 |   0.69 |   0.62 |   0.54 |    0.5  |     0.56 |   0.4  |     0.8 |  0.7  |       0.5  |  0.38 |     0.5  |      0.57 |     0.46 |      0.4 |    1    |   0.36 |    0.5  |      0.6 |    -1   |     -1   |
| Anthony  |     0.67 |  -1    |    0.57 |    0.75 |      0    |   0.5  |  0.71 |     0.83 |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |    0.5  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Minh     |     0.57 |   0.6  |    0.56 |    0.6  |      0.5  |   0    |  0.57 |     0.56 |   0.57 |      0.38 |      0.47 |   0.46 |   0.33 |   0.68 |    0.67 |    -1    |   0.86 |    -1   |  0.67 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.22 |  -1    |   -1    |     -1   |     0.8 |      0.6 |
| Jai      |     0.47 |   0.6  |    0.49 |    0.45 |      0.71 |   0.57 |  0    |     0.55 |   0.42 |      0.66 |      0.59 |   0.75 |  -1    |   0.49 |    0.55 |    -1    |   0.67 |    -1   |  0.77 |       0.2  | -1    |     0.44 |      0.33 |     1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jackie   |     0.45 |   0.67 |    0.54 |    0.58 |      0.83 |   0.56 |  0.55 |     0    |   0.45 |      0.58 |      0.6  |   0.6  |   0.62 |   0.42 |    0.43 |    -1    |   0.5  |     0.4 |  0.4  |      -1    |  0.6  |     0.6  |      0.43 |     0.62 |     -1   |    0.18 |   0.5  |   -1    |      0.6 |    -1   |     -1   |
| Kate     |     0.52 |   0.55 |    0.59 |    0.49 |      0.67 |   0.57 |  0.42 |     0.45 |   0    |      0.59 |      0.49 |   0.56 |   0.67 |   0.55 |    0.25 |     0.17 |   0.58 |    -1   |  0.6  |       0.43 |  0.5  |     0.69 |     -1    |     0.43 |      0.8 |    0.43 |   0.73 |    0.33 |      0.6 |     0.4 |      0.6 |
| Sushant  |     0.51 |   0.57 |    0.51 |    0.58 |     -1    |   0.38 |  0.66 |     0.58 |   0.59 |      0    |      0.51 |   0.52 |   0.45 |   0.56 |    0.71 |     0.83 |   0.5  |    -1   |  0.55 |       0.5  |  0.62 |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Abishek  |     0.65 |   0.44 |    0.56 |    0.49 |      0.8  |   0.47 |  0.59 |     0.6  |   0.49 |      0.51 |      0    |   0.56 |   0.5  |   0.57 |    0.82 |     0.62 |   0.5  |    -1   |  0.54 |       0.71 |  0.38 |    -1    |      0.86 |     0.46 |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Ruhi     |     0.56 |  -1    |    0.5  |    0.69 |     -1    |   0.46 |  0.75 |     0.6  |   0.56 |      0.52 |      0.56 |   0    |   0.29 |   0.47 |    0.56 |    -1    |  -1    |    -1   |  0.43 |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Kish     |     0.4  |   1    |    0.45 |    0.62 |     -1    |   0.33 | -1    |     0.62 |   0.67 |      0.45 |      0.5  |   0.29 |   0    |  -1    |    0.8  |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Alex     |     0.44 |   0.8  |    0.55 |    0.54 |     -1    |   0.68 |  0.49 |     0.42 |   0.55 |      0.56 |      0.57 |   0.47 |  -1    |   0    |    0.6  |     0.33 |   0.8  |    -1   |  0.55 |       0.6  |  0.5  |     0.62 |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jeron    |     0.25 |  -1    |    0.55 |    0.5  |      0.5  |   0.67 |  0.55 |     0.43 |   0.25 |      0.71 |      0.82 |   0.56 |   0.8  |   0.6  |    0    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jade     |     0.31 |  -1    |    0.47 |    0.4  |     -1    |   0.86 |  0.67 |     0.5  |   0.58 |      0.5  |      0.5  |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Sofia    |    -1    |  -1    |   -1    |    0.8  |     -1    |  -1    | -1    |     0.4  |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |     0   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Jay      |     0.28 |  -1    |    0.35 |    0.7  |     -1    |   0.67 |  0.77 |     0.4  |   0.6  |      0.55 |      0.54 |   0.43 |  -1    |   0.55 |   -1    |    -1    |  -1    |    -1   |  0    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    |    -1   | -1    |       0    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    |    -1   | -1    |      -1    |  0    |    -1    |     -1    |    -1    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Tercel   |     0.6  |  -1    |    0.44 |    0.5  |     -1    |  -1    |  0.44 |     0.6  |   0.69 |     -1    |     -1    |  -1    |  -1    |   0.62 |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0    |     -1    |    -1    |      0.4 |    0.6  |   0.2  |    0.67 |     -1   |    -1   |     -1   |
| Karthik  |     0.43 |  -1    |   -1    |    0.57 |     -1    |  -1    |  0.33 |     0.43 |  -1    |     -1    |      0.86 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0    |     0.71 |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Vishal   |     0.56 |  -1    |   -1    |    0.46 |     -1    |  -1    |  1    |     0.62 |   0.43 |     -1    |      0.46 |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |      0.71 |     0    |     -1   |   -1    |  -1    |   -1    |     -1   |    -1   |     -1   |
| Olivia   |    -1    |  -1    |   -1    |    0.4  |     -1    |  -1    | -1    |    -1    |   0.8  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.4  |     -1    |    -1    |      0   |    0.6  |  -1    |   -1    |     -1   |    -1   |     -1   |
| Daisy    |     0    |  -1    |    0.33 |    1    |     -1    |   0.22 | -1    |     0.18 |   0.43 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.6  |     -1    |    -1    |      0.6 |    0    |   0.62 |   -1    |     -1   |     1   |      0.4 |
| Aman     |    -1    |  -1    |    0.67 |    0.36 |     -1    |  -1    | -1    |     0.5  |   0.73 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.2  |     -1    |    -1    |     -1   |    0.62 |   0    |   -1    |      1   |    -1   |     -1   |
| Megan    |    -1    |  -1    |    0.5  |    0.5  |     -1    |  -1    | -1    |    -1    |   0.33 |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |     0.67 |     -1    |    -1    |     -1   |   -1    |  -1    |    0    |     -1   |    -1   |     -1   |
| Andrew   |    -1    |  -1    |    0.4  |    0.6  |     -1    |  -1    | -1    |     0.6  |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |   -1    |   1    |   -1    |      0   |    -1   |     -1   |
| Kevin    |     1    |  -1    |   -1    |   -1    |     -1    |   0.8  | -1    |    -1    |   0.4  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    1    |  -1    |   -1    |     -1   |     0   |      0.6 |
| Selena   |     0.4  |  -1    |   -1    |   -1    |     -1    |   0.6  | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    |    -1   | -1    |      -1    | -1    |    -1    |     -1    |    -1    |     -1   |    0.4  |  -1    |   -1    |     -1   |     0.6 |      0   |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Abishe |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|
| Rachel   |      131 |      4 |      44 |      50 |         4 |     18 |    35 |       51 |     44 |        38 |        34 |     12 |      9 |     29 |          1 |        1 |        0 |      15 |        0 |        4 |      9 |       1 |    13 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |        2 |         4 |        4 |        0 |       0 |       5 |      1 |       0 |        1 |       0 |        3 |    0 |        1 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Peter    |       44 |      1 |     168 |      78 |         3 |     18 |    36 |       59 |     50 |        49 |        51 |     12 |      6 |     35 |          1 |        1 |        0 |      10 |        0 |        7 |      8 |       0 |    13 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |        9 |         0 |        0 |        0 |       1 |       4 |      3 |       3 |        3 |       0 |        0 |    0 |        0 |
| Brian    |       50 |     10 |      78 |     206 |         3 |     21 |    42 |       61 |     75 |        48 |        75 |     12 |      8 |     37 |          1 |        1 |        0 |      14 |        0 |        4 |      9 |       1 |     6 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |        9 |         3 |        7 |        3 |       1 |       0 |      7 |       3 |        2 |       0 |        0 |    0 |        0 |
| Anthony  |        4 |      1 |       3 |       3 |        12 |      3 |     2 |        1 |      3 |         0 |         1 |      2 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Minh     |       18 |      2 |      18 |      21 |         3 |     63 |     9 |       21 |     23 |        20 |        25 |      7 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      1 |       2 |     2 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       7 |      1 |       0 |        3 |       1 |        2 |    0 |        1 |
| Jai      |       35 |      2 |      36 |      42 |         2 |      9 |    89 |       30 |     39 |        16 |        23 |      5 |      2 |     20 |          0 |        0 |        0 |       5 |        0 |        0 |      3 |       0 |     3 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        5 |         4 |        0 |        0 |       0 |       1 |      1 |       0 |        2 |       2 |        1 |    1 |        0 |
| Jackie   |       51 |      2 |      59 |      61 |         1 |     21 |    30 |      161 |     64 |        36 |        45 |      8 |      3 |     36 |          0 |        0 |        1 |      12 |        1 |        1 |      6 |       3 |     9 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       1 |        6 |         4 |        5 |        1 |       2 |       9 |      5 |       1 |        2 |       2 |        0 |    0 |        0 |
| Kate     |       44 |      5 |      50 |      75 |         3 |     23 |    39 |       64 |    166 |        40 |        62 |     16 |      5 |     30 |          0 |        0 |        0 |       9 |        0 |        5 |      5 |       1 |    10 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |        4 |         1 |        4 |        1 |       2 |       8 |      3 |       4 |        2 |       3 |        2 |    1 |        1 |
| Sushant  |       38 |      3 |      49 |      48 |         0 |     20 |    16 |       36 |     40 |       127 |        56 |     16 |      6 |     30 |          2 |        0 |        0 |       5 |        0 |        1 |      5 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       2 |      0 |       0 |        0 |       0 |        1 |    0 |        1 |
| Abishek  |       34 |      5 |      51 |      75 |         1 |     25 |    23 |       45 |     62 |        56 |       162 |     16 |      7 |     33 |          0 |        0 |        0 |       3 |        0 |        3 |      7 |       1 |    11 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |        2 |         1 |        7 |        0 |       0 |       2 |      1 |       0 |        2 |       0 |        0 |    0 |        0 |
| Ruhi     |       12 |      2 |      12 |      12 |         2 |      7 |     5 |        8 |     16 |        16 |        16 |     44 |      5 |      9 |          0 |        0 |        0 |       4 |        0 |        0 |      2 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       3 |      0 |       0 |        0 |       1 |        4 |    0 |        0 |
| Kish     |        9 |      0 |       6 |       8 |         2 |      4 |     2 |        3 |      5 |         6 |         7 |      5 |     21 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Alex     |       29 |      1 |      35 |      37 |         0 |      8 |    20 |       36 |     30 |        30 |        33 |      9 |      2 |     94 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       2 |     5 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jeron    |       15 |      0 |      10 |      14 |         3 |      2 |     5 |       12 |      9 |         5 |         3 |      4 |      1 |      4 |          0 |        0 |        1 |      30 |        1 |        0 |      0 |       1 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jade     |        9 |      2 |       8 |       9 |         0 |      1 |     3 |        6 |      5 |         5 |         7 |      2 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |     18 |       0 |     3 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sofia    |        1 |      0 |       0 |       1 |         0 |      2 |     0 |        3 |      1 |         1 |         1 |      0 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       5 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jay      |       13 |      1 |      13 |       6 |         0 |      2 |     3 |        9 |     10 |        10 |        11 |      4 |      1 |      5 |          0 |        0 |        0 |       2 |        0 |        0 |      3 |       0 |    26 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Derek    |        1 |      0 |       2 |       3 |         0 |      0 |     0 |        1 |      1 |         3 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       4 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Gathenji |        6 |      0 |       1 |       3 |         0 |      0 |     4 |        2 |      4 |         3 |         2 |      2 |      1 |      2 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          7 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      2 |         1 |         1 |      2 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      3 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sai      |        2 |      1 |       2 |       5 |         0 |      2 |     2 |        2 |      4 |         3 |         5 |      0 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     8 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Nabeel   |        0 |      1 |       2 |       1 |         0 |      0 |     0 |        2 |      3 |         0 |         2 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        4 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ronnie   |        1 |      0 |       2 |       0 |         0 |      1 |     0 |        2 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        2 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Neha     |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Kawin    |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      2 |     0 |       2 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Abrar    |        1 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       2 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Tercel   |        2 |      0 |       9 |       9 |         0 |      0 |     5 |        6 |      4 |         4 |         2 |      0 |      0 |      3 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       20 |         0 |        0 |        3 |       2 |       2 |      4 |       2 |        0 |       0 |        0 |    0 |        0 |
| Karthik  |        4 |      0 |       0 |       3 |         0 |      0 |     4 |        4 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         7 |        2 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Vishal   |        4 |      0 |       0 |       7 |         0 |      0 |     0 |        5 |      4 |         0 |         7 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         2 |       13 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Olivia   |        0 |      0 |       0 |       3 |         0 |      0 |     0 |        1 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        5 |       3 |       2 |      4 |       0 |        0 |       0 |        0 |    0 |        0 |
| AlexY    |        0 |      0 |       1 |       1 |         0 |      0 |     0 |        2 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        3 |       4 |       3 |      2 |       1 |        0 |       0 |        0 |    0 |        0 |
| Daisy    |        5 |      0 |       4 |       0 |         0 |      7 |     1 |        9 |      8 |         2 |         2 |      3 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        2 |       3 |      14 |      3 |       1 |        2 |       0 |        3 |    0 |        1 |
| Aman     |        1 |      0 |       3 |       7 |         0 |      1 |     1 |        5 |      3 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        4 |       2 |       3 |     11 |       1 |        0 |       0 |        0 |    0 |        0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       1 |      1 |       6 |        0 |       0 |        0 |    0 |        0 |
| Andrew   |        1 |      0 |       3 |       2 |         0 |      3 |     2 |        2 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      0 |       0 |        5 |       0 |        0 |    0 |        0 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       5 |        2 |    1 |        0 |
| Selena   |        3 |      0 |       0 |       0 |         0 |      2 |     1 |        0 |      2 |         1 |         0 |      4 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       3 |      0 |       0 |        0 |       2 |        5 |    0 |        0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |    1 |        0 |
| Abishe   |        1 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        0 |    0 |        1 |

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Abishe |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|
| Rachel   |       -1 |      2 |       7 |       4 |         2 |      4 |     7 |        9 |      6 |         7 |         7 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      2 |       0 |     2 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        1 |        0 |       0 |       0 |      0 |       0 |        1 |       0 |        0 |    0 |        0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Peter    |        7 |      0 |      -1 |      19 |         2 |      6 |    10 |        8 |      7 |        15 |        18 |      4 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        1 |      2 |       0 |     5 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       1 |        0 |       0 |        0 |    0 |        0 |
| Brian    |        4 |      3 |      19 |      -1 |         3 |      6 |     7 |       11 |     15 |        10 |        24 |      1 |      3 |      6 |          1 |        0 |        0 |       2 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |        3 |         0 |        3 |        2 |       0 |       0 |      4 |       2 |        1 |       0 |        0 |    0 |        0 |
| Anthony  |        2 |      1 |       2 |       3 |        -1 |      2 |     2 |        0 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       2 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Minh     |        4 |      1 |       6 |       6 |         2 |     -1 |     2 |        3 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      1 |       0 |        1 |       1 |        0 |    0 |        0 |
| Jai      |        7 |      0 |      10 |       7 |         2 |      2 |    -1 |        5 |      9 |         6 |         7 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        1 |       2 |        1 |    1 |        0 |
| Jackie   |        9 |      0 |       8 |      11 |         0 |      3 |     5 |       -1 |     11 |         7 |        11 |      1 |      2 |      8 |          0 |        0 |        1 |       3 |        1 |        0 |      1 |       1 |     2 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |        1 |         2 |        3 |        0 |       0 |       2 |      1 |       0 |        0 |       2 |        0 |    0 |        0 |
| Kate     |        6 |      1 |       7 |      15 |         1 |      6 |     9 |       11 |     -1 |         9 |        14 |      3 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      1 |       1 |        0 |       3 |        1 |    1 |        0 |
| Sushant  |        7 |      1 |      15 |      10 |         0 |      7 |     6 |        7 |      9 |        -1 |        21 |      6 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      1 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Abishek  |        7 |      1 |      18 |      24 |         0 |      5 |     7 |       11 |     14 |        21 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       1 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        3 |        0 |       0 |       0 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ruhi     |        2 |      1 |       4 |       1 |         1 |      2 |     3 |        1 |      3 |         6 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        1 |    0 |        0 |
| Kish     |        2 |      0 |       0 |       3 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     6 |        8 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       1 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jeron    |        1 |      0 |       2 |       2 |         2 |      1 |     1 |        3 |      2 |         0 |         0 |      1 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jade     |        2 |      0 |       2 |       0 |         0 |      0 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sofia    |        0 |      0 |       0 |       1 |         0 |      1 |     0 |        1 |      0 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |      -1 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jay      |        2 |      0 |       5 |       1 |         0 |      1 |     1 |        2 |      1 |         3 |         2 |      3 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      1 |       0 |    -1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Greg     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |     -1 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Gathenji |        1 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |         -1 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Caro     |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        1 |      1 |         0 |         0 |      1 |      1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |     -1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sai      |        1 |      0 |       0 |       1 |         0 |      0 |     1 |        1 |      1 |         1 |         1 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |    -1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Nabeel   |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |       -1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ronnie   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |       -1 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Neha     |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |     -1 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ira      |        0 |      0 |       0 |       1 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |    -1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Kawin    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |      -1 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Abrar    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |      -1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Tercel   |        0 |      0 |       1 |       3 |         0 |      0 |     2 |        1 |      0 |         2 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |       -1 |         0 |        0 |        1 |       0 |       0 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |
| Karthik  |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        2 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |        -1 |        1 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Vishal   |        1 |      0 |       0 |       3 |         0 |      0 |     0 |        3 |      0 |         0 |         3 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         1 |       -1 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Olivia   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |       -1 |       0 |       0 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |
| AlexY    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |      -1 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Daisy    |        0 |      0 |       0 |       0 |         0 |      1 |     0 |        2 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |      -1 |      1 |       0 |        0 |       0 |        0 |    0 |        0 |
| Aman     |        0 |      0 |       0 |       4 |         0 |      1 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        2 |       0 |       1 |     -1 |       0 |        0 |       0 |        0 |    0 |        0 |
| Megan    |        0 |      0 |       1 |       2 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |      -1 |        0 |       0 |        0 |    0 |        0 |
| Andrew   |        1 |      0 |       0 |       1 |         0 |      1 |     1 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |       -1 |       0 |        0 |    0 |        0 |
| Kevin    |        0 |      0 |       0 |       0 |         0 |      1 |     2 |        2 |      3 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |      -1 |        2 |    1 |        0 |
| Selena   |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       2 |       -1 |    0 |        0 |
| NA       |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        0 |   -1 |        0 |
| Abishe   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |       -1 |

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |   Tercel |   Karthik |   Vishal |   Olivia |   AlexY |   Daisy |   Aman |   Megan |   Andrew |   Kevin |   Selena |   NA |   Abishe |
|---------|---------|-------|--------|--------|----------|-------|------|---------|-------|----------|----------|-------|-------|-------|-----------|---------|---------|--------|---------|---------|-------|--------|------|-------|--------|-----------|-------|------|---------|---------|-------|------|--------|--------|---------|----------|---------|---------|--------|--------|-------|--------|---------|--------|---------|-----|---------|
| Rachel   |        0 |      4 |      49 |      60 |         8 |     24 |    31 |       42 |     48 |        39 |        64 |     15 |      6 |     23 |          1 |        0 |        1 |       5 |        1 |        3 |      4 |       3 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |        3 |         3 |        5 |        0 |       0 |       0 |      1 |       0 |        0 |       5 |        2 |    1 |        0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Peter    |       49 |      5 |       0 |      76 |         4 |     23 |    34 |       69 |     71 |        51 |        64 |     12 |      5 |     42 |          1 |        0 |        1 |      12 |        1 |        2 |      7 |       3 |     7 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       1 |        7 |         0 |        0 |        2 |       1 |       2 |      6 |       3 |        2 |       0 |        0 |    0 |        0 |
| Brian    |       60 |      2 |      76 |       0 |         9 |     31 |    35 |       85 |     73 |        65 |        73 |     27 |     13 |     44 |          1 |        0 |        1 |      14 |        1 |        5 |      6 |       4 |    14 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       1 |        9 |         4 |        6 |        2 |       3 |       9 |      4 |       3 |        3 |       0 |        0 |    0 |        0 |
| Anthony  |        8 |      0 |       4 |       9 |         0 |      3 |     5 |        5 |      6 |         1 |         4 |      1 |      2 |      0 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Minh     |       24 |      3 |      23 |      31 |         3 |      0 |    12 |       27 |     30 |        12 |        22 |      6 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      6 |       0 |     4 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      3 |       0 |        1 |       4 |        3 |    1 |        0 |
| Jai      |       31 |      3 |      34 |      35 |         5 |     12 |     0 |       37 |     28 |        31 |        33 |     15 |      2 |     19 |          1 |        0 |        0 |       6 |        0 |        2 |      6 |       0 |    10 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       2 |        4 |         2 |        6 |        0 |       0 |       3 |      2 |       0 |        1 |       0 |        1 |    0 |        1 |
| Jackie   |       42 |      4 |      69 |      85 |         5 |     27 |    37 |        0 |     52 |        49 |        68 |     12 |      5 |     26 |          0 |        1 |        0 |       9 |        0 |        2 |      6 |       2 |     6 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |        9 |         3 |        8 |        3 |       1 |       2 |      5 |       1 |        3 |       1 |        3 |    0 |        0 |
| Kate     |       48 |      6 |      71 |      73 |         6 |     30 |    28 |       52 |      0 |        57 |        60 |     20 |     10 |     36 |          2 |        0 |        0 |       3 |        0 |        1 |      7 |       1 |    15 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |        9 |         0 |        3 |        4 |       2 |       6 |      8 |       2 |        3 |       2 |        3 |    0 |        0 |
| Sushant  |       39 |      4 |      51 |      65 |         1 |     12 |    31 |       49 |     57 |         0 |        59 |     17 |      5 |     38 |          0 |        0 |        0 |      12 |        0 |        5 |      5 |       3 |    12 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       2 |        1 |    1 |        0 |
| Abishek  |       64 |      4 |      64 |      73 |         4 |     22 |    33 |       68 |     60 |        59 |         0 |     20 |      7 |     43 |          0 |        0 |        0 |      14 |        0 |        5 |      7 |       3 |    13 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |        2 |         6 |        6 |        0 |       0 |       2 |      2 |       0 |        1 |       1 |        1 |    0 |        0 |
| Ruhi     |       15 |      1 |      12 |      27 |         1 |      6 |    15 |       12 |     20 |        17 |        20 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      2 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       3 |        0 |    1 |        1 |
| Kish     |        6 |      5 |       5 |      13 |         2 |      2 |     2 |        5 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       4 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Alex     |       23 |      4 |      42 |      44 |         0 |     17 |    19 |       26 |     36 |        38 |        43 |      8 |      1 |      0 |          1 |        0 |        0 |       6 |        0 |        2 |      4 |       1 |     6 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |        5 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jeron    |        5 |      1 |      12 |      14 |         3 |      4 |     6 |        9 |      3 |        12 |        14 |      5 |      4 |      6 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       1 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jade     |        4 |      0 |       7 |       6 |         0 |      6 |     6 |        6 |      7 |         5 |         7 |      2 |      0 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sofia    |        3 |      0 |       3 |       4 |         0 |      0 |     0 |        2 |      1 |         3 |         3 |      0 |      0 |      1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Jay      |        5 |      1 |       7 |      14 |         0 |      4 |    10 |        6 |     15 |        12 |        13 |      3 |      0 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Derek    |        3 |      0 |       2 |       1 |         0 |      0 |     2 |        1 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Gathenji |        1 |      0 |       3 |       3 |         0 |      0 |     1 |        2 |      3 |         3 |         5 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Caro     |        1 |      0 |       0 |       3 |         0 |      1 |     0 |        1 |      1 |         2 |         2 |      1 |      2 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Sai      |        1 |      0 |       5 |       3 |         0 |      2 |     1 |        3 |      4 |         5 |         3 |      2 |      0 |      3 |          0 |        0 |        0 |       0 |        0 |        1 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Nabeel   |        2 |      3 |       0 |       3 |         0 |      0 |     1 |        2 |      1 |         0 |         2 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ronnie   |        0 |      0 |       0 |       2 |         0 |      0 |     0 |        0 |      1 |         1 |         2 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Neha     |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Ira      |        0 |      0 |       1 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      1 |     0 |       1 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Kawin    |        0 |      0 |       1 |       2 |         0 |      1 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     1 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Abrar    |        0 |      0 |       1 |       1 |         0 |      0 |     2 |        1 |      0 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Tercel   |        3 |      0 |       7 |       9 |         0 |      0 |     4 |        9 |      9 |         0 |         2 |      0 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     4 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       1 |        0 |         0 |        0 |        2 |       2 |       3 |      1 |       4 |        0 |       0 |        0 |    0 |        0 |
| Karthik  |        3 |      0 |       0 |       4 |         0 |      0 |     2 |        3 |      0 |         0 |         6 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        5 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Vishal   |        5 |      0 |       0 |       6 |         0 |      0 |     6 |        8 |      3 |         0 |         6 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         5 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       0 |        0 |    0 |        0 |
| Olivia   |        0 |      0 |       2 |       2 |         0 |      0 |     0 |        3 |      4 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        0 |       1 |       3 |      0 |       2 |        0 |       0 |        0 |    0 |        0 |
| AlexY    |        0 |      0 |       1 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        2 |         0 |        0 |        1 |       0 |       1 |      1 |       1 |        0 |       0 |        0 |    0 |        0 |
| Daisy    |        0 |      0 |       2 |       9 |         0 |      2 |     3 |        2 |      6 |         0 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        3 |         0 |        0 |        3 |       1 |       0 |      5 |       1 |        2 |       5 |        2 |    1 |        0 |
| Aman     |        1 |      0 |       6 |       4 |         0 |      3 |     2 |        5 |      8 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        1 |         0 |        0 |        0 |       1 |       5 |      0 |       2 |        5 |       0 |        0 |    0 |        0 |
| Megan    |        0 |      0 |       3 |       3 |         0 |      0 |     0 |        1 |      2 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        4 |         0 |        0 |        2 |       1 |       1 |      2 |       0 |        0 |       0 |        0 |    0 |        0 |
| Andrew   |        0 |      0 |       2 |       3 |         0 |      1 |     1 |        3 |      3 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      5 |       0 |        0 |       0 |        0 |    0 |        0 |
| Kevin    |        5 |      0 |       0 |       0 |         0 |      4 |     0 |        1 |      2 |         2 |         1 |      3 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       5 |      0 |       0 |        0 |       0 |        3 |    0 |        1 |
| Selena   |        2 |      0 |       0 |       0 |         0 |      3 |     1 |        3 |      3 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       2 |      0 |       0 |        0 |       3 |        0 |    1 |        1 |
| NA       |        1 |      0 |       0 |       0 |         0 |      1 |     0 |        0 |      0 |         1 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       1 |      0 |       0 |        0 |       0 |        1 |    0 |        0 |
| Abishe   |        0 |      0 |       0 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         0 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |        0 |         0 |        0 |        0 |       0 |       0 |      0 |       0 |        0 |       1 |        1 |    0 |        0 |

### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|---------|---------|-------|--------|--------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|------|
| Rachel   |    -1    |   -1   |    0.28 |    0.47 |   0.44 |  0.23 |     0.42 |   0.4  |      0.37 |      0.57 |   0.14 |   0.43 |   0.38 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.28 |   -1   |   -1    |    0.52 |   0.44 |  0.33 |     0.41 |   0.5  |      0.41 |      0.61 |   0.4  |   0.2  |   0.3  |   -1    |     0.14 |    0.2 |  0.5  |      -1    |  -1   |
| Brian    |     0.47 |    0.5 |    0.52 |   -1    |   0.43 |  0.43 |     0.45 |   0.6  |      0.5  |      0.62 |   0.58 |   0.83 |   0.54 |    0.5  |    -1    |    0.5 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |    0.44 |    0.43 |  -1    |  0    |     0.27 |   0.56 |      0.38 |      0.43 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.23 |   -1   |    0.33 |    0.43 |   0    | -1    |     0.08 |   0.36 |      0.31 |      0.56 |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.42 |   -1   |    0.41 |    0.45 |   0.27 |  0.08 |    -1    |   0.48 |      0.46 |      0.5  |   0    |  -1    |   0.5  |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.4  |    0.6 |    0.5  |    0.6  |   0.56 |  0.36 |     0.48 |  -1    |      0.42 |      0.61 |   0.27 |  -1    |   0.58 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.37 |   -1   |    0.41 |    0.5  |   0.38 |  0.31 |     0.46 |   0.42 |     -1    |      0.56 |   0.43 |   0.4  |   0.44 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1   |
| Abishek  |     0.57 |    0.4 |    0.61 |    0.62 |   0.43 |  0.56 |     0.5  |   0.61 |      0.56 |     -1    |   0.53 |   0.83 |   0.55 |   -1    |    -1    |    0.5 |  0.57 |      -1    |   0.2 |
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
|---------|---------|-------|--------|--------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|
| Rachel   |    -1    |   -1   |    0.28 |    0.44 |   0.44 |  0.25 |     0.42 |   0.38 |      0.38 |      0.55 |   0    |   0.33 |   0.41 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.28 |   -1   |   -1    |    0.5  |   0.29 |  0.29 |     0.37 |   0.41 |      0.38 |      0.57 |   0.4  |  -1    |   0.27 |   -1    |     0.14 |    0.2 |  0.5  |      -1    |
| Brian    |     0.44 |    0.5 |    0.5  |   -1    |   0.38 |  0.4  |     0.44 |   0.57 |      0.49 |      0.61 |   0.5  |  -1    |   0.52 |    0.5  |    -1    |    0.5 | -1    |      -1    |
| Minh     |     0.44 |   -1   |    0.29 |    0.38 |  -1    |  0    |     0.08 |   0.46 |      0.29 |      0.4  |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.25 |   -1   |    0.29 |    0.4  |   0    | -1    |     0.08 |   0.36 |      0.31 |      0.53 |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.42 |   -1   |    0.37 |    0.44 |   0.08 |  0.08 |    -1    |   0.42 |      0.41 |      0.48 |   0    |  -1    |   0.47 |    0.33 |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.38 |    0.6 |    0.41 |    0.57 |   0.46 |  0.36 |     0.42 |  -1    |      0.36 |      0.57 |   0.27 |  -1    |   0.57 |    0.6  |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.38 |   -1   |    0.38 |    0.49 |   0.29 |  0.31 |     0.41 |   0.36 |     -1    |      0.54 |   0.43 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.12 |      -1    |
| Abishek  |     0.55 |    0.4 |    0.57 |    0.61 |   0.4  |  0.53 |     0.48 |   0.57 |      0.54 |     -1    |   0.5  |   0.8  |   0.54 |   -1    |    -1    |    0.5 |  0.57 |      -1    |
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
|---------|-------|---------|-------|------|-------|----------|----------|-------|--------|--------|---------|-------|------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |    0.67 |   -1    |    -1    |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      0.83 |      1    |  -1    |    0.75 |    0.5  |     1    |   0.5  | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |   0    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.83 |    0.25 |     0.25 |   1    | -1    |
| Sushant  |   0.33 |     0.83 |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.73 |    0.64 |     0.5  |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.5  |  0.33 |
| Brian    |   0.67 |     0.75 |      1 | -1    |   0.83 |      0.71 |      0.73 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.25 |      0.58 |      0.64 |   0.75 |    0.89 |   -1    |     0.8  |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |   0.25 |      0.67 |      0.5  |  -1    |    0.8  |    0.8  |    -1    |  -1    | -1    |
| Alex     |  -1    |     0.5  |     -1 |  0    |   1    |      0.67 |      0.88 |   0.5  |    0.83 |    0.33 |    -1    |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |
|---------|-------|---------|-------|------|-------|----------|----------|-------|--------|--------|---------|-------|------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |    0.67 |   -1    |    -1    |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      1    |      1    |  -1    |    0.75 |    0.5  |     1    |   0.75 | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |    -1    |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |    -1    |  -1    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.29 |      0.85 |   0.33 |    0.83 |    0.25 |     0.25 |   1    | -1    |
| Sushant  |   0.33 |     1    |     -1 |  0.33 |   0.29 |     -1    |      0.79 |   0.67 |    0.71 |    0.58 |     0.67 |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.85 |      0.79 |     -1    |   0.67 |    0.85 |    0.64 |     0.5  |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |   0.33 |      0.67 |      0.67 |  -1    |   -1    |    0.75 |    -1    |   0.75 |  0.33 |
| Brian    |   0.67 |     0.75 |      1 | -1    |   0.83 |      0.71 |      0.85 |  -1    |   -1    |    0.89 |     0.8  |   0.83 | -1    |
| Peter    |  -1    |     0.5  |     -1 |  0.25 |   0.25 |      0.58 |      0.64 |   0.75 |    0.89 |   -1    |     0.8  |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |   0.25 |      0.67 |      0.5  |  -1    |    0.8  |    0.8  |    -1    |  -1    | -1    |
| Alex     |  -1    |     0.75 |     -1 | -1    |   1    |      0.67 |      0.88 |   0.75 |    0.83 |    0.33 |    -1    |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |    -1    |  -1    | -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|---------|--------|--------|-------|---------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|------|
| Peter    |   -1    |    0.4  |   0.6  |     0.48 |    0.2 |  0.56 |     0.48 |   0.49 |      0.47 |      0.39 |   0.7  |  -1    |   0.6  |    0.4  |     -1   |   -1   | -1    |       -1   |   0.8 |
| Brian    |    0.6  |   -1    |   0.6  |     0.63 |   -1   |  0.71 |     0.58 |   0.57 |      0.57 |      0.48 |   0.73 |   0.64 |   0.64 |   -1    |      0.6 |   -1   |  0.55 |       -1   |  -1   |
| Minh     |    0.4  |    0.4  |  -1    |     0.5  |   -1   |  0.67 |     0.54 |   0.28 |      0.33 |      0.41 |  -1    |  -1    |   0.33 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Rachel   |    0.52 |    0.37 |   0.5  |    -1    |   -1   |  0.55 |     0.55 |   0.44 |      0.45 |      0.33 |   0.62 |   0.6  |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.29 |   0.33 |     0.45 |   -1   | -1    |     0.45 |   0.29 |      0.38 |      0.24 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Jackie   |    0.52 |    0.42 |   0.46 |     0.45 |   -1   |  0.55 |    -1    |   0.46 |      0.38 |      0.39 |   0.5  |  -1    |   0.53 |   -1    |     -1   |   -1   | -1    |       -1   |  -1   |
| Kate     |    0.51 |    0.43 |   0.72 |     0.56 |    0.5 |  0.71 |     0.54 |  -1    |      0.57 |      0.44 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |    0.8 |  0.44 |       -1   |  -1   |
| Sushant  |    0.53 |    0.43 |   0.67 |     0.55 |   -1   |  0.62 |     0.62 |   0.42 |     -1    |      0.36 |   0.6  |   0.4  |   0.42 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |   0.8 |
| Abishek  |    0.61 |    0.52 |   0.59 |     0.67 |   -1   |  0.76 |     0.61 |   0.56 |      0.64 |     -1    |   0.74 |   0.71 |   0.58 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |  -1   |
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
|---------|--------|--------|-------|---------|-------|------|---------|-------|----------|----------|-------|-------|-------|--------|---------|-------|------|-----------|
| Peter    |   -1    |    0.37 |   0.6  |     0.44 |    0.2 |  0.53 |     0.48 |   0.49 |      0.45 |      0.36 |   0.67 |  -1    |   0.57 |    0.4  |     -1   |   -1   | -1    |       -1   |
| Brian    |    0.63 |   -1    |   0.64 |     0.61 |   -1   |  0.69 |     0.62 |   0.59 |      0.58 |      0.48 |   0.7  |   0.6  |   0.63 |   -1    |      0.6 |   -1   |  0.55 |       -1   |
| Minh     |    0.4  |    0.36 |  -1    |     0.5  |   -1   |  0.6  |     0.54 |   0.29 |      0.33 |      0.36 |  -1    |  -1    |   0.29 |   -1    |     -1   |   -1   | -1    |       -1   |
| Rachel   |    0.56 |    0.39 |   0.5  |    -1    |   -1   |  0.6  |     0.57 |   0.47 |      0.48 |      0.36 |   0.62 |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   |   -1   | -1    |       -1   |
| Jai      |    0.47 |    0.31 |   0.4  |     0.4  |   -1   | -1    |     0.5  |   0.33 |      0.38 |      0.26 |   0.4  |  -1    |   0.25 |   -1    |     -1   |   -1   | -1    |       -1   |
| Jackie   |    0.52 |    0.38 |   0.46 |     0.43 |   -1   |  0.5  |    -1    |   0.46 |      0.38 |      0.36 |   0.43 |  -1    |   0.5  |   -1    |     -1   |   -1   | -1    |       -1   |
| Kate     |    0.51 |    0.41 |   0.71 |     0.53 |    0.5 |  0.67 |     0.54 |  -1    |      0.57 |      0.42 |   0.62 |   0.33 |   0.48 |   -1    |     -1   |    0.8 |  0.44 |       -1   |
| Sushant  |    0.55 |    0.42 |   0.67 |     0.52 |   -1   |  0.62 |     0.62 |   0.42 |     -1    |      0.35 |   0.57 |  -1    |   0.39 |    0.62 |      0.6 |   -1   |  0.17 |       -1   |
| Abishek  |    0.64 |    0.52 |   0.64 |     0.64 |   -1   |  0.74 |     0.64 |   0.57 |      0.65 |     -1    |   0.71 |   0.67 |   0.56 |    0.6  |      0.6 |   -1   |  0.71 |        0.8 |
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

| Strategy   |   Win % |   Sample Size |
|-----------|--------|--------------|
| 3+1        | 0.34375 |            32 |
| 2+2        | 0.375   |            72 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|-----------|---------|--------------|
| 3+1        | 0.3      |            30 |
| 2+2        | 0.338235 |            68 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.433333 |            30 |
| Success      | 0.309735 |           113 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|-------------|---------|--------------|
| Fail         | 0.433333 |            30 |
| Success      | 0.297297 |           111 |

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
|                   0 |            88 |     0.5      |
|                   1 |           118 |     0.364407 |
|                   2 |            16 |     0.5625   |
|                   3 |             5 |     0.4      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|--------------------|--------------|-------------|
|                   0 |            83 |     0.46988  |
|                   1 |           112 |     0.330357 |
|                   2 |            16 |     0.5625   |
|                   3 |             5 |     0.4      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|--------------|------------------------|--------------|----------------|
| Merlin        |                 0.11013 |           227 |              25 |
| Assassin      |                 0.03704 |           189 |               7 |
| Morgana       |                 0.05882 |           221 |              13 |
| Mordred       |                 0.00781 |           128 |               1 |
| Loyal Servant |                 0       |           629 |               0 |
| Oberon        |                 0.01471 |            68 |               1 |
| Minion #1     |                 0.05556 |            36 |               2 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|---------|----------------------------|-------------------|--------------|
| Jeron    |                    0.6      |                  3 |             5 |
| Abishek  |                    0.457143 |                 16 |            35 |
| Minh     |                    0.444444 |                  4 |             9 |
| Alex     |                    0.363636 |                  8 |            22 |
| Jai      |                    0.3125   |                  5 |            16 |
| Kate     |                    0.288889 |                 13 |            45 |
| Rachel   |                    0.269231 |                  7 |            26 |
| Jackie   |                    0.257143 |                  9 |            35 |
| Peter    |                    0.2      |                  7 |            35 |
| Sushant  |                    0.2      |                  4 |            20 |
| Ruhi     |                    0.2      |                  1 |             5 |
| Tercel   |                    0.2      |                  1 |             5 |
| Brian    |                    0.183673 |                  9 |            49 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)


*Competitive games only statistic.*

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|---------|------------------|-------------------|--------------|
| Minh     |          0        |                  0 |             4 |
| Brian    |          0.125    |                  1 |             8 |
| Kate     |          0.3      |                  3 |            10 |
| Sushant  |          0.333333 |                  3 |             9 |
| Jeron    |          0.333333 |                  1 |             3 |
| Abishek  |          0.444444 |                  4 |             9 |
| Alex     |          0.5      |                  2 |             4 |
| Peter    |          0.545455 |                  6 |            11 |
| Jai      |          0.6      |                  3 |             5 |
| Rachel   |          0.666667 |                  6 |             9 |
| Jackie   |          0.75     |                  3 |             4 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

| # Players   |   Assassination % |   # Assassinations |   Sample Size |
|------------|------------------|-------------------|--------------|
| 10          |          0.428571 |                  9 |            21 |
| 5           |          0.75     |                  6 |             8 |
| 5O          |          0.333333 |                  3 |             9 |
| 5X          |          0.5      |                  2 |             4 |
| 6           |          0.285714 |                  6 |            21 |
| 6M          |          0.363636 |                  4 |            11 |
| 6O          |          0.25     |                  3 |            12 |
| 7           |          0.580645 |                 18 |            31 |
| 7O          |          0.6      |                  3 |             5 |
| 8           |          0.526316 |                 10 |            19 |
| 8O          |          0.666667 |                  2 |             3 |
| 9           |          0.458333 |                 11 |            24 |
| 9L          |          0.333333 |                  1 |             3 |
| 9O          |          0        |                  0 |             1 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

| # Players   |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|------------|--------------------|------------------|-------------------|--------------|
| 10          |                   0 |          1        |                  1 |             1 |
| 10          |                   1 |          0.4375   |                  7 |            16 |
| 10          |                   2 |          0        |                  0 |             3 |
| 10          |                   3 |          1        |                  1 |             1 |
| 5           |                   0 |          0.5      |                  2 |             4 |
| 5           |                   1 |          1        |                  4 |             4 |
| 5O          |                   0 |          0.25     |                  2 |             8 |
| 5O          |                   1 |          1        |                  1 |             1 |
| 5X          |                   0 |          0.5      |                  2 |             4 |
| 6           |                   0 |          0.363636 |                  4 |            11 |
| 6           |                   1 |          0.222222 |                  2 |             9 |
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
| 9           |                   0 |          0.5      |                  3 |             6 |
| 9           |                   1 |          0.4375   |                  7 |            16 |
| 9           |                   2 |          0.5      |                  1 |             2 |
| 9L          |                   0 |          1        |                  1 |             1 |
| 9L          |                   1 |          0        |                  0 |             2 |
| 9O          |                   2 |          0        |                  0 |             1 |
