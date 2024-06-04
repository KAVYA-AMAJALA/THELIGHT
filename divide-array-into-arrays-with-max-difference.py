class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        y=[]
        j=0
        for i in range(0,len(nums),3):
            k1=abs(nums[i]-nums[i+2])
            if k1<=k:
                y.append(list(list((nums[i],nums[i+1],nums[i+2]))))
            else:
                y=[]
                break
        return y
        
