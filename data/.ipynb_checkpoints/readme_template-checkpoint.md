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
