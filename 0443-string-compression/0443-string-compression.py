class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0        
        output = []        
        while j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            
            output.append(chars[i])
            if i+1 != j:
                for c in str(j-i):
                    output.append(c)
                
            i = j
            
        chars[:] = output
        return len(output)
        