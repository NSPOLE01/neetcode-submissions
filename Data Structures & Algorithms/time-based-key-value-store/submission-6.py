class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value, timestamp])
            print(self.map)
        else:
            self.map[key] = [[value, timestamp]]
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            array = self.map[key]
        else:
            return ""

        for pair in reversed(array):
            if pair[1] <= timestamp:
                return pair[0]
                
        return ""


        
