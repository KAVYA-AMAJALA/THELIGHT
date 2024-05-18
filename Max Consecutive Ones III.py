class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        m=0
        j=0      
        c=0
        while j<len(nums):
            if nums[j]==0:
                c+=1 
            if c>k:
                if nums[i]==0:
                    c-=1 
                i+=1 
            if c<=k:
                m=max(m,j-i+1)
            j+=1
        return m
        


        
