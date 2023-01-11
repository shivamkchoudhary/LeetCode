class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        negb = { i:[] for i in range(n)}
        
        for par,child in edges:
            negb[par].append(child)
            negb[child].append(par)
            
        def dfs(cur, par):
            time = 0
            for child in negb[cur]:
                if child == par:
                    continue
                cTime = dfs(child, cur)
                if cTime or hasApple[child]:
                    time += 2 + cTime
            return time
        return dfs(0,-1)
        