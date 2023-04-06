#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        big = ((n+1) * n)//2
        original = sum(array)
        return big - original


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends