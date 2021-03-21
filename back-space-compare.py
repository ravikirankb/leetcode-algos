class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1,res2 = [],[]
        for i,s in enumerate(S):
            if s == '#':
                if len(res1) > 0:
                 res1.pop()
            else:
                res1.append(s)
        
        for j,t in enumerate(T):
            if t == '#':
                if len(res2) > 0:
                 res2.pop()
            else:
                res2.append(t)
        
        return ','.join(res1) == ','.join(res2)

    
    ## slightly memory efficient
    
    class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1,res2,len1,len2 = '','',0,0
        for i,s in enumerate(S):
            if s == '#':
                if len1>0:
                 res1 = res1[0:len1-1]                
                 len1 -= 1
            else:
                res1 += s
                len1 += 1
        
        for j,t in enumerate(T):
            if t == '#':
                if len2 >0:
                 res2 = res2[0:len2-1]                
                 len2 -= 1
            else:
                res2 += t
                len2 += 1
                
        return res1 == res2
