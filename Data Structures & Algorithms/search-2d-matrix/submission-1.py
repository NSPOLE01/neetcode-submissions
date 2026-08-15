class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        # l will be row to check
        while l < r:
            mid = l + ((r-l) // 2)
            print(matrix[mid][0])
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid-1

        left = 0
        right = len(matrix[0])- 1
        while left <= right:
            middle = left + ((right-left) // 2)
            if matrix[l][middle] == target:
                return True
            elif matrix[l][middle] < target:
                left = middle + 1
            else:
                right = middle-1
        
        return False
