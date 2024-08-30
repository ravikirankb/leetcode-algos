## beats 90+ %
## simply easy solution

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(filter(lambda a:a%3 !=0,nums))
