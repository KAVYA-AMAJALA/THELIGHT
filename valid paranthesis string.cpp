class Solution {
public:
    bool checkValidString(string s) {
        stack<int>s1;
        stack<int>s2;
        for(int i=0;i<s.length();i++){
            if(s[i]=='('){
                s2.push(i);
            }
            else if(s[i]=='*'){
                s1.push(i);
            }
            else if(s[i]==')'){
                if(s2.empty() && s1.empty())
                    return false;
                else if(!s2.empty())
                    s2.pop();
                else
                    s1.pop();
                }
            }
            while(!s2.empty()){
                if(s1.empty()) return false;
                if(s2.top()>s1.top())return false;
                s2.pop();
                s1.pop();
            }
            return true;
        
    }
};
