class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            curWords = res.get(tuple(count), [])
            curWords.append(word)
            res[tuple(count)] = curWords
        return list(res.values())
