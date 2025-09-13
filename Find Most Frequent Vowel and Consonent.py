class Solution:
    def maxFreqSum(self, s: str) -> int:
        vm=0
        cm=0
        for i in s:
            if i in 'aeiou':
                vm=max(vm,s.count(i))
            else:
                cm=max(cm,s.count(i))
        return vm+cm
        
