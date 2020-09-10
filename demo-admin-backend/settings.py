# settings.py
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os

def getenv(key, default):
    value = os.getenv(key)
    if len(value) is 0:
        return default
    return value


# Demo Admin App API Server Settings
API_SERVER_HOST=getenv("API_SERVER_HOST", default="0.0.0.0")
API_SERVER_PORT=getenv("API_SERVER_PORT", default=5000)
API_SERVER_DEBUG=getenv("API_SERVER_DEBUG", default="False")

# MongoDB connection settings
DB_NAME=getenv("DB_NAME", default="demo-admin-app")
DB_HOST=getenv("DB_HOST", default="demo-admin-app-db")
DB_PORT=getenv("DB_PORT", default=27017)