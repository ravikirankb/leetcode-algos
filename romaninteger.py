class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {}
        romandict['I'] = 1
        romandict['V'] = 5
        romandict['X'] = 10
        romandict['L'] = 50
        romandict['C'] = 100
        romandict['D'] = 500
        romandict['M'] = 1000
        
        result:int = 0
        prev: str =''
        for c in list(s):
            if prev == '':
                prev = c
                result += romandict[c]
            else: 
                if romandict[prev] < romandict[c]:
                   result -= romandict[prev]
                   result += romandict[c] - romandict[prev]
                   prev = c
                else:
                   result += romandict[c]                
                   prev = c
            
        return result
