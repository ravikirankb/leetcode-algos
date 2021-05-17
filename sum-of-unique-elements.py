class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        res = 0
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        
        for k in dict.keys():
            if dict[k] == 1:
                res += k
                
        return res

    ## with two sets- slightly less efficient
    class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        add_set = set()
        remove_set = set()
        
        res = 0
        for n in nums:
            if n in add_set and n in remove_set:
               add_set.remove(n)
               res -= n
            elif n not in add_set and n not in remove_set:
               add_set.add(n)
               res +=n
            
            remove_set.add(n)
            
        return res
