class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def fun(y,l,high):
            if(int(y)>high):
                return l
            l.append(int(y))
            k=str(y)[1:]
            y1=int(k[len(k)-1])+1
            if(y1>9):
                i=1
                s=""
                while(i<=len(y)+1):
                    s+=str(i)
                    i=i+1
                y1=s
                k=y1
            else:
                k+=str(y1)
            fun(k,l,high)
        k=str(low)
        i=1
        s=""
        while(i<=len(k)):
            s+=str(i)
            i=i+1
        l=[]
        fun(s,l,high)
        k=[]
        for i in l:
            if i>=low and i<=high:
                k.append(i)
        return (k)
                
