class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a,b) for a, b in connections}
        neig = { city:[] for city in range(n) }
        visit = set()
        changes = 0
        
        for a,b in connections:
            neig[a].append(b)
            neig[b].append(a)
        
        def dfs(city):
            nonlocal edges, neig, visit, changes
            
            for n in neig[city]:
                if n in visit:
                    continue
                if (n, city) not in edges:
                    changes += 1
                visit.add(n)
                dfs(n)
        visit.add(0)
        dfs(0)
        return changes
        