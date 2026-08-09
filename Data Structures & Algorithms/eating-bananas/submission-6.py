class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = 1

        while rate < math.inf:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            if hours <= h:
                return rate
            else:
                rate +=1

        return rate

        
                
        