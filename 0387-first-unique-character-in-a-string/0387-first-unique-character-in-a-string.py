class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=[]
        for i in range(len(s)):
            count=s.count(s[i])
            c.append(count)
            if count==1:
                return (i)
                break
        if 1 not in c:
            return (-1)
        