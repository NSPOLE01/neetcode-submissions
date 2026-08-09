class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        iter = len(nums)-k
        i = 0
        while i < iter:
            heapq.heappop(nums)
            i +=1
        return heapq.heappop(nums)


        