import os
from dotenv import load_dotenv
from typing import Final

load_dotenv("environments.env", override=True)

class ConfigReader:

    USERNAME:Final[str] = os.getenv("USERNAME")
    PASSWORD:Final[str] = os.getenv("PASSWORD")
    BASE_URL:str = os.getenv("BASE_URL")