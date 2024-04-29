class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        l=[]
        while(i!=j):
            if (numbers[i]+numbers[j])==target:
                l.append(i+1)
                l.append(j+1)
                j-=1
                return (l)
            elif(numbers[i]+numbers[j])>target:
                j-=1
            else:
                i+=1

            
                
                    
                
