class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        # code here
        for i in range(n-1):
            if i%2==0:
                t=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=t
        
