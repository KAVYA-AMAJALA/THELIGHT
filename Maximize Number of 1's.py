#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    i=0
    j=0
    c=0
    ma=0
    while(j<n):
        if arr[j]==0:
            c+=1
        if c>m:
            
            if arr[i]==0:
                c-=1
            i+=1
        if c<=m:
            ma=max(ma,j-i+1)
        j+=1
    return ma
