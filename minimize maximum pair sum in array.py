class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ma=0
        while(i<j):
            k=nums[i]+nums[j]
            if k>ma:
                ma=k
            i+=1
            j-=1
        return (ma)
                
