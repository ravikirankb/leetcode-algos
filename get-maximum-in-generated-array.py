class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0, 1]
        res = 1
        for k in range(2, n + 1):
            #print(k)
            if k % 2 == 0:
                nums.append(nums[k//2])
            else:
                print(k//2,k//2+1)
                nums.append(nums[k//2] + nums[k//2+1])
                
        return max(nums)
