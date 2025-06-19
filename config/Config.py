import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()  # โหลดตัวแปรจาก .env
        # Threat Intelligence Provider Keys
        self.VIRUSTOTAL_KEY = os.getenv('VIRUSTOTAL_API_KEY')
        self.IPINFO_API_KEY = os.getenv('IPINFO_API_KEY')

        # Google API Key for LLM (Google Generative AI)
        self.GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

        # LLM Configuration
        self.LLM_MODEL = os.getenv('LLM_MODEL', 'gemini-2.0-flash-lite')
        self.LLM_TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', 0.05))
        self._validate_config()
        #print(self.LLM_MODEL)

    def _validate_config(self):
        errors = []

        if not self.VIRUSTOTAL_KEY:
            errors.append("VirusTotal API key is missing")

        if not self.IPINFO_API_KEY:
            errors.append("IPInfo API key is missing")

        if not self.GOOGLE_API_KEY:
            errors.append("Google API key is missing")

        if errors:
            raise ValueError("\n".join(errors))

    def get_provider_settings(self):
        return {
            'virustotal': {
                'api_key': self.VIRUSTOTAL_KEY
            },
            'ipinfo': {
                'api_key': self.IPINFO_API_KEY
            }
        }