class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        if(len(nums)!=len(s)):
            return True
        else:
            return False
        