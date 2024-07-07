class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum=numBottles
        while numBottles>=numExchange:
            mod=numBottles%numExchange
            numBottles//=numExchange
            sum+=numBottles
            numBottles+=mod
        return sum
