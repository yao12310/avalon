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

Cheesy wins included: 0.4414 (n = 222)

Cheesy wins excluded: 0.4123 (n = 211)

**Good win % w.r.t. # players:**

Cheesy wins included:

# Players      Sample Size    Good Win %
-----------  -------------  ------------
10                      29      0.413793
5                        8      0.25
5O                       9      0.666667
5X                       6      0.5
6                       23      0.652174
6M                      12      0.583333
6O                      12      0.75
7                       35      0.371429
7O                       5      0.4
8                       35      0.314286
8O                       3      0
9                       40      0.375
9L                       3      0.666667
9O                       2      0.5

Cheesy wins excluded:

# Players      Sample Size    Good Win %
-----------  -------------  ------------
10                      28      0.392857
5                        8      0.25
5O                       9      0.666667
5X                       6      0.5
6                       21      0.619048
6M                      12      0.583333
6O                      12      0.75
7                       32      0.3125
7O                       5      0.4
8                       35      0.314286
8O                       3      0
9                       35      0.285714
9L                       3      0.666667
9O                       2      0.5

### <a id="game-length"></a>Mean and SD game length by winning team

Cheesy wins included:

Winner      Sample Size    Mean Length    SD Length
--------  -------------  -------------  -----------
Bad                 109        27.8807      19.4916
Good                 86        19.0698      15.4948

Cheesy wins excluded:

Winner      Sample Size    Mean Length    SD Length
--------  -------------  -------------  -----------
Bad                 109        27.8807      19.4916
Good                 79        20.0759      15.7739

### <a id="carries"></a>Number of carries by player

Player      # Carries
--------  -----------
Kate                8
Abishek             5
Peter               4
Brian               2
Rachel              2
Jackie              1
Minh                1
Sachin              1
Sushant             1

### <a id="win-rate-leaderboard"></a>Win rate leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Games Behind column reports # games needed to win in a row in order to pass leader.*

Cheesy wins included:

Player       Win %    Good Win %    Bad Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  ------------  -----------  -------------  ------  --------  ----------------------
Abishek   0.59633       0.5          0.723404            109      65        44                       0
Brian     0.570175      0.473684     0.763158            114      65        49                       8
Ewen      0.538462      0.375        0.8                  13       7         6                       2
Kish      0.529412      0.5          0.571429             17       9         8                       3
Kate      0.520833      0.459016     0.628571             96      50        46                      18

Cheesy wins excluded:

Player       Win %    Good Win %    Bad Win %    Sample Size    Wins    Losses    Games Behind Anthony
--------  --------  ------------  -----------  -------------  ------  --------  ----------------------
Anthony   0.6           1            0.5                   5       3         2                       0
Abishek   0.584158      0.446429     0.755556            101      59        42                       5
Brian     0.556604      0.428571     0.805556            106      59        47                      12
Ewen      0.538462      0.375        0.8                  13       7         6                       3
Kish      0.5           0.375        0.666667             14       7         7                       4

### <a id="eev-leaderboard"></a>Win rate over expected value leaderboard (minimum 5 games)


*Competitive games only statistic.*

*Expected value computed based on good/bad % for different game sizes.*

Cheesy wins included:

Player      Win % Over Expected     Win %    Expected Win %    Good %
--------  ---------------------  --------  ----------------  --------
Brian                 0.0887849  0.570175          0.481391  0.666667
Abishek               0.0822853  0.59633           0.514045  0.568807
Kish                  0.0790046  0.529412          0.450407  0.588235
Ewen                  0.0417099  0.538462          0.496752  0.615385
Kate                  0.0392262  0.520833          0.481607  0.635417
Anthony               0.027592   0.5               0.472408  0.166667
Peter                 0.0110549  0.455556          0.444501  0.633333

Cheesy wins excluded:

Player      Win % Over Expected     Win %    Expected Win %    Good %
--------  ---------------------  --------  ----------------  --------
Anthony               0.115152   0.6               0.484848  0.166667
Brian                 0.0885256  0.556604          0.468078  0.666667
Abishek               0.078795   0.584158          0.505363  0.568807
Ewen                  0.0629053  0.538462          0.475556  0.615385
Kish                  0.0288024  0.5               0.471198  0.588235
Kate                  0.0203615  0.494382          0.474021  0.635417

### <a id="role-win-rates"></a>Win rate leaderboard by role (minimum 5 games)


*Competitive games only statistic. Oberon and Minion games excluded.*

*Cheesy wins included.*


*Merlin:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Brian
--------  --------  -------------  ------  --------  --------------------
Brian     0.636364             11       7         4                     0
Kate      0.636364             11       7         4                     1
Minh      0.571429              7       4         3                     2

*Percival:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Jackie
--------  --------  -------------  ------  --------  ---------------------
Jackie    0.666667              9       6         3                      0
Sushant   0.666667              6       4         2                      1
Kate      0.6                  10       6         4                      3

*Assassin:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  -------------  ------  --------  ----------------------
Abishek   0.692308             13       9         4                       0
Brian     0.692308             13       9         4                       1
Sushant   0.666667             12       8         4                       2

*Morgana:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  -------------  ------  --------  ----------------------
Abishek   0.8                  15      12         3                       0
Brian     0.75                 16      12         4                       5
Kate      0.636364             11       7         4                      10

*Mordred:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Kate
--------  --------  -------------  ------  --------  -------------------
Kate      1                    10      10         0                    0
Brian     1                     8       8         0                  nan
Peter     0.857143              7       6         1                  nan

*Loyal Servant:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  -------------  ------  --------  ----------------------
Abishek   0.612903             31      19        12                       0
Ruhi      0.5                  12       6         6                       4
Brian     0.444444             45      20        25                      20


*Cheesy wins excluded.*


*Merlin:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Kate
--------  --------  -------------  ------  --------  -------------------
Kate      0.636364             11       7         4                    0
Brian     0.6                  10       6         4                    2
Minh      0.4                   5       2         3                    4

*Percival:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Sushant
--------  --------  -------------  ------  --------  ----------------------
Sushant   0.666667              6       4         2                       0
Jackie    0.625                 8       5         3                       2
Kate      0.5                   8       4         4                       5

*Assassin:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  -------------  ------  --------  ----------------------
Abishek   0.75                 12       9         3                       0
Brian     0.75                 12       9         3                       1
Sushant   0.727273             11       8         3                       2

*Morgana:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  -------------  ------  --------  ----------------------
Abishek   0.857143             14      12         2                       0
Brian     0.8                  15      12         3                       7
Rachel    0.666667              6       4         2                       9

*Mordred:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Kate
--------  --------  -------------  ------  --------  -------------------
Kate      1                    10      10         0                    0
Brian     1                     8       8         0                  nan
Peter     0.857143              7       6         1                  nan

*Loyal Servant:*

Player       Win %    Sample Size    Wins    Losses    Games Behind Abishek
--------  --------  -------------  ------  --------  ----------------------
Abishek   0.538462             26      14        12                       0
Brian     0.418605             43      18        25                      12
Rachel    0.4                  30      12        18                      10

### <a id="games-played"></a>Games played ranking (minimum 5 games)

Player      Games Played
--------  --------------
Brian                206
Peter                168
Kate                 161
Abishek              161
Jackie               158
Rachel               126
Sushant              125
Alex                  94
Jai                   87
Minh                  58
Ruhi                  40
Jeron                 30
Jay                   26
Kish                  21
Tercel                20
Jade                  18
Vishal                13
Ewen                  13
Anthony               12
Aman                  11
Justin                 9
Daisy                  9
Sai                    8
Karthik                7
Gathenji               7
Megan                  6
Olivia                 5
Sofia                  5
Andrew                 5

### <a id="good-percentage"></a>Percentage good ranking (minimum 5 games)
**Percentage good ranking (minimum 5 games):**

Player      Good %    # Good    # Bad
--------  --------  --------  -------
Gathenji  0.857143         6        1
Daisy     0.777778         7        2
Jade      0.777778        14        4
Rachel    0.714286        90       36
Karthik   0.714286         5        2
Kate      0.689441       111       50
Megan     0.666667         4        2
Justin    0.666667         6        3
Jeron     0.666667        20       10
Jackie    0.658228       104       54
Tercel    0.65            13        7
Alex      0.638298        60       34
Brian     0.631068       130       76
Peter     0.625          105       63
Sai       0.625            5        3
Jai       0.62069         54       33
Kish      0.619048        13        8
Ewen      0.615385         8        5
Jay       0.615385        16       10
Andrew    0.6              3        2
Olivia    0.6              3        2
Sushant   0.568           71       54
Abishek   0.565217        91       70
Minh      0.551724        32       26
Aman      0.545455         6        5
Vishal    0.538462         7        6
Ruhi      0.525           21       19
Sofia     0.4              2        3
Anthony   0.25             3        9

### <a id="kgt-stats"></a>Kate Good Theorem statistics
Weak Success      Count    Good Win %
--------------  -------  ------------
No                    3             0
Yes                   7             0

Strong Success      Count    Good Win %
----------------  -------  ------------
No                      4             0
Yes                     6             0

Weak KGT Applied      Sample Size    Good Win %
------------------  -------------  ------------
No                            208      0.461538
Yes                            10      0

Strong KGT Applied      Sample Size    Good Win %
--------------------  -------------  ------------
No                              208      0.461538
Yes                              10      0


### <a id="player-role-cnts-pcts"></a>Player/role counts/percentages (minimum 5 games)

Total count:

Player      Merlin    Percival    Assassin    Morgana    Mordred    Oberon    Minion #1    Loyal Servant    Sample Size
--------  --------  ----------  ----------  ---------  ---------  --------  -----------  ---------------  -------------
Abishek         20          22          21         21          7        10           11               49            161
Alex            13          13          13         14          4         2            1               34             94
Aman             3           2           1          1          1         2            0                1             11
Andrew           0           0           1          0          1         0            0                3              5
Anthony          0           2           4          4          0         1            0                1             12
Brian           23          37          23         31         14         5            3               70            206
Daisy            0           1           0          2          0         0            0                6              9
Ewen             1           2           2          1          0         2            0                5             13
Gathenji         0           0           0          1          0         0            0                6              7
Jackie          25          20          13         21          9         8            3               59            158
Jade             5           3           1          1          1         1            0                6             18
Jai             10           9           8         12          8         4            1               35             87
Jay              4           3           4          0          5         1            0                9             26
Jeron            5           9           1          5          2         1            1                6             30
Justin           2           0           1          1          1         0            0                4              9
Karthik          2           0           0          1          0         0            1                3              7
Kate            19          17           9         15         12        12            2               75            161
Kish             3           4           1          4          2         0            1                6             21
Megan            2           0           0          0          0         2            0                2              6
Minh             8           6          10          6          6         2            2               18             58
Olivia           1           0           1          0          1         0            0                2              5
Peter           25          22          23         20         10         7            3               58            168
Rachel          18          17          10         13         10         0            3               55            126
Ruhi             1           5           5          7          6         1            0               15             40
Sai              1           1           0          1          2         0            0                3              8
Sofia            0           1           1          2          0         0            0                1              5
Sushant         21           9          18         21          9         4            2               41            125
Tercel           2           5           3          1          3         0            0                6             20
Vishal           3           0           3          2          1         0            0                4             13

Normalized by role (i.e. divided by occcurrences for each role):

*Columns will not necessarily sum to 1 due to players with < 5 games not being included.*

Player      Merlin    Percival    Assassin    Morgana    Mordred    Oberon    Minion #1    Loyal Servant    Sample Size
--------  --------  ----------  ----------  ---------  ---------  --------  -----------  ---------------  -------------
Abishek      0.091       0.103       0.117      0.1        0.06      0.149        0.324            0.082            161
Alex         0.059       0.061       0.072      0.066      0.034     0.03         0.029            0.057             94
Aman         0.014       0.009       0.006      0.005      0.009     0.03         0                0.002             11
Andrew       0           0           0.006      0          0.009     0            0                0.005              5
Anthony      0           0.009       0.022      0.019      0         0.015        0                0.002             12
Brian        0.105       0.173       0.128      0.147      0.12      0.075        0.088            0.117            206
Daisy        0           0.005       0          0.009      0         0            0                0.01               9
Ewen         0.005       0.009       0.011      0.005      0         0.03         0                0.008             13
Gathenji     0           0           0          0.005      0         0            0                0.01               7
Jackie       0.114       0.093       0.072      0.1        0.077     0.119        0.088            0.099            158
Jade         0.023       0.014       0.006      0.005      0.009     0.015        0                0.01              18
Jai          0.046       0.042       0.044      0.057      0.068     0.06         0.029            0.059             87
Jay          0.018       0.014       0.022      0          0.043     0.015        0                0.015             26
Jeron        0.023       0.042       0.006      0.024      0.017     0.015        0.029            0.01              30
Justin       0.009       0           0.006      0.005      0.009     0            0                0.007              9
Karthik      0.009       0           0          0.005      0         0            0.029            0.005              7
Kate         0.087       0.079       0.05       0.071      0.103     0.179        0.059            0.125            161
Kish         0.014       0.019       0.006      0.019      0.017     0            0.029            0.01              21
Megan        0.009       0           0          0          0         0.03         0                0.003              6
Minh         0.037       0.028       0.056      0.028      0.051     0.03         0.059            0.03              58
Olivia       0.005       0           0.006      0          0.009     0            0                0.003              5
Peter        0.114       0.103       0.128      0.095      0.085     0.104        0.088            0.097            168
Rachel       0.082       0.079       0.056      0.062      0.085     0            0.088            0.092            126
Ruhi         0.005       0.023       0.028      0.033      0.051     0.015        0                0.025             40
Sai          0.005       0.005       0          0.005      0.017     0            0                0.005              8
Sofia        0           0.005       0.006      0.009      0         0            0                0.002              5
Sushant      0.096       0.042       0.1        0.1        0.077     0.06         0.059            0.069            125
Tercel       0.009       0.023       0.017      0.005      0.026     0            0                0.01              20
Vishal       0.014       0           0.017      0.009      0.009     0            0                0.007             13

Normalized by player (i.e. divided by games played for each player):

*Row values should sum to 1.*

Player      Merlin    Percival    Assassin    Morgana    Mordred    Oberon    Minion #1    Loyal Servant    Sample Size
--------  --------  ----------  ----------  ---------  ---------  --------  -----------  ---------------  -------------
Abishek      0.124       0.137       0.13       0.13       0.043     0.062        0.068            0.304            161
Alex         0.138       0.138       0.138      0.149      0.043     0.021        0.011            0.362             94
Aman         0.273       0.182       0.091      0.091      0.091     0.182        0                0.091             11
Andrew       0           0           0.2        0          0.2       0            0                0.6                5
Anthony      0           0.167       0.333      0.333      0         0.083        0                0.083             12
Brian        0.112       0.18        0.112      0.15       0.068     0.024        0.015            0.34             206
Daisy        0           0.111       0          0.222      0         0            0                0.667              9
Ewen         0.077       0.154       0.154      0.077      0         0.154        0                0.385             13
Gathenji     0           0           0          0.143      0         0            0                0.857              7
Jackie       0.158       0.127       0.082      0.133      0.057     0.051        0.019            0.373            158
Jade         0.278       0.167       0.056      0.056      0.056     0.056        0                0.333             18
Jai          0.115       0.103       0.092      0.138      0.092     0.046        0.011            0.402             87
Jay          0.154       0.115       0.154      0          0.192     0.038        0                0.346             26
Jeron        0.167       0.3         0.033      0.167      0.067     0.033        0.033            0.2               30
Justin       0.222       0           0.111      0.111      0.111     0            0                0.444              9
Karthik      0.286       0           0          0.143      0         0            0.143            0.429              7
Kate         0.118       0.106       0.056      0.093      0.075     0.075        0.012            0.466            161
Kish         0.143       0.19        0.048      0.19       0.095     0            0.048            0.286             21
Megan        0.333       0           0          0          0         0.333        0                0.333              6
Minh         0.138       0.103       0.172      0.103      0.103     0.034        0.034            0.31              58
Olivia       0.2         0           0.2        0          0.2       0            0                0.4                5
Peter        0.149       0.131       0.137      0.119      0.06      0.042        0.018            0.345            168
Rachel       0.143       0.135       0.079      0.103      0.079     0            0.024            0.437            126
Ruhi         0.025       0.125       0.125      0.175      0.15      0.025        0                0.375             40
Sai          0.125       0.125       0          0.125      0.25      0            0                0.375              8
Sofia        0           0.2         0.2        0.4        0         0            0                0.2                5
Sushant      0.168       0.072       0.144      0.168      0.072     0.032        0.016            0.328            125
Tercel       0.1         0.25        0.15       0.05       0.15      0            0                0.3               20
Vishal       0.231       0           0.231      0.154      0.077     0            0                0.308             13

### <a id="pair-teams-pct"></a>Percentage of times two players are on the same team (minimum 5 games both played, else -1)

Player      Rachel    Ewen    Peter    Brian    Anthony    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Sofia    Jay    Gathenji    Sai    Tercel    Karthik    Vishal    Olivia    Daisy    Aman    Megan    Andrew
--------  --------  ------  -------  -------  ---------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -------  -----  ----------  -----  --------  ---------  --------  --------  -------  ------  -------  --------
Rachel        1       0.5      0.47     0.45       0.33    0.38   0.55      0.56    0.48       0.48       0.34    0.39    0.6     0.56     0.75      0.57    0.69     -1     0.72        0.86  -1         0.4        0.57      0.44      -1      -1      -1       -1         -1
Ewen          0.5     1        0.17     0.83      -1       0.4    0.4       0.33    0.45       0.43       0.56   -1       0       0.2     -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Peter         0.47    0.17     1        0.51       0.43    0.44   0.51      0.46    0.41       0.49       0.44    0.5     0.55    0.45     0.45      0.78    0.53     -1     0.65       -1      0.29      0.56      -1        -1         -1       0.67    0.33     0.5        0.6
Brian         0.45    0.83     0.51     1          0.25    0.4    0.55      0.42    0.51       0.42       0.51    0.31    0.38    0.46     0.5       0.44    0.6       0.2   0.3         0.5    0.62      0.5        0.43      0.54       0.6     0       0.64     0.5        0.4
Anthony       0.33   -1        0.43     0.25       1       0.5    0.29      0.17    0.33      -1          0.2    -1      -1      -1        0.5      -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Minh          0.38    0.4      0.44     0.4        0.5     1      0.47      0.42    0.46       0.6        0.52    0.56    0.67    0.32     0.33     -1       0.14     -1     0.33       -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jai           0.55    0.4      0.51     0.55       0.29    0.47   1         0.45    0.58       0.36       0.41    0.22   -1       0.51     0.45     -1       0.33     -1     0.23        0.8   -1         0.56       0.67      0         -1      -1      -1       -1         -1
Jackie        0.56    0.33     0.46     0.42       0.17    0.42   0.45      1       0.56       0.42       0.39    0.44    0.38    0.58     0.57     -1       0.5       0.6   0.6        -1      0.4       0.4        0.57      0.38      -1       1       0.5     -1          0.4
Kate          0.48    0.45     0.41     0.51       0.33    0.46   0.58      0.56    1          0.41       0.51    0.47    0.33    0.45     0.75      0.83    0.42     -1     0.4         0.57   0.5       0.31      -1         0.57       0.2     0.67    0.27     0.67       0.4
Sushant       0.48    0.43     0.49     0.42      -1       0.6    0.36      0.42    0.41       1          0.49    0.48    0.55    0.44     0.29      0.17    0.5      -1     0.45        0.5    0.38     -1         -1        -1         -1      -1      -1       -1         -1
Abishek       0.34    0.56     0.44     0.51       0.2     0.52   0.41      0.39    0.51       0.49       1       0.44    0.5     0.43     0.18      0.38    0.5      -1     0.46        0.29   0.62     -1          0.14      0.54      -1      -1      -1       -1         -1
Ruhi          0.39   -1        0.5      0.31      -1       0.56   0.22      0.44    0.47       0.48       0.44    1       0.71    0.53     0.44     -1      -1        -1     0.57       -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Kish          0.6     0        0.55     0.38      -1       0.67  -1         0.38    0.33       0.55       0.5     0.71    1      -1        0.2      -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Alex          0.56    0.2      0.45     0.46      -1       0.32   0.51      0.58    0.45       0.44       0.43    0.53   -1       1        0.4       0.67    0.2      -1     0.45        0.4    0.5       0.38      -1        -1         -1      -1      -1       -1         -1
Jeron         0.75   -1        0.45     0.5        0.5     0.33   0.45      0.57    0.75       0.29       0.18    0.44    0.2     0.4      1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Justin        0.57   -1        0.78     0.44      -1      -1     -1        -1       0.83       0.17       0.38   -1      -1       0.67    -1         1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jade          0.69   -1        0.53     0.6       -1       0.14   0.33      0.5     0.42       0.5        0.5    -1      -1       0.2     -1        -1       1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Sofia        -1      -1       -1        0.2       -1      -1     -1         0.6    -1         -1         -1      -1      -1      -1       -1        -1      -1         1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jay           0.72   -1        0.65     0.3       -1       0.33   0.23      0.6     0.4        0.45       0.46    0.57   -1       0.45    -1        -1      -1        -1     1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Gathenji      0.86   -1       -1        0.5       -1      -1      0.8      -1       0.57       0.5        0.29   -1      -1       0.4     -1        -1      -1        -1    -1           1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Sai          -1      -1        0.29     0.62      -1      -1     -1         0.4     0.5        0.38       0.62   -1      -1       0.5     -1        -1      -1        -1    -1          -1      1        -1         -1        -1         -1      -1      -1       -1         -1
Tercel        0.4    -1        0.56     0.5       -1      -1      0.56      0.4     0.31      -1         -1      -1      -1       0.38    -1        -1      -1        -1    -1          -1     -1         1         -1        -1          0.6     0.4     0.8      0.33      -1
Karthik       0.57   -1       -1        0.43      -1      -1      0.67      0.57   -1         -1          0.14   -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1          1         0.29      -1      -1      -1       -1         -1
Vishal        0.44   -1       -1        0.54      -1      -1      0         0.38    0.57      -1          0.54   -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1          0.29      1         -1      -1      -1       -1         -1
Olivia       -1      -1       -1        0.6       -1      -1     -1        -1       0.2       -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.6       -1        -1          1       0.4    -1       -1         -1
Daisy        -1      -1        0.67     0         -1      -1     -1         1       0.67      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.4       -1        -1          0.4     1       0.38    -1         -1
Aman         -1      -1        0.33     0.64      -1      -1     -1         0.5     0.27      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.8       -1        -1         -1       0.38    1       -1          0
Megan        -1      -1        0.5      0.5       -1      -1     -1        -1       0.67      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.33      -1        -1         -1      -1      -1        1         -1
Andrew       -1      -1        0.6      0.4       -1      -1     -1         0.4     0.4       -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1       0       -1          1

### <a id="pair-bad-team-pct"></a>Percentage of times two players are both bad (minimum 5 games both played, else -1)
**Percentage of times two players are both bad (minimum 5 games both played, else -1):**

Player      Rachel    Ewen    Peter    Brian    Anthony    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Sofia    Jay    Gathenji    Sai    Tercel    Karthik    Vishal    Olivia    Daisy    Aman    Megan    Andrew
--------  --------  ------  -------  -------  ---------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -------  -----  ----------  -----  --------  ---------  --------  --------  -------  ------  -------  --------
Rachel       -1       0.25     0.08     0.04       0.17    0.11   0.11      0.1     0.07       0.09       0.07    0.09    0.13    0.12     0.05      0       0.15     -1     0.11        0.14  -1         0          0         0.11      -1      -1      -1       -1         -1
Ewen          0.25   -1        0        0.25      -1       0.2    0         0       0.09       0.14       0.11   -1       0       0       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Peter         0.08    0       -1        0.12       0.29    0.15   0.14      0.06    0.06       0.15       0.16    0.17    0       0.06     0.09      0.11    0.13     -1     0.25       -1      0         0.06      -1        -1         -1       0       0        0.17       0
Brian         0.04    0.25     0.12    -1          0.25    0.12   0.09      0.08    0.1        0.09       0.16    0.03    0.14    0.07     0.07      0       0         0.2   0.05        0      0.12      0.17       0         0.23       0.4     0       0.36     0.33       0.2
Anthony       0.17   -1        0.29     0.25      -1       0.33   0.29      0       0.11      -1          0      -1      -1      -1        0.33     -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Minh          0.11    0.2      0.15     0.12       0.33   -1      0.11      0.04    0.12       0.23       0.11    0.22    0.33    0.08     0.17     -1       0        -1     0.17       -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jai           0.11    0        0.14     0.09       0.29    0.11  -1         0.07    0.12       0.13       0.12    0.11   -1       0.15     0.09     -1       0        -1     0.08        0     -1         0.22       0         0         -1      -1      -1       -1         -1
Jackie        0.1     0        0.06     0.08       0       0.04   0.07     -1       0.09       0.08       0.1     0.06    0.25    0.13     0.14     -1       0.08      0.2   0.13       -1      0.2       0.07       0.29      0.23      -1       0.25    0.1     -1          0
Kate          0.07    0.09     0.06     0.1        0.11    0.12   0.12      0.09   -1          0.09       0.12    0.09    0       0.09     0.17      0.33    0.08     -1     0.04        0      0.12      0         -1         0          0       0.11    0.09     0.17       0
Sushant       0.09    0.14     0.15     0.09      -1       0.23   0.13      0.08    0.09      -1          0.18    0.19    0       0.1      0         0       0.1      -1     0.14        0      0.12     -1         -1        -1         -1      -1      -1       -1         -1
Abishek       0.07    0.11     0.16     0.16       0       0.11   0.12      0.1     0.12       0.18      -1       0.17    0.14    0.11     0         0.25    0        -1     0.08        0      0.12     -1          0         0.23      -1      -1      -1       -1         -1
Ruhi          0.09   -1        0.17     0.03      -1       0.22   0.11      0.06    0.09       0.19       0.17   -1       0.14    0.35     0.11     -1      -1        -1     0.43       -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Kish          0.13    0        0        0.14      -1       0.33  -1         0.25    0          0          0.14    0.14   -1      -1        0.2      -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Alex          0.12    0        0.06     0.07      -1       0.08   0.15      0.13    0.09       0.1        0.11    0.35   -1      -1        0.1       0       0        -1     0.09        0      0.17      0         -1        -1         -1      -1      -1       -1         -1
Jeron         0.05   -1        0.09     0.07       0.33    0.17   0.09      0.14    0.17       0          0       0.11    0.2     0.1     -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Justin        0      -1        0.11     0         -1      -1     -1        -1       0.33       0          0.25   -1      -1       0       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jade          0.15   -1        0.13     0         -1       0      0         0.08    0.08       0.1        0      -1      -1       0       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Sofia        -1      -1       -1        0.2       -1      -1     -1         0.2    -1         -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jay           0.11   -1        0.25     0.05      -1       0.17   0.08      0.13    0.04       0.14       0.08    0.43   -1       0.09    -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Gathenji      0.14   -1       -1        0         -1      -1      0        -1       0          0          0      -1      -1       0       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Sai          -1      -1        0        0.12      -1      -1     -1         0.2     0.12       0.12       0.12   -1      -1       0.17    -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Tercel        0      -1        0.06     0.17      -1      -1      0.22      0.07    0         -1         -1      -1      -1       0       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1          0.2     0       0.2      0         -1
Karthik       0      -1       -1        0         -1      -1      0         0.29   -1         -1          0      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1         -1         0.14      -1      -1      -1       -1         -1
Vishal        0.11   -1       -1        0.23      -1      -1      0         0.23    0         -1          0.23   -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1          0.14     -1         -1      -1      -1       -1         -1
Olivia       -1      -1       -1        0.4       -1      -1     -1        -1       0         -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.2       -1        -1         -1       0      -1       -1         -1
Daisy        -1      -1        0        0         -1      -1     -1         0.25    0.11      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0         -1        -1          0      -1       0.12    -1         -1
Aman         -1      -1        0        0.36      -1      -1     -1         0.1     0.09      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.2       -1        -1         -1       0.12   -1       -1          0
Megan        -1      -1        0.17     0.33      -1      -1     -1        -1       0.17      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0         -1        -1         -1      -1      -1       -1         -1
Andrew       -1      -1        0        0.2       -1      -1     -1         0       0         -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1       0       -1         -1

### <a id="pair-opp-teams-pct"></a>Percentage of times two players are on different teams (minimum 5 games both played, else -1)
**Percentage of times two players are on different teams (minimum 5 games both played, else -1):**

Player      Rachel    Ewen    Peter    Brian    Anthony    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Sofia    Jay    Gathenji    Sai    Tercel    Karthik    Vishal    Olivia    Daisy    Aman    Megan    Andrew
--------  --------  ------  -------  -------  ---------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -------  -----  ----------  -----  --------  ---------  --------  --------  -------  ------  -------  --------
Rachel        0       0.5      0.53     0.55       0.67    0.62   0.45      0.44    0.52       0.52       0.66    0.61    0.4     0.44     0.25      0.43    0.31     -1     0.28        0.14  -1         0.6        0.43      0.56      -1      -1      -1       -1         -1
Ewen          0.5     0        0.83     0.17      -1       0.6    0.6       0.67    0.55       0.57       0.44   -1       1       0.8     -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Peter         0.53    0.83     0        0.49       0.57    0.56   0.49      0.54    0.59       0.51       0.56    0.5     0.45    0.55     0.55      0.22    0.47     -1     0.35       -1      0.71      0.44      -1        -1         -1       0.33    0.67     0.5        0.4
Brian         0.55    0.17     0.49     0          0.75    0.6    0.45      0.58    0.49       0.58       0.49    0.69    0.62    0.54     0.5       0.56    0.4       0.8   0.7         0.5    0.38      0.5        0.57      0.46       0.4     1       0.36     0.5        0.6
Anthony       0.67   -1        0.57     0.75       0       0.5    0.71      0.83    0.67      -1          0.8    -1      -1      -1        0.5      -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Minh          0.62    0.6      0.56     0.6        0.5     0      0.53      0.58    0.54       0.4        0.48    0.44    0.33    0.68     0.67     -1       0.86     -1     0.67       -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jai           0.45    0.6      0.49     0.45       0.71    0.53   0         0.55    0.42       0.64       0.59    0.78   -1       0.49     0.55     -1       0.67     -1     0.77        0.2   -1         0.44       0.33      1         -1      -1      -1       -1         -1
Jackie        0.44    0.67     0.54     0.58       0.83    0.58   0.55      0       0.44       0.58       0.61    0.56    0.62    0.42     0.43     -1       0.5       0.4   0.4        -1      0.6       0.6        0.43      0.62      -1       0       0.5     -1          0.6
Kate          0.52    0.55     0.59     0.49       0.67    0.54   0.42      0.44    0          0.59       0.49    0.53    0.67    0.55     0.25      0.17    0.58     -1     0.6         0.43   0.5       0.69      -1         0.43       0.8     0.33    0.73     0.33       0.6
Sushant       0.52    0.57     0.51     0.58      -1       0.4    0.64      0.58    0.59       0          0.51    0.52    0.45    0.56     0.71      0.83    0.5      -1     0.55        0.5    0.62     -1         -1        -1         -1      -1      -1       -1         -1
Abishek       0.66    0.44     0.56     0.49       0.8     0.48   0.59      0.61    0.49       0.51       0       0.56    0.5     0.57     0.82      0.62    0.5      -1     0.54        0.71   0.38     -1          0.86      0.46      -1      -1      -1       -1         -1
Ruhi          0.61   -1        0.5      0.69      -1       0.44   0.78      0.56    0.53       0.52       0.56    0       0.29    0.47     0.56     -1      -1        -1     0.43       -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Kish          0.4     1        0.45     0.62      -1       0.33  -1         0.62    0.67       0.45       0.5     0.29    0      -1        0.8      -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Alex          0.44    0.8      0.55     0.54      -1       0.68   0.49      0.42    0.55       0.56       0.57    0.47   -1       0        0.6       0.33    0.8      -1     0.55        0.6    0.5       0.62      -1        -1         -1      -1      -1       -1         -1
Jeron         0.25   -1        0.55     0.5        0.5     0.67   0.55      0.43    0.25       0.71       0.82    0.56    0.8     0.6      0        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Justin        0.43   -1        0.22     0.56      -1      -1     -1        -1       0.17       0.83       0.62   -1      -1       0.33    -1         0      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jade          0.31   -1        0.47     0.4       -1       0.86   0.67      0.5     0.58       0.5        0.5    -1      -1       0.8     -1        -1       0        -1    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Sofia        -1      -1       -1        0.8       -1      -1     -1         0.4    -1         -1         -1      -1      -1      -1       -1        -1      -1         0    -1          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Jay           0.28   -1        0.35     0.7       -1       0.67   0.77      0.4     0.6        0.55       0.54    0.43   -1       0.55    -1        -1      -1        -1     0          -1     -1        -1         -1        -1         -1      -1      -1       -1         -1
Gathenji      0.14   -1       -1        0.5       -1      -1      0.2      -1       0.43       0.5        0.71   -1      -1       0.6     -1        -1      -1        -1    -1           0     -1        -1         -1        -1         -1      -1      -1       -1         -1
Sai          -1      -1        0.71     0.38      -1      -1     -1         0.6     0.5        0.62       0.38   -1      -1       0.5     -1        -1      -1        -1    -1          -1      0        -1         -1        -1         -1      -1      -1       -1         -1
Tercel        0.6    -1        0.44     0.5       -1      -1      0.44      0.6     0.69      -1         -1      -1      -1       0.62    -1        -1      -1        -1    -1          -1     -1         0         -1        -1          0.4     0.6     0.2      0.67      -1
Karthik       0.43   -1       -1        0.57      -1      -1      0.33      0.43   -1         -1          0.86   -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1          0         0.71      -1      -1      -1       -1         -1
Vishal        0.56   -1       -1        0.46      -1      -1      1         0.62    0.43      -1          0.46   -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1          0.71      0         -1      -1      -1       -1         -1
Olivia       -1      -1       -1        0.4       -1      -1     -1        -1       0.8       -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.4       -1        -1          0       0.6    -1       -1         -1
Daisy        -1      -1        0.33     1         -1      -1     -1         0       0.33      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.6       -1        -1          0.6     0       0.62    -1         -1
Aman         -1      -1        0.67     0.36      -1      -1     -1         0.5     0.73      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.2       -1        -1         -1       0.62    0       -1          1
Megan        -1      -1        0.5      0.5       -1      -1     -1        -1       0.33      -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1         0.67      -1        -1         -1      -1      -1        0         -1
Andrew       -1      -1        0.4      0.6       -1      -1     -1         0.6     0.6       -1         -1      -1      -1      -1       -1        -1      -1        -1    -1          -1     -1        -1         -1        -1         -1      -1       1       -1          0

### <a id="pair-teams-cnt"></a>Count of times two players are on the same team

Player      Rachel    Ewen    Peter    Brian    Anthony    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Shashank    Angela    Elysia    Jeron    Sachin    Justin    Jade    Sofia    Jay    Greg    Derek    Gathenji    Caro    Sai    Nabeel    Ronnie    Neha    Ira    Kawin    Abrar    Tercel    Karthik    Vishal    Olivia    AlexY    Daisy    Aman    Megan    Andrew
--------  --------  ------  -------  -------  ---------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  ----------  --------  --------  -------  --------  --------  ------  -------  -----  ------  -------  ----------  ------  -----  --------  --------  ------  -----  -------  -------  --------  ---------  --------  --------  -------  -------  ------  -------  --------
Rachel         126       4       44       50          4      14     35        50      42         36         33       9       9      29           1         1         0       15         0         4       9        1     13       0        1           6       0      2         0         1       0      0        0        1         2          4         4         0        0        0       1        0         1
Ewen             4      13        1       10          1       2      2         2       5          3          5       2       0       1           1         0         0        0         0         0       2        0      1       0        0           0       0      1         1         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Peter           44       1      168       78          3      18     36        59      50         49         51      12       6      35           1         1         0       10         0         7       8        0     13       0        2           1       0      2         2         2       1      0        1        1         9          0         0         0        1        4       3        3         3
Brian           50      10       78      206          3      21     42        61      75         48         75      12       8      37           1         1         0       14         0         4       9        1      6       2        3           3       0      5         1         0       0      1        0        0         9          3         7         3        1        0       7        3         2
Anthony          4       1        3        3         12       3      2         1       3          0          1       2       2       0           0         0         0        3         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Minh            14       2       18       21          3      58      9        19      22         18         24       5       4       8           0         0         0        2         0         1       1        2      2       0        0           0       2      2         0         1       0      0        0        0         0          0         0         0        0        3       1        0         3
Jai             35       2       36       42          2       9     87        30      38         16         23       4       2      20           0         0         0        5         0         0       3        0      3       1        0           4       0      2         0         0       0      0        0        0         5          4         0         0        0        1       1        0         2
Jackie          50       2       59       61          1      19     30       158      63         36         44       8       3      36           0         0         1       12         1         1       6        3      9       0        1           2       1      2         2         2       2      0        2        1         6          4         5         1        2        8       5        1         2
Kate            42       5       50       75          3      22     38        63     161         39         62      15       5      30           0         0         0        9         0         5       5        1     10       2        1           4       2      4         3         1       1      1        1        1         4          1         4         1        2        6       3        4         2
Sushant         36       3       49       48          0      18     16        36      39        125         56      15       6      30           2         0         0        5         0         1       5        1     10       2        3           3       1      3         0         1       0      0        0        0         4          0         0         0        0        0       0        0         0
Abishek         33       5       51       75          1      24     23        44      62         56        161      16       7      33           0         0         0        3         0         3       7        1     11       1        2           2       1      5         2         0       0      0        0        1         2          1         7         0        0        1       1        0         2
Ruhi             9       2       12       12          2       5      4         8      15         15         16      40       5       9           0         0         0        4         0         0       2        0      4       1        1           2       2      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Kish             9       0        6        8          2       4      2         3       5          6          7       5      21       2           1         0         0        1         0         0       0        0      1       0        0           1       1      0         2         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Alex            29       1       35       37          0       8     20        36      30         30         33       9       2      94           1         0         0        4         0         4       1        2      5       0        0           2       0      3         0         1       0      0        0        0         3          0         0         0        0        0       0        0         0
Shashank         1       1        1        1          0       0      0         0       0          2          0       0       1       1           2         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Angela           1       0        1        1          0       0      0         0       0          0          0       0       0       0           0         1         0        0         0         1       1        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Elysia           0       0        0        0          0       0      0         1       0          0          0       0       0       0           0         0         1        1         1         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jeron           15       0       10       14          3       2      5        12       9          5          3       4       1       4           0         0         1       30         1         0       0        1      2       0        0           0       1      0         0         0       0      0        0        0         1          0         0         0        0        0       0        0         0
Sachin           0       0        0        0          0       0      0         1       0          0          0       0       0       0           0         0         1        1         1         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Justin           4       0        7        4          0       1      0         1       5          1          3       0       0       4           0         1         0        0         0         9       1        0      0       0        0           0       0      0         0         1       0      0        0        0         0          0         0         0        0        0       0        0         0
Jade             9       2        8        9          0       1      3         6       5          5          7       2       0       1           0         1         0        0         0         1      18        0      3       0        2           0       0      1         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sofia            1       0        0        1          0       2      0         3       1          1          1       0       0       2           0         0         0        1         0         0       0        5      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jay             13       1       13        6          0       2      3         9      10         10         11       4       1       5           0         0         0        2         0         0       3        0     26       0        0           0       0      0         0         0       0      0        0        1         0          0         0         0        0        0       0        0         0
Greg             0       0        0        2          0       0      1         0       2          2          1       1       0       0           0         0         0        0         0         0       0        0      0       2        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Derek            1       0        2        3          0       0      0         1       1          3          2       1       0       0           0         0         0        0         0         0       2        0      0       0        4           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Gathenji         6       0        1        3          0       0      4         2       4          3          2       2       1       2           0         0         0        0         0         0       0        0      0       0        0           7       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Caro             0       0        0        0          0       2      0         1       2          1          1       2       1       0           0         0         0        1         0         0       0        0      0       0        0           0       3      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sai              2       1        2        5          0       2      2         2       4          3          5       0       0       3           0         0         0        0         0         0       1        0      0       0        0           0       0      8         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Nabeel           0       1        2        1          0       0      0         2       3          0          2       0       2       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         4         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Ronnie           1       0        2        0          0       1      0         2       1          1          0       0       0       1           0         0         0        0         0         1       0        0      0       0        0           0       0      0         0         2       0      0        0        0         0          0         0         0        0        0       0        0         0
Neha             0       0        1        0          0       0      0         2       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       2      0        2        0         0          0         0         0        0        0       0        0         0
Ira              0       0        0        1          0       0      0         0       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      1        0        0         0          0         0         0        0        0       0        0         0
Kawin            0       0        1        0          0       0      0         2       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       2      0        2        0         0          0         0         0        0        0       0        0         0
Abrar            1       0        1        0          0       0      0         1       1          0          1       0       0       0           0         0         0        0         0         0       0        0      1       0        0           0       0      0         0         0       0      0        0        2         0          0         0         0        0        0       0        0         0
Tercel           2       0        9        9          0       0      5         6       4          4          2       0       0       3           0         0         0        1         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0        20          0         0         3        2        2       4        2         0
Karthik          4       0        0        3          0       0      4         4       1          0          1       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          7         2         0        0        0       0        0         0
Vishal           4       0        0        7          0       0      0         5       4          0          7       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          2        13         0        0        0       0        0         0
Olivia           0       0        0        3          0       0      0         1       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         3          0         0         5        3        2       4        0         0
AlexY            0       0        1        1          0       0      0         2       2          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         2          0         0         3        4        3       2        1         0
Daisy            0       0        4        0          0       3      1         8       6          0          1       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         2          0         0         2        3        9       3        1         2
Aman             1       0        3        7          0       1      1         5       3          0          1       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         4          0         0         4        2        3      11        1         0
Megan            0       0        3        3          0       0      0         1       4          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         2          0         0         0        1        1       1        6         0
Andrew           1       0        3        2          0       3      2         2       2          0          2       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        2       0        0         5

### <a id="pair-bad-team-cnt"></a>Count of times two players are both bad

Player      Rachel    Ewen    Peter    Brian    Anthony    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Shashank    Angela    Elysia    Jeron    Sachin    Justin    Jade    Sofia    Jay    Greg    Derek    Gathenji    Caro    Sai    Nabeel    Ronnie    Neha    Ira    Kawin    Abrar    Tercel    Karthik    Vishal    Olivia    AlexY    Daisy    Aman    Megan    Andrew
--------  --------  ------  -------  -------  ---------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  ----------  --------  --------  -------  --------  --------  ------  -------  -----  ------  -------  ----------  ------  -----  --------  --------  ------  -----  -------  -------  --------  ---------  --------  --------  -------  -------  ------  -------  --------
Rachel          -1       2        7        4          2       4      7         9       6          7          7       2       2       6           0         0         0        1         0         0       2        0      2       0        0           1       0      1         0         0       0      0        0        0         0          0         1         0        0        0       0        0         1
Ewen             2      -1        0        3          1       1      0         0       1          1          1       1       0       0           1         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Peter            7       0       -1       19          2       6     10         8       7         15         18       4       0       5           0         0         0        2         0         1       2        0      5       0        0           0       0      0         1         0       0      0        0        0         1          0         0         0        0        0       0        1         0
Brian            4       3       19       -1          3       6      7        11      15         10         24       1       3       6           1         0         0        2         0         0       0        1      1       0        0           0       0      1         0         0       0      1        0        0         3          0         3         2        0        0       4        2         1
Anthony          2       1        2        3         -1       2      2         0       1          0          0       1       1       0           0         0         0        2         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Minh             4       1        6        6          2      -1      2         2       6          7          5       2       2       2           0         0         0        1         0         1       0        1      1       0        0           0       1      0         0         0       0      0        0        0         0          0         0         0        0        1       1        0         1
Jai              7       0       10        7          2       2     -1         5       8          6          7       2       0       6           0         0         0        1         0         0       0        0      1       0        0           0       0      1         0         0       0      0        0        0         2          0         0         0        0        0       0        0         1
Jackie           9       0        8       11          0       2      5        -1      10          7         11       1       2       8           0         0         1        3         1         0       1        1      2       0        0           0       1      1         1         0       0      0        0        1         1          2         3         0        0        2       1        0         0
Kate             6       1        7       15          1       6      8        10      -1          9         14       3       0       6           0         0         0        2         0         2       1        0      1       0        0           0       1      1         1         0       0      1        0        0         0          0         0         0        0        1       1        1         0
Sushant          7       1       15       10          0       7      6         7       9         -1         21       6       0       7           1         0         0        0         0         0       1        1      3       0        1           0       0      1         0         0       0      0        0        0         2          0         0         0        0        0       0        0         0
Abishek          7       1       18       24          0       5      7        11      14         21         -1       6       2       8           0         0         0        0         0         2       0        1      2       0        1           0       0      1         1         0       0      0        0        0         1          0         3         0        0        0       1        0         0
Ruhi             2       1        4        1          1       2      2         1       3          6          6      -1       1       6           0         0         0        1         0         0       0        0      3       0        0           1       1      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Kish             2       0        0        3          1       2      0         2       0          0          2       1      -1       0           0         0         0        1         0         0       0        0      0       0        0           0       1      0         1         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Alex             6       0        5        6          0       2      6         8       6          7          8       6       0      -1           0         0         0        1         0         0       0        1      1       0        0           0       0      1         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Shashank         0       1        0        1          0       0      0         0       0          1          0       0       0       0          -1         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Angela           0       0        0        0          0       0      0         0       0          0          0       0       0       0           0        -1         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Elysia           0       0        0        0          0       0      0         1       0          0          0       0       0       0           0         0        -1        1         1         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jeron            1       0        2        2          2       1      1         3       2          0          0       1       1       1           0         0         1       -1         1         0       0        0      0       0        0           0       1      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sachin           0       0        0        0          0       0      0         1       0          0          0       0       0       0           0         0         1        1        -1         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Justin           0       0        1        0          0       1      0         0       2          0          2       0       0       0           0         0         0        0         0        -1       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jade             2       0        2        0          0       0      0         1       1          1          0       0       0       0           0         0         0        0         0         0      -1        0      1       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sofia            0       0        0        1          0       1      0         1       0          1          1       0       0       1           0         0         0        0         0         0       0       -1      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jay              2       0        5        1          0       1      1         2       1          3          2       3       0       1           0         0         0        0         0         0       1        0     -1       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Greg             0       0        0        0          0       0      0         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0      -1        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Derek            0       0        0        0          0       0      0         0       0          1          1       0       0       0           0         0         0        0         0         0       0        0      0       0       -1           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Gathenji         1       0        0        0          0       0      0         0       0          0          0       1       0       0           0         0         0        0         0         0       0        0      0       0        0          -1       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Caro             0       0        0        0          0       1      0         1       1          0          0       1       1       0           0         0         0        1         0         0       0        0      0       0        0           0      -1      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sai              1       0        0        1          0       0      1         1       1          1          1       0       0       1           0         0         0        0         0         0       0        0      0       0        0           0       0     -1         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Nabeel           0       0        1        0          0       0      0         1       1          0          1       0       1       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0        -1         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Ronnie           0       0        0        0          0       0      0         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0        -1       0      0        0        0         0          0         0         0        0        0       0        0         0
Neha             0       0        0        0          0       0      0         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0      -1      0        0        0         0          0         0         0        0        0       0        0         0
Ira              0       0        0        1          0       0      0         0       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0     -1        0        0         0          0         0         0        0        0       0        0         0
Kawin            0       0        0        0          0       0      0         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0       -1        0         0          0         0         0        0        0       0        0         0
Abrar            0       0        0        0          0       0      0         1       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0       -1         0          0         0         0        0        0       0        0         0
Tercel           0       0        1        3          0       0      2         1       0          2          1       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0        -1          0         0         1        0        0       1        0         0
Karthik          0       0        0        0          0       0      0         2       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0         -1         1         0        0        0       0        0         0
Vishal           1       0        0        3          0       0      0         3       0          0          3       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          1        -1         0        0        0       0        0         0
Olivia           0       0        0        2          0       0      0         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         1          0         0        -1        0        0       2        0         0
AlexY            0       0        0        0          0       0      0         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0       -1        0       0        0         0
Daisy            0       0        0        0          0       1      0         2       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0       -1       1        0         0
Aman             0       0        0        4          0       1      0         1       1          0          1       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         1          0         0         2        0        1      -1        0         0
Megan            0       0        1        2          0       0      0         0       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0       -1         0
Andrew           1       0        0        1          0       1      1         0       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0        -1

### <a id="pair-opp-teams-cnt"></a>Count of times two players are on different teams

Player      Rachel    Ewen    Peter    Brian    Anthony    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Shashank    Angela    Elysia    Jeron    Sachin    Justin    Jade    Sofia    Jay    Greg    Derek    Gathenji    Caro    Sai    Nabeel    Ronnie    Neha    Ira    Kawin    Abrar    Tercel    Karthik    Vishal    Olivia    AlexY    Daisy    Aman    Megan    Andrew
--------  --------  ------  -------  -------  ---------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  ----------  --------  --------  -------  --------  --------  ------  -------  -----  ------  -------  ----------  ------  -----  --------  --------  ------  -----  -------  -------  --------  ---------  --------  --------  -------  -------  ------  -------  --------
Rachel           0       4       49       60          8      23     29        40      45         39         64      14       6      23           1         0         1        5         1         3       4        3      5       0        3           1       1      1         2         0       0      0        0        0         3          3         5         0        0        0       1        0         0
Ewen             4       0        5        2          0       3      3         4       6          4          4       1       5       4           1         0         0        1         0         0       0        0      1       0        0           0       0      0         3         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Peter           49       5        0       76          4      23     34        69      71         51         64      12       5      42           1         0         1       12         1         2       7        3      7       2        2           3       0      5         0         0       1      1        1        1         7          0         0         2        1        2       6        3         2
Brian           60       2       76        0          9      31     35        85      73         65         73      27      13      44           1         0         1       14         1         5       6        4     14       0        1           3       3      3         3         2       2      0        2        1         9          4         6         2        3        9       4        3         3
Anthony          8       0        4        9          0       3      5         5       6          1          4       1       2       0           0         0         0        3         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Minh            23       3       23       31          3       0     10        26      26         12         22       4       2      17           0         0         0        4         0         2       6        0      4       0        0           0       1      2         0         0       1      0        1        0         0          0         0         0        0        1       3        0         1
Jai             29       3       34       35          5      10      0        37      27         29         33      14       2      19           1         0         0        6         0         2       6        0     10       1        2           1       0      1         1         0       0      0        0        2         4          2         6         0        0        1       2        0         1
Jackie          40       4       69       85          5      26     37         0      50         49         68      10       5      26           0         1         0        9         0         2       6        2      6       0        1           2       1      3         2         0       0      1        0        1         9          3         8         3        1        0       5        1         3
Kate            45       6       71       73          6      26     27        50       0         56         59      17      10      36           2         0         0        3         0         1       7        1     15       0        1           3       1      4         1         1       1      0        1        0         9          0         3         4        2        3       8        2         3
Sushant         39       4       51       65          1      12     29        49      56          0         59      16       5      38           0         0         0       12         0         5       5        3     12       0        1           3       2      5         0         1       0      0        0        1         0          0         0         0        0        0       0        0         0
Abishek         64       4       64       73          4      22     33        68      59         59          0      20       7      43           0         0         0       14         0         5       7        3     13       1        2           5       2      3         2         2       0      0        0        0         2          6         6         0        0        2       2        0         1
Ruhi            14       1       12       27          1       4     14        10      17         16         20       0       2       8           0         0         0        5         0         0       2        0      3       0        0           2       1      2         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Kish             6       5        5       13          2       2      2         5      10          5          7       2       0       1           1         0         0        4         0         0       0        0      0       0        0           0       2      0         1         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Alex            23       4       42       44          0      17     19        26      36         38         43       8       1       0           1         0         0        6         0         2       4        1      6       0        0           3       0      3         1         1       0      0        0        1         5          0         0         0        0        0       0        0         0
Shashank         1       1        1        1          0       0      1         0       2          0          0       0       1       1           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Angela           0       0        0        0          0       0      0         1       0          0          0       0       0       0           0         0         1        1         1         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Elysia           1       0        1        1          0       0      0         0       0          0          0       0       0       0           0         1         0        0         0         1       1        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jeron            5       1       12       14          3       4      6         9       3         12         14       5       4       6           0         1         0        0         0         1       2        1      1       0        1           0       1      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sachin           1       0        1        1          0       0      0         0       0          0          0       0       0       0           0         1         0        0         0         1       1        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Justin           3       0        2        5          0       2      2         2       1          5          5       0       0       2           0         0         1        1         1         0       0        0      0       0        0           0       0      1         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Jade             4       0        7        6          0       6      6         6       7          5          7       2       0       4           0         0         1        2         1         0       0        0      1       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sofia            3       0        3        4          0       0      0         2       1          3          3       0       0       1           0         0         0        1         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         2          0         0         0        0        0       0        0         0
Jay              5       1        7       14          0       4     10         6      15         12         13       3       0       6           0         0         0        1         0         0       1        0      0       2        0           0       0      2         0         0       0      0        0        0         4          0         0         0        0        0       0        0         0
Greg             0       0        2        0          0       0      1         0       0          0          1       0       0       0           0         0         0        0         0         0       0        0      2       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Derek            3       0        2        1          0       0      2         1       1          1          2       0       0       0           0         0         0        1         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Gathenji         1       0        3        3          0       0      1         2       3          3          5       2       0       3           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Caro             1       0        0        3          0       1      0         1       1          2          2       1       2       0           0         0         0        1         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Sai              1       0        5        3          0       2      1         3       4          5          3       2       0       3           0         0         0        0         0         1       0        0      2       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Nabeel           2       3        0        3          0       0      1         2       1          0          2       0       1       1           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Ronnie           0       0        0        2          0       0      0         0       1          1          2       0       0       1           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        0       0        0         0
Neha             0       0        1        2          0       1      0         0       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      1        0        0         0          0         0         0        0        0       0        0         0
Ira              0       0        1        0          0       0      0         1       0          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       1      0        1        0         0          0         0         0        0        0       0        0         0
Kawin            0       0        1        2          0       1      0         0       1          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      1        0        0         0          0         0         0        0        0       0        0         0
Abrar            0       0        1        1          0       0      2         1       0          1          0       0       0       1           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         1          0         0         0        0        0       0        0         0
Tercel           3       0        7        9          0       0      4         9       9          0          2       0       0       5           0         0         0        0         0         0       0        2      4       0        0           0       0      0         0         0       0      0        0        1         0          0         0         2        2        3       1        4         0
Karthik          3       0        0        4          0       0      2         3       0          0          6       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         5         0        0        0       0        0         0
Vishal           5       0        0        6          0       0      6         8       3          0          6       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          5         0         0        0        0       0        0         0
Olivia           0       0        2        2          0       0      0         3       4          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         2          0         0         0        1        3       0        2         0
AlexY            0       0        1        3          0       0      0         1       2          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         2          0         0         1        0        1       1        1         0
Daisy            0       0        2        9          0       1      1         0       3          0          2       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         3          0         0         3        1        0       5        1         2
Aman             1       0        6        4          0       3      2         5       8          0          2       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         1          0         0         0        1        5       0        2         5
Megan            0       0        3        3          0       0      0         1       2          0          0       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         4          0         0         2        1        1       2        0         0
Andrew           0       0        2        3          0       1      1         3       3          0          1       0       0       0           0         0         0        0         0         0       0        0      0       0        0           0       0      0         0         0       0      0        0        0         0          0         0         0        0        2       5        0         0

### <a id="pair-teams-win-pct"></a>Percentage of times two players win, given that they are on the same team (minimum 5 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

Player      Rachel    Ewen    Peter    Brian    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Jay    Gathenji    Sai
--------  --------  ------  -------  -------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -----  ----------  -----
Rachel       -1       -1       0.28     0.47    0.44   0.23      0.42    0.4        0.37       0.57    0.14    0.43    0.38     0.33     -1       -1     0.4         0.17   -1
Ewen         -1       -1      -1        0.5    -1     -1        -1       0.6       -1          0.4    -1      -1      -1       -1        -1       -1    -1          -1      -1
Peter         0.28    -1      -1        0.52    0.44   0.33      0.41    0.5        0.41       0.61    0.4     0.2     0.3     -1         0.14     0.2   0.5        -1      -1
Brian         0.47     0.5     0.52    -1       0.43   0.43      0.45    0.6        0.5        0.62    0.58    0.83    0.54     0.5      -1        0.5  -1          -1       0.2
Minh          0.44    -1       0.44     0.43   -1      0         0.27    0.56       0.38       0.43    0.2    -1       0.4     -1        -1       -1    -1          -1      -1
Jai           0.23    -1       0.33     0.43    0     -1         0.08    0.36       0.31       0.56   -1      -1       0.33    -1        -1       -1    -1          -1      -1
Jackie        0.42    -1       0.41     0.45    0.27   0.08     -1       0.48       0.46       0.5     0      -1       0.5      0.33     -1       -1    -1          -1      -1
Kate          0.4      0.6     0.5      0.6     0.56   0.36      0.48   -1          0.42       0.61    0.27   -1       0.58     0.6       0.6     -1    -1          -1      -1
Sushant       0.37    -1       0.41     0.5     0.38   0.31      0.46    0.42      -1          0.56    0.43    0.4     0.44    -1        -1       -1     0.12       -1      -1
Abishek       0.57     0.4     0.61     0.62    0.43   0.56      0.5     0.61       0.56      -1       0.53    0.83    0.55    -1        -1        0.5   0.57       -1       0.2
Ruhi          0.14    -1       0.4      0.58    0.2   -1         0       0.27       0.43       0.53   -1      -1       0.56    -1        -1       -1    -1          -1      -1
Kish          0.43    -1       0.2      0.83   -1     -1        -1      -1          0.4        0.83   -1      -1      -1       -1        -1       -1    -1          -1      -1
Alex          0.38    -1       0.3      0.54    0.4    0.33      0.5     0.58       0.44       0.55    0.56   -1      -1       -1        -1       -1    -1          -1      -1
Jeron         0.33    -1      -1        0.5    -1     -1         0.33    0.6       -1         -1      -1      -1      -1       -1        -1       -1    -1          -1      -1
Justin       -1       -1       0.14    -1      -1     -1        -1       0.6       -1         -1      -1      -1      -1       -1        -1       -1    -1          -1      -1
Jade         -1       -1       0.2      0.5    -1     -1        -1      -1         -1          0.5    -1      -1      -1       -1        -1       -1    -1          -1      -1
Jay           0.4     -1       0.5     -1      -1     -1        -1      -1          0.12       0.57   -1      -1      -1       -1        -1       -1    -1          -1      -1
Gathenji      0.17    -1      -1       -1      -1     -1        -1      -1         -1         -1      -1      -1      -1       -1        -1       -1    -1          -1      -1
Sai          -1       -1      -1        0.2    -1     -1        -1      -1         -1          0.2    -1      -1      -1       -1        -1       -1    -1          -1      -1

Cheesy wins excluded:

Player      Rachel    Ewen    Peter    Brian    Minh    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Jay    Gathenji
--------  --------  ------  -------  -------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -----  ----------
Rachel       -1       -1       0.28     0.44    0.44   0.25      0.42    0.38       0.38       0.55    0       0.33    0.41     0.33     -1       -1     0.4         0.17
Ewen         -1       -1      -1        0.5    -1     -1        -1       0.6       -1          0.4    -1      -1      -1       -1        -1       -1    -1          -1
Peter         0.28    -1      -1        0.5     0.29   0.29      0.37    0.41       0.38       0.57    0.4    -1       0.27    -1         0.14     0.2   0.5        -1
Brian         0.44     0.5     0.5     -1       0.38   0.4       0.44    0.57       0.49       0.61    0.5    -1       0.52     0.5      -1        0.5  -1          -1
Minh          0.44    -1       0.29     0.38   -1      0         0.08    0.46       0.29       0.4     0.2    -1      -1       -1        -1       -1    -1          -1
Jai           0.25    -1       0.29     0.4     0     -1         0.08    0.36       0.31       0.53   -1      -1       0.4     -1        -1       -1    -1          -1
Jackie        0.42    -1       0.37     0.44    0.08   0.08     -1       0.42       0.41       0.48    0      -1       0.47     0.33     -1       -1    -1          -1
Kate          0.38     0.6     0.41     0.57    0.46   0.36      0.42   -1          0.36       0.57    0.27   -1       0.57     0.6       0.6     -1    -1          -1
Sushant       0.38    -1       0.38     0.49    0.29   0.31      0.41    0.36      -1          0.54    0.43    0.4     0.42    -1        -1       -1     0.12       -1
Abishek       0.55     0.4     0.57     0.61    0.4    0.53      0.48    0.57       0.54      -1       0.5     0.8     0.54    -1        -1        0.5   0.57       -1
Ruhi          0       -1       0.4      0.5     0.2   -1         0       0.27       0.43       0.5    -1      -1       0.67    -1        -1       -1    -1          -1
Kish          0.33    -1      -1       -1      -1     -1        -1      -1          0.4        0.8    -1      -1      -1       -1        -1       -1    -1          -1
Alex          0.41    -1       0.27     0.52   -1      0.4       0.47    0.57       0.42       0.54    0.67   -1      -1       -1        -1       -1    -1          -1
Jeron         0.33    -1      -1        0.5    -1     -1         0.33    0.6       -1         -1      -1      -1      -1       -1        -1       -1    -1          -1
Justin       -1       -1       0.14    -1      -1     -1        -1       0.6       -1         -1      -1      -1      -1       -1        -1       -1    -1          -1
Jade         -1       -1       0.2      0.5    -1     -1        -1      -1         -1          0.5    -1      -1      -1       -1        -1       -1    -1          -1
Jay           0.4     -1       0.5     -1      -1     -1        -1      -1          0.12       0.57   -1      -1      -1       -1        -1       -1    -1          -1
Gathenji      0.17    -1      -1       -1      -1     -1        -1      -1         -1         -1      -1      -1      -1       -1        -1       -1    -1          -1

### <a id="pair-bad-team-win-pct"></a>Percentage of times two players win, given that they are both bad (minimum 3 games, else -1)


*Competitive games only statistic.*

Cheesy wins included:

Player      Minh    Rachel    Ewen    Jai    Kate    Sushant    Abishek    Ruhi    Brian    Peter    Jackie    Alex    Jay
--------  ------  --------  ------  -----  ------  ---------  ---------  ------  -------  -------  --------  ------  -----
Minh       -1         0.67      -1  -1       0.8        0.33       0.6    -1        0.67    -1        -1      -1     -1
Rachel      0.67     -1         -1   0       0.6        0.83       1      -1        0.75     0.5       1       0.5   -1
Ewen       -1        -1         -1  -1      -1         -1         -1      -1        1       -1        -1      -1     -1
Jai        -1         0         -1  -1       0.67       0.33       0.8    -1       -1        0.25     -1       0     -1
Kate        0.8       0.6       -1   0.67   -1          0.29       0.85    0.33     0.83     0.25      0.25    1     -1
Sushant     0.33      0.83      -1   0.33    0.29      -1          0.79    0.67     0.71     0.58      0.67    0.67  -1
Abishek     0.6       1         -1   0.8     0.85       0.79      -1       0.67     0.73     0.64      0.5     0.88  -1
Ruhi       -1        -1         -1  -1       0.33       0.67       0.67   -1       -1        0.75     -1       0.5    0.33
Brian       0.67      0.75       1  -1       0.83       0.71       0.73   -1       -1        0.89      0.8     0.83  -1
Peter      -1         0.5       -1   0.25    0.25       0.58       0.64    0.75     0.89    -1         0.8     0.33   1
Jackie     -1         1         -1  -1       0.25       0.67       0.5    -1        0.8      0.8      -1      -1     -1
Alex       -1         0.5       -1   0       1          0.67       0.88    0.5      0.83     0.33     -1      -1     -1
Jay        -1        -1         -1  -1      -1         -1         -1       0.33    -1        1        -1      -1     -1

Cheesy wins excluded:

Player      Minh    Rachel    Ewen    Jai    Kate    Sushant    Abishek    Ruhi    Brian    Peter    Jackie    Alex    Jay
--------  ------  --------  ------  -----  ------  ---------  ---------  ------  -------  -------  --------  ------  -----
Minh       -1         0.67      -1  -1       0.8        0.33       0.6    -1        0.67    -1        -1      -1     -1
Rachel      0.67     -1         -1   0       0.6        1          1      -1        0.75     0.5       1       0.75  -1
Ewen       -1        -1         -1  -1      -1         -1         -1      -1        1       -1        -1      -1     -1
Jai        -1         0         -1  -1       0.67       0.33       0.8    -1       -1        0.25     -1      -1     -1
Kate        0.8       0.6       -1   0.67   -1          0.29       0.85    0.33     0.83     0.25      0.25    1     -1
Sushant     0.33      1         -1   0.33    0.29      -1          0.79    0.67     0.71     0.58      0.67    0.67  -1
Abishek     0.6       1         -1   0.8     0.85       0.79      -1       0.67     0.85     0.64      0.5     0.88  -1
Ruhi       -1        -1         -1  -1       0.33       0.67       0.67   -1       -1        0.75     -1       0.75   0.33
Brian       0.67      0.75       1  -1       0.83       0.71       0.85   -1       -1        0.89      0.8     0.83  -1
Peter      -1         0.5       -1   0.25    0.25       0.58       0.64    0.75     0.89    -1         0.8     0.33   1
Jackie     -1         1         -1  -1       0.25       0.67       0.5    -1        0.8      0.8      -1      -1     -1
Alex       -1         0.75      -1  -1       1          0.67       0.88    0.75     0.83     0.33     -1      -1     -1
Jay        -1        -1         -1  -1      -1         -1         -1       0.33    -1        1        -1      -1     -1

### <a id="pair-opp-teams-win-pct"></a>Percentage of times two players win, given that they are on opposite teams (minimum 5 games, else -1)


*Win percentages are presented as row player vs column player.*

*Competitive games only statistic.*

Cheesy wins included:

Player      Peter    Brian    Minh    Rachel    Ewen    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Jay    Gathenji    Sai
--------  -------  -------  ------  --------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -----  ----------  -----
Peter       -1        0.4     0.6       0.48     0.2   0.56      0.48    0.49       0.47       0.39    0.7    -1       0.6      0.4       -1      -1    -1           -1      0.8
Brian        0.6     -1       0.6       0.63    -1     0.71      0.58    0.57       0.57       0.48    0.73    0.64    0.64    -1          0.6    -1     0.55        -1     -1
Minh         0.4      0.4    -1         0.5     -1     0.67      0.54    0.28       0.33       0.41   -1      -1       0.33    -1         -1      -1    -1           -1     -1
Rachel       0.52     0.37    0.5      -1       -1     0.55      0.55    0.44       0.45       0.33    0.62    0.6     0.25    -1         -1      -1    -1           -1     -1
Ewen         0.8     -1      -1        -1       -1    -1        -1       0.5       -1         -1      -1       0.6    -1       -1         -1      -1    -1           -1     -1
Jai          0.44     0.29    0.33      0.45    -1    -1         0.45    0.29       0.38       0.24    0.4    -1       0.25    -1         -1      -1    -1           -1     -1
Jackie       0.52     0.42    0.46      0.45    -1     0.55     -1       0.46       0.38       0.39    0.5    -1       0.53    -1         -1      -1    -1           -1     -1
Kate         0.51     0.43    0.72      0.56     0.5   0.71      0.54   -1          0.57       0.44    0.62    0.4     0.52    -1         -1       0.8   0.44        -1     -1
Sushant      0.53     0.43    0.67      0.55    -1     0.62      0.62    0.42      -1          0.36    0.6     0.4     0.42     0.62       0.6    -1     0.17        -1      0.8
Abishek      0.61     0.52    0.59      0.67    -1     0.76      0.61    0.56       0.64      -1       0.74    0.71    0.58     0.6        0.6    -1     0.71         0.8   -1
Ruhi         0.3      0.27   -1         0.38    -1     0.6       0.5     0.38       0.4        0.26   -1      -1       0.62     0.6       -1      -1    -1           -1     -1
Kish        -1        0.36   -1         0.4      0.4  -1        -1       0.6        0.6        0.29   -1      -1      -1       -1         -1      -1    -1           -1     -1
Alex         0.4      0.36    0.67      0.75    -1     0.75      0.47    0.48       0.58       0.42    0.38   -1      -1       -1         -1      -1    -1           -1     -1
Jeron        0.6     -1      -1        -1       -1    -1        -1      -1          0.38       0.4     0.4    -1      -1       -1         -1      -1    -1           -1     -1
Justin      -1        0.4    -1        -1       -1    -1        -1      -1          0.4        0.4    -1      -1      -1       -1         -1      -1    -1           -1     -1
Jade        -1       -1      -1        -1       -1    -1        -1       0.2       -1         -1      -1      -1      -1       -1         -1      -1    -1           -1     -1
Jay         -1        0.45   -1        -1       -1    -1        -1       0.56       0.83       0.29   -1      -1      -1       -1         -1      -1    -1           -1     -1
Gathenji    -1       -1      -1        -1       -1    -1        -1      -1         -1          0.2    -1      -1      -1       -1         -1      -1    -1           -1     -1
Sai          0.2     -1      -1        -1       -1    -1        -1      -1          0.2       -1      -1      -1      -1       -1         -1      -1    -1           -1     -1

Cheesy wins excluded:

Player      Peter    Brian    Minh    Rachel    Ewen    Jai    Jackie    Kate    Sushant    Abishek    Ruhi    Kish    Alex    Jeron    Justin    Jade    Jay    Gathenji
--------  -------  -------  ------  --------  ------  -----  --------  ------  ---------  ---------  ------  ------  ------  -------  --------  ------  -----  ----------
Peter       -1        0.37    0.6       0.44     0.2   0.53      0.48    0.49       0.45       0.36    0.67   -1       0.57     0.4       -1      -1    -1           -1
Brian        0.63    -1       0.64      0.61    -1     0.69      0.62    0.59       0.58       0.48    0.7     0.6     0.63    -1          0.6    -1     0.55        -1
Minh         0.4      0.36   -1         0.5     -1     0.6       0.54    0.29       0.33       0.36   -1      -1       0.29    -1         -1      -1    -1           -1
Rachel       0.56     0.39    0.5      -1       -1     0.6       0.57    0.47       0.48       0.36    0.62   -1       0.25    -1         -1      -1    -1           -1
Ewen         0.8     -1      -1        -1       -1    -1        -1       0.5       -1         -1      -1       0.6    -1       -1         -1      -1    -1           -1
Jai          0.47     0.31    0.4       0.4     -1    -1         0.5     0.33       0.38       0.26    0.4    -1       0.25    -1         -1      -1    -1           -1
Jackie       0.52     0.38    0.46      0.43    -1     0.5      -1       0.46       0.38       0.36    0.43   -1       0.5     -1         -1      -1    -1           -1
Kate         0.51     0.41    0.71      0.53     0.5   0.67      0.54   -1          0.57       0.42    0.62    0.33    0.48    -1         -1       0.8   0.44        -1
Sushant      0.55     0.42    0.67      0.52    -1     0.62      0.62    0.42      -1          0.35    0.57   -1       0.39     0.62       0.6    -1     0.17        -1
Abishek      0.64     0.52    0.64      0.64    -1     0.74      0.64    0.57       0.65      -1       0.71    0.67    0.56     0.6        0.6    -1     0.71         0.8
Ruhi         0.33     0.3    -1         0.38    -1     0.6       0.57    0.38       0.43       0.29   -1      -1       0.62     0.6       -1      -1    -1           -1
Kish        -1        0.4    -1        -1        0.4  -1        -1       0.67      -1          0.33   -1      -1      -1       -1         -1      -1    -1           -1
Alex         0.43     0.37    0.71      0.75    -1     0.75      0.5     0.52       0.61       0.44    0.38   -1      -1       -1         -1      -1    -1           -1
Jeron        0.6     -1      -1        -1       -1    -1        -1      -1          0.38       0.4     0.4    -1      -1       -1         -1      -1    -1           -1
Justin      -1        0.4    -1        -1       -1    -1        -1      -1          0.4        0.4    -1      -1      -1       -1         -1      -1    -1           -1
Jade        -1       -1      -1        -1       -1    -1        -1       0.2       -1         -1      -1      -1      -1       -1         -1      -1    -1           -1
Jay         -1        0.45   -1        -1       -1    -1        -1       0.56       0.83       0.29   -1      -1      -1       -1         -1      -1    -1           -1
Gathenji    -1       -1      -1        -1       -1    -1        -1      -1         -1          0.2    -1      -1      -1       -1         -1      -1    -1           -1

### <a id="mission2"></a>3+1 vs 2+2 strategy success rate (minimum 5 games, else -1)

Cheesy wins included:

Strategy       Win %    Sample Size
----------  --------  -------------
3+1         0.354839             31
2+2         0.385714             70

Cheesy wins excluded:

Strategy       Win %    Sample Size
----------  --------  -------------
3+1         0.310345             29
2+2         0.348485             66

### <a id="r1-fail"></a>Good win rate w.r.t. R1 fail (filtered for cases where bad guy on R1)

Cheesy wins included:

R1 Outcome       Win %    Sample Size
------------  --------  -------------
Fail          0.433333             30
Success       0.324074            108

Cheesy wins excluded:

R1 Outcome       Win %    Sample Size
------------  --------  -------------
Fail          0.433333             30
Success       0.311321            106

### <a id="flip-stats"></a>Flip statistics for different # bad guys and mission index


*Excludes Oberon in 10-person games.*

*Overall:*

  # Fails    Count         %    Good Win %
---------  -------  --------  ------------
        0       34  0.459459      0.352941
        1       29  0.391892      0.103448
        2       11  0.148649      0.363636

*2 bad guys on mission 1:*

  # Fails    Count         %    Good Win %
---------  -------  --------  ------------
        0       13  0.764706      0.153846
        1        4  0.235294      0

*2 bad guys on mission 2:*

  # Fails    Count         %    Good Win %
---------  -------  --------  ------------
        0       12  0.413793     0.5
        1       12  0.413793     0.0833333
        2        5  0.172414     0.2

*2 bad guys on mission 3:*

  # Fails    Count         %    Good Win %
---------  -------  --------  ------------
        0        8  0.333333      0.5
        1       11  0.458333      0.181818
        2        5  0.208333      0.4

*3 bad guys on mission 2:*

  # Fails    Count     %    Good Win %
---------  -------  ----  ------------
        0        1  0.25             0
        1        2  0.5              0
        2        1  0.25             1

### <a id="good-win-num-percival"></a>Good win % w.r.t. # Percival claims

Cheesy wins included:

  # Percival Claims    Sample Size    Good Win %
-------------------  -------------  ------------
                  0             85      0.517647
                  1            116      0.37069
                  2             16      0.5625
                  3              5      0.4

Cheesy wins excluded:

  # Percival Claims    Sample Size    Good Win %
-------------------  -------------  ------------
                  0             80      0.4875
                  1            110      0.336364
                  2             16      0.5625
                  3              5      0.4

### <a id="role-fake-percival"></a>Percentage of time each role fake claims Percival

Role             Fake Percival Claim %    Sample Size    # Fake Claims
-------------  -----------------------  -------------  ---------------
Merlin                         0.11261            222               25
Assassin                       0.03804            184                7
Morgana                        0.06019            216               13
Mordred                        0.00813            123                1
Loyal Servant                  0                  612                0
Oberon                         0.01493             67                1
Minion #1                      0.05714             35                2

### <a id="wrongly-assassinated"></a>% of time players are wrongly assassinated as non-Merlin good guy (minimum 5 games won as good guy)

*Excludes games where Merlin assassination is unknown.*

Player      Incorrect Assassination %    # Assassinations    Sample Size
--------  ---------------------------  ------------------  -------------
Jeron                        0.6                        3              5
Abishek                      0.457143                  16             35
Minh                         0.444444                   4              9
Alex                         0.363636                   8             22
Jai                          0.3125                     5             16
Kate                         0.288889                  13             45
Rachel                       0.269231                   7             26
Jackie                       0.257143                   9             35
Peter                        0.2                        7             35
Sushant                      0.2                        4             20
Ruhi                         0.2                        1              5
Tercel                       0.2                        1              5
Brian                        0.183673                   9             49

### <a id="correctly-assassinated"></a>% of time players are correctly assassinated as Merlin (minimum 3 games with 3 mission successes as Merlin)


*Competitive games only statistic.*

Player      Assassination %    # Assassinations    Sample Size
--------  -----------------  ------------------  -------------
Minh               0                          0              4
Brian              0.125                      1              8
Kate               0.3                        3             10
Sushant            0.333333                   3              9
Jeron              0.333333                   1              3
Abishek            0.444444                   4              9
Alex               0.5                        2              4
Peter              0.545455                   6             11
Jai                0.6                        3              5
Rachel             0.666667                   6              9
Jackie             0.75                       3              4

### <a id="assassination-game-size"></a>% of time Merlin is assassinated by game size

# Players      Assassination %    # Assassinations    Sample Size
-----------  -----------------  ------------------  -------------
10                    0.4                        8             20
5                     0.75                       6              8
5O                    0.333333                   3              9
5X                    0.5                        2              4
6                     0.285714                   6             21
6M                    0.363636                   4             11
6O                    0.25                       3             12
7                     0.580645                  18             31
7O                    0.6                        3              5
8                     0.470588                   8             17
8O                    0.666667                   2              3
9                     0.434783                  10             23
9L                    0.333333                   1              3
9O                    0                          0              1

### <a id="assassination-game-size-percival"></a>% of time Merlin is assassinated by game size and # Percival claims

# Players      # Percival Claims    Assassination %    # Assassinations    Sample Size
-----------  -------------------  -----------------  ------------------  -------------
10                             1           0.4375                     7             16
10                             2           0                          0              3
10                             3           1                          1              1
5                              0           0.5                        2              4
5                              1           1                          4              4
5O                             0           0.25                       2              8
5O                             1           1                          1              1
5X                             0           0.5                        2              4
6                              0           0.363636                   4             11
6                              1           0.222222                   2              9
6                              3           0                          0              1
6M                             0           0.444444                   4              9
6M                             1           0                          0              2
6O                             0           0.25                       3             12
7                              0           0.615385                   8             13
7                              1           0.642857                   9             14
7                              2           0.333333                   1              3
7                              3           0                          0              1
7O                             0           0.75                       3              4
7O                             2           0                          0              1
8                              0           0.4                        2              5
8                              1           0.5                        6             12
8O                             1           0.666667                   2              3
9                              0           0.5                        3              6
9                              1           0.4                        6             15
9                              2           0.5                        1              2
9L                             0           1                          1              1
9L                             1           0                          0              2
9O                             2           0                          0              1
