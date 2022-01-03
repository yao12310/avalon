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
python -m avalon.main db_write --player_write {True/False, optional, default=True}
```

The script will prompt you to enter each column value for the data row one-by-one.

Updating README Stats:
```
python -m avalon.main update_stat
```
