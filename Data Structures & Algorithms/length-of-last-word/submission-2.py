class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed = " ".join(s.split()[::-1])
        len = 0
        while reversed and reversed[0] != " ":
            len += 1
            reversed = reversed[1:]
        return len