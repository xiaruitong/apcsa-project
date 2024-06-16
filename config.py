import json

class Config:
    def __init__(self):
        self.configs = None
        with open("config.json", "r") as f:
            self.configs = json.load(f)

    def get_token(self) -> str:
        return self.configs["discord"]["token"]

    def get_proxy(self):
        return self.configs["proxy"]
