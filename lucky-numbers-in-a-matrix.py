class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            a=min(matrix[i])
            s=matrix[i].index(a)
            l=[]
            for j in range(len(matrix)):
                l.append(matrix[j][s])
            m=max(l)
            if m==a:
                return [m]
