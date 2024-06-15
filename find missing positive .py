class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
        for i in range(1,len(nums)+2):
            if i not in d:
                return i
        return -1
