class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for k in range(i, len(s)):
                if self.isPalindrome(s, i, k):
                    part.append(s[i:k+1])
                    dfs(k+1)
                    part.pop()
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
            
                