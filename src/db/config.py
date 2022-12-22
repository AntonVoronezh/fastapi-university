import os
import pathlib
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
# db_url = os.environ["DATABASE_URL"]

class Settings(BaseSettings):
    database_url: PostgresDsn
    # database_url = db_url

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings

