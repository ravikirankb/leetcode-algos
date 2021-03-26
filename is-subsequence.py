class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ind, t_ind,matched_count = 0, 0, 0
        
        while s_ind < len(s) and t_ind < len(t):
            if s[s_ind] == t[t_ind]:
               s_ind += 1
               t_ind += 1
               matched_count += 1
            else:
               t_ind += 1
            
        return matched_count == len(s)
            
            
            
            
               
