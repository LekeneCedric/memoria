class Database:

    def __init__(self, init_data: dict):
        self.init_data = init_data

    def get(self, key: str):
        if key not in self.init_data:
            return None
        return self.init_data[key]

    def set(self, key: str, value: str):
        self.init_data[key] = value
