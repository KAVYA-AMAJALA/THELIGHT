#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        if not head:
            temp=Node(data)
            temp.next=temp
            return temp
        if head.data>data:
            temp=Node(head.data)
            temp.next=head.next
            head.next=temp
            head.data=data
        else:
            curr=head
            while curr.next!=head and curr.next.data<data:
                curr=curr.next
            temp=Node(data)
            temp.next=curr.next
            curr.next=temp
        return head
        
        #code here
