class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(start,stones):
            res = 0
            total = sum(piles[start:])
            for i in range(1, min(2 * stones + 1, len(piles) - start + 1)):
                optima = dfs(start + i, max(stones, i))
                res = max(res, total - optima)
            return res

        return dfs(0,1)