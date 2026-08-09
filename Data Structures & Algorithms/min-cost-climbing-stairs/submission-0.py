class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        stairs = [0] * (n+1)

        for i in range(2, n+1):
            stairs[i] = min(stairs[i-1] + cost[i-1], stairs[i-2] + cost[i-2])
        
        return stairs[n]