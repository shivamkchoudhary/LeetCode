class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        toSort = []
        for c in s:
            if c in vowels:
                toSort.append(c)
        toSort.sort()
        i = 0
        res = ""
        for c in s:
            if c in vowels:
                res += toSort[i]
                i += 1
            else:
                res += c
        return res