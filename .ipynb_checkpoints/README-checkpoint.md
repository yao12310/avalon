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
mv path/to/readme/template/template_readme.md avalon/
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
Cheesy wins included: 0.4524
Cheesy wins excluded: 0.3889

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
|           8 |            12 |     0.5      |
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
|                   1 |            31 |     0.354839 |
|                   2 |             4 |     0.5      |
|                   3 |             1 |     1        |

**Mean and SD game length by winning team:**
Cheesy wins included:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |             9 |       39.8889 |     17.9335 |
| Good     |             6 |       28.3333 |     14.9889 |
Cheesy wins excluded:

| Winner   |   Sample Size |   Mean Length |   SD Length |
|----------|---------------|---------------|-------------|
| Bad      |             8 |        36.125 |     14.8943 |
| Good     |             5 |        32.2   |     12.9885 |

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
| Alex     | 0.619048 |     0.5      |    0.692308 |            21 |
| Kate     | 0.558824 |     0.47619  |    0.692308 |            34 |
Cheesy wins excluded:

| Player   |    Win % |   Good Win % |   Bad Win % |   Sample Size |
|----------|----------|--------------|-------------|---------------|
| Ewen     | 0.833333 |     0.666667 |    1        |             6 |
| Alex     | 0.647059 |     0.428571 |    0.8      |            17 |
| Brian    | 0.636364 |     0.5      |    0.909091 |            33 |
| Kate     | 0.566667 |     0.444444 |    0.75     |            30 |
| Abishek  | 0.555556 |     0.444444 |    0.777778 |            27 |

**Kate Good Theorem statistics:**
| Weak Success   |   Count |
|----------------|---------|
| No             |       2 |
| Yes            |       7 |
Cheesy wins excluded:

| Strong Success   |   Count |
|------------------|---------|
| No               |       3 |
| Yes              |       6 |
Cheesy wins excluded:

| Weak KGT Applied   |   Sample Size |   Good Win % |
|--------------------|---------------|--------------|
| No                 |            29 |     0.586207 |
| Yes                |             9 |     0        |
Cheesy wins excluded:

| Strong KGT Applied   |   Sample Size |   Good Win % |
|----------------------|---------------|--------------|
| No                   |            29 |     0.586207 |
| Yes                  |             9 |     0        |
Cheesy wins excluded:


**Player/role counts:**
| Merlin   |   Count |
|----------|---------|
| Sushant  |       7 |
| Rachel   |       6 |
| Peter    |       4 |
| Abishek  |       4 |
| Jai      |       3 |
| Brian    |       3 |
| Kate     |       3 |
| Jade     |       2 |
| Minh     |       2 |
| Jackie   |       2 |
| Angela   |       1 |
| Jay      |       1 |
| Alex     |       1 |

| Percival   |   Count |
|------------|---------|
| Brian      |       9 |
| Abishek    |       5 |
| Kish       |       3 |
| Peter      |       3 |
| Kate       |       3 |
| Rachel     |       2 |
| Minh       |       2 |
| Sushant    |       2 |
| Ruhi       |       2 |
| Jay        |       2 |
| Alex       |       2 |
| Jackie     |       1 |
| Jai        |       1 |
| Greg       |       1 |
| Ewen       |       1 |

| Assassin   |   Count |
|------------|---------|
| Alex       |       7 |
| Peter      |       3 |
| Sushant    |       3 |
| Jay        |       3 |
| Minh       |       3 |
| Jackie     |       2 |
| Abishek    |       2 |
| Jai        |       2 |
| Brian      |       2 |
| Kate       |       2 |
| Ruhi       |       2 |
| Sofia      |       1 |
| Shashank   |       1 |
| Ewen       |       1 |
| Rachel     |       1 |
| Jeron      |       1 |
| Anthony    |       1 |

| Morgana   |   Count |
|-----------|---------|
| Kate      |       6 |
| Brian     |       6 |
| Alex      |       4 |
| Ruhi      |       4 |
| Rachel    |       3 |
| Abishek   |       3 |
| Jai       |       3 |
| Sushant   |       2 |
| Minh      |       1 |
| Elysia    |       1 |
| Peter     |       1 |
| Gathenji  |       1 |
| Jackie    |       1 |

| Mordred   |   Count |
|-----------|---------|
| Rachel    |       6 |
| Kate      |       4 |
| Abishek   |       3 |
| Brian     |       3 |
| Sushant   |       2 |
| Peter     |       2 |
| Ruhi      |       2 |
| Alex      |       2 |
| Kish      |       2 |
| Jeron     |       1 |
| Minh      |       1 |
| Jay       |       1 |
| Jai       |       1 |
| Caro      |       1 |

| Oberon   |   Count |
|----------|---------|
| Ewen     |       2 |
| Abishek  |       2 |
| Sachin   |       1 |
| Kate     |       1 |
| Jeron    |       1 |
| Caro     |       1 |
| Ruhi     |       1 |

| Minion #1   |   Count |
|-------------|---------|
| Sushant     |       1 |

