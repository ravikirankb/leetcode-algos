class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = len(s)
        if l == 0:
            return 0
        if l < 3:
            return max(s)
        else:
            return sorted(set(s))[-3]
            
            
       
        
