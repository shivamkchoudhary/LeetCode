class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        k = 0
        temp = [0]
        for i in gain:
            temp.append(k+i)
            k = k + i
        return max(temp)
            
        