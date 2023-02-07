class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(fruits)):
            nums[fruits[r]] += 1
            while len(nums) > 2:
                nums[fruits[l]] -= 1 
                if not nums[fruits[l]]:
                    nums.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res
        