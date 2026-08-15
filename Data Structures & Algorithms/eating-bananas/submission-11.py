class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total = total + math.ceil(pile / mid)
            if total <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res







        
                
        