#!/usr/bin/env python3
from dotenv import load_dotenv, find_dotenv
import os

dotenv_name = '.app.env'
dotenv_path = dotenv_name if os.path.isfile(
    dotenv_name) else dotenv_name or find_dotenv(dotenv_name)
FOUND = load_dotenv(dotenv_path)
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
NO_KEY = os.getenv('NO_KEY')
