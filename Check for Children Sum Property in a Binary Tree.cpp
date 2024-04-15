/*Complete the function below

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){80
        data = x;
        left = right = NULL;
    }
};
*/

class Solution{
    public:
    int flag=0;
    void checkSum(Node* root){
        if(root==NULL){
            return ;
        }
        if(root->left!=NULL && root->right!=NULL){
            if(root->left->data+root->right->data!=root->data){
                flag=1;
            }
        }
        if(root->left==NULL  and root->right!=NULL){
            if(root->right->data!=root->data){
                flag=1;
            }
        }
        if(root->left!=NULL && root->right==NULL){
            if(root->left->data!=root->data){
                flag=1;
            }
        }
        checkSum(root->left);
        checkSum(root->right);
    }
    //Function to check whether all nodes of a tree have the value 
    //equal to the sum of their child nodes.
    int isSumProperty(Node *root)
    {
     // Add your code here
     checkSum(root);
     if(flag==1){
         return 0;
     }
     else{
         return 1;
     }
    }
};
