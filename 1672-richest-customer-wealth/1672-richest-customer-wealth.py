class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            s= sum(accounts[i])
            if  s > wealth:
                wealth = s
        return wealth
                
        