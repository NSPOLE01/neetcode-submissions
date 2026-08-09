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
        array = self.map[key]
        if array:
            for pair in reversed(array):
                if pair[1] <= timestamp:
                    return pair[0]
            return ""
        else:
            return ""

        
