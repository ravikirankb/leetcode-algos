class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = collections.Counter()
        
        f_word = words[0]
        
        for w in f_word:
            present = True
            for i in range(len(words)):
                if w not in words[i]:
                    present = False
                else:
                    words[i] = words[i].replace(w,'',1)
                    
            if present:
                    ans[w] += 1
                
            present = True
                    
        res = [] 
        for i in ans.items():
            for j in range(i[1]):
                res.append(i[0])
                
        return res
