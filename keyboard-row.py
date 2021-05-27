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
                
                
