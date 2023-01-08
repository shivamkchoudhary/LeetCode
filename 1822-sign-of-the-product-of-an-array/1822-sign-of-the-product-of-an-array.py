class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in(nums):
            mul *= i
        def signFunc(mul):
            if mul >= 1:
                return 1
            elif mul < 0:
                return -1
            else:
                return 0
        return signFunc(mul)
