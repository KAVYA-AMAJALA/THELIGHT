class Solution:
    def subarraySum(self, arr):
        # code here 
        n=len(arr)
        s=0
        for i in range(n):
            s+=arr[i]*(i+1)*(n-i)
        return s
            
        
