"""This module provides the RP To-Do config functionality."""
# rptodo/config.py

import configparser
from pathlib import Path

import typer

from rptodo import (
    DB_WRITE_ERROR,
    DIR_ERROR,
    FILE_ERROR,
    SUCCESS,
    __app_name__,
)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__)) # hold path to the app's directory. can call the get_app_dir() function from the typer module to get the path to the app's directory.
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini" # hold path to the app's configuration file.


def init_app(db_path: str) -> int:
    """Initialize the application configuration."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code
    return SUCCESS

def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(parents=True, exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS

def _create_database(db_path: str) -> int:
    config_parser = configparser.ConfigParser()
    config_parser["General"]  = {"database": db_path}
    try:
        with open(CONFIG_FILE_PATH, "w") as config_file:
            config_parser.write(config_file)
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS