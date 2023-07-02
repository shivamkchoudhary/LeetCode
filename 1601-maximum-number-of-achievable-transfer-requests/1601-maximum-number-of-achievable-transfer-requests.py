class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        l=len(requests)
        for i in range(l,0,-1):
            for j in combinations(requests,i):
                if Counter(x for x ,y in j)==Counter(y for x,y in j):
                    return i

        return 0            