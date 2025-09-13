class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=n*[0]
        l[0]=int(-((n*(n-1))/2))
        for i in range(1,n):
            l[i]=i
        return(l)
        
        
