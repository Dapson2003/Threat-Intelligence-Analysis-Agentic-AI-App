import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()  # โหลดตัวแปรจาก .env
        # LLM Configuration
        self.LLM_MODEL = os.getenv('LLM_MODEL')
        self.LLM_TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', 0.05))
        self.LOCAL_LLM_URL = os.getenv('LOCAL_LLM_URL')
        
        #LangSmith
        os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
        os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
        os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGSMITH_API_KEY')
        os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
        

cfg = Config()