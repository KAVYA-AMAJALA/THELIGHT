#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # code here
        a=n*(n+1)//2
        b=sum(arr)
        return a-b
