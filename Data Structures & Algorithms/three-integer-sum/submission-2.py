class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = 0 - a
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left > 0 and nums[left] == nums[left-1]:
                        left+=1

        return result

        