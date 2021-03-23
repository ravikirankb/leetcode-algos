class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set(allowed)
        count,result = 0,len(words)
        
        for word in words:
            for ch in word:
                if ch not in chars:
                    count += 1
                    
            if count > 0:
               result -= 1
            
            count = 0
                    
        return result
        
