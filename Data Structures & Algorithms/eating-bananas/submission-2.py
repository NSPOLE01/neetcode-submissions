class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        rate = piles[-1]
        result = math.inf

        while rate > 0:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            if hours <= h:
                result = min(result, rate)
                rate -= 1
            else:
                break

        return result

        
                
        