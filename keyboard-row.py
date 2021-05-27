class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        t = set({'q','w','e','r','t','y','u','i','o','p'})
        m = set({'a','d','s','f','g','h','j','k','l'})
        b = set({'z','x','c','v','b','n','m'})
       
        found = True
        result = []
        for word in words:
            for w in word:
                if w.lower() not in t:
                   found = False
                   break
                
            if found:
                result.append(word)
            
            found = True
                
            for w in word:
                if w.lower() not in m:
                   found = False
                   break
                
            if found:
                result.append(word)
                
            found = True
                
            for w in word:
                if w.lower() not in b:
                   found = False
                   break;
                
            if found:
                result.append(word)
                
            found = True
                
                
        return result
    
    
    ## slightly faster solution, avoids extra loops
    class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        t = set({'p', 'o', 'y', 'q', 'r', 'u', 'e', 'w', 't', 'i', 'P', 'O', 'Y', 'Q', 'R', 'U', 'E', 'W', 'T', 'I'})
        m = set({'h', 'a', 's', 'f', 'j', 'l', 'g', 'd', 'k', 'H', 'A', 'S', 'F', 'J', 'L', 'G', 'D', 'K'})
        b = set({'m', 'z', 'b', 'n', 'v', 'x', 'c', 'M', 'Z', 'B', 'N', 'V', 'X', 'C'})
       
        foundin_t,foundin_m,found_b = True,True,True
        result = []
        for word in words:
            for w in word:
                if w not in t:
                   foundin_t = False
                   pass
                    
                if w not in m:
                    foundin_m = False
                    pass
                
                if w not in b:
                    foundin_b = False
                    pass
            
                
            if foundin_t or foundin_m or foundin_b:
                result.append(word)
            
            foundin_t,foundin_m,foundin_b = True,True,True
                
        return result
                
                
                
                
