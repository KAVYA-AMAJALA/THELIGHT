class Solution {
  public:
    int minParentheses(string& s) {
        // code here
        stack<char>st;
        int c=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                st.push(s[i]);
            }
            else{
                if (st.empty()){
                   c+=1 ;
                }
                else{
                    st.pop();
                }
                
            }
        }
        c+=st.size();
        return c;
        
    }
};
