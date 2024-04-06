#User function template for Python 3

class Solution:
    def majorityElement(self, l, n):
        a=n//2
        d={}
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in d:
            if d[i]>a:
                return i
        return -1
                #Your code here
