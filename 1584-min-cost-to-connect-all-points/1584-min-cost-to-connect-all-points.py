class Solution:
	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		map = collections.defaultdict(list)
		for i in range(len(points)):
			for j in range(len(points)):
				if i != j:
					map[i].append((j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
		queue = [(0, 0)]        
		seen = set()
		res = 0
		while queue:
			x, y = heapq.heappop(queue)
			if y not in seen:
				seen.add(y)
				res += x
				for a, b in map[y]:
					heapq.heappush(queue, (b, a))
		return res