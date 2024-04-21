//User function Template for C++

// N is the number of pairs of parentheses
// Return list of all combinations of balanced parantheses
class Solution
{
    public:
     void drinker(int close,int open,string s,int n,vector<string>&vec){
        if(close+open==n*2 ){
            vec.push_back(s);
            return ;
        }
        else if(close>open){
            return ;
        }
        else if(open==n){
            drinker(close+1,open,s+')',n,vec);
        }
        else{
            drinker(close,open+1,s+'(',n,vec);
            drinker(close+1,open,s+')',n,vec);
        }
        // return vec;
     }
    vector<string> AllParenthesis(int n) 
    {
        // Your code goes here 
        vector<string>vec;
        drinker(0,1,"(",n,vec);
        return vec;
    }
};
