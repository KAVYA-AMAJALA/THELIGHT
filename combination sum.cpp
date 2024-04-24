class Solution {
public:
 void Solve(vector<int>arr,int t,vector<vector<int>>&ans,int i,int su,int n,vector<int>temp)
    {
        if(su==t){
            ans.push_back(temp);
            return;
        }
        if(i>=n || su>t){
            return;
        }
        Solve(arr,t,ans,i+1,su,n,temp);
        temp.push_back(arr[i]);
        Solve(arr,t,ans,i,su+arr[i],n,temp);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>ans;
        vector<int>temp;
        Solve(candidates,target,ans,0,0,candidates.size(),temp);
        return ans;
    }
};
