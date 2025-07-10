# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.NAT_SERVER_URL = os.getenv("NAT_SERVER_URL")
cfg = Config()