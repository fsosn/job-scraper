import os
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv("APP_EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("MY_EMAIL")
