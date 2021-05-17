class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a = set()
        for n in nums:
            if n in a:
                return n
            else:
                a.add(n)
