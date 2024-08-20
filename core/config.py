import os
from pathlib import Path

from dotenv import  load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    MYSQL_USER: str = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST: str = os.getenv('MYSQL_HOST')
    MYSQL_DB: str = os.getenv('MYSQL_DB')
    MYSQL_PORT: int = os.getenv('MYSQL_PORT')
    DATABASE_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

settings = Settings()