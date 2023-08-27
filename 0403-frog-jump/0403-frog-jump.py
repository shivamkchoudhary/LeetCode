class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        n = len(stones)
        stack = [(0, 0)]
        visited = set()
        while stack:
            stone, jump = stack.pop()
            for j in [jump-1, jump, jump+1]:
                if j <= 0:
                    continue
                next_stone = stone + j
                if next_stone == stones[-1]:
                    return True
                if next_stone in stones:
                    if (next_stone, j) not in visited:
                        stack.append((next_stone, j))
                        visited.add((next_stone, j))
        return False