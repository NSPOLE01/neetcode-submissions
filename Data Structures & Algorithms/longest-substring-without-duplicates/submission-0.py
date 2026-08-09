class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for index, character in enumerate(s):
            curLen = 1
            curString = character
            while index < len(s)-1 and s[index + 1] not in curString:
                curString = curString + s[index + 1]
                curLen +=1
                index+=1
            maxLen = max(maxLen, curLen)

        return maxLen


        