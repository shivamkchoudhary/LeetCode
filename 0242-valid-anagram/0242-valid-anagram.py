class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return all(s.count(x) == t.count(x) for x in set(s+t))
        s1=sorted(s)
        s2=sorted(t)
        if s1==s2:
            return True
        return False