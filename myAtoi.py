class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.strip()
        res = 0
        hassign = False
        positivesign = True
        try:
           if s[0] == '-':
               positivesign = False
           if s[0] in ('-','+'):
               hassign = True
           for i in range(1 if hassign else 0,len(s)):
               if s[i].isdigit():
                   res = (res *10) + int(s[i])
               else:
                   break

           if not positivesign:
               res = res * -1

           if (-2**31<=res<=(2**31)-1): return res
           if res<0: return -2**31
           else: return 2**31-1
        except Exception as e:
           return 0
