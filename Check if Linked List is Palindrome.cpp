/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/

class Solution{
  public:
    //Function to check whether the list is palindrome.
    bool isPalindrome(Node *head)
    {
        //Your code here
        Node* head1=NULL;
        Node* temp=head1;
        Node* temp3=head;
        while(head){
            int x=head->data;
            Node* y=new Node(x);
            y->next=temp;
            temp=y;
            head=head->next;
        }
        // return temp;
        int c=0;
        while(temp && temp3!=NULL){
            if(temp3->data!=temp->data){
               return false;
            }
            else{
            temp3=temp3->next;
            temp=temp->next;
        }
        }
        return true;
    }
};
