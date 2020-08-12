# vertical scanning python

class Solution:
    def longestCommonPrefix(self, strs):
        prefix=""
        if len(strs)==0: return prefix

        for i in range(len(strs[0])):
            c=strs[0][i]            
            for j in range(1,len(strs)):                        
                if len(strs[j]) == i or strs[j][i] != c:
                    return strs[0][0:i]
              
        return strs[0]
            
