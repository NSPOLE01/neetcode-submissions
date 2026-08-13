class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = 0
        maxRight = 0
        value = 0

        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if maxLeft < maxRight:
                value = value + (maxLeft - height[l])
                l += 1
            else:
                value = value + (maxRight - height[r])
                r -= 1

        return value

        