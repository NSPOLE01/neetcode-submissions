class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                popped = stack.pop()
                if char == "]" and popped != "[":
                    return False
                elif char == "}" and popped != "{":
                    return False
                elif char == ")" and popped != "(":
                    return False

        return len(stack) == 0



        