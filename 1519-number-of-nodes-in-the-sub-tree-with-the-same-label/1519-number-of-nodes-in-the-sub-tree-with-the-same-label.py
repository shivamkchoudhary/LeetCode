class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = collections.defaultdict(list)
        
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        c = [0]*n
        
        def dfs(index,parent):
            count = collections.Counter()
            
            for edge in g[index]:
                if edge != parent:
                    count += dfs(edge,index)
            count[labels[index]] += 1
            c[index] = count[labels[index]]
            return count
        dfs(0,-1)
        return c
            