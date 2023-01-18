import numpy as np
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        temp=[[0] * n for _ in range(n)]
        arr = np.array(temp)
        for q in queries:
            row1=q[0]
            col1=q[1]
            row2=q[2]
            col2=q[3]
            arr[row1:row2+1,col1:col2+1] = arr[row1:row2+1,col1:col2+1] + 1
            
        return arr
        