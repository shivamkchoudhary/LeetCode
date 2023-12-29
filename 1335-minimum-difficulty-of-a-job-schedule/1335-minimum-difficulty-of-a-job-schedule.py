class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n= len(jobDifficulty)
        @lru_cache(None)
        def dfs(idx,k,m):
            if idx == n :
                if k == 0:
                    return 0
                return math.inf
            if k <= 0:
                return math.inf
            
            ans  = dfs(idx+1,k,max(m,jobDifficulty[idx]))
            ans = min(ans,max(m,jobDifficulty[idx]) +dfs(idx+1,k-1,0))
            return ans
        
        a = dfs(0,d,0)
        if a == math.inf:
            return -1
        return a