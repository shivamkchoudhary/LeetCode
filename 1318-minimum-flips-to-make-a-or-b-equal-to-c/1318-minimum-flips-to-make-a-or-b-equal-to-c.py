class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while c > 0:
            if c % 2 != ((a % 2) | (b % 2)):
                if c % 2 == 0:
                    count += (a % 2) + (b % 2)
                else:
                    count += 1
            a //= 2
            b //= 2
            c //= 2

        while a > 0 or b > 0:
            count += (a % 2)
            count += (b % 2)

            a //= 2
            b //= 2

        return count
