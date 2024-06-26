class Solution {
public:
    int precedence(char op){
        if(op=='+' || op=='-')return 1;
        else{
            return 2;
        }
    }
    int evaluate(int n1,int n2,char op){
        if(op=='+')return n1+n2;
        if(op=='-')return n1-n2;
        if(op=='*')return n1*n2;
        if(op=='/')return int(n1/n2);
        return 0;

    }
    int calculate(string s) {
        stack<int>Numbers;
        stack<char>Operators;
        //if the character is a number
        for(int i=0;i<s.size();i++){
            if(s[i]==' ')continue;
            int n=0;
            if(s[i]<='9' && s[i]>='0'){
                while(s[i]>='0' && s[i]<='9'){
                    n=n*10+int(s[i]-'0');
                    i+=1;
                }
            i=i-1;
            Numbers.push(n);
        }
        
        
        //if the character is operator
        else
        {
            if(Operators.empty()){
                Operators.push(s[i]);
            }
            else{
                
                    if(precedence(s[i])>precedence(Operators.top())){
                        Operators.push(s[i]);
                    }
                    else{
                        while(!Operators.empty()&&precedence(s[i])<=precedence(Operators.top())){
                            int n1=Numbers.top();
                            Numbers.pop();
                            int n2=Numbers.top();
                            Numbers.pop();
                            int ans=evaluate(n2,n1,Operators.top());
                            Operators.pop();
                            Numbers.push(ans);
                        }
                        Operators.push(s[i]);
                    }
                }
                    
        }
        }
        
        //if the operators remains in the Operator stack
        while(!Operators.empty()){
                int n1=Numbers.top();
                Numbers.pop();
                int n2=Numbers.top();
                Numbers.pop();
                int ans=evaluate(n2,n1,Operators.top());
                Operators.pop();
                Numbers.push(ans);
        }
        
        return (Numbers.top());
        
    }
};
        
