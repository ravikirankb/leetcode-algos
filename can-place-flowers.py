class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:return True
        i = 0
        l = len(flowerbed)
        while i < l:
            if flowerbed[i] == 0:
                prev = 0 if i == 0 else flowerbed[i-1]
                next = 0 if i == l-1 else flowerbed[i+1]
                
                if prev == 0 and next == 0:
                    n -= 1
                    flowerbed[i] =1
                    if n == 0:
                        return True
                
            i += 1
            
        return False
            
        
                
                    
            
