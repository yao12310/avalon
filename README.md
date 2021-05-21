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
python -m avalon.main db_write --row {comma-separated list of values} --player_write {True/False, optional, default=True}
```

Updating README Stats:
```
python -m avalon.main update_stat
```
## Stats

**Good win %:**

Cheesy wins included: 0.4524 (n = 42)

Cheesy wins excluded: 0.3784 (n = 37)

**Good win % w.r.t. # players:**

Cheesy wins included:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           6 |             3 |     0.666667 |
|           7 |             2 |     1        |
|           8 |            13 |     0.461538 |
|           9 |            15 |     0.4      |
|          10 |             9 |     0.333333 |

Cheesy wins excluded:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           6 |             2 |     0.5      |
|           7 |             1 |     1        |
|           8 |            13 |     0.461538 |
|           9 |            13 |     0.307692 |
|          10 |             8 |     0.25     |

**Good win % w.r.t. # Percival claims:**

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   1 |            37 |     0.432432 |
|                   2 |             4 |     0.5      |
|                   3 |             1 |     1        |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   1 |            32 |      0.34375 |
|                   2 |             4 |      0.5     |
|                   3 |             1 |      1       |

**Mean and SD game length by winning team:**

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |             9 |       39.8889 |     17.9335 |
| Good     |             6 |       28.3333 |     14.9889 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |             9 |       39.8889 |     17.9335 |
| Good     |             5 |       32.2    |     12.9885 |

**Number of carries by player:**

| Player   |   # Carries |
|----------|-------------|
| Brian    |           1 |
| Kate     |           4 |
| Peter    |           2 |
| Rachel   |           1 |
| Sachin   |           1 |

**Win rate leaderboard (minimum 5 games):**

Cheesy wins included:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |
|----------|----------|--------------|-------------|---------------|
| Ewen     | 0.833333 |     0.666667 |    1        |             6 |
| Brian    | 0.684211 |     0.592593 |    0.909091 |            38 |
| Abishek  | 0.625    |     0.545455 |    0.8      |            32 |
| Alex     | 0.590909 |     0.444444 |    0.692308 |            22 |
| Kate     | 0.558824 |     0.47619  |    0.692308 |            34 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |
|----------|----------|--------------|-------------|---------------|
| Ewen     | 0.833333 |     0.666667 |    1        |             6 |
| Brian    | 0.636364 |     0.5      |    0.909091 |            33 |
| Alex     | 0.631579 |     0.375    |    0.818182 |            19 |
| Abishek  | 0.571429 |     0.444444 |    0.8      |            28 |
| Kate     | 0.548387 |     0.421053 |    0.75     |            31 |

**Kate Good Theorem statistics:**
| Weak Success   |   Count |   Good Win % |
|----------------|---------|--------------|
| No             |       2 |            0 |
| Yes            |       7 |            0 |

| Strong Success   |   Count |   Good Win % |
|------------------|---------|--------------|
| No               |       3 |            0 |
| Yes              |       6 |            0 |

| Weak KGT Applied   |   Sample Size |   Good Win % |
|--------------------|---------------|--------------|
| No                 |            29 |     0.586207 |
| Yes                |             9 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |            29 |     0.586207 |
| Yes                  |             9 |     0        |


**Player/role counts/percentages (minimum 5 games):**

Total count:

| Player  |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek |        4 |          5 |          2 |         3 |         3 |        2 |           0 |              13 |            32 |
| Alex    |        1 |          2 |          7 |         4 |         2 |        0 |           0 |               6 |            22 |
| Brian   |        3 |          9 |          2 |         6 |         3 |        0 |           0 |              15 |            38 |
| Ewen    |        0 |          1 |          1 |         0 |         0 |        2 |           0 |               2 |             6 |
| Jackie  |        2 |          1 |          2 |         1 |         0 |        0 |           0 |               5 |            11 |
| Jai     |        3 |          1 |          2 |         3 |         1 |        0 |           0 |               7 |            17 |
| Jay     |        1 |          2 |          3 |         0 |         1 |        0 |           0 |               1 |             8 |
| Kate    |        3 |          3 |          2 |         6 |         4 |        1 |           0 |              15 |            34 |
| Kish    |        0 |          3 |          0 |         0 |         2 |        0 |           0 |               3 |             8 |
| Minh    |        2 |          2 |          3 |         1 |         1 |        0 |           0 |               4 |            13 |
| Peter   |        4 |          3 |          3 |         1 |         2 |        0 |           0 |               7 |            20 |
| Rachel  |        6 |          2 |          1 |         3 |         6 |        0 |           0 |              11 |            29 |
| Ruhi    |        0 |          2 |          2 |         4 |         2 |        1 |           0 |              10 |            21 |
| Sushant |        7 |          2 |          3 |         2 |         2 |        0 |           1 |              14 |            31 |

Normalized by role (i.e. divided by occcurrences for each role):

| Player  |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek |    0.103 |      0.128 |      0.054 |     0.083 |     0.097 |    0.222 |           0 |           0.106 |            32 |
| Alex    |    0.026 |      0.051 |      0.189 |     0.111 |     0.065 |    0     |           0 |           0.049 |            22 |
| Brian   |    0.077 |      0.231 |      0.054 |     0.167 |     0.097 |    0     |           0 |           0.122 |            38 |
| Ewen    |    0     |      0.026 |      0.027 |     0     |     0     |    0.222 |           0 |           0.016 |             6 |
| Jackie  |    0.051 |      0.026 |      0.054 |     0.028 |     0     |    0     |           0 |           0.041 |            11 |
| Jai     |    0.077 |      0.026 |      0.054 |     0.083 |     0.032 |    0     |           0 |           0.057 |            17 |
| Jay     |    0.026 |      0.051 |      0.081 |     0     |     0.032 |    0     |           0 |           0.008 |             8 |
| Kate    |    0.077 |      0.077 |      0.054 |     0.167 |     0.129 |    0.111 |           0 |           0.122 |            34 |
| Kish    |    0     |      0.077 |      0     |     0     |     0.065 |    0     |           0 |           0.024 |             8 |
| Minh    |    0.051 |      0.051 |      0.081 |     0.028 |     0.032 |    0     |           0 |           0.033 |            13 |
| Peter   |    0.103 |      0.077 |      0.081 |     0.028 |     0.065 |    0     |           0 |           0.057 |            20 |
| Rachel  |    0.154 |      0.051 |      0.027 |     0.083 |     0.194 |    0     |           0 |           0.089 |            29 |
| Ruhi    |    0     |      0.051 |      0.054 |     0.111 |     0.065 |    0.111 |           0 |           0.081 |            21 |
| Sushant |    0.179 |      0.051 |      0.081 |     0.056 |     0.065 |    0     |           1 |           0.114 |            31 |

Normalized by player (i.e. divided by games played for each player):

| Player  |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|---------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek |    0.125 |      0.156 |      0.062 |     0.094 |     0.094 |    0.062 |       0     |           0.406 |            32 |
| Alex    |    0.045 |      0.091 |      0.318 |     0.182 |     0.091 |    0     |       0     |           0.273 |            22 |
| Brian   |    0.079 |      0.237 |      0.053 |     0.158 |     0.079 |    0     |       0     |           0.395 |            38 |
| Ewen    |    0     |      0.167 |      0.167 |     0     |     0     |    0.333 |       0     |           0.333 |             6 |
| Jackie  |    0.182 |      0.091 |      0.182 |     0.091 |     0     |    0     |       0     |           0.455 |            11 |
| Jai     |    0.176 |      0.059 |      0.118 |     0.176 |     0.059 |    0     |       0     |           0.412 |            17 |
| Jay     |    0.125 |      0.25  |      0.375 |     0     |     0.125 |    0     |       0     |           0.125 |             8 |
| Kate    |    0.088 |      0.088 |      0.059 |     0.176 |     0.118 |    0.029 |       0     |           0.441 |            34 |
| Kish    |    0     |      0.375 |      0     |     0     |     0.25  |    0     |       0     |           0.375 |             8 |
| Minh    |    0.154 |      0.154 |      0.231 |     0.077 |     0.077 |    0     |       0     |           0.308 |            13 |
| Peter   |    0.2   |      0.15  |      0.15  |     0.05  |     0.1   |    0     |       0     |           0.35  |            20 |
| Rachel  |    0.207 |      0.069 |      0.034 |     0.103 |     0.207 |    0     |       0     |           0.379 |            29 |
| Ruhi    |    0     |      0.095 |      0.095 |     0.19  |     0.095 |    0.048 |       0     |           0.476 |            21 |
| Sushant |    0.226 |      0.065 |      0.097 |     0.065 |     0.065 |    0     |       0.032 |           0.452 |            31 |

**Percentage of times two players are on the same team (minimum 5 games both played, else -1):**

| Player  |   Rachel |   Ewen |   Peter |   Minh |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Jackie |   Kish |   Alex |   Jay |
|---------|----------|--------|---------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|-------|
| Rachel  |    -1    |    0.4 |    0.69 |   0.5  |  0.62 |   0.48 |      0.52 |      0.35 |   0.45 |    0.44 |     0.44 |   0.6  |   0.5  |  0.4  |
| Ewen    |     0.4  |   -1   |   -1    |  -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |  -1    |  -1    | -1    |
| Peter   |     0.69 |   -1   |   -1    |  -1    |  0.44 |   0.38 |      0.33 |      0.57 |   0.38 |    0.58 |    -1    |  -1    |   0.25 |  0.8  |
| Minh    |     0.5  |   -1   |   -1    |  -1    |  0.6  |   0.36 |      0.55 |      0.55 |   0.67 |    0.45 |     0.6  |  -1    |   0    | -1    |
| Jai     |     0.62 |   -1   |    0.44 |   0.6  | -1    |   0.53 |      0.53 |      0.43 |   0.17 |    0.44 |     0.6  |  -1    |   0.44 | -1    |
| Kate    |     0.48 |   -1   |    0.38 |   0.36 |  0.53 |  -1    |      0.55 |      0.5  |   0.4  |    0.58 |     0.5  |   0.33 |   0.41 |  0.38 |
| Sushant |     0.52 |   -1   |    0.33 |   0.55 |  0.53 |   0.55 |     -1    |      0.52 |   0.38 |    0.6  |     0.5  |   0.43 |   0.44 |  0.38 |
| Abishek |     0.35 |   -1   |    0.57 |   0.55 |  0.43 |   0.5  |      0.52 |     -1    |   0.45 |    0.57 |     0.67 |   0.4  |   0.45 |  0.62 |
| Ruhi    |     0.45 |   -1   |    0.38 |   0.67 |  0.17 |   0.4  |      0.38 |      0.45 |  -1    |    0.45 |     0.2  |  -1    |   0.69 |  0.4  |
| Brian   |     0.44 |   -1   |    0.58 |   0.45 |  0.44 |   0.58 |      0.6  |      0.57 |   0.45 |   -1    |     0.64 |   0.5  |   0.38 |  0    |
| Jackie  |     0.44 |   -1   |   -1    |   0.6  |  0.6  |   0.5  |      0.5  |      0.67 |   0.2  |    0.64 |    -1    |  -1    |   0.17 | -1    |
| Kish    |     0.6  |   -1   |   -1    |  -1    | -1    |   0.33 |      0.43 |      0.4  |  -1    |    0.5  |    -1    |  -1    |  -1    | -1    |
| Alex    |     0.5  |   -1   |    0.25 |   0    |  0.44 |   0.41 |      0.44 |      0.45 |   0.69 |    0.38 |     0.17 |  -1    |  -1    | -1    |
| Jay     |     0.4  |   -1   |    0.8  |  -1    | -1    |   0.38 |      0.38 |      0.62 |   0.4  |    0    |    -1    |  -1    |  -1    | -1    |

**3+1 vs 2+1 strategy success rate:**

Cheesy wins included:

|    Win % |   Sample Size |
|----------|---------------|
| 0.333333 |             6 |
| 0.466667 |            15 |

Cheesy wins excluded:

|    Win % |   Sample Size |
|----------|---------------|
| 0.2      |             5 |
| 0.384615 |            13 |

**Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1):**

Cheesy wins included:

|   Win % |   Sample Size |
|---------|---------------|
|    0.5  |             6 |
|    0.35 |            20 |

Cheesy wins excluded:

|    Win % |   Sample Size |
|----------|---------------|
| 0.5      |             6 |
| 0.315789 |            19 |
