class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
                l.append(i)
            else:
                d[i]=1
        return l
