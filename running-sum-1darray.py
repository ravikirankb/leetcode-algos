## memory efficient

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            try:
                result.append(result[i - 1] + nums[i])
            except:
                result.append(nums[i])
            
        return result
