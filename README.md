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

Cheesy wins included: 0.3937 (n = 127)

Cheesy wins excluded: 0.3529 (n = 119)

**Good win % w.r.t. # players:**

Cheesy wins included:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           5 |             5 |     0.2      |
|           6 |            19 |     0.631579 |
|           7 |            20 |     0.45     |
|           8 |            32 |     0.28125  |
|           9 |            29 |     0.344828 |
|          10 |            22 |     0.409091 |

Cheesy wins excluded:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           5 |             5 |     0.2      |
|           6 |            18 |     0.611111 |
|           7 |            17 |     0.352941 |
|           8 |            32 |     0.28125  |
|           9 |            26 |     0.269231 |
|          10 |            21 |     0.380952 |

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            62 |       32.3871 |     21.856  |
| Good     |            38 |       21.7895 |     15.6812 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            62 |       32.3871 |     21.856  |
| Good     |            34 |       23.3235 |     15.8931 |

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
| Abishek  | 0.595745 |     0.482143 |    0.763158 |            94 |     56 |       38 |                      0 |
| Brian    | 0.55102  |     0.447761 |    0.774194 |            98 |     54 |       44 |                     11 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      2 |
| Kish     | 0.529412 |     0.5      |    0.571429 |            17 |      9 |        8 |                      3 |
| Kate     | 0.506173 |     0.423077 |    0.655172 |            81 |     41 |       40 |                     18 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |   Wins |   Losses |   Games Behind Anthony |
|----------|----------|--------------|-------------|---------------|--------|----------|------------------------|
| Anthony  | 0.6      |     1        |    0.5      |             5 |      3 |        2 |                      0 |
| Abishek  | 0.574713 |     0.42     |    0.783784 |            87 |     50 |       37 |                      6 |
| Ewen     | 0.538462 |     0.375    |    0.8      |            13 |      7 |        6 |                      3 |
| Brian    | 0.527473 |     0.393443 |    0.8      |            91 |     48 |       43 |                     17 |
| Kish     | 0.5      |     0.375    |    0.666667 |            14 |      7 |        7 |                      4 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Kish     |             0.0912199 | 0.529412 |         0.438192 | 0.588235 |
| Brian    |             0.0883684 | 0.55102  |         0.462652 | 0.683673 |
| Abishek  |             0.087945  | 0.595745 |         0.5078   | 0.595745 |
| Ewen     |             0.0407225 | 0.538462 |         0.497739 | 0.615385 |
| Kate     |             0.035173  | 0.506173 |         0.471    | 0.641975 |
| Jackie   |             0.022647  | 0.46     |         0.437353 | 0.74     |
| Peter    |             0.0146524 | 0.465753 |         0.451101 | 0.657534 |
| Anthony  |             0.0134921 | 0.5      |         0.486508 | 0.166667 |
| Sushant  |             0.0118299 | 0.468354 |         0.456524 | 0.607595 |

Cheesy wins excluded:

| Player   |   Win % Over Expected |    Win % |   Expected Win % |   Good % |
|----------|-----------------------|----------|------------------|----------|
| Anthony  |             0.0881818 | 0.6      |         0.511818 | 0.166667 |
| Brian    |             0.0811085 | 0.527473 |         0.446364 | 0.683673 |
| Abishek  |             0.0806856 | 0.574713 |         0.494027 | 0.595745 |
| Ewen     |             0.0674624 | 0.538462 |         0.470999 | 0.615385 |
| Kish     |             0.0366174 | 0.5      |         0.463383 | 0.588235 |
| Kate     |             0.0171759 | 0.48     |         0.462824 | 0.641975 |

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
| Brian    | 0.4375   |            16 |      7 |        9 |                     9 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.8      |            10 |      8 |        2 |                      0 |
| Brian    | 0.75     |             8 |      6 |        2 |                      3 |
| Sushant  | 0.727273 |            11 |      8 |        3 |                      5 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.846154 |            13 |     11 |        2 |                      0 |
| Peter    | 0.8      |             5 |      4 |        1 |                      2 |
| Brian    | 0.733333 |            15 |     11 |        4 |                     12 |

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
| Rachel   | 0.444444 |            27 |     12 |       15 |                     12 |


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
| Kate     | 0.428571 |             7 |      3 |        4 |                     4 |
| Abishek  | 0.333333 |            18 |      6 |       12 |                    15 |

*Assassin:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.888889 |             9 |      8 |        1 |                      0 |
| Sushant  | 0.8      |            10 |      8 |        2 |                      9 |
| Brian    | 0.75     |             8 |      6 |        2 |                     11 |

*Morgana:*

| Player   |    Win % |   Sample Size |   Wins |   Losses |   Games Behind Abishek |
|----------|----------|---------------|--------|----------|------------------------|
| Abishek  | 0.846154 |            13 |     11 |        2 |                      0 |
| Peter    | 0.8      |             5 |      4 |        1 |                      2 |
| Brian    | 0.785714 |            14 |     11 |        3 |                      6 |

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
| Rachel   | 0.4      |            25 |     10 |       15 |                      7 |
| Ruhi     | 0.4      |            10 |      4 |        6 |                      3 |

### <a id="games-played"></a>Games played ranking (minimum 5 games)

| Player   |   Games Played |
|----------|----------------|
| Brian    |            116 |
| Abishek  |            106 |
| Kate     |             96 |
| Peter    |             94 |
| Sushant  |             87 |
| Rachel   |             78 |
| Alex     |             76 |
| Jackie   |             71 |
| Minh     |             49 |
| Jai      |             46 |
| Ruhi     |             33 |
| Kish     |             17 |
| Jeron    |             17 |
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
| Jackie   | 0.746479 |       53 |      18 |
| Jeron    | 0.705882 |       12 |       5 |
| Rachel   | 0.666667 |       52 |      26 |
| Justin   | 0.666667 |        6 |       3 |
| Jai      | 0.652174 |       30 |      16 |
| Brian    | 0.646552 |       75 |      41 |
| Kate     | 0.645833 |       62 |      34 |
| Alex     | 0.644737 |       49 |      27 |
| Sai      | 0.625    |        5 |       3 |
| Peter    | 0.617021 |       58 |      36 |
| Ewen     | 0.615385 |        8 |       5 |
| Sushant  | 0.597701 |       52 |      35 |
| Abishek  | 0.59434  |       63 |      43 |
| Kish     | 0.588235 |       10 |       7 |
| Jay      | 0.571429 |        8 |       6 |
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
| No                 |           113 |     0.424779 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |           113 |     0.424779 |
| Yes                  |            10 |     0        |


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |       13 |         19 |         12 |        14 |         6 |        7 |           4 |              31 |           106 |
| Alex     |        7 |         12 |         11 |        10 |         4 |        1 |           1 |              30 |            76 |
| Anthony  |        0 |          1 |          3 |         2 |         0 |        0 |           0 |               0 |             6 |
| Brian    |       12 |         17 |          9 |        22 |         9 |        0 |           1 |              46 |           116 |
| Ewen     |        1 |          2 |          2 |         1 |         0 |        2 |           0 |               5 |            13 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |       12 |         11 |          5 |         5 |         4 |        3 |           1 |              30 |            71 |
| Jade     |        3 |          1 |          0 |         0 |         1 |        1 |           0 |               4 |            10 |
| Jai      |        5 |          4 |          5 |         5 |         3 |        3 |           0 |              21 |            46 |
| Jay      |        2 |          2 |          3 |         0 |         2 |        1 |           0 |               4 |            14 |
| Jeron    |        3 |          7 |          1 |         2 |         1 |        1 |           0 |               2 |            17 |
| Justin   |        2 |          0 |          1 |         1 |         1 |        0 |           0 |               4 |             9 |
| Kate     |       10 |         10 |          8 |        10 |         8 |        6 |           2 |              42 |            96 |
| Kish     |        1 |          3 |          1 |         3 |         2 |        0 |           1 |               6 |            17 |
| Minh     |        6 |          4 |         10 |         5 |         5 |        1 |           2 |              16 |            49 |
| Peter    |       15 |         12 |         14 |         9 |         7 |        4 |           2 |              31 |            94 |
| Rachel   |       14 |          9 |          8 |         8 |         9 |        0 |           1 |              29 |            78 |
| Ruhi     |        1 |          3 |          4 |         7 |         5 |        1 |           0 |              12 |            33 |
| Sai      |        1 |          1 |          0 |         1 |         2 |        0 |           0 |               3 |             8 |
| Sushant  |       15 |          5 |         11 |        14 |         8 |        1 |           1 |              32 |            87 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.105 |      0.152 |      0.107 |     0.115 |     0.076 |    0.206 |       0.25  |           0.084 |           106 |
| Alex     |    0.056 |      0.096 |      0.098 |     0.082 |     0.051 |    0.029 |       0.062 |           0.082 |            76 |
| Anthony  |    0     |      0.008 |      0.027 |     0.016 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.097 |      0.136 |      0.08  |     0.18  |     0.114 |    0     |       0.062 |           0.125 |           116 |
| Ewen     |    0.008 |      0.016 |      0.018 |     0.008 |     0     |    0.059 |       0     |           0.014 |            13 |
| Gathenji |    0     |      0     |      0     |     0.008 |     0     |    0     |       0     |           0.016 |             7 |
| Jackie   |    0.097 |      0.088 |      0.045 |     0.041 |     0.051 |    0.088 |       0.062 |           0.082 |            71 |
| Jade     |    0.024 |      0.008 |      0     |     0     |     0.013 |    0.029 |       0     |           0.011 |            10 |
| Jai      |    0.04  |      0.032 |      0.045 |     0.041 |     0.038 |    0.088 |       0     |           0.057 |            46 |
| Jay      |    0.016 |      0.016 |      0.027 |     0     |     0.025 |    0.029 |       0     |           0.011 |            14 |
| Jeron    |    0.024 |      0.056 |      0.009 |     0.016 |     0.013 |    0.029 |       0     |           0.005 |            17 |
| Justin   |    0.016 |      0     |      0.009 |     0.008 |     0.013 |    0     |       0     |           0.011 |             9 |
| Kate     |    0.081 |      0.08  |      0.071 |     0.082 |     0.101 |    0.176 |       0.125 |           0.114 |            96 |
| Kish     |    0.008 |      0.024 |      0.009 |     0.025 |     0.025 |    0     |       0.062 |           0.016 |            17 |
| Minh     |    0.048 |      0.032 |      0.089 |     0.041 |     0.063 |    0.029 |       0.125 |           0.043 |            49 |
| Peter    |    0.121 |      0.096 |      0.125 |     0.074 |     0.089 |    0.118 |       0.125 |           0.084 |            94 |
| Rachel   |    0.113 |      0.072 |      0.071 |     0.066 |     0.114 |    0     |       0.062 |           0.079 |            78 |
| Ruhi     |    0.008 |      0.024 |      0.036 |     0.057 |     0.063 |    0.029 |       0     |           0.033 |            33 |
| Sai      |    0.008 |      0.008 |      0     |     0.008 |     0.025 |    0     |       0     |           0.008 |             8 |
| Sushant  |    0.121 |      0.04  |      0.098 |     0.115 |     0.101 |    0.029 |       0.062 |           0.087 |            87 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.123 |      0.179 |      0.113 |     0.132 |     0.057 |    0.066 |       0.038 |           0.292 |           106 |
| Alex     |    0.092 |      0.158 |      0.145 |     0.132 |     0.053 |    0.013 |       0.013 |           0.395 |            76 |
| Anthony  |    0     |      0.167 |      0.5   |     0.333 |     0     |    0     |       0     |           0     |             6 |
| Brian    |    0.103 |      0.147 |      0.078 |     0.19  |     0.078 |    0     |       0.009 |           0.397 |           116 |
| Ewen     |    0.077 |      0.154 |      0.154 |     0.077 |     0     |    0.154 |       0     |           0.385 |            13 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.169 |      0.155 |      0.07  |     0.07  |     0.056 |    0.042 |       0.014 |           0.423 |            71 |
| Jade     |    0.3   |      0.1   |      0     |     0     |     0.1   |    0.1   |       0     |           0.4   |            10 |
| Jai      |    0.109 |      0.087 |      0.109 |     0.109 |     0.065 |    0.065 |       0     |           0.457 |            46 |
| Jay      |    0.143 |      0.143 |      0.214 |     0     |     0.143 |    0.071 |       0     |           0.286 |            14 |
| Jeron    |    0.176 |      0.412 |      0.059 |     0.118 |     0.059 |    0.059 |       0     |           0.118 |            17 |
| Justin   |    0.222 |      0     |      0.111 |     0.111 |     0.111 |    0     |       0     |           0.444 |             9 |
| Kate     |    0.104 |      0.104 |      0.083 |     0.104 |     0.083 |    0.062 |       0.021 |           0.438 |            96 |
| Kish     |    0.059 |      0.176 |      0.059 |     0.176 |     0.118 |    0     |       0.059 |           0.353 |            17 |
| Minh     |    0.122 |      0.082 |      0.204 |     0.102 |     0.102 |    0.02  |       0.041 |           0.327 |            49 |
| Peter    |    0.16  |      0.128 |      0.149 |     0.096 |     0.074 |    0.043 |       0.021 |           0.33  |            94 |
| Rachel   |    0.179 |      0.115 |      0.103 |     0.103 |     0.115 |    0     |       0.013 |           0.372 |            78 |
| Ruhi     |    0.03  |      0.091 |      0.121 |     0.212 |     0.152 |    0.03  |       0     |           0.364 |            33 |
| Sai      |    0.125 |      0.125 |      0     |     0.125 |     0.25  |    0     |       0     |           0.375 |             8 |
| Sushant  |    0.172 |      0.057 |      0.126 |     0.161 |     0.092 |    0.011 |       0.011 |           0.368 |            87 |

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     1    |   0.5  |    0.44 |    0.46 |      0.33 |   0.36 |  0.62 |     0.49 |   0.47 |      0.48 |      0.34 |   0.33 |   0.58 |   0.57 |    0.9  |     0.57 |   0.67 |  0.5  |       0.86 | -1    |
| Ewen     |     0.5  |   1    |    0.17 |    0.83 |     -1    |   0.4  |  0.4  |     0.33 |   0.45 |      0.43 |      0.56 |  -1    |   0    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.44 |   0.17 |    1    |    0.52 |     -1    |   0.38 |  0.42 |     0.51 |   0.38 |      0.53 |      0.45 |   0.5  |   0.62 |   0.48 |    0.36 |     0.78 |   0.71 |  0.75 |      -1    |  0.29 |
| Brian    |     0.46 |   0.83 |    0.52 |    1    |      0.33 |   0.37 |  0.51 |     0.55 |   0.53 |      0.41 |      0.48 |   0.38 |   0.35 |   0.48 |    0.6  |     0.44 |   0.71 |  0.15 |       0.5  |  0.62 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |      1    |   0.5  | -1    |    -1    |   0.33 |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.36 |   0.4  |    0.38 |    0.37 |      0.5  |   1    |  0.5  |     0.44 |   0.46 |      0.6  |      0.55 |   0.56 |   0.67 |   0.32 |    0.33 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.62 |   0.4  |    0.42 |    0.51 |     -1    |   0.5  |  1    |     0.48 |   0.65 |      0.34 |      0.43 |   0.18 |  -1    |   0.52 |   -1    |    -1    |  -1    | -1    |       0.8  | -1    |
| Jackie   |     0.49 |   0.33 |    0.51 |    0.55 |     -1    |   0.44 |  0.48 |     1    |   0.53 |      0.49 |      0.47 |   0.27 |   0.43 |   0.55 |    0.64 |    -1    |  -1    | -1    |      -1    |  0.4  |
| Kate     |     0.47 |   0.45 |    0.38 |    0.53 |      0.33 |   0.46 |  0.65 |     0.53 |   1    |      0.45 |      0.49 |   0.38 |   0.29 |   0.4  |    0.78 |     0.83 |   0.44 |  0.29 |       0.57 |  0.5  |
| Sushant  |     0.48 |   0.43 |    0.53 |    0.41 |     -1    |   0.6  |  0.34 |     0.49 |   0.45 |      1    |      0.5  |   0.48 |   0.5  |   0.45 |    0.27 |     0.17 |   0.57 |  0.5  |       0.5  |  0.38 |
| Abishek  |     0.34 |   0.56 |    0.45 |    0.48 |      0.2  |   0.55 |  0.43 |     0.47 |   0.49 |      0.5  |      1    |   0.47 |   0.46 |   0.44 |    0.13 |     0.38 |   0.71 |  0.57 |       0.29 |  0.62 |
| Ruhi     |     0.33 |  -1    |    0.5  |    0.38 |     -1    |   0.56 |  0.18 |     0.27 |   0.38 |      0.48 |      0.47 |   1    |   0.67 |   0.53 |    0.17 |    -1    |  -1    |  0.57 |      -1    | -1    |
| Kish     |     0.58 |   0    |    0.62 |    0.35 |     -1    |   0.67 | -1    |     0.43 |   0.29 |      0.5  |      0.46 |   0.67 |   1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.57 |   0.2  |    0.48 |    0.48 |     -1    |   0.32 |  0.52 |     0.55 |   0.4  |      0.45 |      0.44 |   0.53 |  -1    |   1    |    0.67 |     0.67 |   0.2  |  0.6  |       0.4  |  0.5  |
| Jeron    |     0.9  |  -1    |    0.36 |    0.6  |     -1    |   0.33 | -1    |     0.64 |   0.78 |      0.27 |      0.13 |   0.17 |  -1    |   0.67 |    1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.57 |  -1    |    0.78 |    0.44 |     -1    |  -1    | -1    |    -1    |   0.83 |      0.17 |      0.38 |  -1    |  -1    |   0.67 |   -1    |     1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.67 |  -1    |    0.71 |    0.71 |     -1    |   0    | -1    |    -1    |   0.44 |      0.57 |      0.71 |  -1    |  -1    |   0.2  |   -1    |    -1    |   1    | -1    |      -1    | -1    |
| Jay      |     0.5  |  -1    |    0.75 |    0.15 |     -1    |  -1    | -1    |    -1    |   0.29 |      0.5  |      0.57 |   0.57 |  -1    |   0.6  |   -1    |    -1    |  -1    |  1    |      -1    | -1    |
| Gathenji |     0.86 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.8  |    -1    |   0.57 |      0.5  |      0.29 |  -1    |  -1    |   0.4  |   -1    |    -1    |  -1    | -1    |       1    | -1    |
| Sai      |    -1    |  -1    |    0.29 |    0.62 |     -1    |  -1    | -1    |     0.4  |   0.5  |      0.38 |      0.62 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  1    |

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |    -1    |   0.25 |    0.07 |    0.06 |      0.33 |   0.12 |  0.15 |     0.07 |   0.1  |      0.12 |      0.06 |   0.11 |   0.17 |   0.14 |    0.1  |     0    |   0.17 |  0    |       0.14 | -1    |
| Ewen     |     0.25 |  -1    |    0    |    0.25 |     -1    |   0.2  |  0    |     0    |   0.09 |      0.14 |      0.11 |  -1    |   0    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.07 |   0    |   -1    |    0.14 |     -1    |   0.16 |  0.13 |     0.05 |   0.06 |      0.15 |      0.14 |   0.22 |   0    |   0.08 |    0    |     0.11 |   0.29 |  0.38 |      -1    |  0    |
| Brian    |     0.06 |   0.25 |    0.14 |   -1    |      0.33 |   0.12 |  0.05 |     0.11 |   0.12 |      0.08 |      0.12 |   0.03 |   0.12 |   0.09 |    0.07 |     0    |   0    |  0    |       0    |  0.12 |
| Anthony  |     0.33 |  -1    |   -1    |    0.33 |     -1    |   0.33 | -1    |    -1    |   0.17 |     -1    |      0    |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.12 |   0.2  |    0.16 |    0.12 |      0.33 |  -1    |  0.14 |     0.03 |   0.15 |      0.23 |      0.12 |   0.22 |   0.33 |   0.08 |    0.17 |    -1    |   0    | -1    |      -1    | -1    |
| Jai      |     0.15 |   0    |    0.13 |    0.05 |     -1    |   0.14 | -1    |     0    |   0.18 |      0.06 |      0.14 |   0.18 |  -1    |   0.14 |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Jackie   |     0.07 |   0    |    0.05 |    0.11 |     -1    |   0.03 |  0    |    -1    |   0.06 |      0.06 |      0.09 |   0    |   0.29 |   0.07 |    0.18 |    -1    |  -1    | -1    |      -1    |  0.2  |
| Kate     |     0.1  |   0.09 |    0.06 |    0.12 |      0.17 |   0.15 |  0.18 |     0.06 |  -1    |      0.12 |      0.12 |   0.08 |   0    |   0.09 |    0.22 |     0.33 |   0.11 |  0.07 |       0    |  0.12 |
| Sushant  |     0.12 |   0.14 |    0.15 |    0.08 |     -1    |   0.23 |  0.06 |     0.06 |   0.12 |     -1    |      0.17 |   0.19 |   0    |   0.1  |    0    |     0    |   0    |  0.14 |       0    |  0.12 |
| Abishek  |     0.06 |   0.11 |    0.14 |    0.12 |      0    |   0.12 |  0.14 |     0.09 |   0.12 |      0.17 |     -1    |   0.19 |   0.15 |   0.1  |    0    |     0.25 |   0    |  0.14 |       0    |  0.12 |
| Ruhi     |     0.11 |  -1    |    0.22 |    0.03 |     -1    |   0.22 |  0.18 |     0    |   0.08 |      0.19 |      0.19 |  -1    |   0.17 |   0.35 |    0    |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.17 |   0    |    0    |    0.12 |     -1    |   0.33 | -1    |     0.29 |   0    |      0    |      0.15 |   0.17 |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.14 |   0    |    0.08 |    0.09 |     -1    |   0.08 |  0.14 |     0.07 |   0.09 |      0.1  |      0.1  |   0.35 |  -1    |  -1    |    0.17 |     0    |   0    |  0.2  |       0    |  0.17 |
| Jeron    |     0.1  |  -1    |    0    |    0.07 |     -1    |   0.17 | -1    |     0.18 |   0.22 |      0    |      0    |   0    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0    |  -1    |    0.11 |    0    |     -1    |  -1    | -1    |    -1    |   0.33 |      0    |      0.25 |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.17 |  -1    |    0.29 |    0    |     -1    |   0    | -1    |    -1    |   0.11 |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Jay      |     0    |  -1    |    0.38 |    0    |     -1    |  -1    | -1    |    -1    |   0.07 |      0.14 |      0.14 |   0.43 |  -1    |   0.2  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0    |     -1    |  -1    |  0    |    -1    |   0    |      0    |      0    |  -1    |  -1    |   0    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Sai      |    -1    |  -1    |    0    |    0.12 |     -1    |  -1    | -1    |     0.2  |   0.12 |      0.12 |      0.12 |  -1    |  -1    |   0.17 |   -1    |    -1    |  -1    | -1    |      -1    | -1    |

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |   Sai |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|-------|
| Rachel   |     0    |   0.5  |    0.56 |    0.54 |      0.67 |   0.64 |  0.38 |     0.51 |   0.53 |      0.52 |      0.66 |   0.67 |   0.42 |   0.43 |    0.1  |     0.43 |   0.33 |  0.5  |       0.14 | -1    |
| Ewen     |     0.5  |   0    |    0.83 |    0.17 |     -1    |   0.6  |  0.6  |     0.67 |   0.55 |      0.57 |      0.44 |  -1    |   1    |   0.8  |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Peter    |     0.56 |   0.83 |    0    |    0.48 |     -1    |   0.62 |  0.58 |     0.49 |   0.62 |      0.47 |      0.55 |   0.5  |   0.38 |   0.52 |    0.64 |     0.22 |   0.29 |  0.25 |      -1    |  0.71 |
| Brian    |     0.54 |   0.17 |    0.48 |    0    |      0.67 |   0.63 |  0.49 |     0.45 |   0.47 |      0.59 |      0.52 |   0.62 |   0.65 |   0.52 |    0.4  |     0.56 |   0.29 |  0.85 |       0.5  |  0.38 |
| Anthony  |     0.67 |  -1    |   -1    |    0.67 |      0    |   0.5  | -1    |    -1    |   0.67 |     -1    |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Minh     |     0.64 |   0.6  |    0.62 |    0.63 |      0.5  |   0    |  0.5  |     0.56 |   0.54 |      0.4  |      0.45 |   0.44 |   0.33 |   0.68 |    0.67 |    -1    |   1    | -1    |      -1    | -1    |
| Jai      |     0.38 |   0.6  |    0.58 |    0.49 |     -1    |   0.5  |  0    |     0.52 |   0.35 |      0.66 |      0.57 |   0.82 |  -1    |   0.48 |   -1    |    -1    |  -1    | -1    |       0.2  | -1    |
| Jackie   |     0.51 |   0.67 |    0.49 |    0.45 |     -1    |   0.56 |  0.52 |     0    |   0.47 |      0.51 |      0.53 |   0.73 |   0.57 |   0.45 |    0.36 |    -1    |  -1    | -1    |      -1    |  0.6  |
| Kate     |     0.53 |   0.55 |    0.62 |    0.47 |      0.67 |   0.54 |  0.35 |     0.47 |   0    |      0.55 |      0.51 |   0.62 |   0.71 |   0.6  |    0.22 |     0.17 |   0.56 |  0.71 |       0.43 |  0.5  |
| Sushant  |     0.52 |   0.57 |    0.47 |    0.59 |     -1    |   0.4  |  0.66 |     0.51 |   0.55 |      0    |      0.5  |   0.52 |   0.5  |   0.55 |    0.73 |     0.83 |   0.43 |  0.5  |       0.5  |  0.62 |
| Abishek  |     0.66 |   0.44 |    0.55 |    0.52 |      0.8  |   0.45 |  0.57 |     0.53 |   0.51 |      0.5  |      0    |   0.53 |   0.54 |   0.56 |    0.87 |     0.62 |   0.29 |  0.43 |       0.71 |  0.38 |
| Ruhi     |     0.67 |  -1    |    0.5  |    0.62 |     -1    |   0.44 |  0.82 |     0.73 |   0.62 |      0.52 |      0.53 |   0    |   0.33 |   0.47 |    0.83 |    -1    |  -1    |  0.43 |      -1    | -1    |
| Kish     |     0.42 |   1    |    0.38 |    0.65 |     -1    |   0.33 | -1    |     0.57 |   0.71 |      0.5  |      0.54 |   0.33 |   0    |  -1    |   -1    |    -1    |  -1    | -1    |      -1    | -1    |
| Alex     |     0.43 |   0.8  |    0.52 |    0.52 |     -1    |   0.68 |  0.48 |     0.45 |   0.6  |      0.55 |      0.56 |   0.47 |  -1    |   0    |    0.33 |     0.33 |   0.8  |  0.4  |       0.6  |  0.5  |
| Jeron    |     0.1  |  -1    |    0.64 |    0.4  |     -1    |   0.67 | -1    |     0.36 |   0.22 |      0.73 |      0.87 |   0.83 |  -1    |   0.33 |    0    |    -1    |  -1    | -1    |      -1    | -1    |
| Justin   |     0.43 |  -1    |    0.22 |    0.56 |     -1    |  -1    | -1    |    -1    |   0.17 |      0.83 |      0.62 |  -1    |  -1    |   0.33 |   -1    |     0    |  -1    | -1    |      -1    | -1    |
| Jade     |     0.33 |  -1    |    0.29 |    0.29 |     -1    |   1    | -1    |    -1    |   0.56 |      0.43 |      0.29 |  -1    |  -1    |   0.8  |   -1    |    -1    |   0    | -1    |      -1    | -1    |
| Jay      |     0.5  |  -1    |    0.25 |    0.85 |     -1    |  -1    | -1    |    -1    |   0.71 |      0.5  |      0.43 |   0.43 |  -1    |   0.4  |   -1    |    -1    |  -1    |  0    |      -1    | -1    |
| Gathenji |     0.14 |  -1    |   -1    |    0.5  |     -1    |  -1    |  0.2  |    -1    |   0.43 |      0.5  |      0.71 |  -1    |  -1    |   0.6  |   -1    |    -1    |  -1    | -1    |       0    | -1    |
| Sai      |    -1    |  -1    |    0.71 |    0.38 |     -1    |  -1    | -1    |     0.6  |   0.5  |      0.62 |      0.38 |  -1    |  -1    |   0.5  |   -1    |    -1    |  -1    | -1    |      -1    |  0    |

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Anthony |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Shashank |   Angela |   Elysia |   Jeron |   Sachin |   Justin |   Jade |   Sofia |   Jay |   Greg |   Derek |   Gathenji |   Caro |   Sai |   Nabeel |   Ronnie |   Neha |   Ira |   Kawin |
|----------|----------|--------|---------|---------|-----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|------------|----------|----------|---------|----------|----------|--------|---------|-------|--------|---------|------------|--------|-------|----------|----------|--------|-------|---------|
| Rachel   |       78 |      4 |      25 |      31 |         2 |     12 |    21 |       22 |     28 |        28 |        22 |      6 |      7 |     25 |          1 |        1 |        0 |       9 |        0 |        4 |      4 |       0 |     4 |      0 |       1 |          6 |      0 |     2 |        0 |        1 |      0 |     0 |       0 |
| Ewen     |        4 |     13 |       1 |      10 |         1 |      2 |     2 |        2 |      5 |         3 |         5 |      2 |      0 |      1 |          1 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Peter    |       25 |      1 |      94 |      44 |         0 |     12 |    16 |       31 |     26 |        35 |        35 |      9 |      5 |     29 |          1 |        1 |        0 |       4 |        0 |        7 |      5 |       0 |     6 |      0 |       2 |          1 |      0 |     2 |        2 |        2 |      1 |     0 |       1 |
| Brian    |       31 |     10 |      44 |     116 |         2 |     16 |    21 |       35 |     47 |        33 |        47 |     12 |      6 |     32 |          1 |        1 |        0 |       9 |        0 |        4 |      5 |       0 |     2 |      2 |       3 |          3 |      0 |     5 |        1 |        0 |      0 |     1 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |         6 |      3 |     0 |        0 |      2 |         0 |         1 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |       12 |      2 |      12 |      16 |         3 |     49 |     7 |       16 |     18 |        18 |        22 |      5 |      4 |      8 |          0 |        0 |        0 |       2 |        0 |        1 |      0 |       2 |     1 |      0 |       0 |          0 |      2 |     2 |        0 |        1 |      0 |     0 |       0 |
| Jai      |       21 |      2 |      16 |      21 |         0 |      7 |    46 |       13 |     26 |        12 |        15 |      2 |      2 |     15 |          0 |        0 |        0 |       3 |        0 |        0 |      0 |       0 |     2 |      1 |       0 |          4 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |
| Jackie   |       22 |      2 |      31 |      35 |         0 |     16 |    13 |       71 |     28 |        23 |        27 |      3 |      3 |     24 |          0 |        0 |        1 |       7 |        1 |        1 |      1 |       1 |     2 |      0 |       1 |          2 |      1 |     2 |        2 |        2 |      2 |     0 |       2 |
| Kate     |       28 |      5 |      26 |      47 |         2 |     18 |    26 |       28 |     96 |        29 |        39 |     10 |      4 |     23 |          0 |        0 |        0 |       7 |        0 |        5 |      4 |       1 |     4 |      2 |       1 |          4 |      2 |     4 |        3 |        1 |      1 |     1 |       1 |
| Sushant  |       28 |      3 |      35 |      33 |         0 |     18 |    12 |       23 |     29 |        87 |        41 |     13 |      5 |     27 |          2 |        0 |        0 |       4 |        0 |        1 |      4 |       1 |     7 |      2 |       3 |          3 |      1 |     3 |        0 |        1 |      0 |     0 |       0 |
| Abishek  |       22 |      5 |      35 |      47 |         1 |     22 |    15 |       27 |     39 |        41 |       106 |     15 |      6 |     30 |          0 |        0 |        0 |       2 |        0 |        3 |      5 |       0 |     8 |      1 |       2 |          2 |      1 |     5 |        2 |        0 |      0 |     0 |       0 |
| Ruhi     |        6 |      2 |       9 |      12 |         0 |      5 |     2 |        3 |     10 |        13 |        15 |     33 |      4 |      9 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     4 |      1 |       1 |          2 |      2 |     0 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        7 |      0 |       5 |       6 |         1 |      4 |     2 |        3 |      4 |         5 |         6 |      4 |     17 |      2 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          1 |      1 |     0 |        2 |        0 |      0 |     0 |       0 |
| Alex     |       25 |      1 |      29 |      32 |         0 |      8 |    15 |       24 |     23 |        27 |        30 |      9 |      2 |     76 |          1 |        0 |        0 |       4 |        0 |        4 |      1 |       1 |     3 |      0 |       0 |          2 |      0 |     3 |        0 |        1 |      0 |     0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         2 |         0 |      0 |      1 |      1 |          2 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        9 |      0 |       4 |       9 |         0 |      2 |     3 |        7 |      7 |         4 |         2 |      1 |      1 |      4 |          0 |        0 |        1 |      17 |        1 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        4 |      0 |       7 |       4 |         0 |      1 |     0 |        1 |      5 |         1 |         3 |      0 |      0 |      4 |          0 |        1 |        0 |       0 |        0 |        9 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        1 |      0 |     0 |       0 |
| Jade     |        4 |      2 |       5 |       5 |         0 |      0 |     0 |        1 |      4 |         4 |         5 |      1 |      0 |      1 |          0 |        1 |        0 |       0 |        0 |        1 |     10 |       0 |     1 |      0 |       2 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        0 |      0 |       0 |       0 |         0 |      2 |     0 |        1 |      1 |         1 |         0 |      0 |      0 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       2 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        4 |      1 |       6 |       2 |         0 |      1 |     2 |        2 |      4 |         7 |         8 |      4 |      1 |      3 |          0 |        0 |        0 |       2 |        0 |        0 |      1 |       0 |    14 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Greg     |        0 |      0 |       0 |       2 |         0 |      0 |     1 |        0 |      2 |         2 |         1 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      2 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Derek    |        1 |      0 |       2 |       3 |         0 |      0 |     0 |        1 |      1 |         3 |         2 |      1 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      2 |       0 |     0 |      0 |       4 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
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
| Rachel   |       -1 |      2 |       4 |       4 |         2 |      4 |     5 |        3 |      6 |         7 |         4 |      2 |      2 |      6 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      0 |       0 |          1 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Ewen     |        2 |     -1 |       0 |       3 |         1 |      1 |     0 |        0 |      1 |         1 |         1 |      1 |      0 |      0 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Peter    |        4 |      0 |      -1 |      12 |         0 |      5 |     5 |        3 |      4 |        10 |        11 |      4 |      0 |      5 |          0 |        0 |        0 |       0 |        0 |        1 |      2 |       0 |     3 |      0 |       0 |          0 |      0 |     0 |        1 |        0 |      0 |     0 |       0 |
| Brian    |        4 |      3 |      12 |      -1 |         2 |      5 |     2 |        7 |     11 |         6 |        12 |      1 |      2 |      6 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     1 |       0 |
| Anthony  |        2 |      1 |       0 |       2 |        -1 |      2 |     0 |        0 |      1 |         0 |         0 |      0 |      1 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |        4 |      1 |       5 |       5 |         2 |     -1 |     2 |        1 |      6 |         7 |         5 |      2 |      2 |      2 |          0 |        0 |        0 |       1 |        0 |        1 |      0 |       1 |     1 |      0 |       0 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jai      |        5 |      0 |       5 |       2 |         0 |      2 |    -1 |        0 |      7 |         2 |         5 |      2 |      0 |      4 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Jackie   |        3 |      0 |       3 |       7 |         0 |      1 |     0 |       -1 |      3 |         3 |         5 |      0 |      2 |      3 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     0 |       0 |
| Kate     |        6 |      1 |       4 |      11 |         1 |      6 |     7 |        3 |     -1 |         8 |        10 |      2 |      0 |      5 |          0 |        0 |        0 |       2 |        0 |        2 |      1 |       0 |     1 |      0 |       0 |          0 |      1 |     1 |        1 |        0 |      0 |     1 |       0 |
| Sushant  |        7 |      1 |      10 |       6 |         0 |      7 |     2 |        3 |      8 |        -1 |        14 |      5 |      0 |      6 |          1 |        0 |        0 |       0 |        0 |        0 |      0 |       1 |     2 |      0 |       1 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Abishek  |        4 |      1 |      11 |      12 |         0 |      5 |     5 |        5 |     10 |        14 |        -1 |      6 |      2 |      7 |          0 |        0 |        0 |       0 |        0 |        2 |      0 |       0 |     2 |      0 |       1 |          0 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Ruhi     |        2 |      1 |       4 |       1 |         0 |      2 |     2 |        0 |      2 |         5 |         6 |     -1 |      1 |      6 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     3 |      0 |       0 |          1 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        2 |      0 |       0 |       2 |         1 |      2 |     0 |        2 |      0 |         0 |         2 |      1 |     -1 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      1 |     0 |        1 |        0 |      0 |     0 |       0 |
| Alex     |        6 |      0 |       5 |       6 |         0 |      2 |     4 |        3 |      5 |         6 |         7 |      6 |      0 |     -1 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
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
| Derek    |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        0 |      0 |         1 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |      -1 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
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
| Rachel   |        0 |      4 |      32 |      36 |         4 |     21 |    13 |       23 |     31 |        30 |        43 |     12 |      5 |     19 |          1 |        0 |        1 |       1 |        1 |        3 |      2 |       1 |     4 |      0 |       3 |          1 |      1 |     1 |        2 |        0 |      0 |     0 |       0 |
| Ewen     |        4 |      0 |       5 |       2 |         0 |      3 |     3 |        4 |      6 |         4 |         4 |      1 |      5 |      4 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        3 |        0 |      0 |     0 |       0 |
| Peter    |       32 |      5 |       0 |      40 |         1 |     20 |    22 |       30 |     42 |        31 |        42 |      9 |      3 |     32 |          1 |        0 |        1 |       7 |        1 |        2 |      2 |       2 |     2 |      2 |       2 |          3 |      0 |     5 |        0 |        0 |      1 |     1 |       1 |
| Brian    |       36 |      2 |      40 |       0 |         4 |     27 |    20 |       29 |     42 |        47 |        51 |     20 |     11 |     34 |          1 |        0 |        1 |       6 |        1 |        5 |      2 |       2 |    11 |      0 |       1 |          3 |      3 |     3 |        3 |        2 |      2 |     0 |       2 |
| Anthony  |        4 |      0 |       1 |       4 |         0 |      3 |     1 |        1 |      4 |         1 |         4 |      0 |      2 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Minh     |       21 |      3 |      20 |      27 |         3 |      0 |     7 |       20 |     21 |        12 |        18 |      4 |      2 |     17 |          0 |        0 |        0 |       4 |        0 |        2 |      5 |       0 |     3 |      0 |       0 |          0 |      1 |     2 |        0 |        0 |      1 |     0 |       1 |
| Jai      |       13 |      3 |      22 |      20 |         1 |      7 |     0 |       14 |     14 |        23 |        20 |      9 |      0 |     14 |          1 |        0 |        0 |       1 |        0 |        2 |      3 |       0 |     2 |      1 |       2 |          1 |      0 |     1 |        1 |        0 |      0 |     0 |       0 |
| Jackie   |       23 |      4 |      30 |      29 |         1 |     20 |    14 |        0 |     25 |        24 |        30 |      8 |      4 |     20 |          0 |        1 |        0 |       4 |        0 |        2 |      3 |       1 |     1 |      0 |       1 |          2 |      1 |     3 |        2 |        0 |      0 |     1 |       0 |
| Kate     |       31 |      6 |      42 |      42 |         4 |     21 |    14 |       25 |      0 |        36 |        41 |     16 |     10 |     34 |          2 |        0 |        0 |       2 |        0 |        1 |      5 |       1 |    10 |      0 |       1 |          3 |      1 |     4 |        1 |        1 |      1 |     0 |       1 |
| Sushant  |       30 |      4 |      31 |      47 |         1 |     12 |    23 |       24 |     36 |         0 |        41 |     14 |      5 |     33 |          0 |        0 |        0 |      11 |        0 |        5 |      3 |       0 |     7 |      0 |       1 |          3 |      2 |     5 |        0 |        1 |      0 |     0 |       0 |
| Abishek  |       43 |      4 |      42 |      51 |         4 |     18 |    20 |       30 |     41 |        41 |         0 |     17 |      7 |     38 |          0 |        0 |        0 |      13 |        0 |        5 |      2 |       1 |     6 |      1 |       2 |          5 |      2 |     3 |        2 |        2 |      0 |     0 |       0 |
| Ruhi     |       12 |      1 |       9 |      20 |         0 |      4 |     9 |        8 |     16 |        14 |        17 |      0 |      2 |      8 |          0 |        0 |        0 |       5 |        0 |        0 |      1 |       0 |     3 |      0 |       0 |          2 |      1 |     2 |        0 |        0 |      0 |     0 |       0 |
| Kish     |        5 |      5 |       3 |      11 |         2 |      2 |     0 |        4 |     10 |         5 |         7 |      2 |      0 |      1 |          1 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      2 |     0 |        1 |        0 |      0 |     0 |       0 |
| Alex     |       19 |      4 |      32 |      34 |         0 |     17 |    14 |       20 |     34 |        33 |        38 |      8 |      1 |      0 |          1 |        0 |        0 |       2 |        0 |        2 |      4 |       0 |     2 |      0 |       0 |          3 |      0 |     3 |        1 |        1 |      0 |     0 |       0 |
| Shashank |        1 |      1 |       1 |       1 |         0 |      0 |     1 |        0 |      2 |         0 |         0 |      0 |      1 |      1 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Angela   |        0 |      0 |       0 |       0 |         0 |      0 |     0 |        1 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Elysia   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jeron    |        1 |      1 |       7 |       6 |         0 |      4 |     1 |        4 |      2 |        11 |        13 |      5 |      1 |      2 |          0 |        1 |        0 |       0 |        0 |        1 |      2 |       0 |     1 |      0 |       1 |          0 |      1 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sachin   |        1 |      0 |       1 |       1 |         0 |      0 |     0 |        0 |      0 |         0 |         0 |      0 |      0 |      0 |          0 |        1 |        0 |       0 |        0 |        1 |      1 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Justin   |        3 |      0 |       2 |       5 |         0 |      2 |     2 |        2 |      1 |         5 |         5 |      0 |      0 |      2 |          0 |        0 |        1 |       1 |        1 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     1 |        0 |        0 |      0 |     0 |       0 |
| Jade     |        2 |      0 |       2 |       2 |         0 |      5 |     3 |        3 |      5 |         3 |         2 |      1 |      0 |      4 |          0 |        0 |        1 |       2 |        1 |        0 |      0 |       0 |     1 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Sofia    |        1 |      0 |       2 |       2 |         0 |      0 |     0 |        1 |      1 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Jay      |        4 |      1 |       2 |      11 |         0 |      3 |     2 |        1 |     10 |         7 |         6 |      3 |      0 |      2 |          0 |        0 |        0 |       1 |        0 |        0 |      1 |       0 |     0 |      2 |       0 |          0 |      0 |     2 |        0 |        0 |      0 |     0 |       0 |
| Greg     |        0 |      0 |       2 |       0 |         0 |      0 |     1 |        0 |      0 |         0 |         1 |      0 |      0 |      0 |          0 |        0 |        0 |       0 |        0 |        0 |      0 |       0 |     2 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
| Derek    |        3 |      0 |       2 |       1 |         0 |      0 |     2 |        1 |      1 |         1 |         2 |      0 |      0 |      0 |          0 |        0 |        0 |       1 |        0 |        0 |      0 |       0 |     0 |      0 |       0 |          0 |      0 |     0 |        0 |        0 |      0 |     0 |       0 |
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
| Rachel   |    -1    |   -1   |    0.22 |    0.45 |   0.44 |  0.2  |     0.41 |   0.39 |      0.4  |      0.53 |   0.17 |   0.43 |   0.35 |    0.33 |    -1    |   -1   | -1    |       0.17 |  -1   |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Peter    |     0.22 |   -1   |   -1    |    0.5  |   0.43 |  0.3  |     0.43 |   0.5  |      0.44 |      0.61 |   0.44 |   0.2  |   0.3  |   -1    |     0.14 |   -1   |  0.6  |      -1    |  -1   |
| Brian    |     0.45 |    0.5 |    0.5  |   -1    |   0.38 |  0.37 |     0.43 |   0.58 |      0.5  |      0.61 |   0.58 |   0.83 |   0.52 |    0.5  |    -1    |    0.4 | -1    |      -1    |   0.2 |
| Minh     |     0.44 |   -1   |    0.43 |    0.38 |  -1    |  0    |     0.25 |   0.53 |      0.38 |      0.45 |   0.2  |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jai      |     0.2  |   -1   |    0.3  |    0.37 |   0    | -1    |     0.1  |   0.35 |      0.33 |      0.5  |  -1    |  -1    |   0.33 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jackie   |     0.41 |   -1   |    0.43 |    0.43 |   0.25 |  0.1  |    -1    |   0.45 |      0.53 |      0.5  |  -1    |  -1    |   0.41 |    0.33 |    -1    |   -1   | -1    |      -1    |  -1   |
| Kate     |     0.39 |    0.6 |    0.5  |    0.58 |   0.53 |  0.35 |     0.45 |  -1    |      0.42 |      0.59 |   0.3  |  -1    |   0.5  |    0.6  |     0.6  |   -1   | -1    |      -1    |  -1   |
| Sushant  |     0.4  |   -1   |    0.44 |    0.5  |   0.38 |  0.33 |     0.53 |   0.42 |     -1    |      0.57 |   0.46 |   0.4  |   0.42 |   -1    |    -1    |   -1   |  0.17 |      -1    |  -1   |
| Abishek  |     0.53 |    0.4 |    0.61 |    0.61 |   0.45 |  0.5  |     0.5  |   0.59 |      0.57 |     -1    |   0.53 |   0.83 |   0.52 |   -1    |    -1    |    0.4 |  0.5  |      -1    |   0.2 |
| Ruhi     |     0.17 |   -1   |    0.44 |    0.58 |   0.2  | -1    |    -1    |   0.3  |      0.46 |      0.53 |  -1    |  -1    |   0.56 |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Kish     |     0.43 |   -1   |    0.2  |    0.83 |  -1    | -1    |    -1    |  -1    |      0.4  |      0.83 |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Alex     |     0.35 |   -1   |    0.3  |    0.52 |   0.4  |  0.33 |     0.41 |   0.5  |      0.42 |      0.52 |   0.56 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Jay      |    -1    |   -1   |    0.6  |   -1    |  -1    | -1    |    -1    |  -1    |      0.17 |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |
| Sai      |    -1    |   -1   |   -1    |    0.2  |  -1    | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |  -1   |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Peter |   Brian |   Minh |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jade |   Jay |   Gathenji |
|----------|----------|--------|---------|---------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|--------|-------|------------|
| Rachel   |    -1    |   -1   |    0.22 |    0.41 |   0.44 |  0.22 |     0.41 |   0.36 |      0.42 |      0.5  |  -1    |   0.33 |   0.38 |    0.33 |    -1    |   -1   | -1    |       0.17 |
| Ewen     |    -1    |   -1   |   -1    |    0.5  |  -1    | -1    |    -1    |   0.6  |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Peter    |     0.22 |   -1   |   -1    |    0.47 |   0.33 |  0.22 |     0.41 |   0.42 |      0.41 |      0.57 |   0.44 |  -1    |   0.27 |   -1    |     0.14 |   -1   |  0.6  |      -1    |
| Brian    |     0.41 |    0.5 |    0.47 |   -1    |   0.33 |  0.33 |     0.41 |   0.55 |      0.48 |      0.58 |   0.5  |  -1    |   0.5  |    0.5  |    -1    |    0.4 | -1    |      -1    |
| Minh     |     0.44 |   -1   |    0.33 |    0.33 |  -1    |  0    |     0.1  |   0.46 |      0.29 |      0.42 |   0.2  |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jai      |     0.22 |   -1   |    0.22 |    0.33 |   0    | -1    |     0.1  |   0.35 |      0.33 |      0.46 |  -1    |  -1    |   0.4  |   -1    |    -1    |   -1   | -1    |      -1    |
| Jackie   |     0.41 |   -1   |    0.41 |    0.41 |   0.1  |  0.1  |    -1    |   0.39 |      0.47 |      0.47 |  -1    |  -1    |   0.38 |    0.33 |    -1    |   -1   | -1    |      -1    |
| Kate     |     0.36 |    0.6 |    0.42 |    0.55 |   0.46 |  0.35 |     0.39 |  -1    |      0.35 |      0.54 |   0.3  |  -1    |   0.47 |    0.6  |     0.6  |   -1   | -1    |      -1    |
| Sushant  |     0.42 |   -1   |    0.41 |    0.48 |   0.29 |  0.33 |     0.47 |   0.35 |     -1    |      0.54 |   0.46 |   0.4  |   0.39 |   -1    |    -1    |   -1   |  0.17 |      -1    |
| Abishek  |     0.5  |    0.4 |    0.57 |    0.58 |   0.42 |  0.46 |     0.47 |   0.54 |      0.54 |     -1    |   0.5  |   0.8  |   0.5  |   -1    |    -1    |    0.4 |  0.5  |      -1    |
| Ruhi     |    -1    |   -1   |    0.44 |    0.5  |   0.2  | -1    |    -1    |   0.3  |      0.46 |      0.5  |  -1    |  -1    |   0.67 |   -1    |    -1    |   -1   | -1    |      -1    |
| Kish     |     0.33 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |      0.4  |      0.8  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Alex     |     0.38 |   -1   |    0.27 |    0.5  |  -1    |  0.4  |     0.38 |   0.47 |      0.39 |      0.5  |   0.67 |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jeron    |     0.33 |   -1   |   -1    |    0.5  |  -1    | -1    |     0.33 |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Justin   |    -1    |   -1   |    0.14 |   -1    |  -1    | -1    |    -1    |   0.6  |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jade     |    -1    |   -1   |   -1    |    0.4  |  -1    | -1    |    -1    |  -1    |     -1    |      0.4  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Jay      |    -1    |   -1   |    0.6  |   -1    |  -1    | -1    |    -1    |  -1    |      0.17 |      0.5  |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |
| Gathenji |     0.17 |   -1   |   -1    |   -1    |  -1    | -1    |    -1    |  -1    |     -1    |     -1    |  -1    |  -1    |  -1    |   -1    |    -1    |   -1   | -1    |      -1    |

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Minh |   Rachel |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |
|----------|--------|----------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|
| Minh     |  -1    |    -1    | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |    -1   |     -1   |  -1    |
| Rachel   |  -1    |    -1    |  0    |   0.6  |      0.83 |     -1    |  -1    |   -1    |    -1   |     -1   |   0.5  |
| Jai      |  -1    |     0    | -1    |   0.67 |     -1    |      0.8  |  -1    |   -1    |    -1   |     -1   |  -1    |
| Kate     |   0.8  |     0.6  |  0.67 |  -1    |      0.33 |      0.9  |  -1    |    0.8  |    -1   |     -1   |   1    |
| Sushant  |   0.33 |     0.83 | -1    |   0.33 |     -1    |      0.83 |   0.8  |    0.67 |     0.7 |     -1   |   0.67 |
| Abishek  |   0.6  |    -1    |  0.8  |   0.9  |      0.83 |     -1    |   0.67 |    0.8  |     0.7 |     -1   |   0.86 |
| Ruhi     |  -1    |    -1    | -1    |  -1    |      0.8  |      0.67 |  -1    |   -1    |    -1   |     -1   |   0.5  |
| Brian    |  -1    |    -1    | -1    |   0.8  |      0.67 |      0.8  |  -1    |   -1    |     1   |      0.8 |   0.83 |
| Peter    |  -1    |    -1    | -1    |  -1    |      0.7  |      0.7  |  -1    |    1    |    -1   |     -1   |  -1    |
| Jackie   |  -1    |    -1    | -1    |  -1    |     -1    |     -1    |  -1    |    0.8  |    -1   |     -1   |  -1    |
| Alex     |  -1    |     0.5  | -1    |   1    |      0.67 |      0.86 |   0.5  |    0.83 |    -1   |     -1   |  -1    |

Cheesy wins excluded:

| Player   |   Minh |   Rachel |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Peter |   Jackie |   Alex |
|----------|--------|----------|-------|--------|-----------|-----------|--------|---------|---------|----------|--------|
| Minh     |  -1    |     -1   | -1    |   0.8  |      0.33 |      0.6  |  -1    |   -1    |    -1   |     -1   |  -1    |
| Rachel   |  -1    |     -1   | -1    |   0.6  |      1    |     -1    |  -1    |   -1    |    -1   |     -1   |  -1    |
| Jai      |  -1    |     -1   | -1    |   0.67 |     -1    |      0.8  |  -1    |   -1    |    -1   |     -1   |  -1    |
| Kate     |   0.8  |      0.6 |  0.67 |  -1    |      0.33 |      0.9  |  -1    |    0.8  |    -1   |     -1   |   1    |
| Sushant  |   0.33 |      1   | -1    |   0.33 |     -1    |      0.83 |   0.8  |    0.67 |     0.7 |     -1   |   0.67 |
| Abishek  |   0.6  |     -1   |  0.8  |   0.9  |      0.83 |     -1    |   0.67 |    0.89 |     0.7 |     -1   |   0.86 |
| Ruhi     |  -1    |     -1   | -1    |  -1    |      0.8  |      0.67 |  -1    |   -1    |    -1   |     -1   |  -1    |
| Brian    |  -1    |     -1   | -1    |   0.8  |      0.67 |      0.89 |  -1    |   -1    |     1   |      0.8 |   0.83 |
| Peter    |  -1    |     -1   | -1    |  -1    |      0.7  |      0.7  |  -1    |    1    |    -1   |     -1   |  -1    |
| Jackie   |  -1    |     -1   | -1    |  -1    |     -1    |     -1    |  -1    |    0.8  |    -1   |     -1   |  -1    |
| Alex     |  -1    |     -1   | -1    |   1    |      0.67 |      0.86 |  -1    |    0.83 |    -1   |     -1   |  -1    |

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |   Sai |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|-------|
| Peter    |   -1    |    0.42 |   0.62 |     0.48 |    0.2 |  0.56 |     0.47 |   0.53 |      0.44 |      0.39 |   0.67 |  -1    |   0.69 |    0.4  |     -1   | -1    |       -1   |   0.8 |
| Brian    |    0.58 |   -1    |   0.59 |     0.62 |   -1   |  0.67 |     0.5  |   0.57 |      0.55 |      0.47 |   0.7  |   0.64 |   0.68 |   -1    |      0.6 |  0.5  |       -1   |  -1   |
| Minh     |    0.38 |    0.41 |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.27 |      0.33 |      0.4  |  -1    |  -1    |   0.33 |   -1    |     -1   | -1    |       -1   |  -1   |
| Rachel   |    0.52 |    0.38 |   0.5  |    -1    |   -1   |  0.5  |     0.53 |   0.39 |      0.41 |      0.34 |   0.58 |   0.6  |   0.27 |   -1    |     -1   | -1    |       -1   |  -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jai      |    0.44 |    0.33 |  -1    |     0.5  |   -1   | -1    |     0.38 |   0.25 |      0.36 |      0.26 |   0.33 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |  -1   |
| Jackie   |    0.53 |    0.5  |   0.5  |     0.47 |   -1   |  0.62 |    -1    |   0.5  |      0.32 |      0.41 |   0.5  |  -1    |   0.56 |   -1    |     -1   | -1    |       -1   |  -1   |
| Kate     |    0.47 |    0.43 |   0.73 |     0.61 |    0.5 |  0.75 |     0.5  |  -1    |      0.54 |      0.41 |   0.62 |   0.4  |   0.52 |   -1    |     -1   |  0.38 |       -1   |  -1   |
| Sushant  |    0.56 |    0.45 |   0.67 |     0.59 |   -1   |  0.64 |     0.68 |   0.46 |     -1    |      0.38 |   0.57 |   0.4  |   0.47 |    0.62 |      0.6 |  0.2  |       -1   |   0.8 |
| Abishek  |    0.61 |    0.53 |   0.6  |     0.66 |   -1   |  0.74 |     0.59 |   0.59 |      0.62 |     -1    |   0.71 |   0.71 |   0.62 |    0.6  |      0.6 |  0.6  |        0.8 |  -1   |
| Ruhi     |    0.33 |    0.3  |  -1    |     0.42 |   -1   |  0.67 |     0.5  |   0.38 |      0.43 |      0.29 |  -1    |  -1    |   0.62 |    0.6  |     -1   | -1    |       -1   |  -1   |
| Kish     |   -1    |    0.36 |  -1    |     0.4  |    0.4 | -1    |    -1    |   0.6  |      0.6  |      0.29 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Alex     |    0.31 |    0.32 |   0.67 |     0.73 |   -1   |  0.73 |     0.44 |   0.48 |      0.53 |      0.38 |   0.38 |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Jay      |   -1    |    0.5  |  -1    |    -1    |   -1   | -1    |    -1    |   0.62 |      0.8  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |
| Sai      |    0.2  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.2  |     -1    |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |  -1   |

Cheesy wins excluded:

| Player   |   Peter |   Brian |   Minh |   Rachel |   Ewen |   Jai |   Jackie |   Kate |   Sushant |   Abishek |   Ruhi |   Kish |   Alex |   Jeron |   Justin |   Jay |   Gathenji |
|----------|---------|---------|--------|----------|--------|-------|----------|--------|-----------|-----------|--------|--------|--------|---------|----------|-------|------------|
| Peter    |   -1    |    0.41 |   0.62 |     0.43 |    0.2 |  0.53 |     0.47 |   0.53 |      0.42 |      0.37 |   0.62 |  -1    |   0.67 |    0.4  |     -1   | -1    |       -1   |
| Brian    |    0.59 |   -1    |   0.6  |     0.59 |   -1   |  0.64 |     0.53 |   0.58 |      0.55 |      0.47 |   0.67 |   0.6  |   0.68 |   -1    |      0.6 |  0.5  |       -1   |
| Minh     |    0.38 |    0.4  |  -1    |     0.5  |   -1   | -1    |     0.5  |   0.29 |      0.33 |      0.38 |  -1    |  -1    |   0.29 |   -1    |     -1   | -1    |       -1   |
| Rachel   |    0.57 |    0.41 |   0.5  |    -1    |   -1   |  0.56 |     0.56 |   0.42 |      0.44 |      0.37 |   0.58 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |
| Ewen     |    0.8  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |   0.5  |     -1    |     -1    |  -1    |   0.6  |  -1    |   -1    |     -1   | -1    |       -1   |
| Jai      |    0.47 |    0.36 |  -1    |     0.44 |   -1   | -1    |     0.43 |   0.3  |      0.37 |      0.29 |   0.33 |  -1    |   0.27 |   -1    |     -1   | -1    |       -1   |
| Jackie   |    0.53 |    0.47 |   0.5  |     0.44 |   -1   |  0.57 |    -1    |   0.5  |      0.32 |      0.38 |   0.43 |  -1    |   0.53 |   -1    |     -1   | -1    |       -1   |
| Kate     |    0.47 |    0.42 |   0.71 |     0.58 |    0.5 |  0.7  |     0.5  |  -1    |      0.54 |      0.4  |   0.62 |   0.33 |   0.48 |   -1    |     -1   |  0.38 |       -1   |
| Sushant  |    0.58 |    0.45 |   0.67 |     0.56 |   -1   |  0.63 |     0.68 |   0.46 |     -1    |      0.37 |   0.54 |  -1    |   0.43 |    0.62 |      0.6 |  0.2  |       -1   |
| Abishek  |    0.63 |    0.53 |   0.62 |     0.63 |   -1   |  0.71 |     0.62 |   0.6  |      0.63 |     -1    |   0.67 |   0.67 |   0.6  |    0.6  |      0.6 |  0.6  |        0.8 |
| Ruhi     |    0.38 |    0.33 |  -1    |     0.42 |   -1   |  0.67 |     0.57 |   0.38 |      0.46 |      0.33 |  -1    |  -1    |   0.62 |    0.6  |     -1   | -1    |       -1   |
| Kish     |   -1    |    0.4  |  -1    |    -1    |    0.4 | -1    |    -1    |   0.67 |     -1    |      0.33 |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Alex     |    0.33 |    0.32 |   0.71 |     0.73 |   -1   |  0.73 |     0.47 |   0.52 |      0.57 |      0.4  |   0.38 |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jeron    |    0.6  |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.38 |      0.4  |   0.4  |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Justin   |   -1    |    0.4  |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |      0.4  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Jay      |   -1    |    0.5  |  -1    |    -1    |   -1   | -1    |    -1    |   0.62 |      0.8  |      0.4  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |
| Gathenji |   -1    |   -1    |  -1    |    -1    |   -1   | -1    |    -1    |  -1    |     -1    |      0.2  |  -1    |  -1    |  -1    |   -1    |     -1   | -1    |       -1   |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.333333 |            21 |
| 2+2        | 0.369565 |            46 |

Cheesy wins excluded:

| Strategy   |    Win % |   Sample Size |
|------------|----------|---------------|
| 3+1        | 0.3      |            20 |
| 2+2        | 0.309524 |            42 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.444444 |            18 |
| Success      | 0.328125 |            64 |

Cheesy wins excluded:

| R1 Outcome   |    Win % |   Sample Size |
|--------------|----------|---------------|
| Fail         | 0.444444 |            18 |
| Success      | 0.306452 |            62 |

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
|                   0 |            23 |     0.478261 |
|                   1 |            89 |     0.348315 |
|                   2 |            13 |     0.538462 |
|                   3 |             2 |     0.5      |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   0 |            21 |     0.428571 |
|                   1 |            83 |     0.301205 |
|                   2 |            13 |     0.538462 |
|                   3 |             2 |     0.5      |

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

| Role          |   Fake Percival Claim % |   Sample Size |   # Fake Claims |
|---------------|-------------------------|---------------|-----------------|
| Merlin        |                 0.11811 |           127 |              15 |
| Assassin      |                 0.0431  |           116 |               5 |
| Morgana       |                 0.04724 |           127 |               6 |
| Mordred       |                 0.01176 |            85 |               1 |
| Loyal Servant |                 0       |           382 |               0 |
| Oberon        |                 0       |            34 |               0 |
| Minion #1     |                 0       |            17 |               0 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

| Player   |   Incorrect Assassination % |   # Assassinations |   Sample Size |
|----------|-----------------------------|--------------------|---------------|
| Jai      |                   0.428571  |                  3 |             7 |
| Rachel   |                   0.416667  |                  5 |            12 |
| Abishek  |                   0.333333  |                  8 |            24 |
| Alex     |                   0.333333  |                  6 |            18 |
| Jackie   |                   0.294118  |                  5 |            17 |
| Kate     |                   0.285714  |                  6 |            21 |
| Minh     |                   0.285714  |                  2 |             7 |
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
| Abishek  |          0.454545 |                  5 |            11 |
| Jai      |          0.5      |                  2 |             4 |
| Jackie   |          0.5      |                  4 |             8 |
| Rachel   |          0.6      |                  6 |            10 |
| Alex     |          0.6      |                  3 |             5 |
| Peter    |          0.615385 |                  8 |            13 |

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

|   # Players |   Assassination % |   # Assassinations |   Sample Size |
|-------------|-------------------|--------------------|---------------|
|           5 |          0.8      |                  4 |             5 |
|           6 |          0.294118 |                  5 |            17 |
|           7 |          0.526316 |                 10 |            19 |
|           8 |          0.529412 |                  9 |            17 |
|           9 |          0.428571 |                  6 |            14 |
|          10 |          0.4      |                  6 |            15 |

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

|   # Players |   # Percival Claims |   Assassination % |   # Assassinations |   Sample Size |
|-------------|---------------------|-------------------|--------------------|---------------|
|           5 |                   0 |          0.5      |                  1 |             2 |
|           5 |                   1 |          1        |                  3 |             3 |
|           6 |                   0 |          0.375    |                  3 |             8 |
|           6 |                   1 |          0.25     |                  2 |             8 |
|           6 |                   3 |          0        |                  0 |             1 |
|           7 |                   0 |          0.555556 |                  5 |             9 |
|           7 |                   1 |          0.625    |                  5 |             8 |
|           7 |                   2 |          0        |                  0 |             2 |
|           8 |                   0 |          0.5      |                  1 |             2 |
|           8 |                   1 |          0.533333 |                  8 |            15 |
|           9 |                   0 |          1        |                  1 |             1 |
|           9 |                   1 |          0.363636 |                  4 |            11 |
|           9 |                   2 |          0.5      |                  1 |             2 |
|          10 |                   1 |          0.5      |                  6 |            12 |
|          10 |                   2 |          0        |                  0 |             3 |
