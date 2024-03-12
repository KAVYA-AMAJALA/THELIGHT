class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k=nums1+nums2
        k.sort()
        l=len(k)
        if l%2==1:
            return float(k[l//2])
        else:
            m=k[l//2]
            n=k[l//2-1]
            return float(float(m)+float(n))/2.0
        
