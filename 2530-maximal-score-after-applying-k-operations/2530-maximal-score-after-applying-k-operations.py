class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        score = 0
        while k:
            score += -heappushpop(nums, nums[0]//3)
            k -= 1     
        return score    
        