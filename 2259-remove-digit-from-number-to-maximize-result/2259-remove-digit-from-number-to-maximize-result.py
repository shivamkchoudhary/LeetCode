class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        pos = -1
        possibleNumber = []
        for i in range(len(number)):
            if number[i] == digit:
                possibleNumber.append(number[0:i]+number[i+1:])
        
        return max(possibleNumber)
            
            
        