class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        k = nums.index(target) if target in nums else nums.append(target)
        nums.sort()
        return nums.index(target)
