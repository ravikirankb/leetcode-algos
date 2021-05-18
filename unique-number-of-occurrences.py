class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for v in arr:
            if v in dict:
                dict[v] +=1
            else:
                dict[v] = 1
        
        u_set = set()
        for v in dict.values():
            if v in u_set:
                return False
            else:
                u_set.add(v)
        
        return True
