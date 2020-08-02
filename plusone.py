class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dlen = len(digits) - 1 
        
        while dlen >= 0:
              if digits[dlen] < 9:                 
                 digits[dlen] = digits[dlen] + 1
                 return digits
              
              digits[dlen] = 0
              dlen = dlen - 1
                
        darr = [0] * (len(digits) + 1)
        darr[0] = 1
        
        return darr
