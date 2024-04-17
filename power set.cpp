#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        # Code here
        import math
        n=len(s)
        k=int(math.pow(2,n))
        l=[]
        for i in range(1,k):
            j=0
            s1=""
            while(j<n):
                if(i&(1<<j)):
                    s1+=s[j]
                j+=1
            l.append(s1)
        return (sorted(l))
