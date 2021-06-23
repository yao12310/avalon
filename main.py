"""
Entry point script.
"""

import argparse

from .utils.constants import NON_COMPETITIVE
from .utils.constants import GAME_LOG_COLS
from .utils.constants import NA
from .utils.sheets import write_game_log
from .utils.read_update import write_stats

def main_db_write(args):
    if args.row is not None:
        data = [args.row.split('=')]
    else:
        data = []
        for col in GAME_LOG_COLS:
            data.append(input("{}: ".format(col)) or NA)
        
    non_competitive = data[GAME_LOG_COLS.index(NON_COMPETITIVE)]
    
    player_write = args.player_write and non_competitive != 'Yes'
    write_game_log([data], player_write)

def main_update_stat(args):
    write_stats()
    
def main():
    parser = argparse.ArgumentParser(
        prog="saas_avalon",
        description="database and analysis tools for SAAS avalon sessions.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    subparsers = parser.add_subparsers(title="modules", help="saas_avalon submodules, use -h/--help for help")
    sub_db_write = subparsers.add_parser("db_write", description="write to sheets db game log and (optionally) players")
    sub_update_stat = subparsers.add_parser("update_stat", description="update README.md with stats")
    sub_stats = subparsers.add_parser("stats", description="run statistical analyses (no update to README)")
    
    sub_db_write.add_argument('--row', '-r', action='store', type=str, required=False, default=None, help="row of game log data")
    sub_db_write.add_argument('--player_write', '-p', action='store', type=bool, required=False, default=True, help="update player data worksheets")
    sub_db_write.set_defaults(func=main_db_write)
    
    sub_update_stat.set_defaults(func=main_update_stat)
    
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
    
if __name__ == '__main__':
    main()
