import os

# FILE PATHS

ROOT = '/'.join(os.path.realpath(__file__).split('/')[:-2]) +'/' # not super elegant, but works
README = ROOT + "README.md"

# data

DATA_ROOT = ROOT + "data/"
GAME_LOG_TSV = DATA_ROOT + "game_{}.tsv" # YYYYMMDD format
README_DEFAULT = DATA_ROOT + "readme_template.md"

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

SIZES = ['5', '5O', '5P', '5X', '6', '6O', '6M', '7', '7O', '8', '8O', '9', '9O', '9L', '10']
MAX_LOYAL = 4
MAX_ROUNDS = 5
SAMPLE_THRESH = 5
GOOD_WIN_RATES_BALANCE = {
    '5': .4,
    '5O': .4,
    '5P': .4,
    '5X': .4,
    '6': 1 / 3,
    '6O': 1 / 3,
    '6M': 1 / 3,
    '7': 3 / 7,
    '7O': 3 / 7,
    '8': .375,
    '8O': .375,
    '9': 1 / 3,
    '9O': 1 / 3,
    '9L': 1 / 3,
    '10': .4
}
NUM_PLAYERS_MAP = {
    '5': (5, 3),
    '5O': (5, 3),
    '5P': (5, 3),
    '5X': (5, 3),
    '6': (6, 4),
    '6O': (6, 4),
    '6M': (6, 4),
    '7': (7, 4),
    '7O': (7, 4),
    '8': (8, 5),
    '8O': (8, 5),
    '9': (9, 6),
    '9O': (9, 6),
    '9L': (9, 6),
    '10': (10, 6)
}
R4_DOUBLE_FAIL_REQ = {
    '5': False,
    '5O': False,
    '5P': False,
    '5X': False,
    '6': False,
    '6O': False,
    '6M': False,
    '7': True,
    '7O': True,
    '8': True,
    '8O': True,
    '9': True,
    '9O': True,
    '9L': True,
    '10': True
}

# data

# game data
DATE = "Date"
GAME_INDEX = "Game Index"
NUM_PLAYERS = "# Players"
NON_COMPETITIVE = "Non-Competitive"

SUCCESS = "Success"
FAIL = "Fail"

MERLIN = "Merlin"
PERCIVAL = "Percival"
ASSASSIN = "Assassin"
MORGANA = "Morgana"
MORDRED = "Mordred"
OBERON = "Oberon"
MINION = "Minion #1"
LOYAL = "Loyal #{}" # idx
LOYAL_SERVANT = "Loyal Servant"

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

LENGTH = "Length (minutes)"

NOTES = "Notes"

GAME_LOG_COLS = (
    [DATE, GAME_INDEX, NUM_PLAYERS, NON_COMPETITIVE] + # identifiers
    ROLES + # role info
    [name.format(round_idx) for round_idx in range(1, MAX_ROUNDS + 1) for name in [TEAM_ROUND, FAILS_ROUND]] +
    [SUCCESSES, FAILS, ASSASSINATION, WINNER, GOOD_WIN, CHEESY_WIN] + # outcomes
    [NUM_PERCIVAL, FAKE_PERCIVAL] + # percival data
    [LENGTH] + # misc
    [NOTES]
)

GAME_LOG_NUM_COLS = [GAME_INDEX, SUCCESSES, FAILS, GOOD_WIN, NUM_PERCIVAL, LENGTH]

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
NONE = "None"
LOYAL_SERVANT = "Loyal Servant"
