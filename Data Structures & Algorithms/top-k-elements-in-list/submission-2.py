class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)

        heap = []
        for num in num_map.keys():
            heapq.heappush(heap, (num_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        