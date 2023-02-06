class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
        # l1 = nums[:n]
        # l2 = nums[n:]
        # l=[]
        # for i in range(len(l1)):
        #     l.append(l1[i])
        #     l.append(l2[i])
        # return l
        