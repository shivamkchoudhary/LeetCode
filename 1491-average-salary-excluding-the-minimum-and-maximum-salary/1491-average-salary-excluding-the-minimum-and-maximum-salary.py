class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()
        total = sum(salary) - salary[0] - salary[n-1]
        return total / (n-2)