class Solution:
    def pivotInteger(self, n: int) -> int:
        s=0
        sl=[]
        x=0
        for i in range(1,n+1):
            s+=i
            sl.append(s)
        el=[]
        s=0
        for i in range(n,0,-1):
            s+=i
            el.append(s)    
        el.reverse()
        for i in range(len(sl)):
            if sl[i]==el[i]:
                x=i+1
                break
        if x!=0:
            return (x)
        else:
            return (-1)
                
