class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)-1


        while t <= b:
            m = (t +  b) //2
            if target > matrix[m][-1]:
                t = m+1   
            elif target < matrix[m][0]:
                b = m-1
            else:
                break

        if not (t<=b):
            return False

        l = 0
        r = len(matrix[m])-1

        while l<=r:
            mid = (l+r) //2 
            if target < matrix[m][mid]:
                r = mid -1
            elif target > matrix[m][mid]:
                l = mid + 1
            else:
                return True

        return False


        