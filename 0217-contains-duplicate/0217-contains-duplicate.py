class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = list(set(nums))
        return (len(numSet)!=len(nums))
        