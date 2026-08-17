class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.map.get(key, [])
        values.append({timestamp, value})
        self.map[key] = values

        
    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        max_timestamp = None
        max_value = None
        
        for cur_timestamp, value in values:
            if cur_timestamp <= timestamp:
                if not max_timestamp:
                    max_timestamp = cur_timestamp
                    max_value = value
                else:
                    max_timestamp = max(max_timestamp, cur_timestamp)
                    max_value = max(max_value, value)
        if not max_value:
            return ""
        else:
            return max_value



        
