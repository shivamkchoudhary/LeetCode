class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, distMap):
            q = deque()
            q.append([src, 0])
            distMap[src] = 0
            
            while q:
                node, dist = q.popleft()
                for neg in adj[node]:
                    if neg not in distMap:
                        q.append([neg, dist + 1])
                        distMap[neg] = dist + 1
                    
        node1Dict = {}
        node2Dict = {}
        
        bfs(node1, node1Dict)
        bfs(node2, node2Dict)
        
        output = -1
        tempDist = float("inf")
        for i in range(len(edges)):
            if i in node1Dict and i in node2Dict:
                dist = max(node1Dict[i], node2Dict[i])
                if dist < tempDist:
                    output = i
                    tempDist = dist
        return output 
           
        