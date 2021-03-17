class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums),2):
            #print(i)
            for j in range(0,nums[i]):
                result.append(nums[i + 1])
                
        return result
