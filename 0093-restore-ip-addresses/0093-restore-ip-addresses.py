class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        
        def back(i, dots, currentIP):
            if dots == 4 and i == len(s):
                res.append(currentIP[:-1])
                return
            if dots > 4:
                return
            
            for k in range(i, min(i+3, len(s))):
                if int(s[i:k+1]) < 256 and (i==k or s[i] != '0'):
                    back(k+1, dots +1, currentIP + s[i:k+1] + ".")
        back(0, 0, "")
        return res
        