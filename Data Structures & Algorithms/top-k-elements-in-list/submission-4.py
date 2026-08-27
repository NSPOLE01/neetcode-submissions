class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = Counter(nums)
        heap = []

        for key, value in counted_nums.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res


        