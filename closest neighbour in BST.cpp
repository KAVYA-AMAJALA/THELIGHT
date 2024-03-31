class Solution {
  public:
    int findMaxForN(Node* root, int n) {
        // code here
        if(root==NULL){
            return -1;
        }
        if(root->key>n){
            return findMaxForN(root->left,n);
        }
        return max(root->key,findMaxForN(root->right,n));
    }
};
