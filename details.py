import os
from os import getenv


API_ID = int(getenv("API_ID", 23454876))
API_HASH = getenv("API_HASH", "b42626ee535fcaf915232af564a95bea")
BOT_TOKEN = getenv("BOT_TOKEN", "7198600769:8027492776:AAFfBBiQpzp-xLDHSRkLaz0HygBhQyyrgKE")
OWNER_ID = int(getenv("OWNER_ID", "8043047247"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8043047247").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002253133527"))
