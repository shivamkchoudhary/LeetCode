class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        l1, l2, curr = 1, 1, 0
        for i in range(1, len(s)):
            if '1' <= s[i] <= '9':
                curr = l1
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += l2
            l1, l2, curr = curr, l1, 0
        return l1
        