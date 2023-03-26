class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        visited = [False] * n
        best = -1

        def visit(x):
            t = 0
            when = {}

            while not visited[x]:
                visited[x] = True
                when[x] = t
                t += 1
                if edges[x] != -1:
                    x = edges[x]
                    if x in when:
                        nonlocal best
                        best = max(best, t - when[x])
                        return

        for i in range(n):
            if not visited[i] and edges[i] != -1:
                visit(i)
        return best