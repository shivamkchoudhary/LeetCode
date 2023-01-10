import numpy as np
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        l = len(mat)
        for i in range(l):
            for j in range(l):
                if i==j or i+j == l-1:
                    s += mat[i][j]
        return s