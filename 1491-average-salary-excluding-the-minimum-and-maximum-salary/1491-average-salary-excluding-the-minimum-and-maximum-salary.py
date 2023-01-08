class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        del salary[0]
        return sum(salary)/len(salary)