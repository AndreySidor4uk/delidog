from pathlib import Path

from envparse import env

env.read_envfile()

BASE_DIR = Path(__file__).resolve().parent

DATABASE_URL = env('DATABASE_URL', default="sqlite:///db.sqlite3")

BOT_TOKEN = env('BOT_TOKEN', default='')
