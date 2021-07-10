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

Cheesy wins included: 0.3864 (n = 132)

Cheesy wins excluded: 0.3468 (n = 124)

**Good win % w.r.t. # players:**

Cheesy wins included:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           5 |             5 |     0.2      |
|           6 |            19 |     0.631579 |
|           7 |            21 |     0.428571 |
|           8 |            32 |     0.28125  |
|           9 |            32 |     0.34375  |
|          10 |            23 |     0.391304 |

Cheesy wins excluded:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           5 |             5 |     0.2      |
|           6 |            18 |     0.611111 |
|           7 |            18 |     0.333333 |
|           8 |            32 |     0.28125  |
|           9 |            29 |     0.275862 |
|          10 |            22 |     0.363636 |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            66 |       32.4091 |     21.4261 |
| Good     |            39 |       22.7692 |     16.6393 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            66 |       32.4091 |     21.4261 |
| Good     |            35 |       24.3714 |     16.8402 |

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
| Abishek  | 0.608247 |     0.491228 |    0.775    |            97 |     59 |       38 |                      0 |
| Brian    | 0.55     |     0.441176 |    0.78125  |           100 |     55 |       45 |                     15 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                      4 |
| Kate     | 0.518072 |     0.433962 |    0.666667 |            83 |     43 |       40 |                     20 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|----------|----------|--------------|-------------|---------------|--------|----------|------------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.588889 |     0.431373 |    0.794872 |            90 |     53 |       37 |                      3 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Brian    | 0.526882 |     0.387097 |    0.806452 |            93 |     49 |       44 |                     18 |
| Kish     | 0.5      |     0.375    |    0.666667 |            14 |      7 |        7 |                      4 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Abishek  |             0.101578  | 0.608247 |         0.50667  | 0.587629 |
| Brian    |             0.0888998 | 0.55     |         0.4611   | 0.68     |
| Kish     |             0.0839853 | 0.529412 |         0.445426 | 0.588235 |
| Ewen     |             0.0449665 | 0.538462 |         0.493495 | 0.615385 |
| Kate     |             0.0448642 | 0.518072 |         0.473208 | 0.638554 |
| Jackie   |             0.0152276 | 0.45283  |         0.437603 | 0.754717 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Abishek  |             0.0925972 | 0.588889 |         0.496292 | 0.587629 |
| Anthony  |             0.0881818 | 0.6      |         0.511818 | 0.166667 |
| Brian    |             0.0801914 | 0.526882 |         0.44669  | 0.68     |
| Ewen     |             0.0709141 | 0.538462 |         0.467547 | 0.615385 |
| Kish     |             0.0320387 | 0.5      |         0.467961 | 0.588235 |
| Kate     |             0.027136  | 0.493506 |         0.46637  | 0.638554 |
| Jeron    |             0.0158046 | 0.5      |         0.484195 | 0.583333 |

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

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|---------|---------------|--------|----------|-----------------------|
| Jackie   |  0.625  |             8 |      5 |        3 |                     0 |
| Kate     |  0.6    |            10 |      6 |        4 |                     1 |
| Brian    |  0.4375 |            16 |      7 |        9 |                     9 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.8      |            10 |      8 |        2 |                      0 |
| Brian    | 0.777778 |             9 |      7 |        2 |                      2 |
| Sushant  | 0.727273 |            11 |      8 |        3 |                      5 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Peter    | 0.833333 |             6 |      5 |        1 |                      2 |
| Brian    | 0.733333 |            15 |     11 |        4 |                     14 |

*Mordred:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|---------|---------------|--------|----------|---------------------|
| Kate     |       1 |             9 |      9 |        0 |                   0 |
| Brian    |       1 |             7 |      7 |        0 |                 nan |
| Peter    |       1 |             6 |      6 |        0 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.62069  |            29 |     18 |       11 |                      0 |
| Ruhi     | 0.5      |            12 |      6 |        6 |                      4 |
| Rachel   | 0.464286 |            28 |     13 |       15 |                     12 |


*Cheesy wins excluded.*


*Merlin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Brian |
|----------|----------|---------------|--------|----------|----------------------|
| Brian    | 0.555556 |             9 |      5 |        4 |                    0 |
| Kate     | 0.555556 |             9 |      5 |        4 |                    1 |
| Sushant  | 0.428571 |            14 |      6 |        8 |                    5 |

*Percival:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Jackie |
|----------|----------|---------------|--------|----------|-----------------------|
| Jackie   | 0.625    |             8 |      5 |        3 |                     0 |
| Kate     | 0.5      |             8 |      4 |        4 |                     3 |
| Abishek  | 0.333333 |            18 |      6 |       12 |                    15 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.888889 |             9 |      8 |        1 |                      0 |
| Sushant  | 0.8      |            10 |      8 |        2 |                      9 |
| Brian    | 0.777778 |             9 |      7 |        2 |                     10 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.857143 |            14 |     12 |        2 |                      0 |
| Peter    | 0.833333 |             6 |      5 |        1 |                      2 |
| Brian    | 0.785714 |            14 |     11 |        3 |                      8 |

*Mordred:*

| Player   |   Win % |   Sample Size |   Wins |   Losses |   Games Behind Kate |
|----------|---------|---------------|--------|----------|---------------------|
| Kate     |       1 |             9 |      9 |        0 |                   0 |
| Brian    |       1 |             7 |      7 |        0 |                 nan |
| Peter    |       1 |             6 |      6 |        0 |                 nan |

*Loyal Servant:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.541667 |            24 |     13 |       11 |                      0 |
| Rachel   | 0.423077 |            26 |     11 |       15 |                      7 |
| Ruhi     | 0.4      |            10 |      4 |        6 |                      4 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|----------|----------------|
| Brian    |            118 |
| Abishek  |            111 |
| Kate     |            100 |
| Peter    |             99 |
| Sushant  |             92 |
| Rachel   |             83 |
| Alex     |             80 |
| Jackie   |             76 |
| Jai      |             49 |
| Minh     |             49 |
| Ruhi     |             33 |
| Jay      |             19 |
| Kish     |             17 |
| Jeron    |             17 |
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
| Jackie   | 0.75     |       57 |      19 |
| Jeron    | 0.705882 |       12 |       5 |
| Rachel   | 0.686747 |       57 |      26 |
| Justin   | 0.666667 |        6 |       3 |
| Kate     | 0.65     |       65 |      35 |
| Brian    | 0.644068 |       76 |      42 |
| Alex     | 0.6375   |       51 |      29 |
| Jai      | 0.632653 |       31 |      18 |
| Jay      | 0.631579 |       12 |       7 |
| Sai      | 0.625    |        5 |       3 |
| Ewen     | 0.615385 |        8 |       5 |
| Peter    | 0.606061 |       60 |      39 |
| Abishek  | 0.594595 |       66 |      45 |
| Kish     | 0.588235 |       10 |       7 |
| Sushant  | 0.586957 |       54 |      38 |
| Minh     | 0.530612 |       26 |      23 |
| Ruhi     | 0.484848 |       16 |      17 |
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
| No                 |           118 |     0.415254 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           118 |     0.415254 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       14 |         19 |         12 |        15 |         6 |        7 |           5 |              33 |           111 |
| Alex     |        7 |         13 |         12 |        11 |         4 |        1 |           1 |              31 |            80 |
| Anthony  |        0 |          1 |          3 |         2 |         0 |        0 |           0 |               0 |             6 |
| Brian    |       12 |         17 |         10 |        22 |         9 |        0 |           1 |              47 |           118 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       13 |         11 |          5 |         5 |         4 |        4 |           1 |              33 |            76 |
| Jade     |        3 |          1 |          0 |         0 |         1 |        1 |           0 |               4 |            10 |
| Jai      |        6 |          4 |          5 |         5 |         5 |        3 |           0 |              21 |            49 |
| Jay      |        3 |          3 |          3 |         0 |         3 |        1 |           0 |               6 |            19 |
| Jeron    |        3 |          7 |          1 |         2 |         1 |        1 |           0 |               2 |            17 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       10 |         11 |          8 |        10 |         9 |        6 |           2 |              44 |           100 |
| Kish     |        1 |          3 |          1 |         3 |         2 |        0 |           1 |               6 |            17 |
| Minh     |        6 |          4 |         10 |         5 |         5 |        1 |           2 |              16 |            49 |
| Peter    |       15 |         12 |         16 |        10 |         7 |        4 |           2 |              33 |            99 |
| Rachel   |       15 |         10 |          8 |         8 |         9 |        0 |           1 |              32 |            83 |
| Ruhi     |        1 |          3 |          4 |         7 |         5 |        1 |           0 |              12 |            33 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       15 |          5 |         12 |        16 |         8 |        1 |           1 |              34 |            92 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.109 |      0.146 |      0.103 |     0.118 |     0.072 |    0.2   |       0.294 |           0.085 |           111 |
| Alex     |    0.054 |      0.1   |      0.103 |     0.087 |     0.048 |    0.029 |       0.059 |           0.08  |            80 |
| Anthony  |    0     |      0.008 |      0.026 |     0.016 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.093 |      0.131 |      0.085 |     0.173 |     0.108 |    0     |       0.059 |           0.122 |           118 |
| Ewen     |    0.008 |      0.015 |      0.017 |     0.008 |     0     |    0.057 |       0     |           0.013 |            13 |
| Gathenji |    0     |      0     |      0     |     0.008 |     0     |    0     |       0     |           0.016 |             7 |
| Jackie   |    0.101 |      0.085 |      0.043 |     0.039 |     0.048 |    0.114 |       0.059 |           0.085 |            76 |
| Jade     |    0.023 |      0.008 |      0     |     0     |     0.012 |    0.029 |       0     |           0.01  |            10 |
| Jai      |    0.047 |      0.031 |      0.043 |     0.039 |     0.06  |    0.086 |       0     |           0.054 |            49 |
| Jay      |    0.023 |      0.023 |      0.026 |     0     |     0.036 |    0.029 |       0     |           0.016 |            19 |
| Jeron    |    0.023 |      0.054 |      0.009 |     0.016 |     0.012 |    0.029 |       0     |           0.005 |            17 |
| Justin   |    0.016 |      0     |      0.009 |     0.008 |     0.012 |    0     |       0     |           0.01  |             9 |
| Kate     |    0.078 |      0.085 |      0.068 |     0.079 |     0.108 |    0.171 |       0.118 |           0.114 |           100 |
| Kish     |    0.008 |      0.023 |      0.009 |     0.024 |     0.024 |    0     |       0.059 |           0.016 |            17 |
| Minh     |    0.047 |      0.031 |      0.085 |     0.039 |     0.06  |    0.029 |       0.118 |           0.041 |            49 |
| Peter    |    0.116 |      0.092 |      0.137 |     0.079 |     0.084 |    0.114 |       0.118 |           0.085 |            99 |
| Rachel   |    0.116 |      0.077 |      0.068 |     0.063 |     0.108 |    0     |       0.059 |           0.083 |            83 |
| Ruhi     |    0.008 |      0.023 |      0.034 |     0.055 |     0.06  |    0.029 |       0     |           0.031 |            33 |
| Sai      |    0.008 |      0.008 |      0     |     0.008 |     0.024 |    0     |       0     |           0.008 |             8 |
| Sushant  |    0.116 |      0.038 |      0.103 |     0.126 |     0.096 |    0.029 |       0.059 |           0.088 |            92 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.126 |      0.171 |      0.108 |     0.135 |     0.054 |    0.063 |       0.045 |           0.297 |           111 |
| Alex     |    0.088 |      0.162 |      0.15  |     0.138 |     0.05  |    0.012 |       0.012 |           0.388 |            80 |
| Anthony  |    0     |      0.167 |      0.5   |     0.333 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.102 |      0.144 |      0.085 |     0.186 |     0.076 |    0     |       0.008 |           0.398 |           118 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.171 |      0.145 |      0.066 |     0.066 |     0.053 |    0.053 |       0.013 |           0.434 |            76 |
| Jade     |    0.3   |      0.1   |      0     |     0     |     0.1   |    0.1   |       0     |           0.4   |            10 |
| Jai      |    0.122 |      0.082 |      0.102 |     0.102 |     0.102 |    0.061 |       0     |           0.429 |            49 |
| Jay      |    0.158 |      0.158 |      0.158 |     0     |     0.158 |    0.053 |       0     |           0.316 |            19 |
| Jeron    |    0.176 |      0.412 |      0.059 |     0.118 |     0.059 |    0.059 |       0     |           0.118 |            17 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.1   |      0.11  |      0.08  |     0.1   |     0.09  |    0.06  |       0.02  |           0.44  |           100 |
| Kish     |    0.059 |      0.176 |      0.059 |     0.176 |     0.118 |    0     |       0.059 |           0.353 |            17 |
| Minh     |    0.122 |      0.082 |      0.204 |     0.102 |     0.102 |    0.02  |       0.041 |           0.327 |            49 |
| Peter    |    0.152 |      0.121 |      0.162 |     0.101 |     0.071 |    0.04  |       0.02  |           0.333 |            99 |
| Rachel   |    0.181 |      0.12  |      0.096 |     0.096 |     0.108 |    0     |       0.012 |           0.386 |            83 |
| Ruhi     |    0.03  |      0.091 |      0.121 |     0.212 |     0.152 |    0.03  |       0     |           0.364 |            33 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.163 |      0.054 |      0.13  |     0.174 |     0.087 |    0.011 |       0.011 |           0.37  |            92 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.44 |    0.46 |      0.33 |   0.36 |  0.59 |     0.52 |   0.49 |      0.48 |      0.36 |   0.33 |   0.58 |   0.56 |    0.9  |     0.57 |   0.67 |  0.62 |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.44 |   0.17 |    1    |    0.53 |     -1    |   0.38 |  0.41 |     0.48 |   0.38 |      0.54 |      0.45 |   0.5  |   0.62 |   0.45 |    0.36 |     0.78 |   0.71 |  0.69 |      -1    |  0.29 |
| Brian    |     0.46 |   0.83 |    0.53 |    1    |      0.33 |   0.37 |  0.51 |     0.55 |   0.52 |      0.41 |      0.48 |   0.38 |   0.35 |   0.48 |    0.6  |     0.44 |   0.71 |  0.2  |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |      1    |   0.5  | -1    |    -1    |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.36 |   0.4  |    0.38 |    0.37 |      0.5  |   1    |  0.5  |     0.44 |   0.46 |      0.6  |      0.55 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.59 |   0.4  |    0.41 |    0.51 |     -1    |   0.5  |  1    |     0.5  |   0.63 |      0.37 |      0.42 |   0.18 |  -1    |   0.53 |   -1    |    -1    |  -1    |  0.29 |       0.8  | -1    |
| Jackie   |     0.52 |   0.33 |    0.48 |    0.55 |     -1    |   0.44 |  0.5  |     1    |   0.53 |      0.5  |      0.47 |   0.27 |   0.43 |   0.56 |    0.64 |    -1    |  -1    |  0.62 |      -1    |  0.4  |
| Kate     |     0.49 |   0.45 |    0.38 |    0.52 |      0.33 |   0.46 |  0.63 |     0.53 |   1    |      0.42 |      0.51 |   0.38 |   0.29 |   0.43 |    0.78 |     0.83 |   0.44 |  0.33 |       0.57 |  0.5  |
| Sushant  |     0.48 |   0.43 |    0.54 |    0.41 |     -1    |   0.6  |  0.37 |     0.5  |   0.42 |      1    |      0.47 |   0.48 |   0.5  |   0.44 |    0.27 |     0.17 |   0.57 |  0.53 |       0.5  |  0.38 |
| Abishek  |     0.36 |   0.56 |    0.45 |    0.48 |      0.2  |   0.55 |  0.42 |     0.47 |   0.51 |      0.47 |      1    |   0.47 |   0.46 |   0.46 |    0.13 |     0.38 |   0.71 |  0.53 |       0.29 |  0.62 |
| Ruhi     |     0.33 |  -1    |    0.5  |    0.38 |     -1    |   0.56 |  0.18 |     0.27 |   0.38 |      0.48 |      0.47 |   1    |   0.67 |   0.53 |    0.17 |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.58 |   0    |    0.62 |    0.35 |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.56 |   0.2  |    0.45 |    0.48 |     -1    |   0.32 |  0.53 |     0.56 |   0.43 |      0.44 |      0.46 |   0.53 |  -1    |   1    |    0.67 |     0.67 |   0.2  |  0.44 |       0.4  |  0.5  |
| Jeron    |     0.9  |  -1    |    0.36 |    0.6  |     -1    |   0.33 | -1    |     0.64 |   0.78 |      0.27 |      0.13 |   0.17 |  -1    |   0.67 |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.67 |  -1    |    0.71 |    0.71 |     -1    |   0    | -1    |    -1    |   0.44 |      0.57 |      0.71 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.62 |  -1    |    0.69 |    0.2  |     -1    |  -1    |  0.29 |     0.62 |   0.33 |      0.53 |      0.53 |   0.57 |  -1    |   0.44 |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.06 |    0.06 |      0.33 |   0.12 |  0.14 |     0.06 |   0.1  |      0.11 |      0.06 |   0.11 |   0.17 |   0.12 |    0.1  |     0    |   0.17 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.06 |   0    |   -1    |    0.15 |     -1    |   0.16 |  0.15 |     0.05 |   0.06 |      0.17 |      0.15 |   0.22 |   0    |   0.08 |    0    |     0.11 |   0.29 |  0.31 |      -1    |  0    |
| Brian    |     0.06 |   0.25 |    0.15 |   -1    |      0.33 |   0.12 |  0.05 |     0.11 |   0.12 |      0.07 |      0.13 |   0.03 |   0.12 |   0.09 |    0.07 |     0    |   0    |  0    |       0    |  0.12 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |     -1    |   0.33 | -1    |    -1    |   0.17 |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.12 |   0.2  |    0.16 |    0.12 |      0.33 |  -1    |  0.14 |     0.03 |   0.15 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.14 |   0    |    0.15 |    0.05 |     -1    |   0.14 | -1    |     0.03 |   0.16 |      0.11 |      0.13 |   0.18 |  -1    |   0.16 |   -1    |    -1    |  -1    |  0.14 |       0    | -1    |
| Jackie   |     0.06 |   0    |    0.05 |    0.11 |     -1    |   0.03 |  0.03 |    -1    |   0.05 |      0.08 |      0.08 |   0    |   0.29 |   0.08 |    0.18 |    -1    |  -1    |  0    |      -1    |  0.2  |
| Kate     |     0.1  |   0.09 |    0.06 |    0.12 |      0.17 |   0.15 |  0.16 |     0.05 |  -1    |      0.12 |      0.13 |   0.08 |   0    |   0.1  |    0.22 |     0.33 |   0.11 |  0.06 |       0    |  0.12 |
| Sushant  |     0.11 |   0.14 |    0.17 |    0.07 |     -1    |   0.23 |  0.11 |     0.08 |   0.12 |     -1    |      0.16 |   0.19 |   0    |   0.11 |    0    |     0    |   0    |  0.16 |       0    |  0.12 |
| Abishek  |     0.06 |   0.11 |    0.15 |    0.13 |      0    |   0.12 |  0.13 |     0.08 |   0.13 |      0.16 |     -1    |   0.19 |   0.15 |   0.11 |    0    |     0.25 |   0    |  0.11 |       0    |  0.12 |
| Ruhi     |     0.11 |  -1    |    0.22 |    0.03 |     -1    |   0.22 |  0.18 |     0    |   0.08 |      0.19 |      0.19 |  -1    |   0.17 |   0.35 |    0    |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.17 |   0    |    0    |    0.12 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.12 |   0    |    0.08 |    0.09 |     -1    |   0.08 |  0.16 |     0.08 |   0.1  |      0.11 |      0.11 |   0.35 |  -1    |  -1    |    0.17 |     0    |   0    |  0.11 |       0    |  0.17 |
| Jeron    |     0.1  |  -1    |    0    |    0.07 |     -1    |   0.17 | -1    |     0.18 |   0.22 |      0    |      0    |   0    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.17 |  -1    |    0.29 |    0    |     -1    |   0    | -1    |    -1    |   0.11 |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jay      |     0    |  -1    |    0.31 |    0    |     -1    |  -1    |  0.14 |     0    |   0.06 |      0.16 |      0.11 |   0.43 |  -1    |   0.11 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     0    |   0.5  |    0.56 |    0.54 |      0.67 |   0.64 |  0.41 |     0.48 |   0.51 |      0.52 |      0.64 |   0.67 |   0.42 |   0.44 |    0.1  |     0.43 |   0.33 |  0.38 |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.56 |   0.83 |    0    |    0.47 |     -1    |   0.62 |  0.59 |     0.52 |   0.62 |      0.46 |      0.55 |   0.5  |   0.38 |   0.55 |    0.64 |     0.22 |   0.29 |  0.31 |      -1    |  0.71 |
| Brian    |     0.54 |   0.17 |    0.47 |    0    |      0.67 |   0.63 |  0.49 |     0.45 |   0.48 |      0.59 |      0.52 |   0.62 |   0.65 |   0.52 |    0.4  |     0.56 |   0.29 |  0.8  |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |   -1    |    0.67 |      0    |   0.5  | -1    |    -1    |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.64 |   0.6  |    0.62 |    0.63 |      0.5  |   0    |  0.5  |     0.56 |   0.54 |      0.4  |      0.45 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   1    | -1    |      -1    | -1    |
| Jai      |     0.41 |   0.6  |    0.59 |    0.49 |     -1    |   0.5  |  0    |     0.5  |   0.37 |      0.63 |      0.58 |   0.82 |  -1    |   0.47 |   -1    |    -1    |  -1    |  0.71 |       0.2  | -1    |
| Jackie   |     0.48 |   0.67 |    0.52 |    0.45 |     -1    |   0.56 |  0.5  |     0    |   0.47 |      0.5  |      0.53 |   0.73 |   0.57 |   0.44 |    0.36 |    -1    |  -1    |  0.38 |      -1    |  0.6  |
| Kate     |     0.51 |   0.55 |    0.62 |    0.48 |      0.67 |   0.54 |  0.37 |     0.47 |   0    |      0.58 |      0.49 |   0.62 |   0.71 |   0.57 |    0.22 |     0.17 |   0.56 |  0.67 |       0.43 |  0.5  |
| Sushant  |     0.52 |   0.57 |    0.46 |    0.59 |     -1    |   0.4  |  0.63 |     0.5  |   0.58 |      0    |      0.53 |   0.52 |   0.5  |   0.56 |    0.73 |     0.83 |   0.43 |  0.47 |       0.5  |  0.62 |
| Abishek  |     0.64 |   0.44 |    0.55 |    0.52 |      0.8  |   0.45 |  0.58 |     0.53 |   0.49 |      0.53 |      0    |   0.53 |   0.54 |   0.54 |    0.87 |     0.62 |   0.29 |  0.47 |       0.71 |  0.38 |
| Ruhi     |     0.67 |  -1    |    0.5  |    0.62 |     -1    |   0.44 |  0.82 |     0.73 |   0.62 |      0.52 |      0.53 |   0    |   0.33 |   0.47 |    0.83 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.42 |   1    |    0.38 |    0.65 |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.44 |   0.8  |    0.55 |    0.52 |     -1    |   0.68 |  0.47 |     0.44 |   0.57 |      0.56 |      0.54 |   0.47 |  -1    |   0    |    0.33 |     0.33 |   0.8  |  0.56 |       0.6  |  0.5  |
| Jeron    |     0.1  |  -1    |    0.64 |    0.4  |     -1    |   0.67 | -1    |     0.36 |   0.22 |      0.73 |      0.87 |   0.83 |  -1    |   0.33 |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.33 |  -1    |    0.29 |    0.29 |     -1    |   1    | -1    |    -1    |   0.56 |      0.43 |      0.29 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.38 |  -1    |    0.31 |    0.8  |     -1    |  -1    |  0.71 |     0.38 |   0.67 |      0.47 |      0.47 |   0.43 |  -1    |   0.56 |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |   Abrar |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|---------|
| Rachel   |       83 |      4 |      27 |      32 |         2 |     12 |    22 |       26 |     31 |        30 |        25 |      6 |      7 |     27 |          1 |        1 |        0 |       9 |        0 |        4 |      4 |       0 |     8 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |       1 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       27 |      1 |      99 |      46 |         0 |     12 |    17 |       32 |     27 |        38 |        37 |      9 |      5 |     29 |          1 |        1 |        0 |       4 |        0 |        7 |      5 |       0 |     9 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |       1 |
| Brian    |       32 |     10 |      46 |     118 |         2 |     16 |    21 |       36 |     47 |        34 |        48 |     12 |      6 |     32 |          1 |        1 |        0 |       9 |        0 |        4 |      5 |       0 |     3 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |         6 |      3 |     0 |        0 |      2 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       12 |      2 |      12 |      16 |         3 |     49 |     7 |       16 |     18 |        18 |        22 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |       0 |
| Jai      |       22 |      2 |      17 |      21 |         0 |      7 |    49 |       15 |     27 |        14 |        16 |      2 |      2 |     17 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     2 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |       26 |      2 |      32 |      36 |         0 |     16 |    15 |       76 |     30 |        26 |        29 |      3 |      3 |     27 |          0 |        0 |        1 |       7 |        1 |        1 |      1 |       1 |     5 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |       0 |
| Kate     |       31 |      5 |      27 |      47 |         2 |     18 |    27 |       30 |    100 |        29 |        43 |     10 |      4 |     26 |          0 |        0 |        0 |       7 |        0 |        5 |      4 |       1 |     6 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |       1 |
| Sushant  |       30 |      3 |      38 |      34 |         0 |     18 |    14 |       26 |     29 |        92 |        41 |     13 |      5 |     28 |          2 |        0 |        0 |       4 |        0 |        1 |      4 |       1 |    10 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Abishek  |       25 |      5 |      37 |      48 |         1 |     22 |    16 |       29 |     43 |        41 |       111 |     15 |      6 |     33 |          0 |        0 |        0 |       2 |        0 |        3 |      5 |       0 |    10 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |       1 |
| Ruhi     |        6 |      2 |       9 |      12 |         0 |      5 |     2 |        3 |     10 |        13 |        15 |     33 |      4 |      9 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        7 |      0 |       5 |       6 |         1 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     17 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       27 |      1 |      29 |      32 |         0 |      8 |    17 |       27 |     26 |        28 |        33 |      9 |      2 |     80 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       1 |     4 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        9 |      0 |       4 |       9 |         0 |      2 |     3 |        7 |      7 |         4 |         2 |      1 |      1 |      4 |          0 |        0 |        1 |      17 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |       0 |
| Jade     |        4 |      2 |       5 |       5 |         0 |      0 |     0 |        1 |      4 |         4 |         5 |      1 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |     10 |       0 |     1 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Peter    |        4 |      0 |      -1 |      13 |         0 |      5 |     6 |        3 |      4 |        12 |        12 |      4 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        1 |      2 |       0 |     4 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Brian    |        4 |      3 |      13 |      -1 |         2 |      5 |     2 |        7 |     11 |         6 |        13 |      1 |      2 |      6 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |        -1 |      2 |     0 |        0 |      1 |         0 |         0 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |        4 |      1 |       5 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jai      |        5 |      0 |       6 |       2 |         0 |      2 |    -1 |        1 |      7 |         4 |         5 |      2 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jackie   |        3 |      0 |       3 |       7 |         0 |      1 |     1 |       -1 |      3 |         4 |         5 |      0 |      2 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Kate     |        6 |      1 |       4 |      11 |         1 |      6 |     7 |        3 |     -1 |         8 |        11 |      2 |      0 |      6 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |       0 |
| Sushant  |        7 |      1 |      12 |       6 |         0 |      7 |     4 |        4 |      8 |        -1 |        14 |      5 |      0 |      7 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       1 |     3 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Abishek  |        4 |      1 |      12 |      13 |         0 |      5 |     5 |        5 |     11 |        14 |        -1 |      6 |      2 |      8 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       0 |
| Ruhi     |        2 |      1 |       4 |       1 |         0 |      2 |     2 |        0 |      2 |         5 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        2 |      0 |       0 |       2 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     5 |        4 |      6 |         7 |         8 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Shashank |        0 |      1 |       0 |       1 |         0 |      0 |     0 |        0 |      0 |         1 |         0 |      0 |      0 |      0 |         -1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |       -1 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |       -1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        1 |      0 |       0 |       1 |         0 |      1 |     0 |        2 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        1 |      -1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |       -1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Justin   |        0 |      0 |       1 |       0 |         0 |      1 |     0 |        0 |      2 |         0 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |       -1 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jade     |        1 |      0 |       2 |       0 |         0 |      0 |     0 |        0 |      1 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |     -1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |        0 |      4 |      35 |      37 |         4 |     21 |    15 |       24 |     32 |        33 |        45 |     12 |      5 |     21 |          1 |        0 |        1 |       1 |        1 |        3 |      2 |       1 |     5 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |       0 |
| Peter    |       35 |      5 |       0 |      40 |         1 |     20 |    24 |       34 |     45 |        33 |        45 |      9 |      3 |     36 |          1 |        0 |        1 |       7 |        1 |        2 |      2 |       2 |     4 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |       0 |
| Brian    |       37 |      2 |      40 |       0 |         4 |     27 |    20 |       30 |     43 |        48 |        52 |     20 |     11 |     35 |          1 |        0 |        1 |       6 |        1 |        5 |      2 |       2 |    12 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |       0 |
| Anthony  |        4 |      0 |       1 |       4 |         0 |      3 |     1 |        1 |      4 |         1 |         4 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Minh     |       21 |      3 |      20 |      27 |         3 |      0 |     7 |       20 |     21 |        12 |        18 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      5 |       0 |     3 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |       0 |
| Jai      |       15 |      3 |      24 |      20 |         1 |      7 |     0 |       15 |     16 |        24 |        22 |      9 |      0 |     15 |          1 |        0 |        0 |       1 |        0 |        2 |      3 |       0 |     5 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |       1 |
| Jackie   |       24 |      4 |      34 |      30 |         1 |     20 |    15 |        0 |     27 |        26 |        33 |      8 |      4 |     21 |          0 |        1 |        0 |       4 |        0 |        2 |      3 |       1 |     3 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |       1 |
| Kate     |       32 |      6 |      45 |      43 |         4 |     21 |    16 |       27 |      0 |        40 |        41 |     16 |     10 |     35 |          2 |        0 |        0 |       2 |        0 |        1 |      5 |       1 |    12 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |       0 |
| Sushant  |       33 |      4 |      33 |      48 |         1 |     12 |    24 |       26 |     40 |         0 |        46 |     14 |      5 |     36 |          0 |        0 |        0 |      11 |        0 |        5 |      3 |       0 |     9 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |       1 |
| Abishek  |       45 |      4 |      45 |      52 |         4 |     18 |    22 |       33 |     41 |        46 |         0 |     17 |      7 |     39 |          0 |        0 |        0 |      13 |        0 |        5 |      2 |       1 |     9 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |       0 |
| Ruhi     |       12 |      1 |       9 |      20 |         0 |      4 |     9 |        8 |     16 |        14 |        17 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      1 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |       0 |
| Kish     |        5 |      5 |       3 |      11 |         2 |      2 |     0 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |       0 |
| Alex     |       21 |      4 |      36 |      35 |         0 |     17 |    15 |       21 |     35 |        36 |        39 |      8 |      1 |      0 |          1 |        0 |        0 |       2 |        0 |        2 |      4 |       0 |     5 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |       1 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jeron    |        1 |      1 |       7 |       6 |         0 |      4 |     1 |        4 |      2 |        11 |        13 |      5 |      1 |      2 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |       0 |
| Jade     |        2 |      0 |       2 |       2 |         0 |      5 |     3 |        3 |      5 |         3 |         2 |      1 |      0 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |       0 |
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
| Rachel   |    -1    |   -1   |    0.21 |    0.43 |   0.44 |  0.2  |     0.4  |   0.42 |      0.37 |      0.55 |   0.17 |   0.43 |   0.38 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.21 |   -1   |   -1    |    0.5  |   0.43 |  0.27 |     0.42 |   0.5  |      0.42 |      0.62 |   0.44 |   0.2  |   0.3  |   -1    |     0.14 |   -1   |  0.5  |      -1    |  -1   |
| Brian    |     0.43 |    0.5 |    0.5  |   -1    |   0.38 |  0.37 |     0.42 |   0.58 |      0.48 |      0.62 |   0.58 |   0.83 |   0.52 |    0.5  |    -1    |    0.4 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |    0.43 |    0.38 |  -1    |  0    |     0.25 |   0.53 |      0.38 |      0.45 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.2  |   -1   |    0.27 |    0.37 |   0    | -1    |     0.1  |   0.35 |      0.31 |      0.5  |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.4  |   -1   |    0.42 |    0.42 |   0.25 |  0.1  |    -1    |   0.48 |      0.48 |      0.52 |  -1    |  -1    |   0.44 |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.42 |    0.6 |    0.5  |    0.58 |   0.53 |  0.35 |     0.48 |  -1    |      0.42 |      0.61 |   0.3  |  -1    |   0.55 |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.37 |   -1   |    0.42 |    0.48 |   0.38 |  0.31 |     0.48 |   0.42 |     -1    |      0.57 |   0.46 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.12 |      -1    |  -1   |
| Abishek  |     0.55 |    0.4 |    0.62 |    0.62 |   0.45 |  0.5  |     0.52 |   0.61 |      0.57 |     -1    |   0.53 |   0.83 |   0.55 |   -1    |    -1    |    0.4 |  0.57 |      -1    |   0.2 |
| Ruhi     |     0.17 |   -1   |    0.44 |    0.58 |   0.2  | -1    |    -1    |   0.3  |      0.46 |      0.53 |  -1    |  -1    |   0.56 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Alex     |     0.38 |   -1   |    0.3  |    0.52 |   0.4  |  0.33 |     0.44 |   0.55 |      0.42 |      0.55 |   0.56 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|
| Rachel   |    -1    |   -1   |    0.21 |    0.39 |   0.44 |  0.22 |     0.4  |   0.39 |      0.38 |      0.53 |  -1    |   0.33 |   0.41 |    0.33 |    -1    |   -1   |  0.4  |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.21 |   -1   |   -1    |    0.47 |   0.33 |  0.2  |     0.39 |   0.42 |      0.38 |      0.59 |   0.44 |  -1    |   0.27 |   -1    |     0.14 |   -1   |  0.5  |      -1    |
| Brian    |     0.39 |    0.5 |    0.47 |   -1    |   0.33 |  0.33 |     0.4  |   0.55 |      0.47 |      0.59 |   0.5  |  -1    |   0.5  |    0.5  |    -1    |    0.4 | -1    |      -1    |
| Minh     |     0.44 |   -1   |    0.33 |    0.33 |  -1    |  0    |     0.1  |   0.46 |      0.29 |      0.42 |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.22 |   -1   |    0.2  |    0.33 |   0    | -1    |     0.1  |   0.35 |      0.31 |      0.46 |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.4  |   -1   |    0.39 |    0.4  |   0.1  |  0.1  |    -1    |   0.42 |      0.42 |      0.5  |  -1    |  -1    |   0.41 |    0.33 |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.39 |    0.6 |    0.42 |    0.55 |   0.46 |  0.35 |     0.42 |  -1    |      0.35 |      0.57 |   0.3  |  -1    |   0.52 |    0.6  |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.38 |   -1   |    0.38 |    0.47 |   0.29 |  0.31 |     0.42 |   0.35 |     -1    |      0.54 |   0.46 |   0.4  |   0.39 |   -1    |    -1    |   -1   |  0.12 |      -1    |
| Abishek  |     0.53 |    0.4 |    0.59 |    0.59 |   0.42 |  0.46 |     0.5  |   0.57 |      0.54 |     -1    |   0.5  |   0.8  |   0.54 |   -1    |    -1    |    0.4 |  0.57 |      -1    |
| Ruhi     |    -1    |   -1   |    0.44 |    0.5  |   0.2  | -1    |    -1    |   0.3  |      0.46 |      0.5  |  -1    |  -1    |   0.67 |   -1    |    -1    |   -1   | -1    |      -1    |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Alex     |     0.41 |   -1   |    0.27 |    0.5  |  -1    |  0.4  |     0.41 |   0.52 |      0.39 |      0.54 |   0.67 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jay      |     0.4  |   -1   |    0.5  |   -1    |  -1    | -1    |    -1    |  -1    |      0.12 |      0.57 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |
|----------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |   -1    |     -1   |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      0.83 |      1    |  -1    |    0.75 |    0.33 |      1   |   0.5  | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |     -1   |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |     -1   |   0    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.33 |      0.91 |  -1    |    0.8  |    0.33 |     -1   |   1    | -1    |
| Sushant  |   0.33 |     0.83 |     -1 |  0.33 |   0.33 |     -1    |      0.83 |   0.8  |    0.67 |    0.64 |     -1   |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.91 |      0.83 |     -1    |   0.67 |    0.82 |    0.73 |      0.5 |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |  -1    |      0.8  |      0.67 |  -1    |   -1    |    0.75 |     -1   |   0.5  |  0.33 |
| Brian    |  -1    |     0.75 |      1 | -1    |   0.8  |      0.67 |      0.82 |  -1    |   -1    |    1    |      0.8 |   0.83 | -1    |
| Peter    |  -1    |     0.33 |     -1 |  0.25 |   0.33 |      0.64 |      0.73 |   0.75 |    1    |   -1    |     -1   |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |  -1    |     -1    |      0.5  |  -1    |    0.8  |   -1    |     -1   |  -1    | -1    |
| Alex     |  -1    |     0.5  |     -1 |  0    |   1    |      0.67 |      0.88 |   0.5  |    0.83 |    0.33 |     -1   |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |     -1   |  -1    | -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |   Jay |
|----------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|-------|
| Minh     |  -1    |     0.67 |     -1 | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |   -1    |     -1   |  -1    | -1    |
| Rachel   |   0.67 |    -1    |     -1 |  0    |   0.6  |      1    |      1    |  -1    |    0.75 |    0.33 |      1   |   0.75 | -1    |
| Ewen     |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |    1    |   -1    |     -1   |  -1    | -1    |
| Jai      |  -1    |     0    |     -1 | -1    |   0.67 |      0.33 |      0.8  |  -1    |   -1    |    0.25 |     -1   |  -1    | -1    |
| Kate     |   0.8  |     0.6  |     -1 |  0.67 |  -1    |      0.33 |      0.91 |  -1    |    0.8  |    0.33 |     -1   |   1    | -1    |
| Sushant  |   0.33 |     1    |     -1 |  0.33 |   0.33 |     -1    |      0.83 |   0.8  |    0.67 |    0.64 |     -1   |   0.67 | -1    |
| Abishek  |   0.6  |     1    |     -1 |  0.8  |   0.91 |      0.83 |     -1    |   0.67 |    0.9  |    0.73 |      0.5 |   0.88 | -1    |
| Ruhi     |  -1    |    -1    |     -1 | -1    |  -1    |      0.8  |      0.67 |  -1    |   -1    |    0.75 |     -1   |   0.75 |  0.33 |
| Brian    |  -1    |     0.75 |      1 | -1    |   0.8  |      0.67 |      0.9  |  -1    |   -1    |    1    |      0.8 |   0.83 | -1    |
| Peter    |  -1    |     0.33 |     -1 |  0.25 |   0.33 |      0.64 |      0.73 |   0.75 |    1    |   -1    |     -1   |   0.33 |  1    |
| Jackie   |  -1    |     1    |     -1 | -1    |  -1    |     -1    |      0.5  |  -1    |    0.8  |   -1    |     -1   |  -1    | -1    |
| Alex     |  -1    |     0.75 |     -1 | -1    |   1    |      0.67 |      0.88 |   0.75 |    0.83 |    0.33 |     -1   |  -1    | -1    |
| Jay      |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |   0.33 |   -1    |    1    |     -1   |  -1    | -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |   Sai |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|-------|
| Peter    |   -1    |    0.42 |   0.62 |     0.48 |    0.2 |  0.56 |     0.47 |   0.5  |      0.46 |      0.37 |   0.67 |  -1    |   0.64 |    0.4  |     -1   | -1    |       -1   |   0.8 |
| Brian    |    0.58 |   -1    |   0.59 |     0.63 |   -1   |  0.67 |     0.53 |   0.56 |      0.56 |      0.46 |   0.7  |   0.64 |   0.66 |   -1    |      0.6 |  0.55 |       -1   |  -1   |
| Minh     |    0.38 |    0.41 |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.27 |      0.33 |      0.4  |  -1    |  -1    |   0.33 |   -1    |     -1   | -1    |       -1   |  -1   |
| Rachel   |    0.52 |    0.37 |   0.5  |    -1    |   -1   |  0.55 |     0.53 |   0.38 |      0.43 |      0.33 |   0.58 |   0.6  |   0.25 |   -1    |     -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.33 |  -1    |     0.45 |   -1   | -1    |     0.33 |   0.23 |      0.36 |      0.25 |   0.33 |  -1    |   0.25 |   -1    |     -1   | -1    |       -1   |  -1   |
| Jackie   |    0.53 |    0.47 |   0.5  |     0.47 |   -1   |  0.67 |    -1    |   0.47 |      0.35 |      0.38 |   0.5  |  -1    |   0.53 |   -1    |     -1   | -1    |       -1   |  -1   |
| Kate     |    0.5  |    0.44 |   0.73 |     0.62 |    0.5 |  0.77 |     0.53 |  -1    |      0.57 |      0.41 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |  0.44 |       -1   |  -1   |
| Sushant  |    0.54 |    0.44 |   0.67 |     0.57 |   -1   |  0.64 |     0.65 |   0.43 |     -1    |      0.35 |   0.57 |   0.4  |   0.44 |    0.62 |      0.6 |  0.17 |       -1   |   0.8 |
| Abishek  |    0.63 |    0.54 |   0.6  |     0.67 |   -1   |  0.75 |     0.62 |   0.59 |      0.65 |     -1    |   0.71 |   0.71 |   0.62 |    0.6  |      0.6 |  0.71 |        0.8 |  -1   |
| Ruhi     |    0.33 |    0.3  |  -1    |     0.42 |   -1   |  0.67 |     0.5  |   0.38 |      0.43 |      0.29 |  -1    |  -1    |   0.62 |    0.6  |     -1   | -1    |       -1   |  -1   |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Alex     |    0.36 |    0.34 |   0.67 |     0.75 |   -1   |  0.75 |     0.47 |   0.48 |      0.56 |      0.38 |   0.38 |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|
| Peter    |   -1    |    0.41 |   0.62 |     0.44 |    0.2 |  0.53 |     0.47 |   0.5  |      0.44 |      0.35 |   0.62 |  -1    |   0.62 |    0.4  |     -1   | -1    |       -1   |
| Brian    |    0.59 |   -1    |   0.6  |     0.61 |   -1   |  0.64 |     0.56 |   0.56 |      0.56 |      0.46 |   0.67 |   0.6  |   0.66 |   -1    |      0.6 |  0.55 |       -1   |
| Minh     |    0.38 |    0.4  |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.29 |      0.33 |      0.38 |  -1    |  -1    |   0.29 |   -1    |     -1   | -1    |       -1   |
| Rachel   |    0.56 |    0.39 |   0.5  |    -1    |   -1   |  0.6  |     0.56 |   0.41 |      0.46 |      0.35 |   0.58 |  -1    |   0.25 |   -1    |     -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |
| Jai      |    0.47 |    0.36 |  -1    |     0.4  |   -1   | -1    |     0.38 |   0.27 |      0.37 |      0.28 |   0.33 |  -1    |   0.25 |   -1    |     -1   | -1    |       -1   |
| Jackie   |    0.53 |    0.44 |   0.5  |     0.44 |   -1   |  0.62 |    -1    |   0.47 |      0.35 |      0.36 |   0.43 |  -1    |   0.5  |   -1    |     -1   | -1    |       -1   |
| Kate     |    0.5  |    0.44 |   0.71 |     0.59 |    0.5 |  0.73 |     0.53 |  -1    |      0.57 |      0.4  |   0.62 |   0.33 |   0.48 |   -1    |     -1   |  0.44 |       -1   |
| Sushant  |    0.56 |    0.44 |   0.67 |     0.54 |   -1   |  0.63 |     0.65 |   0.43 |     -1    |      0.34 |   0.54 |  -1    |   0.4  |    0.62 |      0.6 |  0.17 |       -1   |
| Abishek  |    0.65 |    0.54 |   0.62 |     0.65 |   -1   |  0.72 |     0.64 |   0.6  |      0.66 |     -1    |   0.67 |   0.67 |   0.6  |    0.6  |      0.6 |  0.71 |        0.8 |
| Ruhi     |    0.38 |    0.33 |  -1    |     0.42 |   -1   |  0.67 |     0.57 |   0.38 |      0.46 |      0.33 |  -1    |  -1    |   0.62 |    0.6  |     -1   | -1    |       -1   |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Alex     |    0.38 |    0.34 |   0.71 |     0.75 |   -1   |  0.75 |     0.5  |   0.52 |      0.6  |      0.4  |   0.38 |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jay      |   -1    |    0.45 |  -1    |    -1    |   -1   | -1    |    -1    |   0.56 |      0.83 |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.347826 |            23 |
| 2+2        | 0.369565 |            46 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.318182 |            22 |
| 2+2        | 0.309524 |            42 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.4      |            20 |
| Success      | 0.323077 |            65 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.4      |            20 |
| Success      | 0.301587 |            63 |

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
|                   0 |            25 |     0.44     |
|                   1 |            89 |     0.348315 |
|                   2 |            14 |     0.571429 |
|                   3 |             4 |     0.25     |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            23 |     0.391304 |
|                   1 |            83 |     0.301205 |
|                   2 |            14 |     0.571429 |
|                   3 |             4 |     0.25     |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.12121 |           132 |              16 |
| Assassin      |                 0.04959 |           121 |               6 |
| Morgana       |                 0.06061 |           132 |               8 |
| Mordred       |                 0.01124 |            89 |               1 |
| Loyal Servant |                 0       |           400 |               0 |
| Oberon        |                 0.02857 |            35 |               1 |
| Minion #1     |                 0       |            18 |               0 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Jai      |                   0.428571  |                  3 |             7 |
| Rachel   |                   0.384615  |                  5 |            13 |
| Alex     |                   0.368421  |                  7 |            19 |
| Abishek  |                   0.32      |                  8 |            25 |
| Minh     |                   0.285714  |                  2 |             7 |
| Jackie   |                   0.277778  |                  5 |            18 |
| Kate     |                   0.272727  |                  6 |            22 |
| Peter    |                   0.2       |                  3 |            15 |
| Sushant  |                   0.153846  |                  2 |            13 |
| Brian    |                   0.0833333 |                  2 |            24 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)

| Player   |   Assassination % |   # Assassinations |   Sample Size |
|----------|-------------------|--------------------|---------------|
| Minh     |          0        |                  0 |             3 |
| Sushant  |          0.125    |                  1 |             8 |
| Brian    |          0.222222 |                  2 |             9 |
| Jeron    |          0.333333 |                  1 |             3 |
| Kate     |          0.444444 |                  4 |             9 |
| Jai      |          0.5      |                  2 |             4 |
| Abishek  |          0.5      |                  6 |            12 |
| Jackie   |          0.555556 |                  5 |             9 |
| Alex     |          0.6      |                  3 |             5 |
| Peter    |          0.615385 |                  8 |            13 |
| Rachel   |          0.636364 |                  7 |            11 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

|   # Players |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
|           5 |          0.8      |                  4 |             5 |
|           6 |          0.294118 |                  5 |            17 |
|           7 |          0.55     |                 11 |            20 |
|           8 |          0.529412 |                  9 |            17 |
|           9 |          0.4375   |                  7 |            16 |
|          10 |          0.4375   |                  7 |            16 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

|   # Players |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
|           5 |                   0 |          0.5      |                  1 |             2 |
|           5 |                   1 |          1        |                  3 |             3 |
|           6 |                   0 |          0.375    |                  3 |             8 |
|           6 |                   1 |          0.25     |                  2 |             8 |
|           6 |                   3 |          0        |                  0 |             1 |
|           7 |                   0 |          0.6      |                  6 |            10 |
|           7 |                   1 |          0.625    |                  5 |             8 |
|           7 |                   2 |          0        |                  0 |             2 |
|           8 |                   0 |          0.5      |                  1 |             2 |
|           8 |                   1 |          0.533333 |                  8 |            15 |
|           9 |                   0 |          1        |                  2 |             2 |
|           9 |                   1 |          0.363636 |                  4 |            11 |
|           9 |                   2 |          0.333333 |                  1 |             3 |
|          10 |                   1 |          0.5      |                  6 |            12 |
|          10 |                   2 |          0        |                  0 |             3 |
|          10 |                   3 |          1        |                  1 |             1 |
