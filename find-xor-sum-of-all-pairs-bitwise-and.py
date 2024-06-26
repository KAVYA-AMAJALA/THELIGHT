class Solution:
    def getXORSum(self, a: List[int], b: List[int]) -> int:
        l=[]
        s=a[0]
        for i in range(1,len(a)):
            s=s^a[i]
        s1=b[0]
        for i in range(1,len(b)):
            s1=s1^b[i]
        return (s&s1)
