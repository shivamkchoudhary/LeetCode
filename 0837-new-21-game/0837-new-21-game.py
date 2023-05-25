class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <= n:
            return 1.0
        
        winSum = 0
        for i in range(k, k + maxPts):
            winSum += 1 if i <= n else 0
            
        
        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = winSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)            
            winSum += dp[i] - remove
            
        return dp[0]
        
        