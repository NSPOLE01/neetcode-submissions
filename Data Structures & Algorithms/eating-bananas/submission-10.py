class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        go = True
        minimum = 1

        while go:
            current = 0
            for pile in piles:
                current = current + math.ceil(pile / minimum)
            if current <= h:
                return minimum
            else:
                minimum += 1





        
                
        