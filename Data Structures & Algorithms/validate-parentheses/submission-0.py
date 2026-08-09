class Solution:
    def isValid(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l <= r:
            if s[l] == "[":
                if s[r] != "]":
                    return False
            elif s[l] == "{":
                if s[r] != "}":
                    return False
            elif s[l] == "(":
                if s[r] != ")":
                    return False
            else:
                return False
            l +=1
            r -=1

        return True


        