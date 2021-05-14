class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nop = 0
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i] += 1
                nop += 1
            elif nums[i-1] > nums[i]:
                diff = nums[i-1] - nums[i]
                nums[i] += diff + 1
                nop += diff + 1
        
        return nop
