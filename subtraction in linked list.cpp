#User function Template for python3

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s=""
        while(l1):
            x=l1.data;
            s+=str(x)
            l1=l1.next
        s1=""
        while(l2):
            x=l2.data
            s1+=str(x)
            l2=l2.next
        a=int(s)
        b=int(s1)
        if(a>=b):
            val=a-b
        else:
            val=b-a
        val=str(val)
        temp=Node(0)
        temp1=temp
        for i in val:
            x=int(i)
            y=Node(x)
            temp1.next=y
            temp1=y
            # temp1=temp1.next
        return temp.next
            
