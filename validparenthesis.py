class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        stack =[]
        charlist = list(s)
        for c in charlist:
            if self.isOpeningBrace(c):
                stack.append(c)
            else: 
                if len(stack) == 0:
                    return False
                
                cp = stack.pop()
                isvalid = self.isMatchingParen(cp, c)
                if not isvalid:
                    return False
            
            
        return len(stack) == 0
                                
    def isOpeningBrace(self, c: str) -> bool:
        if c == '(' or c == '[' or c == '{':
            return True
        else: return False
        
    def isMatchingParen(self, a: str,b:str) -> bool:
        if a == '(' and b == ')':
            return True
        if a == '{' and b == '}':
            return True
        if a == '[' and b == ']':
            return True
        else: return False
