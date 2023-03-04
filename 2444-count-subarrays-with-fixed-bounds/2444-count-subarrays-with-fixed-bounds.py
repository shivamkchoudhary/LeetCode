class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minfound = maxfound = False
        start = minstart = maxstart = 0
        total = 0

        for i in range(len(nums)):
            if nums[i] == minK:
                minstart = i
                minfound = True
            if nums[i] == maxK:
                maxstart = i
                maxfound = True
            if not minK <= nums[i] <= maxK:
                minfound = maxfound = False
                start = i+1
            if minfound and maxfound:
                total += min(minstart,maxstart) - start + 1

        return total
        