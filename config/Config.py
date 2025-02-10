import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()

        # Threat Intelligence Provider Keys
        self.VIRUSTOTAL_KEY = os.getenv('VIRUSTOTAL_API_KEY')
        self.IPINFO_API_KEY = os.getenv('IPINFO_API_KEY')

        # LLM Configuration
        self.LLM_MODEL = os.getenv('LLM_MODEL', 'gemini-1.5-pro-latest')
        self.LLM_TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', 0.05))

        # Validation
        self._validate_config()

    def _validate_config(self):
        """Validate critical configuration parameters"""
        errors = []

        if not self.VIRUSTOTAL_KEY:
            errors.append("VirusTotal API key is missing")

        if not self.IPINFO_API_KEY:
            errors.append("IPInfo API key is missing")

        if errors:
            raise ValueError("\n".join(errors))

    def get_provider_settings(self):
        """Return provider-specific settings"""
        return {
            'virustotal': {
                'api_key': self.VIRUSTOTAL_KEY
            },
            'ipinfo': {
                'api_key': self.IPINFO_API_KEY
            }
        }