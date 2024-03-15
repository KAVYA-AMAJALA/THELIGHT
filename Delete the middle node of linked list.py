class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        int c=0;
        ListNode* t=head;
        while(t){
            c+=1;
            t=t->next;
        }
        
        int n=(c/2);
        ListNode* temp=head;
        for(int i=1;i<n;i++){
            temp=temp->next;
        }
        ListNode* slow=head;
        ListNode* fast=head;
        while(fast!=NULL && fast->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        temp->next=slow->next;
        if(c==1){
            head=NULL;
        }
        return head;

    }
};
