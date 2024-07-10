class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i!='./' and i!='../':
                c+=1
            elif c>0 and i=='../':
                c-=1
        return c
