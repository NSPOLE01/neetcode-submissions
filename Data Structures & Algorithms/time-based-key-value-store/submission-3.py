class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = [value, timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            if  self.map[key][1] <= timestamp:
                return self.map[key][0]
            else:
                return ""
        else:
            return ""
        
