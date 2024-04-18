#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        import math
        for i in range(r):
            s1=""
            for j in range(len(s)):
                if len(s1)>=math.pow(10,3):
                    break
                if s[j]=='1':
                    s1+='10'
                else:
                    s1+='01'
            s=s1
        return (s[n])

            
