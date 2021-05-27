class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
         l = len(set(candyType))
         
         tl = len(candyType) //2
        
         return tl if tl<=l else l
