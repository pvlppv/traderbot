import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
FinnHub_ApiKey = str(os.getenv("FinnHub_ApiKey"))

admins = [384993580]
