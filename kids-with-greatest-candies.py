class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c,result = max(candies),[]
        for i,v in enumerate(candies):
            if v + extraCandies >= max_c:
                result.append(True)
            else:
                result.append(False)
        return result
