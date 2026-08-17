class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.map.get(key, [])
        values.append([timestamp, value])
        self.map[key] = values
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        res = ""
        l = 0
        r = len(values) - 1

        while l <= r:
            m = (l+r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m+1
            else:
                r = m-1
        return res



        
