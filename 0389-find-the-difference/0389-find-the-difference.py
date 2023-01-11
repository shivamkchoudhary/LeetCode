class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_ascii=0
        for i in t:
            sum_ascii += ord(i)
        for i in s:
            sum_ascii -= ord(i)
        return chr(sum_ascii)
        