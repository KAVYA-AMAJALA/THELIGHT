class Solution:
	def printString(self, s, ch, count):
		# code here
	
		c=0
		a=0
		
        for i in range(len(s)):
            if s[i]==ch:
                c+=1
            if c==count:
                a=i
                return s[a+1:len(s)+1]
    
        return ""
            
