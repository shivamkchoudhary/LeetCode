class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        
        def dfs(word):            
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if ((prefix in wordSet and suffix in wordSet) or
                    (prefix in wordSet and dfs(suffix))) :
                        return True
                    
        output = []
        for w in words:
            if dfs(w):
                output.append(w)
        return output
                        
        