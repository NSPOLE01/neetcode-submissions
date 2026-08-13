class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in current:
                current.remove(s[l])
                l += 1
            current.add(s[r])
            res = max(res, r-l+1)
        return res



        