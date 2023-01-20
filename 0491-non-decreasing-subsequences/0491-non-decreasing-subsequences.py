class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        def find(i,l,c):
            if i==n:
                if len(c) >=2:
                    ans.add(tuple(c))
                return
            if nums[i] >= l:
                c.append(nums[i])
                find(i+1,nums[i],c)
                c.pop()
            find(i+1,l,c)
        find(0,-10000, [])
        return ans



        