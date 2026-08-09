class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = [value, timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        return self.map[key][0]
        
