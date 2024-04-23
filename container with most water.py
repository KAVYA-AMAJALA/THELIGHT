class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        b=len(height)-1
        l=[]
        while(a!=b):
            if height[a]<height[b]:
                min_a=height[a]
                width=abs(a-b)
                ma=min_a*width
                l.append(ma)
                a+=1
            else:
                min_a=height[b]
                width=abs(a-b)
                ma=min_a*width
                l.append(ma)
                b-=1
        return  (max(l))
        
       


    

        
