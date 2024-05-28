class Solution {
    public long minimumPossibleSum(int n, int target) {
        long sum=0;
        int cnt=0;
        for(int i=1; i<=target/2 && i<=n;i++){
            sum+=i;
            cnt++;
        }
        int need=n-cnt;
    int i=target;
    while(need!=0)
    {
        sum+=i;
        i++;
        need--;
    }
    return sum;
    }
    
}
