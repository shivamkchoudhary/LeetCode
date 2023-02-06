class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = nums[:n]
        l2 = nums[n:]
        l=[]
        for i in range(len(l1)):
            l.append(l1[i])
            l.append(l2[i])
        return l
        