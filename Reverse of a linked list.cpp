class Solution
{
    public:
    //Function to reverse a linked list.
    struct Node* reverseList(struct Node *head)
    {
        // code here
        // return head of reversed list
         Node* head1=NULL;
         Node* temp=head1;
        while(head){
            int x=head->data;
            Node* y=new  Node(x);
            y->next=temp;
            temp=y;
            head=head->next;
        }
        return temp;
    }
    
};
    
