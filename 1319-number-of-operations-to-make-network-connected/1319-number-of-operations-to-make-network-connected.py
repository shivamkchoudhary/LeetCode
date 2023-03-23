class Solution:
    def makeConnected(self, N: int, connections: List[List[int]]) -> int:
        E = len(connections)
        if E < N - 1:
            return -1
        
        adj_list = collections.defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * N

        def bfs(start):
            q = collections.deque()
            q.append(start)

            while len(q) > 0:
                current = q.popleft()
                
                for v in adj_list[current]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

        count = 0
        for i in range(N):
            if not visited[i]:
                count += 1
                bfs(i)
        return count - 1