class Solution(object):
    def countOrders(self, n):
        res, modulo = 1, 1000000007
        for i in range(1, n+1):
            res = res * i * (2*i - 1) % modulo
        return res
        
        