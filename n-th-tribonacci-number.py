class Solution:
    def tribonacci(self, n: int) -> int:
        one,two,three=0,1,1
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        ans=0
        for i in range(3,n+1):
            ans=one+two+three
            one,two,three=two,three,ans
        return ans
