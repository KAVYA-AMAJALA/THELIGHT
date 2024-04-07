
class Solution:
  def trappingWater(self, arr,n):
      #Code here
      l1=[]
      max=0
      for i in arr:
          if i>max:
              max=i
              l1.append(i)  
          else:
              l1.append(max)
      
      l2=[]
      max=0
      for i in range(len(arr)-1,-1,-1):
          if arr[i]>max:
              max=arr[i]
              l2.append(arr[i])
          else:
              l2.append(max)
      l2.reverse()
      
      s=0
      for i in range(len(arr)):
          l_max=l1[i]
          r_max=l2[i]
          min_val=min(l_max,r_max)
          fin_val=min_val-arr[i]
          s+=fin_val
      return (s)
          
          
  




