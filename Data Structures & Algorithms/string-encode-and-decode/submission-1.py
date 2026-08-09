class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s + "/"
        return result
    
    def decode(self, s: str) -> List[str]:
        substring = ""
        result = []
        for c in s:
            if c == "/":
                result.append(substring)
                substring = ""
            else:
                substring = substring + c

        return result

