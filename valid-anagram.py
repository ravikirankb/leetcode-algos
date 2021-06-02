class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = collections.Counter(s)
        t_c = collections.Counter(t)
        
        return s_c == t_c
