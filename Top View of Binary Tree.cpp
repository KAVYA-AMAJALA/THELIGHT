/*
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/
class Solution
{
    public:
    void TopView(Node* root,int BalFac,int level,map<int,vector<int>>&m){
        if(root==NULL)return ;
        if(m[BalFac].empty()){
            m[BalFac].push_back(level);
            m[BalFac].push_back(root->data);
        }
        else{
             if(m[BalFac][0]>level){
                 m[BalFac].clear();
                 m[BalFac].push_back(level);
                 m[BalFac].push_back(root->data);
             }
        }
        TopView(root->left,BalFac-1,level+1,m);
        TopView(root->right,BalFac+1,level+1,m);
    }
    //Function to return a list of nodes visible from the top view 
    //from left to right in Binary Tree.
    vector<int> topView(Node *root)
    {
        //Your code here
        map<int,vector<int>>m;
        TopView(root,0,0,m);
        vector<int>res;
        for(auto a:m){
            res.push_back(a.second[1]);
        }
        return res;
    }

};
