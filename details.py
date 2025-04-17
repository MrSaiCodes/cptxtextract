import os
from os import getenv


API_ID = int(getenv("API_ID", 23454876))
API_HASH = getenv("API_HASH", "b42626ee535fcaf915232af564a95bea")
BOT_TOKEN = getenv("BOT_TOKEN", "7705829246:AAGkrOC-1RiFyhqndeuva45RIbUGs54HfRI")
OWNER_ID = int(getenv("OWNER_ID", "662494886"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "662494886").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://saik:F@v@NHpt@7TFAb9@cluster0.brflswq.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002253133527"))
