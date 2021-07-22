## two pointer approach
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
        
        
  ## using a dictionary.              
 class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0,len(numbers)):
            m = target - numbers[i]
            if m in dict:
               return [dict[m]+1,i+1]
            else:
                dict[numbers[i]] = i
                
                
                
                
             
        
             
