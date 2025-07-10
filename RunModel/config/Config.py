# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.NAT_SERVER_URL = os.getenv("NAT_SERVER_URL")
        self.AUTO_OPEN_CONNECTION = os.getenv("AUTO_OPEN_CONNECTION", "false").lower() == "true"
        self.STREAM_NAME = os.getenv("STREAM_NAME", "model_server")
        self.STREAM_PREFIX = os.getenv("STREAM_PREFIX", "agent-type")
        self.DURABLE_NAME = os.getenv("DURABLE_NAME", "model_server_durable")
        self.INPUT_SUBJECT = self.STREAM_PREFIX + os.getenv("INPUT_SUBJECT_SUFFIX", ".Input")
        self.OUTPUT_SUBJECT = self.STREAM_PREFIX + os.getenv("OUTPUT_SUBJECT_SUFFIX", ".Output")
        
cfg = Config()