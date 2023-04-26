class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while (num > 0):
            n = num % 10
            s = s + n
            num = num // 10
            
            if(num == 0 and s > 9):
                num = s
                s =0
        return s
            
        