class Solution:
    def totalFine(self, n, date, car, fine):
        #Code here
        s=0
        for i in range(len(car)):
            if date%2==0:
                if car[i]%2==1:
                    s+=fine[i]
            else:
                if car[i]%2==0:
                    s+=fine[i]
        return s
    
    
