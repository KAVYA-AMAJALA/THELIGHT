#User function Template for python3

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
            num=0
            while n!=0:
                num^=n
                n>>=1
            return num
            
