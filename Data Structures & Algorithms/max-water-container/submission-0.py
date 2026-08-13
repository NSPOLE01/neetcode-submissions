class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = (j - i)
                height = min(heights[i], heights[j])
                max_area = max(max_area, width * height)
        
        return max_area

        