class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        index = -1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[l] < nums[m] and target < nums[m] and target >= nums[l]:
                r = m-1
            else:
                l = m+1
        
        return index


        