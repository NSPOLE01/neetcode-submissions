class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        resultSet = set()
        for num in nums:
            if num in resultSet:
                return True
            else:
                resultSet.add(num)
        return False
        