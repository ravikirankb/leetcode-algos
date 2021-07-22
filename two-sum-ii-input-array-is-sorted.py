class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,l = 0,len(numbers)-1
        while i < l:
            n = numbers[i] + numbers[l]
            if n < target:
                i += 1
            if n > target:
                l -= 1
            if n == target:
                return [i+1,l+1]
                
        
             
