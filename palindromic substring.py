class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        for  i in range(len(s)):
            for j in range(i,len(s)):
                x=s[i:j+1]
                s1=x[::-1]
                if x==s1:
                    c+=1
        return (c)
                
