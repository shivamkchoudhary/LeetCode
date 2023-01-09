class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        l = len(nums)
        for i in range(l):
            if nums[i]!=0:
                nums[count] = nums[i]
                count +=1
                
        while count < l:
            nums[count] = 0
            count +=1
        