z=''
y=''
a=''
for i in range(len(s)):
    if s[i]!='.':
       a+=s[i]
    else:
        y=a[::-1]
        y+=s[i]
        z+=y
        a=''  
z+=a[::-1]
print(z)

        
        
