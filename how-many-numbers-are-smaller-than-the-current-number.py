class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = sorted(nums,reverse=True)
        dict = {}
        result = []
        for i,n in enumerate(new_nums):
            for j in range(i+1,len(new_nums)):
                if n == new_nums[j]:
                    break
                elif n > new_nums[j]:
                    if n in dict:
                        dict[n] +=1 
                    else:
                        dict[n] = 1
                        
        for n in nums:
            result.append(dict[n] if n in dict else 0)
            
        return result
