class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:

        i=0
        j=0
        s=0
        # k=11
        je=[]
        while(j<len(nums)):
            s+=nums[j]
            while(s>k):
                je.append(len(nums[i:j+1]))
                s-=nums[i]
                i+=1
            if s==k:
                je.append(len(nums[i:j+1]))
            
            j+=1
        if len(je)==0:
            return (0)
        else:
            return (min(je))
                
