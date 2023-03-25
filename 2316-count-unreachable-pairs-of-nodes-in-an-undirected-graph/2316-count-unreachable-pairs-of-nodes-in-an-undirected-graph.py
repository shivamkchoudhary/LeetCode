class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range (n)]
        
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]
        
        def uunion(a, b):
            ua = ufind(b)
            ub = ufind(a)
            
            parents[ua] = ub
        
        for u, v in edges:
            uunion(u, v)
        
        counts = collections.Counter()
        for i in range(n):
            counts[ufind(i)] += 1
            
        total = 0
        for k in counts.keys():
            total += counts[k] * (n - (counts[k]))
        return total // 2
        
        
        