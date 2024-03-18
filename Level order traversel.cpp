class Solution
{
    public:
    //Function to return the level order traversal of a tree.
    vector<int> levelOrder(Node* root)
    {
      //Your code here
      vector<int>v;
      queue<Node*>q;
      q.push(root);
      while(!q.empty()){
          int s=q.size();
          for(int i=0;i<s;i++){
              Node* node=q.front();
              q.pop();
              v.push_back(node->data);
              if(node->left){
              q.push(node->left);
          }
          if(node->right){
              q.push(node->right);
          }
          }
          
      }
      return v;
      
    }
};
