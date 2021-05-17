class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        res = 0
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        
        for k in dict.keys():
            if dict[k] == 1:
                res += k
                
        return res
