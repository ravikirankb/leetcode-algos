from queue import PriorityQueue
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == 1:
            for n in s:
                return n
        
        if len(s) == 2:
            r = []
            for n in s:
                r.append(n)
            return max(r[0],r[1])
        
        
        q = PriorityQueue()
        
        for n in s:
            q.put((-n,n))
            
        c = 1
        
        while not q.empty():
            if c == 3:
                return q.get()[1]
            
            q.get()
            c += 1
            
        return 0
            
       
        
