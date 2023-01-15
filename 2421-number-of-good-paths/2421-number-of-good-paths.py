class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        l = len(vals)
        parents = [i for i in range(l)]
        
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]
        
        def union(a,b):
            ua = ufind(a)
            ub = ufind(b)
            
            parents[ua] = ub
            
        lookup = collections.defaultdict(list)
        for index, i in enumerate(vals):
            lookup[i].append(index)

        adj_list = collections.defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        output = 0
        for x in sorted(lookup.keys()):
            nodes = lookup[x]

            for u in nodes:
                for v in adj_list[u]:
                    if x>= vals[v]:
                        union(u,v)
            look = collections.Counter()
            for u in nodes:
                output += look[ufind(u)]
                look[ufind(u)] += 1
            
        output += l       
        return output

        
        