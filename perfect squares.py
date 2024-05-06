class Solution:
    def numSquares(self, n: int) -> int:
        i=2
        c=1
        ma=1
        s=0
        l=[]
        while(n!=0):
            l.append(ma)
            ma=(i*i)
            if ma>n:
                break
            x=i
            c+=1
            i+=1
        if n==l[len(l)-1]:
            return 1
        k=0
        for i in range(0,len(l)):
            s=n-l[i]
            if s in l:
                k=2
                break
            else:
                for j in range(0,len(l)):
                    a=s-l[j]
                    if a in l:
                        k=3
                        break
        if k!=0:
            n1=k
        else:
            n1=4
        return n1
