class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
    
        l,s = len(nums), sum(nums)
        r = s-x   

        if r==0: return l

        d = {0:-1}
        ll = ss = 0

        for i,e in enumerate(nums):
            ss += e
            if ss-r in d:
                ll = max(ll, i-d[ss-r])
            if ss not in d:
                d[ss] = i

        return [l-ll, -1][ll==0]
	
        