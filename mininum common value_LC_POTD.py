class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        x=0
        while(i<len(nums1) and  j<len(nums2)):
            if nums1[i]==nums2[j]:
                x=nums1[i]
                break
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        if x!=0:
            return (x)
        else:
            return (-1)
