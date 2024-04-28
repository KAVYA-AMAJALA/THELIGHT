class Solution:
    def reverseWords(self, s: str) -> str:
        s1=""
        l=[]
        for i in range(len(s)):
            if s[i]!=' ':
                s1+=s[i]
            else:
                if(s1!="" and s1!=' '):
                    l.append(s1)
                    s1=""
        if l==[]:
            return (s)
        else:
            s2=""
            for i in range(len(s)-1,-1,-1):
                    if s[i]!=' ':
                        s2=s[i]+s2
                    else:
                        l.append(s2)
                        break
            x=""
            for i in range(len(l)-1,-1,-1):
                if l[i]==' ':
                    x+=l[i]
                else:
                    x+=l[i]+' '
            if x[0]==' ':
                return (x[1:-1])
            else:
                return (x[:-1])
