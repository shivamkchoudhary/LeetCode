import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 == str2 + str1):
            gcd = math.gcd(len(str1), len(str2))
            return str1[:gcd]
        else:
            return ''
        
#         len1, len2 = len(str1), len(str2)
        
#         def isDiv(l):
#             if len1 % l and len2 % l:
#                 return False
#             f1, f2 = len1 // l, len2 // l
#             return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
        
#         for l in range(min(len1, len2), 0, -1):
#             if isDiv(l):
#                 return str1[:l]
#         return ""
        
    
        
    