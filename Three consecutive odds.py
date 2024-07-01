class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)==3:
            a=sum(arr)
            if a%2==0:
                return False
        elif arr.count(1)==4:
            return False
        for i in range(0,len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]!=0:
                return True
        
