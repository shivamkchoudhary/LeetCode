class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack,greater,n_dict = [], [], {}
        
        for n in reversed(nums2):
            while stack and stack[-1] < n:
                stack.pop()
            if stack:
                n_dict[n] = stack[-1]
            else:
                n_dict[n] = -1
            stack.append(n)
        for num in nums1:
            greater.append(n_dict[num])
        return greater
            
        