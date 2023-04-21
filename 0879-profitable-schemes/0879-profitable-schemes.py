class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        
        dp = defaultdict(int) 
        
        for m in range(n + 1):
            dp[(len(group), m, minProfit)] = 1
            
        for i in range(len(group) - 1, -1, -1):
            for m in range(n + 1):
                for p in range(minProfit + 1):
                    dp[(i, m, p)] = dp[(i + 1, m, p)]
                    if m + group[i] <= n:
                        dp[(i, m, p)] += \
                            dp[(i + 1, m + group[i], min(minProfit, p + profit[i]))] % mod
        return dp[(0, 0, 0)] % mod
        