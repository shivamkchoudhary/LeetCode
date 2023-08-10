class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        c=Counter(nums)
        for i,v in c.items():
            if i==target:
                return True
        return False