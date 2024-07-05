import os
from typing import Dict
import uuid

class Session:
    def __init__(self):
        self.session_id = str(uuid.uuid4())

    def set_api_keys(self, api_keys: Dict[str, str]):
        for provider, key in api_keys.items():
            os.environ[f"{self.session_id}_{provider.upper()}_API_KEY"] = key

    def get_api_key(self, provider: str) -> str:
        return os.environ.get(f"{self.session_id}_{provider.upper()}_API_KEY")

    def clear_api_keys(self):
        for key in list(os.environ.keys()):
            if key.startswith(self.session_id):
                del os.environ[key]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear_api_keys()