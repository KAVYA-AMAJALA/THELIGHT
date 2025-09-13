class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c=0
        a=0
        for i in s:
            if i in 'AEIOUaeiou':
                c+=1
        if c==0:
            return False
        if c%2==0:
            a=c-(c-1)
        else:
            return True
        if a%2==0:
            return False
        else:
            return True


        
