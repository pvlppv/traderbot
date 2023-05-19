import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN")
CURRENCY_API_TOKEN: str = os.getenv("CURRENCY_API_TOKEN")