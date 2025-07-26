class Solution:
    def findMajority(self, arr):
        # code here
        n=len(arr)//3
        d={}
        l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>n:
                l.append(i)
        l.sort()
        return l
