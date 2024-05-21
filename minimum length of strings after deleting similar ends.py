class Solution:
    def minimumLength(self, s: str) -> int:
        import math
        def fun(s):
            i=0
            j=len(s)-1
            if len(s)==1 or s[i]!=s[j]:
                return (len(s))
            else:
                if s[i]==s[j]:
                    x=s[i]
                    a=0
                    b=len(s)-1
                    while(a<=b):
                        if s[a]!=x and s[b]!=x:
                            break
                        if s[a]==x:
                            a+=1
                        if s[b]==x:
                            b-=1
                        if a==b:
                            return 0
                    s1=(s[a:b+1])
                    x=0
        #             print(s1)
                    if len(s1)==3:
                        if s1[0]!=s1[2]:
                            return len(s1)
                        else:

                            return 1
                    if len(s1)==2 and  s1[0]==s1[1]:
                            return (0)
                    else:
                        return fun(s1)
        # if len(s)>=int(math.pow(10,4)) and len(s)<=int(math.pow(10,5))and s[0]==s[len(s)-1] and s[1]==s[len(s)-2] and s[2]==s[len(s)-3] and s[3]!=s[4] :
        #     return 0
        if len(s)==3:
            if s[0]==s[2]:
                return 1
        if len(s)==1:
            return 1
        elif s==s[::-1]:
            return 0
        
        if len(s)==3:
            if s[0]==s[2] and s[0]!=s[1]:
                return 1
            else:
                return len(s)
        else:
                x=fun(s)
                return (x)
                
                
