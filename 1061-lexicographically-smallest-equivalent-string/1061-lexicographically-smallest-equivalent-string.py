class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        smallest = {}
        
        for i in string.ascii_lowercase:
            smallest[i] = i
        
        def smaller(x):
            if smallest[x] != x:
                smallest[x] = smaller(smallest[x])
            return smallest[x]
        
        for a,b in zip(s1,s2):
            s = min(smaller(a), smaller(b))
            
            smallest[smaller(a)] = s
            smallest[smaller(b)] = s
            
        output = []
        for j in baseStr:
            output.append(smaller(j))
            
        return "".join(output)