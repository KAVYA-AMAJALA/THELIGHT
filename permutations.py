class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def fun(l,s,e,li):
            if(len(li)==math.factorial(len(l))):
                return li
            if(s>=e):
                li.append(list(l))
                return 
            for i in range(s,e+1):
                temp=l[s]
                l[s]=l[i]
                l[i]=temp
                fun(l,s+1,e,li)
                temp=l[s]
                l[s]=l[i]
                l[i]=temp 
        li=[]
        fun(nums,0,len(nums)-1,li)
        return li
