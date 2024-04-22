#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        #code here
        b=[]
        for i in a:
            b.append(sum(i))
        return b.index(min(b))+1
