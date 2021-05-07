from pathlib import Path
from datetime import datetime
from plugins.yaml import YAMLPlugin

import toml
import click

from utils import handle_new_til, read_until_interrupt

USER_HOME = Path.home()
TIL_CONFIG_NAME = ".til.toml"
DEFAULT_CONFIG_NAME = ".til.toml.default"
TIL_CONFIG_PATH = USER_HOME / TIL_CONFIG_NAME
CURRENT_DIR = Path(__file__).parent
DEFAULT_CONFIG_FILE = CURRENT_DIR / DEFAULT_CONFIG_NAME

class TILConfig:

    def __init__(self):
        # Read Default config
        til_config = toml.load(DEFAULT_CONFIG_FILE)
        try:
            # Try reading the user config
            til_config = toml.load(TIL_CONFIG_PATH)
        except FileNotFoundError:
            # If user config does not exist, pass
            pass

        self.data = til_config


pass_config = click.make_pass_decorator(TILConfig, ensure=True)

@click.group()
def til():
    pass

@til.command()
@click.argument('title', type=str, required=True)
@click.option('-d', '--date', type=click.DateTime(formats=["%Y/%m/%d"]), help="I learnt it on YYYY/mm/dd?")
@pass_config
def new(config, title, date=None):
    if not date:
        date = datetime.utcnow()
    print("Content:\n")
    content = read_until_interrupt()
    handle_new_til(title, date, content, config.data["plugins"])
