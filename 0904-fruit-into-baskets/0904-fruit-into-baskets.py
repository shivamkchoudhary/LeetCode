class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        fruit_count = {}
        max_fruits = 0

        while end < len(fruits):
            if fruits[end] in fruit_count:
                fruit_count[fruits[end]] += 1
            else:
                fruit_count[fruits[end]] = 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)
            end += 1

        return max_fruits
        