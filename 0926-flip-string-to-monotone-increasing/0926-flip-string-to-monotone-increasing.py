class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:        
        num_one, num_zero = 0, 0
        for i in s:
            if i == '1':
                num_one += 1
            else:
                num_zero += 1
                if num_zero > num_one:
                    num_zero = num_one
        return num_zero