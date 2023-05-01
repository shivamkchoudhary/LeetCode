class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        min_salary = float('inf')
        max_salary = float('-inf')
        total = 0
        for s in salary:
            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)
            total += s
        return (total - min_salary - max_salary) / (n-2)