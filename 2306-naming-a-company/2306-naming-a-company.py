class Solution:
    def distinctNames(self, ideas: List[str]) -> int:        
        swap_dict = Counter()
        ideas = set(ideas)
        res = 0
        for idea in ideas:
            c = idea[0]
            for x in string.ascii_lowercase:
                if x+idea[1:] not in ideas:
                    res += swap_dict[(c,x)]*2
                    swap_dict[(x, c)] += 1
        return res
        