class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if not len(trust) and n < 2:
            return 1

        count = [0] * (n + 1)
        for i, j in trust:
            count[i] = count[i] - 1
            count[j] = count[j] +  1
        m = max(count)
        
        return (count.index(m) if m == n - 1 else -1)
        