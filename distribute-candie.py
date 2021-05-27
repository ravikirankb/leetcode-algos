class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
         l = len(set(candyType))
         
         cl = len(candyType)
         tl = cl // 2
        
         return tl if tl<=l else l
