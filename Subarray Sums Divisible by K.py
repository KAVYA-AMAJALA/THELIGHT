class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={}
        c=0
        s=0
        for i in nums:
            s+=i
            r=s%k
            if r not in d:
                d[r]=1
            else:
                c+=d[r]
                d[r]+=1
            if r==0:
                c+=1
        return c
