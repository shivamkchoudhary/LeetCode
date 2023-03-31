class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = (pizza[i][j] == 'A') + (dp[i+1][j] if i < m-1 else 0) + (dp[i][j+1] if j < n-1 else 0) - (dp[i+1][j+1] if i < m-1 and j < n-1 else 0)
        # print(dp)
        @lru_cache(None)
        def dfs(i, j, k):
            if dp[i][j] == 0:
                return 0
            if k == 1:
                return 1
            res = 0
            for x in range(i+1, m):
                if dp[x][j] < dp[i][j]:
                    res += dfs(x, j, k-1)
            for y in range(j+1, n):
                if dp[i][y] < dp[i][j]:
                    res += dfs(i, y, k-1)
            return res
        return dfs(0, 0, k) % (10**9 + 7)