class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=0
        for i in arr:
            a=arr.count(i)
            if a==1:
                c+=1
                if c==k:
                    return i
        return ""
