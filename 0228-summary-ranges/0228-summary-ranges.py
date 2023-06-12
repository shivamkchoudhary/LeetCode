class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(10 ** 20)
        ans = []
        start = None
        end = None
        
        for n in nums:
            if start is None:
                start = n
                end = n
            else:
                if n == end + 1:
                    end = n
                else:
                    if start == end:
                        ans.append(str(start))
                    else:
                        ans.append(f"{start}->{end}")
                    start = n
                    end = n
        return ans
                        
                
        