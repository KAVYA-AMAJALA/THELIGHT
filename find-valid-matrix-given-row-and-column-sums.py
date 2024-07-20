class Solution:
    def restoreMatrix(self, rowsum: List[int], colsum: List[int]) -> List[List[int]]:
     n=len(rowsum)
     m=len(colsum)
     matrix=[[0]*m for i in range(n)]
     for i in range(n):
        for j in range(m):
            matrix[i][j]=min(rowsum[i],colsum[j])
            rowsum[i]-=matrix[i][j]
            colsum[j]-=matrix[i][j]
     return matrix
