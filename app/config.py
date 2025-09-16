import os

from dotenv import load_dotenv

load_dotenv(override=True)

token = os.getenv("TOKEN")
admin_list = os.getenv("ADMIN_LIST")
db_url = os.getenv("DB_URL")