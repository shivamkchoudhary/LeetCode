class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dp = matrix[:]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i == 0 and j == 0:
                        dp[i][j] = 10000
                    elif i == 0:
                        dp[i][j] = matrix[i][j-1] + 1
                    elif j == 0:
                        dp[i][j] = matrix[i-1][j] + 1
                    else:
                        dp[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + 1


        for x in range(m-1,-1,-1):
            for y in range(n-1, -1, -1):
                if matrix[x][y] != 0:
                    if x == m-1 and y == n-1:
                        matrix[x][y] = dp[x][y]
                    elif x == m-1:
                        matrix[x][y] = min(dp[x][y], 1+matrix[x][y+1])
                    elif y == n-1:
                        matrix[x][y] = min(dp[x][y], 1+matrix[x+1][y])
                    else:
                        matrix[x][y] = min(dp[x][y], 1+min(matrix[x+1][y], matrix[x][y+1]))


        return matrix