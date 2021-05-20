# FILE PATHS

ROOT = "/Users/brianyao/Code/projects/avalon/"

# data

DATA_ROOT = ROOT + "data/"
GAME_LOG_TSV = DATA_ROOT + "game_{}.tsv" # YYYYMMDD format

# keys

KEYS_ROOT = ROOT + "keys/"
CLIENT_SECRET_KEY = KEYS_ROOT + "client.json" # must get from google

# FUNCTIONAL

# meta

SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
SHEET_NAME = "Avalon Stats"
GAME_LOG = "Game Log"
TEMPLATE = "Template"

# game metadata

MAX_LOYAL = 4
MAX_ROUNDS = 5

# data

# game data
DATE = "Date"
GAME_INDEX = "Game Index"
NUM_PLAYERS = "# Players"

MERLIN = "Merlin"
PERCIVAL = "Percival"
ASSASSIN = "Assassin"
MORGANA = "Morgana"
MORDRED = "Mordred"
OBERON = "Oberon"
MINION = "Minion #1"
LOYAL = "Loyal #{}" # idx

BADS = [ASSASSIN, MORGANA, MORDRED, OBERON, MINION]
LOYALS = [LOYAL.format(idx) for idx in range(1, MAX_LOYAL + 1)]
ROLES = [MERLIN, PERCIVAL] + BADS + LOYALS

TEAM_ROUND = "Round {} Team" # round idx
FAILS_ROUND = "Round {} Fails" # round idx

SUCCESSES = "Successes"
FAILS = "Fails"
ASSASSINATION = "Assassination"
WINNER = "Winner"
GOOD_WIN = "Good Win"
CHEESY_WIN = "Cheesy Win"

NUM_PERCIVAL = "# Percival Claims"
FAKE_PERCIVAL = "Fake Percival Claims"

WEAK_KGT_APPLY = "Weak KGT Applied"
WEAK_KGT_SUCCESS = "Weak KGT Success"
STRONG_KGT_APPLY = "Strong KGT Applied"
STRONG_KGT_SUCCESS = "Strong KGT Success"

LENGTH = "Length (minutes)"

GAME_LOG_COLS = (
    [DATE, GAME_INDEX, NUM_PLAYERS] + # identifiers
    ROLES + # role info
    [name.format(round_idx) for round_idx in range(1, MAX_ROUNDS + 1) for name in [TEAM_ROUND, FAILS_ROUND]] +
    [SUCCESSES, FAILS, ASSASSINATION, WINNER, GOOD_WIN, CHEESY_WIN] + # outcomes
    [NUM_PERCIVAL, FAKE_PERCIVAL] + # percival data
    [WEAK_KGT_APPLY, WEAK_KGT_SUCCESS, STRONG_KGT_APPLY, STRONG_KGT_SUCCESS] + # kgt info
    [LENGTH] # misc
)

# player data
# some inconsistencies in col naming due to legacy reasons
TEAM = "Team"
ROLE = "Role"
SUCCEEDED_MISSIONS = "Succeeded Missions"
FAILED_MISSIONS = "Failed Missions"
MERLIN_ASSASSINATION = "Merlin Assassination"
WIN = "Win?"
NOTES = "Notes"

PLAYER_LOG_COLS = [
    DATE, GAME_INDEX, TEAM, ROLE, SUCCEEDED_MISSIONS, FAILED_MISSIONS,
    MERLIN_ASSASSINATION, WIN, NUM_PLAYERS, NOTES
]

# special entries
GOOD = "Good"
BAD = "Bad"
SAFE = "Safe"
ASSASSINATED = "Assassinated"
NA = "N/A"
UNK = "UNK"
UTD = "UTD"
LOYAL_SERVANT = "Loyal Servant"