class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        rate = 1

        while rate < piles[-1]:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            if hours <= h:
                return rate
            else:
                rate +=1

        return rate

        
                
        