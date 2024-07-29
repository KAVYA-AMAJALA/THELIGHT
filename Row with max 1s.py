class Solution:

	def rowWithMax1s(self,arr):
		# code here
		 l=[]
         for i in arr:
            l.append(i.count(1))
         s=max(l)
         if sum(l)==0:
             return -1
         else:
             return l.index(s)
