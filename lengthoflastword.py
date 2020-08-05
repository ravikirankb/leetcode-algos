class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        
        charFound:bool = False
        length:int = 0               
          
        for j in range(len(s) -1,-1,-1):               
            if s[j] != ' ':
               charFound = True
               length = length + 1
            elif charFound == True:                 
                 return length
               
            
        return length
