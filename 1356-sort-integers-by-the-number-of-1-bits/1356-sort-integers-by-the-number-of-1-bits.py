class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:        
        newArr = []
        for num in arr:
            newArr.append((bin(num).count("1"), num))
        return [r[1] for r in sorted(newArr)]
