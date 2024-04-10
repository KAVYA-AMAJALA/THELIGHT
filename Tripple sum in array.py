#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        A.sort()
        c=0
        for x in range(len(A)):
            i=x+1
            j=len(A)-1
           
            while(i<j):
                k=abs(X-A[x])
                if (A[i]+A[j])==k:
                    # print(A[i],A[j],A[x])
                    c+=1
                    break
                elif (A[i]+A[j])>k:
                    j-=1
                else:
                    i+=1
        if c>=1:
            return 1
        else:
            return 0
