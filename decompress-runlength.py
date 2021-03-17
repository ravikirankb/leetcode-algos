class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(0,len(nums),2): # range has start, stop, skip
            result += [nums[i+1]] * nums[i] # oohoo can use * to repeat the element n times
        return result
