class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listCharOne = sorted(s)
        listCharTwo = sorted(t)
        if listCharOne == listCharTwo:
            return True
        return False
        