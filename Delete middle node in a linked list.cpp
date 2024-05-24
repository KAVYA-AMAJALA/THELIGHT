/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
