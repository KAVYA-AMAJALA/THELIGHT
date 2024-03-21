Node* deleteNode(Node *head,int x)
{
    //Your code here
    if(x==1){
        return head->next;
    }
    int i=1;
    Node* temp=head;
    while(i<x-1){
        temp=temp->next;
        i++;
    }
    temp->next=temp->next->next;
    return head;
}
