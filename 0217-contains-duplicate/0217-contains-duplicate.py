class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        duplicates = []
        for item in nums:
            if item in seen:
                duplicates.append(item)
            else:
                seen[item] = True
        return duplicates

        
        
        
        
        # s=set(nums)
        # if(len(nums)!=len(s)):
        #     return True
        # else:
        #     return False
        