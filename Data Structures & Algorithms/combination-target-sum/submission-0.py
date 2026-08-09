class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if total == target:
                reuslt.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            curr.append([nums[i]])
            dfs(i, curr, total + nums[i])
            result.pop()
            dfs(i+1, curr, total)

        return dfs(0, [], 0)





        