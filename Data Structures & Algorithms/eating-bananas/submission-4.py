class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        rate = piles[-1]
        result = math.inf

        while rate > 0:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
                if hours > h:
                    return rate+1
            result = min(result, rate)
            rate -= 1

        return result

        
                
        