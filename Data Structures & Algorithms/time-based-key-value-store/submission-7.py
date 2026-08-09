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

        l = 0
        r = len(array) - 1
        res = ""

        while(l <= r):
            m = (l+r) // 2
            if array[m][1] <= timestamp:
                res = array[m][0]
                l = m+1
            else:
                r= m-1

        return res



        
