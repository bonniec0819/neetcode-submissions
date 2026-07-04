class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        c = {}
        left = 0
        maxLen = 0
        for i in range(len(s)):
            if s[i] in c:
                left = max(left, c[s[i]]+1)
            c[s[i]] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen
