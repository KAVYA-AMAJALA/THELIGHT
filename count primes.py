class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[True]*(n)
        c=0
        if n<=1:
            c=0
        else:
            primes[0]=False
            primes[1]=False
            for i in range(2,int(n**0.5)+1):
                if primes[i]:
                    for j in range(i*i,n,i):
                        if primes[j]:
                            primes[j]=False
            for i in range(n):
                if primes[i]:
                    c+=1
        return c
        
