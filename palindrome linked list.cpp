class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* head1=NULL;
        ListNode* temp=head1;
        ListNode* res=head;
        while(head){
           int  x=head->val;
            ListNode* y=new ListNode(x);
            y->next=temp;
            temp=y;
            head=head->next;
        }
        
        while(res && temp){
            if(temp->val!=res->val){
                return false;
            }
            else{
                res=res->next;
                temp=temp->next;
            }
        }
        return true;
    }
};
