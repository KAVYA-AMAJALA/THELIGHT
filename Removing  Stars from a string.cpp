class Solution {
public:
    string removeStars(string s) {
        stack<char>st;
        string result;
        int i=0;
        for(int i=0;i<s.size();i++){
            if(s[i]!='*'){
                st.push(s[i]);
            }
            else{
                if(!st.empty() && st.top()!='*'){
                    st.pop();
                }
            }
        }
       while(!st.empty()){
            result+=st.top();
            st.pop();
       }
       reverse(result.begin(),result.end());
       return result;
        }
    
};
