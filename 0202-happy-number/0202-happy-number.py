class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while(True):
            sum=0
            while(n>0):
                mod=n%10
                sum+=mod*mod
                n//=10
            if sum==1:
                return True
                break
            elif(sum in s):
                return False
                break
            s.add(sum)
            n=sum