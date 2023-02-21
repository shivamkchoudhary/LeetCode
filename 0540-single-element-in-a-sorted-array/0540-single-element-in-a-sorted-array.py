class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)
        keys = [k for k, v in d.items() if v == 1]
        return keys[0]
        
            
        