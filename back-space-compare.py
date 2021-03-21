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
