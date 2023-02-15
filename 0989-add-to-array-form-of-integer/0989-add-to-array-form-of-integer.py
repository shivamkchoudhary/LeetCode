class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        c=""
        for i in num:
            c += str(i)
        s = int(c) + k
        l=[]
        for i in str(s):
            l.append(int(i))
        return l
        