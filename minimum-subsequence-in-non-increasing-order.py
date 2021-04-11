class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        new_sum = 0
        for i in range(len(nums)):
            new_sum += nums[i]
            total_sum -= nums[i]
            if new_sum > total_sum:
                ans = nums[:i+1]
                return ans 
