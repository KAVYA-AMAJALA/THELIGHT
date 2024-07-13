class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]
        temp=0
        for i in range(len(gain)):
            temp=temp+gain[i]
            l.append(temp)
        return max(l)
