class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # nums = [3,1,-2,-5,2,-4]
# nums=[1,-1]
        p=[]
        for i in nums:
            if i>0:
                p.append(i)
        n=[]
        for i in nums:
            if i<0:
                n.append(i)
        # print(p,n)
        k=[p[0]]
        a=0
        b=1
        for i in range(1,len(nums)):
            if i%2!=0:
                k.append(n[a])
                a+=1
            else:
                k.append(p[b])
                b+=1
        return (k)
        
