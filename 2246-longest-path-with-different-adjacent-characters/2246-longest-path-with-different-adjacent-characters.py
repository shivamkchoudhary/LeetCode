class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        
        for i,parent in enumerate(parent):
            graph[parent].append(i)
            
        count = 1
        def dfs(node):
            nonlocal count
            
            first = second = 0
            for child in graph[node]:
                path_length = dfs(child)
                
                if s[child] != s[node]:
                    if path_length > first:
                        second = first
                        first = path_length
                    elif path_length > second:
                        second = path_length
                        
            count = max(count, first + second + 1)
            
            return first + 1
        dfs(0)
        
        return count
        