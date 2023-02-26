class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        else:
            while len(stones) !=1 or len(stones) == 0:
                stones.sort()
                m = max(stones)
                k = stones.pop()
                m1 = max(stones)
                stones.pop()
                stones.append(m-m1)
        return stones[0]
        