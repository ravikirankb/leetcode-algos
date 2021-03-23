# fast and memory efficient
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set(allowed)
        result = len(words)
        
        for word in words:
            for ch in word:
                if ch not in chars:
                    result -=1
                    break
                    
        return result
        
