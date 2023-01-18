class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eleSum = sum(nums)
        digiSum = 0
        for i in nums:
            while i:
                k = i % 10
                digiSum += k
                i = i //10
        return abs(eleSum-digiSum)

        