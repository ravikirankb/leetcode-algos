class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return 0 if i == 0 else i
            elif i == len(nums) - 1:
                return i + 1
      
        
