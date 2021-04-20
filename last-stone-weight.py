class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
                stones = list(i * -1 for i in stones)
                heapq.heapify(stones)
                
                while len(stones) > 1:
                    val1 = heapq.heappop(stones)
                    val2 = heapq.heappop(stones)
                    
                    if val1 != val2:
                       heapq.heappush(stones,val1 - val2)
                    
                try:
                    return -(stones[0])
                except:
                    return 0
                    
                    
