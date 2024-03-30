class Solution {
  public:
    int x=0;
    void fun(Node* root){
        if(root==NULL){
            return;
        }
        else if(root!=NULL && root->left==NULL){
            x=root->data;
            return ;
        }
        else{
            fun(root->left);
        }
    }
    int minValue(Node* root) {
        // Code here
        fun(root);
        if(x==0){
            return -1;
        }
        else{
            return x;
        }
}
