class Solution:
    def isValid(self, s: str) -> bool:
        idk = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        while s:
            if s[0] in idk:
                stack.append(s[0])
            else:
                if stack and idk.get(stack[-1]) == s[0]:
                    stack.pop()
                else:
                    return False
            s = s[1:]
        if stack:
            return False
        return True