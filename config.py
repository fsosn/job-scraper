import os
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv("FROM_EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")
