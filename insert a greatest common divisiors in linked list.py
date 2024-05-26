# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
         import math
         slow=head
         fast=head.next
         t1=slow
         t2=fast
         while(t1 and t2):
                y1=int(t1.val)
                y2=int(t2.val)
                x=math.gcd(y1,y2)
                res=ListNode(x)
                t3=t1.next
                t1.next=res
                res.next=t2
                t1=t3
                t2=t2.next
         return slow
            
        
        
