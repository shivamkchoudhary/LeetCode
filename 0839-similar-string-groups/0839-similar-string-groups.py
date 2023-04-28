class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        def calculateDelta(x, y):
            d = 0
            for a, b in zip(x, y):
                if a != b:
                    d += 1
            return d

        adj_list = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if calculateDelta(strs[i], strs[j]) <= 2:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = [False] * n
        count = 0

        def visit(x):
            for v in adj_list[x]:
                if not visited[v]:
                    visited[v] = True
                    visit(v)

        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                visit(i)
        
        return count