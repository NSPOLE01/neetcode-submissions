class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        maxLength = 0
        l, r = 0,1
        while r < len(s):
            current.add(s[l])
            if s[r] in current:
                maxLength = max(maxLength, r-l)
                l=r
            else:
                current.add(s[r])
            r += 1
        return maxLength



        