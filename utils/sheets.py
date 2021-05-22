"""
Utilities for interaction with sheet data from Google Sheets API.
"""

import sys

from collections import defaultdict
from datetime import date

import gspread
import pandas as pd

from oauth2client.service_account import ServiceAccountCredentials

# hack, but needed for testing in jupyter
if __name__ == 'avalon.utils.sheets':
    from .constants import *
else:
    sys.path.append('..')
    from utils.constants import *

def init_client():
    """
    Initialize a service account client.
    return : gspread.client.Client
    """
    creds = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRET_KEY, SCOPE)
    return gspread.authorize(creds)

def fetch_game_log(parse_cols=False, save=False):
    """
    Fetch current version of master game data.
    parse_cols : bool
        parse non-string columns as specific dtypes
    save : bool
        save game log into local directory
    return : pd.DataFrame
    """
    client = init_client()
    worksheet = client.open(SHEET_NAME).worksheet(GAME_LOG)
    df = pd.DataFrame(worksheet.get_all_values()[1:], columns=GAME_LOG_COLS)
    if parse_cols:
        df[GAME_LOG_NUM_COLS] = df[GAME_LOG_NUM_COLS].apply(pd.to_numeric)
        df[DATE] = pd.to_datetime(df[DATE])
    if save:
        df.to_csv(
            GAME_LOG_TSV.format(date.today().strftime("%Y%m%d")),
            sep='\t',
            index=False
        )
    return df

def fetch_player_data(player):
    """
    Fetch current data for specific player.
    player : str
        player name
    return : pd.DataFrame
    """
    client = init_client()
    worksheet = client.open(SHEET_NAME).worksheet(player)
    values = worksheet.get_all_values()[1:]
    values = list(filter(lambda row: any(row), [row[:len(PLAYER_LOG_COLS)] for row in values]))
    return pd.DataFrame(values, columns=PLAYER_LOG_COLS)

def write_game_log(data, write_ind=True):
    """
    Update game log.
    data : []list
        list of game data rows
    write_ind : bool
        update individual player worksheets
    return : None
    """
    assert(all([len(row) == len(GAME_LOG_COLS) for row in data]))
    client = init_client()
    sheet = client.open(SHEET_NAME)
    row_idx = fetch_game_log().shape[0] + 2
    sheet.values_update(
        "{}!A{}".format(GAME_LOG, row_idx),
        params={
            'valueInputOption': 'USER_ENTERED'
        },
        body={
            'values': data
        }
    )
    
    if write_ind:
        player_data = defaultdict(list)
        for row in data:
            row_dict = dict(zip(GAME_LOG_COLS, row))
            if row_dict[ASSASSINATION] == NA:
                merlin_status = NA
            elif row_dict[ASSASSINATION] == UNK:
                merlin_status = SAFE # probably safe to assume
            elif row_dict[MERLIN] == row_dict[ASSASSINATION]:
                merlin_status = ASSASSINATED
            else:
                merlin_status = SAFE
            for role in ROLES:
                player = row_dict[role]
                if player == NA or player == UNK:
                    continue
                    
                if role in LOYALS:
                    role = LOYAL_SERVANT
                
                if role in BADS:
                    team = BAD
                else:
                    team = GOOD
                    
                win = int(team == row_dict[WINNER])
                
                player_data[player].append(
                    [
                        row_dict[DATE], row_dict[GAME_INDEX], team, role,
                        row_dict[SUCCESSES], row_dict[FAILS], merlin_status, win, row_dict[NUM_PLAYERS]
                    ]
                )
                
        for player in player_data:
            write_player_data(player, player_data[player])
                
def write_player_data(player, data):
    """
    Update player data.
    player : str
        player name
    data : []list
        list of player data rows
    return : None
    """
    client = init_client()
    sheet = client.open(SHEET_NAME)
    
    if all([player != worksheet.title for worksheet in sheet.worksheets()]):
        template_id = sheet.worksheet(TEMPLATE).id
        sheet.duplicate_sheet(template_id, new_sheet_name=player)
    
    row_idx = fetch_player_data(player).shape[0] + 2
    sheet.values_update(
        "{}!A{}".format(player, row_idx),
        params={
            'valueInputOption': 'USER_ENTERED'
        },
        body={
            'values': data
        }
    )
    