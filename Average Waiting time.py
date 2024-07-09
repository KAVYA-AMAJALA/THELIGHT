m=0
s=0
for i in range(len(customers)):
    if m <customers[i][0]:
        m=customers[i][0]
        m+=customers[i][1]
        s+=(m-customers[i][0])
    else:
        m+=customers[i][1]
        s+=(m-customers[i][0])
return s/len(customers)
