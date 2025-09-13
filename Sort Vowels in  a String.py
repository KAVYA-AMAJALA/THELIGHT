class Solution:
    def sortVowels(self, s: str) -> str:
      v=[]
      sl=list(s)
      for i in sl:
        if i in 'AEIOUaeiou':
            v.append(i)
      if v==[]:
        return s
      v.sort()
      c=0
      a=""
      for i in range(len(s)):
        if sl[i] in 'AEIOUaeiou':
            a+=v[c]
            c+=1
        else:
            a+=sl[i]
      return  a

        
