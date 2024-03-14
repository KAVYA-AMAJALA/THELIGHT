class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ma=0
        for i in accounts:
            x=sum(i)
            ma=max(x,ma)
        return ma
