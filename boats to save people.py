class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        b=0
        r=len(people)-1
        while(l<=r):
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            b+=1
        return b
