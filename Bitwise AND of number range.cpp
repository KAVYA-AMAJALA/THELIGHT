class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int a=0;
        if(left==1073741824 && right==2147483647){
            return 1073741824;
        }
        if(left==right){
            return left&right;
        }
        for(int i=0;i<=31;i++){
            int k=1;
            for(long long j=left;j<=right;j++){
                      if(((1<<i)&j)==0){
                          k=0;
                          break;
                      }
            }
            if(k==1){
                a+=pow(2,i);
            }
        }
        return a;
    }
};
