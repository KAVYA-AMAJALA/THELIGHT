# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import sys
        sys.set_int_max_str_digits(50000)
        
        s=""
        while(head):
            x=head.val
            s+=(str(x))
            head=head.next
        
        x=int(s)*2
        a=str(x)
        temp=ListNode(0)
        temp1=temp
        for i in range(len(a)):
            y=int(a[i])
            y=ListNode(y)
            temp1.next=y
            temp1=y
        return temp.next   
