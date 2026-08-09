class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = []
        for stone in stones:
            result.append(stone * -1)
        heapq.heapify(result)

        while len(result) > 1:
            stoneOne = heapq.heappop(result) * -1
            stoneTwo = heapq.heappop(result) * -1
            if stoneOne > stoneTwo:
                heapq.heappush(result, stoneOne - stoneTwo)
        
        if len(result) == 1:
            return heapq.heappop(result) * -1
        
        return 0

        