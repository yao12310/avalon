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
   - [w.r.t. # players](#good-win-num-players)
   - [w.r.t. # Percival claims](#good-win-num-percival)
2. [Mean and SD Game Length](#game-length)
3. [Number of carries by player](#carries)
4. [Win rate leaderboard](#win-rate-leaderboard)
5. [Win rate over expected value leaderboard](#eev-leaderboard)
6. [Games played ranking](#games-played)
7. [Percentage good ranking](#percentage-good)
8. [Kate Good Theorem statistics](#kgt)
9. [Player/role counts/percentages](#player-role)
10. [Percentage of times two players are on the same team](#same-team)
11. [Percentage of times two players win, given that they are on the same team](#same-wins)
12. [Percentage of times two players win, given that they are on opposite teams](#opposite-wins)
13. [3+1 vs 2+2 strategy success rate](#mission2)
14. [Good win rate w.r.t. R1 fail](#r1-fail)
15. [Flip statistics for different # bad guys and mission index](#flip)
16. [% of time players are wrongly assassinated as non-Merlin good guy](#wrongly-assassinated)
17. [% of time players are correctly assassinated as Merlin](#correctly-assassinated)

## Stats

Note: The friends and memories made in this game far outweigh any statistic you will find on this page. In any case, most of these stats are super high variance—especially individual stats, which depend heavily on team composition.

### <a id="good-win"></a>Good win percentage

Cheesy wins included: 0.4138 (n = 58)

Cheesy wins excluded: 0.3585 (n = 53)

**<a id="good-win-num-players"></a>Good win % w.r.t. # players:**

Cheesy wins included:

| # Players | Sample Size | Good Win % |

|-------------|---------------|--------------|

| 6 | 7 | 0.714286 |

| 7 | 4 | 0.5 |

| 8 | 16 | 0.375 |

| 9 | 18 | 0.333333 |

| 10 | 13 | 0.384615 |

Cheesy wins excluded:

| # Players | Sample Size | Good Win % |

|-------------|---------------|--------------|

| 6 | 6 | 0.666667 |

| 7 | 3 | 0.333333 |

| 8 | 16 | 0.375 |

| 9 | 16 | 0.25 |

| 10 | 12 | 0.333333 |

**<a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims:**

Cheesy wins included:

| # Percival Claims | Sample Size | Good Win % |

|---------------------|---------------|--------------|

| 1 | 52 | 0.403846 |

| 2 | 5 | 0.4 |

| 3 | 1 | 1 |

Cheesy wins excluded:

| # Percival Claims | Sample Size | Good Win % |

|---------------------|---------------|--------------|

| 1 | 47 | 0.340426 |

| 2 | 5 | 0.4 |

| 3 | 1 | 1 |

### <a id="game-length"></a>Mean and SD game length by winning team:

Cheesy wins included:

| Winner | Sample Size | Mean Length | SD Length |

|----------|---------------|---------------|-------------|

| Bad | 20 | 36.95 | 18.5088 |

| Good | 11 | 27.0909 | 17.997 |

Cheesy wins excluded:

| Winner | Sample Size | Mean Length | SD Length |

|----------|---------------|---------------|-------------|

| Bad | 20 | 36.95 | 18.5088 |

| Good | 10 | 28.9 | 17.8851 |

### <a id="carries"></a>Number of carries by player:

| Player | # Carries |

|----------|-------------|

| Abishek | 3 |

| Brian | 1 |

| Kate | 4 |

| Minh | 1 |

| Peter | 2 |

| Rachel | 1 |

| Sachin | 1 |

### <a id="win-rate-leaderboard"></a>Win rate leaderboard:

_Minimum 5 games._

_Games Behind column reports # games needed to win in a row in order to pass leader._

Cheesy wins included:

| Player | Win % | Good Win % | Bad Win % | Sample Size | Wins | Losses | Games Behind Ewen |

|----------|----------|--------------|-------------|---------------|--------|----------|---------------------|

| Ewen | 0.75 | 0.6 | 1 | 8 | 6 | 2 | 0 |

| Brian | 0.666667 | 0.552632 | 0.9375 | 54 | 36 | 18 | 19 |

| Abishek | 0.604167 | 0.5 | 0.777778 | 48 | 29 | 19 | 29 |

| Kish | 0.545455 | 0.5 | 0.666667 | 11 | 6 | 5 | 10 |

| Peter | 0.529412 | 0.4 | 0.714286 | 34 | 18 | 16 | 31 |

Cheesy wins excluded:

| Player | Win % | Good Win % | Bad Win % | Sample Size | Wins | Losses | Games Behind Ewen |

|----------|----------|--------------|-------------|---------------|--------|----------|---------------------|

| Ewen | 0.75 | 0.6 | 1 | 8 | 6 | 2 | 0 |

| Brian | 0.632653 | 0.484848 | 0.9375 | 49 | 31 | 18 | 24 |

| Abishek | 0.568182 | 0.423077 | 0.777778 | 44 | 25 | 19 | 33 |

| Peter | 0.5 | 0.333333 | 0.714286 | 32 | 16 | 16 | 33 |

| Kate | 0.489362 | 0.366667 | 0.705882 | 47 | 23 | 24 | 50 |

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard:

_Minimum 5 games._

_Expected value computed based on good/bad % for different game sizes._

Cheesy wins included:

| Player | Win % Over Expected | Win % | Expected Win % | Good % |

|----------|-----------------------|----------|------------------|----------|

| Ewen | 0.291667 | 0.75 | 0.458333 | 0.625 |

| Brian | 0.192053 | 0.666667 | 0.474613 | 0.703704 |

| Abishek | 0.106618 | 0.604167 | 0.497548 | 0.625 |

| Kish | 0.104312 | 0.545455 | 0.441142 | 0.727273 |

| Peter | 0.0473362 | 0.529412 | 0.482076 | 0.588235 |

Cheesy wins excluded:

| Player | Win % Over Expected | Win % | Expected Win % | Good % |

|----------|-----------------------|----------|------------------|----------|

| Ewen | 0.3125 | 0.75 | 0.4375 | 0.625 |

| Brian | 0.173469 | 0.632653 | 0.459184 | 0.703704 |

| Abishek | 0.0842803 | 0.568182 | 0.483902 | 0.625 |

| Peter | 0.0325521 | 0.5 | 0.467448 | 0.588235 |

### <a id="games-played"></a>Games played ranking:

_Minimum 5 games._

| Player | Games Played |

|----------|----------------|

| Brian | 54 |

| Kate | 50 |

| Abishek | 48 |

| Sushant | 43 |

| Rachel | 36 |

| Peter | 34 |

| Alex | 32 |

| Ruhi | 25 |

| Jai | 21 |

| Jackie | 19 |

| Minh | 17 |

| Kish | 11 |

| Jay | 11 |

| Ewen | 8 |

| Jade | 7 |

| Gathenji | 7 |

### <a id="percentage-good"></a>Percentage good ranking:

_Minimum 5 games._

| Player | Good % | # Good | # Bad |

|----------|----------|----------|---------|

| Jade | 1 | 7 | 0 |

| Gathenji | 0.857143 | 6 | 1 |

| Jackie | 0.736842 | 14 | 5 |

| Kish | 0.727273 | 8 | 3 |

| Brian | 0.703704 | 38 | 16 |

| Rachel | 0.666667 | 24 | 12 |

| Jai | 0.666667 | 14 | 7 |

| Sushant | 0.651163 | 28 | 15 |

| Kate | 0.64 | 32 | 18 |

| Ewen | 0.625 | 5 | 3 |

| Abishek | 0.625 | 30 | 18 |

| Peter | 0.588235 | 20 | 14 |

| Minh | 0.588235 | 10 | 7 |

| Ruhi | 0.56 | 14 | 11 |

| Alex | 0.53125 | 17 | 15 |

| Jay | 0.454545 | 5 | 6 |

### <a id="kgt"></a>Kate Good Theorem statistics:

| Weak Success | Count | Good Win % |

|----------------|---------|--------------|

| No | 3 | 0 |

| Yes | 7 | 0 |

| Strong Success | Count | Good Win % |

|------------------|---------|--------------|

| No | 4 | 0 |

| Yes | 6 | 0 |

| Weak KGT Applied | Sample Size | Good Win % |

|--------------------|---------------|--------------|

| No | 44 | 0.5 |

| Yes | 10 | 0 |

| Strong KGT Applied | Sample Size | Good Win % |

|----------------------|---------------|--------------|

| No | 44 | 0.5 |

| Yes | 10 | 0 |

### <a id="player-role"></a>Player-role counts/percentages:

_Minimum 5 games._

Total count:

| Player | Merlin | Percival | Assassin | Morgana | Mordred | Oberon | Minion #1 | Loyal Servant | Sample Size |

|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|

| Abishek | 4 | 8 | 4 | 5 | 4 | 3 | 2 | 18 | 48 |

| Alex | 3 | 4 | 7 | 6 | 2 | 0 | 0 | 10 | 32 |

| Brian | 7 | 10 | 2 | 9 | 5 | 0 | 0 | 21 | 54 |

| Ewen | 0 | 2 | 1 | 0 | 0 | 2 | 0 | 3 | 8 |

| Gathenji | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 6 | 7 |

| Jackie | 2 | 4 | 3 | 1 | 0 | 1 | 0 | 8 | 19 |

| Jade | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 7 |

| Jai | 4 | 1 | 3 | 3 | 1 | 0 | 0 | 9 | 21 |

| Jay | 1 | 2 | 3 | 0 | 2 | 1 | 0 | 2 | 11 |

| Kate | 5 | 3 | 5 | 7 | 5 | 1 | 0 | 24 | 50 |

| Kish | 0 | 3 | 0 | 1 | 2 | 0 | 0 | 5 | 11 |

| Minh | 3 | 2 | 5 | 1 | 1 | 0 | 0 | 5 | 17 |

| Peter | 5 | 5 | 7 | 3 | 4 | 0 | 0 | 10 | 34 |

| Rachel | 8 | 4 | 3 | 3 | 6 | 0 | 0 | 12 | 36 |

| Ruhi | 1 | 2 | 2 | 5 | 3 | 1 | 0 | 11 | 25 |

| Sushant | 8 | 3 | 4 | 5 | 4 | 1 | 1 | 17 | 43 |

Normalized by role (i.e. divided by occcurrences for each role):

_Columns will not necessarily sum to 1 due to players with < 5 games not being included._

| Player | Merlin | Percival | Assassin | Morgana | Mordred | Oberon | Minion #1 | Loyal Servant | Sample Size |

|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|

| Abishek | 0.073 | 0.145 | 0.075 | 0.096 | 0.098 | 0.231 | 0.667 | 0.104 | 48 |

| Alex | 0.055 | 0.073 | 0.132 | 0.115 | 0.049 | 0 | 0 | 0.058 | 32 |

| Brian | 0.127 | 0.182 | 0.038 | 0.173 | 0.122 | 0 | 0 | 0.121 | 54 |

| Ewen | 0 | 0.036 | 0.019 | 0 | 0 | 0.154 | 0 | 0.017 | 8 |

| Gathenji | 0 | 0 | 0 | 0.019 | 0 | 0 | 0 | 0.035 | 7 |

| Jackie | 0.036 | 0.073 | 0.057 | 0.019 | 0 | 0.077 | 0 | 0.046 | 19 |

| Jade | 0.055 | 0 | 0 | 0 | 0 | 0 | 0 | 0.023 | 7 |

| Jai | 0.073 | 0.018 | 0.057 | 0.058 | 0.024 | 0 | 0 | 0.052 | 21 |

| Jay | 0.018 | 0.036 | 0.057 | 0 | 0.049 | 0.077 | 0 | 0.012 | 11 |

| Kate | 0.091 | 0.055 | 0.094 | 0.135 | 0.122 | 0.077 | 0 | 0.139 | 50 |

| Kish | 0 | 0.055 | 0 | 0.019 | 0.049 | 0 | 0 | 0.029 | 11 |

| Minh | 0.055 | 0.036 | 0.094 | 0.019 | 0.024 | 0 | 0 | 0.029 | 17 |

| Peter | 0.091 | 0.091 | 0.132 | 0.058 | 0.098 | 0 | 0 | 0.058 | 34 |

| Rachel | 0.145 | 0.073 | 0.057 | 0.058 | 0.146 | 0 | 0 | 0.069 | 36 |

| Ruhi | 0.018 | 0.036 | 0.038 | 0.096 | 0.073 | 0.077 | 0 | 0.064 | 25 |

| Sushant | 0.145 | 0.055 | 0.075 | 0.096 | 0.098 | 0.077 | 0.333 | 0.098 | 43 |

Normalized by player (i.e. divided by games played for each player):

_Row values should sum to 1._

| Player | Merlin | Percival | Assassin | Morgana | Mordred | Oberon | Minion #1 | Loyal Servant | Sample Size |

|----------|----------|------------|------------|-----------|-----------|----------|-------------|-----------------|---------------|

| Abishek | 0.083 | 0.167 | 0.083 | 0.104 | 0.083 | 0.062 | 0.042 | 0.375 | 48 |

| Alex | 0.094 | 0.125 | 0.219 | 0.188 | 0.062 | 0 | 0 | 0.312 | 32 |

| Brian | 0.13 | 0.185 | 0.037 | 0.167 | 0.093 | 0 | 0 | 0.389 | 54 |

| Ewen | 0 | 0.25 | 0.125 | 0 | 0 | 0.25 | 0 | 0.375 | 8 |

| Gathenji | 0 | 0 | 0 | 0.143 | 0 | 0 | 0 | 0.857 | 7 |

| Jackie | 0.105 | 0.211 | 0.158 | 0.053 | 0 | 0.053 | 0 | 0.421 | 19 |

| Jade | 0.429 | 0 | 0 | 0 | 0 | 0 | 0 | 0.571 | 7 |

| Jai | 0.19 | 0.048 | 0.143 | 0.143 | 0.048 | 0 | 0 | 0.429 | 21 |

| Jay | 0.091 | 0.182 | 0.273 | 0 | 0.182 | 0.091 | 0 | 0.182 | 11 |

| Kate | 0.1 | 0.06 | 0.1 | 0.14 | 0.1 | 0.02 | 0 | 0.48 | 50 |

| Kish | 0 | 0.273 | 0 | 0.091 | 0.182 | 0 | 0 | 0.455 | 11 |

| Minh | 0.176 | 0.118 | 0.294 | 0.059 | 0.059 | 0 | 0 | 0.294 | 17 |

| Peter | 0.147 | 0.147 | 0.206 | 0.088 | 0.118 | 0 | 0 | 0.294 | 34 |

| Rachel | 0.222 | 0.111 | 0.083 | 0.083 | 0.167 | 0 | 0 | 0.333 | 36 |

| Ruhi | 0.04 | 0.08 | 0.08 | 0.2 | 0.12 | 0.04 | 0 | 0.44 | 25 |

| Sushant | 0.186 | 0.07 | 0.093 | 0.116 | 0.093 | 0.023 | 0.023 | 0.395 | 43 |

### <a id="same-team"></a>Percentage of times two players are on the same team:

_minimum 5 games both played, else -1_

| Player | Rachel | Ewen | Peter | Minh | Jai | Kate | Sushant | Abishek | Ruhi | Brian | Jackie | Kish | Alex | Jade | Jay | Gathenji |

|----------|----------|--------|---------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|--------|-------|------------|

| Rachel | -1 | 0.4 | 0.5 | 0.5 | 0.6 | 0.46 | 0.52 | 0.37 | 0.46 | 0.41 | 0.36 | 0.62 | 0.61 | -1 | 0.4 | 0.86 |

| Ewen | 0.4 | -1 | -1 | -1 | -1 | 0.5 | 0.5 | -1 | -1 | 1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Peter | 0.5 | -1 | -1 | 0.2 | 0.38 | 0.33 | 0.48 | 0.5 | 0.45 | 0.55 | 0.64 | 0.57 | 0.33 | -1 | 0.83 | -1 |

| Minh | 0.5 | -1 | 0.2 | -1 | 0.67 | 0.47 | 0.5 | 0.47 | 0.62 | 0.4 | 0.64 | -1 | 0.14 | -1 | -1 | -1 |

| Jai | 0.6 | -1 | 0.38 | 0.67 | -1 | 0.58 | 0.42 | 0.39 | 0.14 | 0.55 | 0.71 | -1 | 0.45 | -1 | -1 | -1 |

| Kate | 0.46 | 0.5 | 0.33 | 0.47 | 0.58 | -1 | 0.49 | 0.48 | 0.42 | 0.59 | 0.56 | 0.38 | 0.41 | 0.33 | 0.27 | 0.57 |

| Sushant | 0.52 | 0.5 | 0.48 | 0.5 | 0.42 | 0.49 | -1 | 0.49 | 0.5 | 0.48 | 0.43 | 0.5 | 0.42 | 0.67 | 0.55 | 0.5 |

| Abishek | 0.37 | -1 | 0.5 | 0.47 | 0.39 | 0.48 | 0.49 | -1 | 0.38 | 0.57 | 0.47 | 0.43 | 0.47 | 0.83 | 0.55 | 0.29 |

| Ruhi | 0.46 | -1 | 0.45 | 0.62 | 0.14 | 0.42 | 0.5 | 0.38 | -1 | 0.42 | 0.29 | 0.67 | 0.69 | -1 | 0.57 | -1 |

| Brian | 0.41 | 1 | 0.55 | 0.4 | 0.55 | 0.59 | 0.48 | 0.57 | 0.42 | -1 | 0.74 | 0.45 | 0.39 | 0.71 | 0.09 | 0.5 |

| Jackie | 0.36 | -1 | 0.64 | 0.64 | 0.71 | 0.56 | 0.43 | 0.47 | 0.29 | 0.74 | -1 | -1 | 0.27 | -1 | -1 | -1 |

| Kish | 0.62 | -1 | 0.57 | -1 | -1 | 0.38 | 0.5 | 0.43 | 0.67 | 0.45 | -1 | -1 | -1 | -1 | -1 | -1 |

| Alex | 0.61 | -1 | 0.33 | 0.14 | 0.45 | 0.41 | 0.42 | 0.47 | 0.69 | 0.39 | 0.27 | -1 | -1 | -1 | -1 | 0.4 |

| Jade | -1 | -1 | -1 | -1 | -1 | 0.33 | 0.67 | 0.83 | -1 | 0.71 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jay | 0.4 | -1 | 0.83 | -1 | -1 | 0.27 | 0.55 | 0.55 | 0.57 | 0.09 | -1 | -1 | -1 | -1 | -1 | -1 |

| Gathenji | 0.86 | -1 | -1 | -1 | -1 | 0.57 | 0.5 | 0.29 | -1 | 0.5 | -1 | -1 | 0.4 | -1 | -1 | -1 |

### <a id="same-wins"></a>Percentage of times two players win, given that they are on the same team:

_minimum 5 games, else -1_

Cheesy wins included:

| Player | Rachel | Ewen | Minh | Peter | Jai | Kate | Sushant | Abishek | Ruhi | Brian | Jackie | Kish | Alex | Jade | Jay | Gathenji |

|----------|----------|--------|--------|---------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|--------|-------|------------|

| Rachel | -1 | -1 | 0.6 | 0.2 | 0.11 | 0.38 | 0.27 | 0.6 | 0.17 | 0.46 | 0.6 | 0.4 | 0.36 | -1 | -1 | 0.17 |

| Ewen | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0.67 | -1 | -1 | -1 | -1 | -1 | -1 |

| Minh | 0.6 | -1 | -1 | -1 | -1 | 0.43 | 0.29 | 0.29 | 0.2 | 0.33 | 0.14 | -1 | -1 | -1 | -1 | -1 |

| Peter | 0.2 | -1 | -1 | -1 | 0.4 | 0.5 | 0.33 | 0.79 | 0.4 | 0.72 | 0.57 | -1 | 0.17 | -1 | 0.6 | -1 |

| Jai | 0.11 | -1 | -1 | 0.4 | -1 | 0.36 | 0.12 | 0.43 | -1 | 0.36 | 0.2 | -1 | 0.2 | -1 | -1 | -1 |

| Kate | 0.38 | -1 | 0.43 | 0.5 | 0.36 | -1 | 0.35 | 0.59 | 0.3 | 0.66 | 0.5 | -1 | 0.46 | -1 | -1 | -1 |

| Sushant | 0.27 | -1 | 0.29 | 0.33 | 0.12 | 0.35 | -1 | 0.47 | 0.3 | 0.5 | 0.33 | 0.4 | 0.4 | -1 | 0.17 | -1 |

| Abishek | 0.6 | -1 | 0.29 | 0.79 | 0.43 | 0.59 | 0.47 | -1 | 0.44 | 0.73 | 0.5 | -1 | 0.57 | 0.4 | 0.5 | -1 |

| Ruhi | 0.17 | -1 | 0.2 | 0.4 | -1 | 0.3 | 0.3 | 0.44 | -1 | 0.6 | -1 | -1 | 0.56 | -1 | -1 | -1 |

| Brian | 0.46 | 0.67 | 0.33 | 0.72 | 0.36 | 0.66 | 0.5 | 0.73 | 0.6 | -1 | 0.57 | 1 | 0.75 | 0.4 | -1 | -1 |

| Jackie | 0.6 | -1 | 0.14 | 0.57 | 0.2 | 0.5 | 0.33 | 0.5 | -1 | 0.57 | -1 | -1 | -1 | -1 | -1 | -1 |

| Kish | 0.4 | -1 | -1 | -1 | -1 | -1 | 0.4 | -1 | -1 | 1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Alex | 0.36 | -1 | -1 | 0.17 | 0.2 | 0.46 | 0.4 | 0.57 | 0.56 | 0.75 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jade | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0.4 | -1 | 0.4 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jay | -1 | -1 | -1 | 0.6 | -1 | -1 | 0.17 | 0.5 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Gathenji | 0.17 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

Cheesy wins excluded:

| Player | Rachel | Ewen | Minh | Peter | Jai | Kate | Sushant | Abishek | Ruhi | Brian | Jackie | Kish | Alex | Jade | Jay | Gathenji |

|----------|----------|--------|--------|---------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|--------|-------|------------|

| Rachel | -1 | -1 | 0.6 | 0.2 | 0.12 | 0.38 | 0.29 | 0.6 | -1 | 0.42 | 0.6 | -1 | 0.4 | -1 | -1 | 0.17 |

| Ewen | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0.67 | -1 | -1 | -1 | -1 | -1 | -1 |

| Minh | 0.6 | -1 | -1 | -1 | -1 | 0.33 | 0.17 | 0.17 | 0.2 | 0.2 | 0 | -1 | -1 | -1 | -1 | -1 |

| Peter | 0.2 | -1 | -1 | -1 | -1 | 0.44 | 0.33 | 0.75 | 0.4 | 0.69 | 0.57 | -1 | 0.17 | -1 | 0.6 | -1 |

| Jai | 0.12 | -1 | -1 | -1 | -1 | 0.36 | 0.12 | 0.33 | -1 | 0.3 | 0.2 | -1 | -1 | -1 | -1 | -1 |

| Kate | 0.38 | -1 | 0.33 | 0.44 | 0.36 | -1 | 0.32 | 0.55 | 0.3 | 0.63 | 0.44 | -1 | 0.46 | -1 | -1 | -1 |

| Sushant | 0.29 | -1 | 0.17 | 0.33 | 0.12 | 0.32 | -1 | 0.44 | 0.3 | 0.47 | 0.2 | 0.4 | 0.4 | -1 | 0.17 | -1 |

| Abishek | 0.6 | -1 | 0.17 | 0.75 | 0.33 | 0.55 | 0.44 | -1 | 0.38 | 0.68 | 0.43 | -1 | 0.54 | 0.4 | 0.5 | -1 |

| Ruhi | -1 | -1 | 0.2 | 0.4 | -1 | 0.3 | 0.3 | 0.38 | -1 | 0.5 | -1 | -1 | 0.67 | -1 | -1 | -1 |

| Brian | 0.42 | 0.67 | 0.2 | 0.69 | 0.3 | 0.63 | 0.47 | 0.68 | 0.5 | -1 | 0.54 | -1 | 0.73 | 0.4 | -1 | -1 |

| Jackie | 0.6 | -1 | 0 | 0.57 | 0.2 | 0.44 | 0.2 | 0.43 | -1 | 0.54 | -1 | -1 | -1 | -1 | -1 | -1 |

| Kish | -1 | -1 | -1 | -1 | -1 | -1 | 0.4 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Alex | 0.4 | -1 | -1 | 0.17 | -1 | 0.46 | 0.4 | 0.54 | 0.67 | 0.73 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jade | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0.4 | -1 | 0.4 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jay | -1 | -1 | -1 | 0.6 | -1 | -1 | 0.17 | 0.5 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Gathenji | 0.17 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

### <a id="opposite-wins"></a>Percentage of times two players win, given that they are on opposite teams:

_minimum 5 games, else -1_

_Win percentages are presented as row player vs column player._

Cheesy wins included:

| Player | Peter | Minh | Rachel | Ewen | Jai | Kate | Sushant | Abishek | Ruhi | Brian | Jackie | Kish | Alex | Jade | Jay | Gathenji |

|----------|---------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|--------|-------|------------|

| Peter | -1 | -1 | 0.5 | -1 | 0.5 | 0.6 | 0.62 | 0.43 | 1 | 0.33 | -1 | -1 | 0.83 | -1 | -1 | -1 |

| Minh | -1 | -1 | 0.2 | -1 | -1 | 0.12 | 0.29 | 0.38 | -1 | 0.22 | -1 | -1 | 0.33 | -1 | -1 | -1 |

| Rachel | 0.5 | 0.8 | -1 | -1 | 0.5 | 0.4 | 0.5 | 0.29 | 0.57 | 0.32 | 0.56 | -1 | 0.14 | -1 | -1 | -1 |

| Ewen | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jai | 0.5 | -1 | 0.5 | -1 | -1 | 0.25 | 0.45 | 0.27 | 0.33 | 0.33 | -1 | -1 | 0.17 | -1 | -1 | -1 |

| Kate | 0.4 | 0.88 | 0.6 | -1 | 0.75 | -1 | 0.62 | 0.38 | 0.64 | 0.3 | 0.62 | 0.4 | 0.53 | -1 | 0.38 | -1 |

| Sushant | 0.38 | 0.71 | 0.5 | -1 | 0.55 | 0.38 | -1 | 0.25 | 0.6 | 0.27 | 0.62 | 0.4 | 0.29 | -1 | 0.2 | -1 |

| Abishek | 0.57 | 0.62 | 0.71 | -1 | 0.73 | 0.62 | 0.75 | -1 | 0.73 | 0.45 | 0.67 | -1 | 0.56 | -1 | 0.6 | 0.8 |

| Ruhi | 0 | -1 | 0.43 | -1 | 0.67 | 0.36 | 0.4 | 0.27 | -1 | 0.14 | 0.4 | -1 | -1 | -1 | -1 | -1 |

| Brian | 0.67 | 0.78 | 0.68 | -1 | 0.67 | 0.7 | 0.73 | 0.55 | 0.86 | -1 | 0.8 | 0.83 | 0.74 | -1 | 0.5 | -1 |

| Jackie | -1 | -1 | 0.44 | -1 | -1 | 0.38 | 0.38 | 0.33 | 0.6 | 0.2 | -1 | -1 | 0.5 | -1 | -1 | -1 |

| Kish | -1 | -1 | -1 | -1 | -1 | 0.6 | 0.6 | -1 | -1 | 0.17 | -1 | -1 | -1 | -1 | -1 | -1 |

| Alex | 0.17 | 0.67 | 0.86 | -1 | 0.83 | 0.47 | 0.71 | 0.44 | -1 | 0.26 | 0.5 | -1 | -1 | -1 | -1 | -1 |

| Jade | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jay | -1 | -1 | -1 | -1 | -1 | 0.62 | 0.8 | 0.4 | -1 | 0.5 | -1 | -1 | -1 | -1 | -1 | -1 |

| Gathenji | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0.2 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

Cheesy wins excluded:

| Player | Peter | Minh | Rachel | Ewen | Jai | Kate | Sushant | Abishek | Ruhi | Brian | Jackie | Kish | Alex | Jade | Jay | Gathenji |

|----------|---------|--------|----------|--------|-------|--------|-----------|-----------|--------|---------|----------|--------|--------|--------|-------|------------|

| Peter | -1 | -1 | 0.44 | -1 | 0.5 | 0.6 | 0.58 | 0.43 | 1 | 0.33 | -1 | -1 | 0.82 | -1 | -1 | -1 |

| Minh | -1 | -1 | -1 | -1 | -1 | 0.12 | 0.29 | 0.38 | -1 | 0.22 | -1 | -1 | 0.2 | -1 | -1 | -1 |

| Rachel | 0.56 | -1 | -1 | -1 | 0.6 | 0.43 | 0.54 | 0.33 | 0.57 | 0.35 | 0.62 | -1 | 0.14 | -1 | -1 | -1 |

| Ewen | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jai | 0.5 | -1 | 0.4 | -1 | -1 | 0.29 | 0.44 | 0.3 | 0.33 | 0.38 | -1 | -1 | 0.17 | -1 | -1 | -1 |

| Kate | 0.4 | 0.88 | 0.57 | -1 | 0.71 | -1 | 0.62 | 0.39 | 0.64 | 0.32 | 0.62 | 0.4 | 0.5 | -1 | 0.38 | -1 |

| Sushant | 0.42 | 0.71 | 0.46 | -1 | 0.56 | 0.38 | -1 | 0.26 | 0.56 | 0.29 | 0.62 | -1 | 0.23 | -1 | 0.2 | -1 |

| Abishek | 0.57 | 0.62 | 0.67 | -1 | 0.7 | 0.61 | 0.74 | -1 | 0.69 | 0.45 | 0.67 | -1 | 0.5 | -1 | 0.6 | 0.8 |

| Ruhi | 0 | -1 | 0.43 | -1 | 0.67 | 0.36 | 0.44 | 0.31 | -1 | 0.17 | -1 | -1 | -1 | -1 | -1 | -1 |

| Brian | 0.67 | 0.78 | 0.65 | -1 | 0.62 | 0.68 | 0.71 | 0.55 | 0.83 | -1 | 0.8 | 0.83 | 0.71 | -1 | 0.5 | -1 |

| Jackie | -1 | -1 | 0.38 | -1 | -1 | 0.38 | 0.38 | 0.33 | -1 | 0.2 | -1 | -1 | 0.43 | -1 | -1 | -1 |

| Kish | -1 | -1 | -1 | -1 | -1 | 0.6 | -1 | -1 | -1 | 0.17 | -1 | -1 | -1 | -1 | -1 | -1 |

| Alex | 0.18 | 0.8 | 0.86 | -1 | 0.83 | 0.5 | 0.77 | 0.5 | -1 | 0.29 | 0.57 | -1 | -1 | -1 | -1 | -1 |

| Jade | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

| Jay | -1 | -1 | -1 | -1 | -1 | 0.62 | 0.8 | 0.4 | -1 | 0.5 | -1 | -1 | -1 | -1 | -1 | -1 |

| Gathenji | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0.2 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate:

Cheesy wins included:

| Strategy | Win % | Sample Size |

|------------|----------|---------------|

| 3+1 | 0.428571 | 7 |

| 2+2 | 0.392857 | 28 |

Cheesy wins excluded:

| Strategy | Win % | Sample Size |

|------------|----------|---------------|

| 3+1 | 0.333333 | 6 |

| 2+2 | 0.346154 | 26 |

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail:

_filtered for cases where bad guy on R1_

Cheesy wins included:

| R1 Outcome | Win % | Sample Size |

|--------------|----------|---------------|

| Fail | 0.375 | 8 |

| Success | 0.344828 | 29 |

Cheesy wins excluded:

| R1 Outcome | Win % | Sample Size |

|--------------|----------|---------------|

| Fail | 0.375 | 8 |

| Success | 0.321429 | 28 |

### <a id="flip"></a>Flip statistics for different # bad guys and mission index:\*\*

_Excludes Oberon in 10-person games._

_Overall:_

| # Fails | Count | % | Good Win % |

|-----------|---------|----------|--------------|

| 0 | 9 | 0.321429 | 0.444444 |

| 1 | 12 | 0.428571 | 0.166667 |

| 2 | 7 | 0.25 | 0.571429 |

_2 bad guys on mission 1:_

| # Fails | Count | % | Good Win % |

|-----------|---------|-----|--------------|

| 0 | 3 | 0.5 | 0 |

| 1 | 3 | 0.5 | 0 |

_2 bad guys on mission 2:_

| # Fails | Count | % | Good Win % |

|-----------|---------|----------|--------------|

| 0 | 5 | 0.555556 | 0.6 |

| 1 | 2 | 0.222222 | 0.5 |

| 2 | 2 | 0.222222 | 0.5 |

_2 bad guys on mission 3:_

| # Fails | Count | % | Good Win % |

|-----------|---------|-----------|--------------|

| 0 | 1 | 0.0909091 | 1 |

| 1 | 6 | 0.545455 | 0.166667 |

| 2 | 4 | 0.363636 | 0.5 |

_3 bad guys on mission 2:_

| # Fails | Count | % | Good Win % |

|-----------|---------|-----|--------------|

| 1 | 1 | 0.5 | 0 |

| 2 | 1 | 0.5 | 1 |

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games good guy):

_Excludes games where Merlin assassination is unknown._

| Player | Incorrect Assassination % | # Assassinations | Sample Size |

|----------|-----------------------------|--------------------|---------------|

| Peter | 0.375 | 3 | 8 |

| Jackie | 0.333333 | 2 | 6 |

| Alex | 0.272727 | 3 | 11 |

| Abishek | 0.25 | 4 | 16 |

| Rachel | 0.125 | 1 | 8 |

| Kate | 0.125 | 2 | 16 |

| Sushant | 0.0909091 | 1 | 11 |

| Ruhi | 0 | 0 | 6 |

| Brian | 0 | 0 | 19 |

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games Merlin):

| Player | Assassination % | # Assassinations | Sample Size |

|----------|-------------------|--------------------|---------------|

| Jade | 0 | 0 | 3 |

| Minh | 0 | 0 | 3 |

| Sushant | 0.125 | 1 | 8 |

| Brian | 0.142857 | 1 | 7 |

| Kate | 0.2 | 1 | 5 |

| Jai | 0.25 | 1 | 4 |

| Abishek | 0.25 | 1 | 4 |

| Peter | 0.4 | 2 | 5 |

| Rachel | 0.5 | 4 | 8 |

| Alex | 0.666667 | 2 | 3
