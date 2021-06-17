## intersection of two arrays using dictionary approach.
## high speed and less memory efficient
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = collections.Counter(nums1)
        set2 = collections.Counter(nums2)
        
        res =[]
        if len(set1) >= len(set2):
           for i in set1:
               if i in set2:
                    if set1[i] >= set2[i]:
                        for j in range(set2[i]):
                            res.append(i)
                    else:
                        for j in range(set1[i]):
                            res.append(i)
        else:
           for i in set2:
               if i in set1:
                    if set2[i] >= set1[i]:
                        for j in range(set1[i]):
                            res.append(i)
                    else:
                        for j in range(set2[i]):
                            res.append(i)
        
        return res
        
        
