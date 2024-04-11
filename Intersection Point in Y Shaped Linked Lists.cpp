

/* Linked List Node
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}; */

//Function to find intersection point in Y shaped Linked Lists.
int intersectPoint(Node* head1, Node* head2)
{
    // Your Code Here'
    Node* temp1=head1;
    Node* temp2=head2;
    int c=0;
    while(temp1){
        c+=1;
        temp1=temp1->next;
    }
    int c1=0;
    while(temp2){
        c1+=1;
        temp2=temp2->next;
    }
    int k=abs(c-c1);
    // Node* head3;
    // // while(head1&&head2){
    // //     if(c<c1){
    // //         int i=0;
    // //         if(i==k){
    // //             head3=head1;
    // //         }
    // //         head1=head1->next;
    // //     }
    // //     else{
    // //         int i=0;
    // //         i
    // //     }
    // // }
    // if(c>c1){
    //     int i=0;
    //     while(head1){
    //         if(i==k){
    //             head3=head1;
    //         }
    //         else{
    //             i+=1;
    //             head1=head1->next;
    //         }
    //     }
    // }
    // else{
    //     int i=0;
    //     while(head2){
    //         if(i==k){
    //           head3=head2;
    //         }
    //         else{
    //             i+=1;
    //             head2=head2->next;
    //         }
    //     }
 
    // }
  
    // if(c>c1){
    //     while(head3!=NULL && head2!=NULL){
    //         if(head3==head2){
    //             return head3->data;
    //         }
    //         head3=head3->next;
    //         head2=head2->next;
    //     }
    // }
    // else{
    //     while(head3!=NULL && head1!=NULL){
    //         if(head3==head1){
    //             return head3->data;
    //         }
    //         head3=head3->next;
    //         head1=head1->next;
    //     }
    // }
    if(c>c1){
        for(int i=0;i<k;i++){
            head1=head1->next;
        }
    }
    else{
        for(int i=0;i<k;i++){
            head2=head2->next;
        }
    }
    while(head1&&head2){
        if(head1==head2){
            return head1->data;
        }
        head1=head1->next;
        head2=head2->next;
    }
    return -1;
}
