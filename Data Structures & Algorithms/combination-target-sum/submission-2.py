class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(currentSum, subset, i):
            if currentSum == target:
                result.append(subset.copy())
                return
            if i >= len(nums) or currentSum > target:
                return
            subset.append(nums[i])
            dfs(currentSum + nums[i], subset, i)
            subset.pop()
            dfs(currentSum, subset, i+1)

        dfs(0, [], 0)
        return result
            







        