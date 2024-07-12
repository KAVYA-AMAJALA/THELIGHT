class Solution:
    def modify(self, s):
        # code here
        v=''
        for i in s:
            if i in "aeiou":
                v+=i
        v1=v[::-1]
        j=0
        a=''
        for i in range(len(s)):
            if s[i] in 'aeiou':
                a+=v1[j]
                j+=1
            else:
                a+=s[i]
        return a
