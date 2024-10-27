lass Solution:
    def findTriplet(self, arr):
        n=len(arr)
        a=set(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j] in a:
                    return True
        return False
