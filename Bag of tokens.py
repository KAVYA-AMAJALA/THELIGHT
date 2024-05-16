class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score=0
        i=0
        j=len(tokens)-1
        while(i<=j):
            if(tokens[i]<=power ):
                power=power-tokens[i]
                score+=1
                i+=1
            elif score>=1 and tokens[j]>power and (j-i)>1:
                power=power+tokens[j]
                score-=1
                j-=1
            else:
                i+=1
                j-=1
        return score
