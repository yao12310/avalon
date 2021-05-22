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
## Stats

Note: The friends and memories made in this game far outweigh any statistic you will find on this page.In any case, most of these stats are super high variance—especially individual stats, which depend heavily on team composition.

**Good win %:**

Cheesy wins included: 0.4400 (n = 50)

Cheesy wins excluded: 0.3778 (n = 45)

**Good win % w.r.t. # players:**

Cheesy wins included:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           6 |             5 |     0.8      |
|           7 |             2 |     1        |
|           8 |            15 |     0.4      |
|           9 |            17 |     0.352941 |
|          10 |            11 |     0.363636 |

Cheesy wins excluded:

|   # Players |   Sample Size |   Good Win % |
|-------------|---------------|--------------|
|           6 |             4 |     0.75     |
|           7 |             1 |     1        |
|           8 |            15 |     0.4      |
|           9 |            15 |     0.266667 |
|          10 |            10 |     0.3      |

**Good win % w.r.t. # Percival claims:**

Cheesy wins included:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   1 |            44 |     0.431818 |
|                   2 |             5 |     0.4      |
|                   3 |             1 |     1        |

Cheesy wins excluded:

|   # Percival Claims |   Sample Size |   Good Win % |
|---------------------|---------------|--------------|
|                   1 |            39 |     0.358974 |
|                   2 |             5 |     0.4      |
|                   3 |             1 |     1        |

**Mean and SD game length by winning team:**

Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            14 |       39      |     17.1105 |
| Good     |             9 |       29.4444 |     18.7757 |

Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |            14 |            39 |     17.1105 |
| Good     |             8 |            32 |     18.3225 |

**Number of carries by player:**

| Player   |   # Carries |
|----------|-------------|
| Abishek  |           3 |
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
| Brian    | 0.695652 |     0.59375  |    0.928571 |            46 |
| Abishek  | 0.625    |     0.541667 |    0.75     |            40 |
| Alex     | 0.518519 |     0.416667 |    0.6      |            27 |
| Peter    | 0.5      |     0.411765 |    0.636364 |            28 |

Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |
|----------|----------|--------------|-------------|---------------|
| Ewen     | 0.833333 |     0.666667 |    1        |             6 |
| Brian    | 0.658537 |     0.518519 |    0.928571 |            41 |
| Abishek  | 0.583333 |     0.45     |    0.75     |            36 |
| Alex     | 0.541667 |     0.363636 |    0.692308 |            24 |
| Jay      | 0.5      |     0.25     |    0.75     |             8 |

**Games played ranking (minimum 5 games):**

| Player   |   Games Played |
|----------|----------------|
| Brian    |             46 |
| Kate     |             42 |
| Abishek  |             40 |
| Sushant  |             35 |
| Rachel   |             34 |
| Peter    |             28 |
| Alex     |             27 |
| Ruhi     |             23 |
| Jai      |             19 |
| Jackie   |             19 |
| Minh     |             14 |
| Kish     |             10 |
| Jay      |              8 |
| Gathenji |              7 |
| Ewen     |              6 |

**Kate Good Theorem statistics:**
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
| No                 |            36 |     0.555556 |
| Yes                |            10 |     0        |

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |            36 |     0.555556 |
| Yes                  |            10 |     0        |


**Player/role counts/percentages (minimum 5 games):**

Total count:

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |        4 |          6 |          4 |         5 |         4 |        3 |           0 |              14 |            40 |
| Alex     |        1 |          3 |          7 |         6 |         2 |        0 |           0 |               8 |            27 |
| Brian    |        4 |         10 |          2 |         8 |         4 |        0 |           0 |              18 |            46 |
| Ewen     |        0 |          1 |          1 |         0 |         0 |        2 |           0 |               2 |             6 |
| Gathenji |        0 |          0 |          0 |         1 |         0 |        0 |           0 |               6 |             7 |
| Jackie   |        2 |          4 |          3 |         1 |         0 |        1 |           0 |               8 |            19 |
| Jai      |        4 |          1 |          2 |         3 |         1 |        0 |           0 |               8 |            19 |
| Jay      |        1 |          2 |          3 |         0 |         1 |        0 |           0 |               1 |             8 |
| Kate     |        5 |          3 |          3 |         6 |         4 |        1 |           0 |              20 |            42 |
| Kish     |        0 |          3 |          0 |         1 |         2 |        0 |           0 |               4 |            10 |
| Minh     |        3 |          2 |          3 |         1 |         1 |        0 |           0 |               4 |            14 |
| Peter    |        4 |          4 |          5 |         2 |         4 |        0 |           0 |               9 |            28 |
| Rachel   |        7 |          3 |          3 |         3 |         6 |        0 |           0 |              12 |            34 |
| Ruhi     |        1 |          2 |          2 |         4 |         2 |        1 |           0 |              11 |            23 |
| Sushant  |        8 |          2 |          3 |         2 |         4 |        0 |           1 |              15 |            35 |

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.085 |      0.128 |      0.089 |     0.114 |     0.108 |    0.273 |           0 |           0.094 |            40 |
| Alex     |    0.021 |      0.064 |      0.156 |     0.136 |     0.054 |    0     |           0 |           0.054 |            27 |
| Brian    |    0.085 |      0.213 |      0.044 |     0.182 |     0.108 |    0     |           0 |           0.121 |            46 |
| Ewen     |    0     |      0.021 |      0.022 |     0     |     0     |    0.182 |           0 |           0.013 |             6 |
| Gathenji |    0     |      0     |      0     |     0.023 |     0     |    0     |           0 |           0.04  |             7 |
| Jackie   |    0.043 |      0.085 |      0.067 |     0.023 |     0     |    0.091 |           0 |           0.054 |            19 |
| Jai      |    0.085 |      0.021 |      0.044 |     0.068 |     0.027 |    0     |           0 |           0.054 |            19 |
| Jay      |    0.021 |      0.043 |      0.067 |     0     |     0.027 |    0     |           0 |           0.007 |             8 |
| Kate     |    0.106 |      0.064 |      0.067 |     0.136 |     0.108 |    0.091 |           0 |           0.134 |            42 |
| Kish     |    0     |      0.064 |      0     |     0.023 |     0.054 |    0     |           0 |           0.027 |            10 |
| Minh     |    0.064 |      0.043 |      0.067 |     0.023 |     0.027 |    0     |           0 |           0.027 |            14 |
| Peter    |    0.085 |      0.085 |      0.111 |     0.045 |     0.108 |    0     |           0 |           0.06  |            28 |
| Rachel   |    0.149 |      0.064 |      0.067 |     0.068 |     0.162 |    0     |           0 |           0.081 |            34 |
| Ruhi     |    0.021 |      0.043 |      0.044 |     0.091 |     0.054 |    0.091 |           0 |           0.074 |            23 |
| Sushant  |    0.17  |      0.043 |      0.067 |     0.045 |     0.108 |    0     |           1 |           0.101 |            35 |

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

| Player   |   Merlin |   Percival |   Assassin |   Morgana |   Mordred |   Oberon |   Minion #1 |   Loyal Servant |   Sample Size |
|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|
| Abishek  |    0.1   |      0.15  |      0.1   |     0.125 |     0.1   |    0.075 |       0     |           0.35  |            40 |
| Alex     |    0.037 |      0.111 |      0.259 |     0.222 |     0.074 |    0     |       0     |           0.296 |            27 |
| Brian    |    0.087 |      0.217 |      0.043 |     0.174 |     0.087 |    0     |       0     |           0.391 |            46 |
| Ewen     |    0     |      0.167 |      0.167 |     0     |     0     |    0.333 |       0     |           0.333 |             6 |
| Gathenji |    0     |      0     |      0     |     0.143 |     0     |    0     |       0     |           0.857 |             7 |
| Jackie   |    0.105 |      0.211 |      0.158 |     0.053 |     0     |    0.053 |       0     |           0.421 |            19 |
| Jai      |    0.211 |      0.053 |      0.105 |     0.158 |     0.053 |    0     |       0     |           0.421 |            19 |
| Jay      |    0.125 |      0.25  |      0.375 |     0     |     0.125 |    0     |       0     |           0.125 |             8 |
| Kate     |    0.119 |      0.071 |      0.071 |     0.143 |     0.095 |    0.024 |       0     |           0.476 |            42 |
| Kish     |    0     |      0.3   |      0     |     0.1   |     0.2   |    0     |       0     |           0.4   |            10 |
| Minh     |    0.214 |      0.143 |      0.214 |     0.071 |     0.071 |    0     |       0     |           0.286 |            14 |
| Peter    |    0.143 |      0.143 |      0.179 |     0.071 |     0.143 |    0     |       0     |           0.321 |            28 |
| Rachel   |    0.206 |      0.088 |      0.088 |     0.088 |     0.176 |    0     |       0     |           0.353 |            34 |
| Ruhi     |    0.043 |      0.087 |      0.087 |     0.174 |     0.087 |    0.043 |       0     |           0.478 |            23 |
| Sushant  |    0.229 |      0.057 |      0.086 |     0.057 |     0.114 |    0     |       0.029 |           0.429 |            35 |

**Percentage of times two players are on the same team (minimum 5 games both played, else -1):**

| Player   |   Rachel |   Ewen |   Peter |   Minh |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Jackie |   Kish |   Alex |   Jay |   Gathenji |
|----------|----------|--------|---------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|-------|------------|
| Rachel   |    -1    |    0.4 |    0.5  |   0.5  |  0.6  |   0.46 |      0.52 |      0.4  |   0.46 |    0.4  |     0.36 |   0.71 |   0.56 |  0.4  |       0.86 |
| Ewen     |     0.4  |   -1   |   -1    |  -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |  -1    |  -1    | -1    |      -1    |
| Peter    |     0.5  |   -1   |   -1    |  -1    |  0.45 |   0.42 |      0.37 |      0.5  |   0.4  |    0.63 |     0.64 |   0.67 |   0.23 |  0.8  |      -1    |
| Minh     |     0.5  |   -1   |   -1    |  -1    |  0.6  |   0.42 |      0.55 |      0.5  |   0.67 |    0.42 |     0.64 |  -1    |   0.14 | -1    |      -1    |
| Jai      |     0.6  |   -1   |    0.45 |   0.6  | -1    |   0.53 |      0.47 |      0.38 |   0.17 |    0.5  |     0.71 |  -1    |   0.5  | -1    |      -1    |
| Kate     |     0.46 |   -1   |    0.42 |   0.42 |  0.53 |  -1    |      0.58 |      0.47 |   0.45 |    0.56 |     0.56 |   0.38 |   0.41 |  0.38 |       0.57 |
| Sushant  |     0.52 |   -1   |    0.37 |   0.55 |  0.47 |   0.58 |     -1    |      0.52 |   0.44 |    0.56 |     0.43 |   0.44 |   0.42 |  0.38 |       0.5  |
| Abishek  |     0.4  |   -1   |    0.5  |   0.5  |  0.38 |   0.47 |      0.52 |     -1    |   0.41 |    0.53 |     0.47 |   0.43 |   0.44 |  0.62 |       0.29 |
| Ruhi     |     0.46 |   -1   |    0.4  |   0.67 |  0.17 |   0.45 |      0.44 |      0.41 |  -1    |    0.45 |     0.29 |   0.67 |   0.69 |  0.4  |      -1    |
| Brian    |     0.4  |   -1   |    0.63 |   0.42 |  0.5  |   0.56 |      0.56 |      0.53 |   0.45 |   -1    |     0.74 |   0.4  |   0.35 |  0    |       0.5  |
| Jackie   |     0.36 |   -1   |    0.64 |   0.64 |  0.71 |   0.56 |      0.43 |      0.47 |   0.29 |    0.74 |    -1    |  -1    |   0.27 | -1    |      -1    |
| Kish     |     0.71 |   -1   |    0.67 |  -1    | -1    |   0.38 |      0.44 |      0.43 |   0.67 |    0.4  |    -1    |  -1    |  -1    | -1    |      -1    |
| Alex     |     0.56 |   -1   |    0.23 |   0.14 |  0.5  |   0.41 |      0.42 |      0.44 |   0.69 |    0.35 |     0.27 |  -1    |  -1    | -1    |       0.4  |
| Jay      |     0.4  |   -1   |    0.8  |  -1    | -1    |   0.38 |      0.38 |      0.62 |   0.4  |    0    |    -1    |  -1    |  -1    | -1    |      -1    |
| Gathenji |     0.86 |   -1   |   -1    |  -1    | -1    |   0.57 |      0.5  |      0.29 |  -1    |    0.5  |    -1    |  -1    |   0.4  | -1    |      -1    |

**Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1):**

Cheesy wins included:

| Player   |   Rachel |   Ewen |   Minh |   Peter |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Jackie |   Kish |   Alex |   Jay |   Gathenji |
|----------|----------|--------|--------|---------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|-------|------------|
| Rachel   |    -1    |     -1 |   0.6  |    0.22 |  0.11 |   0.42 |      0.29 |      0.6  |   0.17 |    0.5  |     0.6  |    0.4 |   0.44 |  -1   |       0.17 |
| Ewen     |    -1    |     -1 |  -1    |   -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |   -1   |  -1    |  -1   |      -1    |
| Minh     |     0.6  |     -1 |  -1    |   -1    | -1    |   0.4  |      0.33 |      0.33 |  -1    |    0.4  |     0.14 |   -1   |  -1    |  -1   |      -1    |
| Peter    |     0.22 |     -1 |  -1    |   -1    |  0.4  |   0.5  |      0.14 |      0.82 |  -1    |    0.71 |     0.57 |   -1   |  -1    |  -1   |      -1    |
| Jai      |     0.11 |     -1 |  -1    |    0.4  | -1    |   0.33 |      0.12 |      0.5  |  -1    |    0.33 |     0.2  |   -1   |   0.2  |  -1   |      -1    |
| Kate     |     0.42 |     -1 |   0.4  |    0.5  |  0.33 |  -1    |      0.37 |      0.61 |   0.3  |    0.7  |     0.5  |   -1   |   0.55 |  -1   |      -1    |
| Sushant  |     0.29 |     -1 |   0.33 |    0.14 |  0.12 |   0.37 |     -1    |      0.5  |   0.25 |    0.53 |     0.33 |   -1   |   0.5  |  -1   |      -1    |
| Abishek  |     0.6  |     -1 |   0.33 |    0.82 |  0.5  |   0.61 |      0.5  |     -1    |   0.44 |    0.8  |     0.5  |   -1   |   0.64 |   0.6 |      -1    |
| Ruhi     |     0.17 |     -1 |  -1    |   -1    | -1    |   0.3  |      0.25 |      0.44 |  -1    |    0.6  |    -1    |   -1   |   0.56 |  -1   |      -1    |
| Brian    |     0.5  |     -1 |   0.4  |    0.71 |  0.33 |   0.7  |      0.53 |      0.8  |   0.6  |   -1    |     0.57 |   -1   |   0.89 |  -1   |      -1    |
| Jackie   |     0.6  |     -1 |   0.14 |    0.57 |  0.2  |   0.5  |      0.33 |      0.5  |  -1    |    0.57 |    -1    |   -1   |  -1    |  -1   |      -1    |
| Kish     |     0.4  |     -1 |  -1    |   -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |   -1   |  -1    |  -1   |      -1    |
| Alex     |     0.44 |     -1 |  -1    |   -1    |  0.2  |   0.55 |      0.5  |      0.64 |   0.56 |    0.89 |    -1    |   -1   |  -1    |  -1   |      -1    |
| Jay      |    -1    |     -1 |  -1    |   -1    | -1    |  -1    |     -1    |      0.6  |  -1    |   -1    |    -1    |   -1   |  -1    |  -1   |      -1    |
| Gathenji |     0.17 |     -1 |  -1    |   -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |   -1   |  -1    |  -1   |      -1    |

Cheesy wins excluded:

| Player   |   Rachel |   Ewen |   Minh |   Peter |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Jackie |   Kish |   Alex |   Jay |   Gathenji |
|----------|----------|--------|--------|---------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|-------|------------|
| Rachel   |    -1    |     -1 |    0.6 |    0.22 |  0.12 |   0.42 |      0.31 |      0.6  |  -1    |    0.45 |     0.6  |     -1 |   0.5  |  -1   |       0.17 |
| Ewen     |    -1    |     -1 |   -1   |   -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |     -1 |  -1    |  -1   |      -1    |
| Minh     |     0.6  |     -1 |   -1   |   -1    | -1    |  -1    |      0.2  |      0.2  |  -1    |   -1    |     0    |     -1 |  -1    |  -1   |      -1    |
| Peter    |     0.22 |     -1 |   -1   |   -1    | -1    |   0.44 |      0.14 |      0.78 |  -1    |    0.67 |     0.57 |     -1 |  -1    |  -1   |      -1    |
| Jai      |     0.12 |     -1 |   -1   |   -1    | -1    |   0.33 |      0.12 |      0.4  |  -1    |    0.25 |     0.2  |     -1 |  -1    |  -1   |      -1    |
| Kate     |     0.42 |     -1 |   -1   |    0.44 |  0.33 |  -1    |      0.33 |      0.56 |   0.3  |    0.67 |     0.44 |     -1 |   0.55 |  -1   |      -1    |
| Sushant  |     0.31 |     -1 |    0.2 |    0.14 |  0.12 |   0.33 |     -1    |      0.47 |   0.25 |    0.5  |     0.2  |     -1 |   0.5  |  -1   |      -1    |
| Abishek  |     0.6  |     -1 |    0.2 |    0.78 |  0.4  |   0.56 |      0.47 |     -1    |   0.38 |    0.75 |     0.43 |     -1 |   0.6  |   0.6 |      -1    |
| Ruhi     |    -1    |     -1 |   -1   |   -1    | -1    |   0.3  |      0.25 |      0.38 |  -1    |    0.5  |    -1    |     -1 |   0.67 |  -1   |      -1    |
| Brian    |     0.45 |     -1 |   -1   |    0.67 |  0.25 |   0.67 |      0.5  |      0.75 |   0.5  |   -1    |     0.54 |     -1 |   0.88 |  -1   |      -1    |
| Jackie   |     0.6  |     -1 |    0   |    0.57 |  0.2  |   0.44 |      0.2  |      0.43 |  -1    |    0.54 |    -1    |     -1 |  -1    |  -1   |      -1    |
| Kish     |    -1    |     -1 |   -1   |   -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |     -1 |  -1    |  -1   |      -1    |
| Alex     |     0.5  |     -1 |   -1   |   -1    | -1    |   0.55 |      0.5  |      0.6  |   0.67 |    0.88 |    -1    |     -1 |  -1    |  -1   |      -1    |
| Jay      |    -1    |     -1 |   -1   |   -1    | -1    |  -1    |     -1    |      0.6  |  -1    |   -1    |    -1    |     -1 |  -1    |  -1   |      -1    |
| Gathenji |     0.17 |     -1 |   -1   |   -1    | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |     -1 |  -1    |  -1   |      -1    |

**Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1):**


*Win percentages are presented as row player vs column player.*

Cheesy wins included:

| Player   |   Peter |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Jackie |   Kish |   Alex |   Jay |   Gathenji |
|----------|---------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|-------|------------|
| Peter    |   -1    |  -1    |     0.44 |     -1 |  0.5  |   0.57 |      0.58 |      0.36 |   1    |    0.2  |    -1    |  -1    |   0.8  |  -1   |       -1   |
| Minh     |   -1    |  -1    |     0.2  |     -1 | -1    |   0.14 |      0.2  |      0.33 |  -1    |    0.14 |    -1    |  -1    |   0.33 |  -1   |       -1   |
| Rachel   |    0.56 |   0.8  |    -1    |     -1 |  0.5  |   0.43 |      0.54 |      0.33 |   0.57 |    0.33 |     0.56 |  -1    |   0.14 |  -1   |       -1   |
| Ewen     |   -1    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |  -1    |  -1    |  -1   |       -1   |
| Jai      |    0.5  |  -1    |     0.5  |     -1 | -1    |   0.25 |      0.44 |      0.2  |   0.4  |    0.33 |    -1    |  -1    |   0    |  -1   |       -1   |
| Kate     |    0.43 |   0.86 |     0.57 |     -1 |  0.75 |  -1    |      0.64 |      0.35 |   0.67 |    0.28 |     0.62 |   0.4  |   0.5  |   0.2 |       -1   |
| Sushant  |    0.42 |   0.8  |     0.46 |     -1 |  0.56 |   0.36 |     -1    |      0.2  |   0.6  |    0.2  |     0.62 |   0.4  |   0.18 |   0.2 |       -1   |
| Abishek  |    0.64 |   0.67 |     0.67 |     -1 |  0.8  |   0.65 |      0.8  |     -1    |   0.77 |    0.44 |     0.67 |  -1    |   0.5  |  -1   |        0.8 |
| Ruhi     |    0    |  -1    |     0.43 |     -1 |  0.6  |   0.33 |      0.4  |      0.23 |  -1    |    0.08 |     0.4  |  -1    |  -1    |  -1   |       -1   |
| Brian    |    0.8  |   0.86 |     0.67 |     -1 |  0.67 |   0.72 |      0.8  |      0.56 |   0.92 |   -1    |     0.8  |   0.83 |   0.71 |   0.5 |       -1   |
| Jackie   |   -1    |  -1    |     0.44 |     -1 | -1    |   0.38 |      0.38 |      0.33 |   0.6  |    0.2  |    -1    |  -1    |   0.5  |  -1   |       -1   |
| Kish     |   -1    |  -1    |    -1    |     -1 | -1    |   0.6  |      0.6  |     -1    |  -1    |    0.17 |    -1    |  -1    |  -1    |  -1   |       -1   |
| Alex     |    0.2  |   0.67 |     0.86 |     -1 |  1    |   0.5  |      0.82 |      0.5  |  -1    |    0.29 |     0.5  |  -1    |  -1    |  -1   |       -1   |
| Jay      |   -1    |  -1    |    -1    |     -1 | -1    |   0.8  |      0.8  |     -1    |  -1    |    0.5  |    -1    |  -1    |  -1    |  -1   |       -1   |
| Gathenji |   -1    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |      0.2  |  -1    |   -1    |    -1    |  -1    |  -1    |  -1   |       -1   |

Cheesy wins excluded:

| Player   |   Peter |   Minh |   Rachel |   Ewen |   Jai |   Kate |   Sushant |   Abishek |   Ruhi |   Brian |   Jackie |   Kish |   Alex |   Jay |   Gathenji |
|----------|---------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|-------|------------|
| Peter    |   -1    |  -1    |     0.38 |     -1 |  0.5  |   0.57 |      0.55 |      0.36 |   1    |    0.2  |    -1    |  -1    |   0.78 |  -1   |       -1   |
| Minh     |   -1    |  -1    |    -1    |     -1 | -1    |   0.14 |      0.2  |      0.33 |  -1    |    0.14 |    -1    |  -1    |   0.2  |  -1   |       -1   |
| Rachel   |    0.62 |  -1    |    -1    |     -1 |  0.6  |   0.46 |      0.58 |      0.38 |   0.57 |    0.38 |     0.62 |  -1    |   0.14 |  -1   |       -1   |
| Ewen     |   -1    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |     -1    |  -1    |   -1    |    -1    |  -1    |  -1    |  -1   |       -1   |
| Jai      |    0.5  |  -1    |     0.4  |     -1 | -1    |   0.29 |      0.43 |      0.22 |   0.4  |    0.38 |    -1    |  -1    |   0    |  -1   |       -1   |
| Kate     |    0.43 |   0.86 |     0.54 |     -1 |  0.71 |  -1    |      0.64 |      0.37 |   0.67 |    0.29 |     0.62 |   0.4  |   0.46 |   0.2 |       -1   |
| Sushant  |    0.45 |   0.8  |     0.42 |     -1 |  0.57 |   0.36 |     -1    |      0.21 |   0.56 |    0.21 |     0.62 |  -1    |   0.1  |   0.2 |       -1   |
| Abishek  |    0.64 |   0.67 |     0.62 |     -1 |  0.78 |   0.63 |      0.79 |     -1    |   0.73 |    0.44 |     0.67 |  -1    |   0.42 |  -1   |        0.8 |
| Ruhi     |    0    |  -1    |     0.43 |     -1 |  0.6  |   0.33 |      0.44 |      0.27 |  -1    |    0.1  |    -1    |  -1    |  -1    |  -1   |       -1   |
| Brian    |    0.8  |   0.86 |     0.62 |     -1 |  0.62 |   0.71 |      0.79 |      0.56 |   0.9  |   -1    |     0.8  |   0.83 |   0.67 |   0.5 |       -1   |
| Jackie   |   -1    |  -1    |     0.38 |     -1 | -1    |   0.38 |      0.38 |      0.33 |  -1    |    0.2  |    -1    |  -1    |   0.43 |  -1   |       -1   |
| Kish     |   -1    |  -1    |    -1    |     -1 | -1    |   0.6  |     -1    |     -1    |  -1    |    0.17 |    -1    |  -1    |  -1    |  -1   |       -1   |
| Alex     |    0.22 |   0.8  |     0.86 |     -1 |  1    |   0.54 |      0.9  |      0.58 |  -1    |    0.33 |     0.57 |  -1    |  -1    |  -1   |       -1   |
| Jay      |   -1    |  -1    |    -1    |     -1 | -1    |   0.8  |      0.8  |     -1    |  -1    |    0.5  |    -1    |  -1    |  -1    |  -1   |       -1   |
| Gathenji |   -1    |  -1    |    -1    |     -1 | -1    |  -1    |     -1    |      0.2  |  -1    |   -1    |    -1    |  -1    |  -1    |  -1   |       -1   |

**3+1 vs 2+1 strategy success rate:**

Cheesy wins included:

|    Win % |   Sample Size |
|----------|---------------|
| 0.333333 |             6 |
| 0.454545 |            22 |

Cheesy wins excluded:

|   Win % |   Sample Size |
|---------|---------------|
|     0.2 |             5 |
|     0.4 |            20 |

**Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1):**

Cheesy wins included:

|    Win % |   Sample Size |
|----------|---------------|
| 0.428571 |             7 |
| 0.347826 |            23 |

Cheesy wins excluded:

|    Win % |   Sample Size |
|----------|---------------|
| 0.428571 |             7 |
| 0.318182 |            22 |

**Flip statistics for different # bad guys and mission index:**


*Excludes Oberon in 10-person games.*
*Overall:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       7 | 0.318182 |     0.428571 |
|         1 |      10 | 0.454545 |     0.2      |
|         2 |       5 | 0.227273 |     0.6      |

*2 bad guys on mission 1:*

|   # Fails |   Count |   % |   Good Win % |
|-----------|---------|-----|--------------|
|         0 |       3 | 0.6 |            0 |
|         1 |       2 | 0.4 |            0 |

*2 bad guys on mission 2:*

|   # Fails |   Count |        % |   Good Win % |
|-----------|---------|----------|--------------|
|         0 |       3 | 0.428571 |     0.666667 |
|         1 |       2 | 0.285714 |     0.5      |
|         2 |       2 | 0.285714 |     0.5      |

*2 bad guys on mission 3:*

|   # Fails |   Count |     % |   Good Win % |
|-----------|---------|-------|--------------|
|         0 |       1 | 0.125 |          1   |
|         1 |       5 | 0.625 |          0.2 |
|         2 |       2 | 0.25  |          0.5 |

*3 bad guys on mission 2:*

|   # Fails |   Count |   % |   Good Win % |
|-----------|---------|-----|--------------|
|         1 |       1 | 0.5 |            0 |
|         2 |       1 | 0.5 |            1 |
