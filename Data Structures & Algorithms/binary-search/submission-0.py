class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searching(0, len(nums)-1, nums, target)
       
    def searching(self, l, r, nums, target) -> int:
        while(l <= r):
            m = l + ((r-l) // 2)
            if target < nums[m]:
                return self.searching(l, m - 1, nums, target)
            elif target > nums[m]:
                return self.searching(m+1, r, nums, target)
            else:
                return m
        return -1
        
