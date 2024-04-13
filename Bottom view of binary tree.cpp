//Function to return a list containing the bottom view of the given tree.

class Solution {
  public:
   void BottomView(Node* root,int BF,int level,map<int,vector<int>>&m){
       if(root==NULL)return ;
       if(m[BF].empty()){
           m[BF].push_back(level);
           m[BF].push_back(root->data);
       }
       else{
           
              
                   if(m[BF][0]<=level){
                        m[BF].clear();
                        m[BF].push_back(level);
                        m[BF].push_back(root->data);
                       
                   }
               
               
           
           
       }
       BottomView(root->left,BF-1,level+1,m);
       BottomView(root->right,BF+1,level+1,m);
   }
    vector <int> bottomView(Node *root) {
        // Your Code Here
        map<int,vector<int>>m;
        BottomView(root,0,0,m);
        vector<int>res;
        for(auto it:m){
            res.push_back(it.second[1]);
        }
        return res;
    }
};
