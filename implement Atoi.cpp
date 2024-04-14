#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        s1=""
        if(len(s)==1):
            if (s[0]=='0'):
                return int(s)
        # else:
        #     if(s[0]=='0'):
        #         return -1
        if(len(s)!=0):
            if s[0]=='-':
                s1+=s[0]
                for i in range(1,len(s)):
                    if s[i].isdigit():
                        s1+=s[i]
            
              
            else:
                for i in range(len(s)):
                    if s[i].isdigit():
                        s1+=s[i]
        
            # k=str(s1)
        # v=int(s)
        if(len(s1)!=0 and len(s1)==len(s)):
            if(s1[0]!='0'):
                if s1==s:
                    return (int(s1))
                else:
                    return (-1)
            else:
                y=s1[1:]
                return( int(y))
        else:
            return -1
            
