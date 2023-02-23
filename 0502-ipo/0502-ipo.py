class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCaptial = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCaptial)
        
        for i in range(k):
            while minCaptial and minCaptial[0][0] <= w:
                c, p = heapq.heappop(minCaptial)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)
        return w