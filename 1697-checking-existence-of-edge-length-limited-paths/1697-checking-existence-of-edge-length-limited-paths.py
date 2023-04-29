class Solution:
    def distanceLimitedPathsExist(self, N: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        Q = len(queries)
        # DSU, Union-Find, Minimum Spanning Tree, Spanning Tree

        parents = [x for x in range(N)]

        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            parents[ua] = ub

        edges = collections.defaultdict(list)
        for u, v, d in edgeList:
            edges[d].append((u, v))

        qs = collections.defaultdict(list)
        for index, (p, q, l) in enumerate(queries):
            qs[l].append((p, q, index))

        ans = [None] * Q
        for x in sorted(set(list(qs.keys()) + list(edges.keys()))):
            if len(qs[x]) > 0:
                for p, q, index in qs[x]:
                    ans[index] = (ufind(p) == ufind(q))

            if len(edges[x]) > 0:
                for u, v in edges[x]:
                    uunion(u, v)

        return ans
    
# Revise this again