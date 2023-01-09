class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
         return max([sum(arr) for arr in accounts])
        