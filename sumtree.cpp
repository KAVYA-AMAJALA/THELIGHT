/*  Tree node
struct Node
{
    int data;
    Node* left, * right;
}; */

// Should return true if tree is Sum Tree, else false
class Solution
{
    public:
    int a=0;
    int fun(Node* root){
        if(root==NULL){
            return 0;
        }
        if(root->left==NULL && root->right==NULL){
            return root->data;
        }
        int x=fun(root->left);
        int y=fun(root->right);
        if(x+y!=root->data){
            a=1;
        }
        return (x+y+root->data);
    }
    bool isSumTree(Node* root)
    {
         // Your code here
        fun(root);
        
        if(a==1){
            return 0;
        }
        else{
            return 1;
        }
    }
};
