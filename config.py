import os
from dotenv import load_dotenv

load_dotenv()

APP_EMAIL = os.getenv("APP_EMAIL")
PASSWORD = os.getenv("PASSWORD")
MY_EMAIL = os.getenv("MY_EMAIL")
