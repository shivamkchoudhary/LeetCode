class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        T = len(target)
        W = len(words)
        L = len(words[0])
        MOD = 10 ** 9 + 7

        f = [[0] * 26 for _ in range(L + 1)]

        for word in words:
            for index, c in enumerate(word):
                x = ord(c) - ord('a')
                f[index][x] += 1

        has_cache = [[False] * (L + 1) for _ in range(T + 1)]
        cache = [[None] * (L + 1) for _ in range(T + 1)]

        # tindex -> 0 to T
        # windex -> 0 to L
        def count(tindex, windex):
            if tindex == T:
                return 1
            if windex == L:
                return 0

            if has_cache[tindex][windex]:
                return cache[tindex][windex]

            ways = 0
            # we use "windex" and move on
            # f -> in the windex, how many times does target[tindex] appear
            ways += count(tindex + 1, windex + 1) * f[windex][ord(target[tindex]) - ord('a')]
            # we want to try to use another index
            ways += count(tindex, windex + 1)

            has_cache[tindex][windex] = True
            cache[tindex][windex] = ways % MOD
            return ways % MOD

        return count(0, 0) % MOD