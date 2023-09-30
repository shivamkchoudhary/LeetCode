class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        last = float("-inf")
        stack = []
        
        for ele in nums[::-1]:
            if ele < last:
                return True
            
            while stack and stack[-1] < ele:
                last = stack.pop()
            
            stack.append(ele)
        
        return False