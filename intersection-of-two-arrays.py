class Solution:
     def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        res = []
        if len(set1) < len(set2):
            for n in set1:
                if n in set2:
                    res.append(n)
        else:
            for n in set2:
                if n in set1:
                    res.append(n)
                    
        return res
                    
