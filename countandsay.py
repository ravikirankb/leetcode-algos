class Solution:
    def countAndSay(self, n: int) -> str:
       self.countandsay:str = '1'
        
       for i in range(n):
         if i == 0:
                self.countandsay = '1'
         else:
             self.countandsay = self.gencountandsay(self.countandsay)         
        
       return self.countandsay
            
    def gencountandsay(self,value:str) -> str:
        rstr:str =''        
                   
        counter:int = 0
        prev = ''        
        for c in list(value):            
            if prev == '':
               prev = c                 
               counter = counter + 1
            else:
                cur = c
                if prev == cur:
                   counter = counter + 1                    
                else:                        
                    rstr += str(counter) + prev                   
                    counter = 1                    
                    prev = cur 
                       
          
        rstr += str(counter) + prev
        
        return rstr
                
        
        
        
