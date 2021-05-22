class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        
        check_set = set()
        for word in words:
            match = True
            for w in word:
                if w not in check_set:
                   if word.count(w) > chars.count(w):
                      match = False
                      break
                
                check_set.add(w)
                    
            if match:
                res += len(word)
            check_set = set()
            match = True
            
        return res
