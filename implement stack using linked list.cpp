

//Function to push an integer into the stack.
void MyStack ::push(int x) 
{
    // Your Code
    StackNode* y=new StackNode(x);
    y->next=top;
    top=y;
}

//Function to remove an item from top of the stack.
int MyStack ::pop() 
{
    // Your Code
    if(top==NULL) return -1;
    StackNode* temp=top;
    int ans=temp->data;
    top=top->next;
    return ans;
}
