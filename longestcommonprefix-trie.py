class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.children = [None] * 26

class Solution:
    def longestCommonPrefix(self, strs):
        root = TrieNode()
        self.construcTrie(strs,root)
        
        return self.walkTrie(root)
    
    def construcTrie(self,arr,root):
        for i in arr:
            self.insert(i,root)
    
    def insert(self,key,root):
        pCrawl = root
        for i in range(len(key)):
            ind = ord(key[i]) - ord('a')
            if pCrawl.children[ind] == None:
                pCrawl.children[ind] = TrieNode()
            pCrawl = pCrawl.children[ind]
        pCrawl.isLeaf = True
        
    def getValidPrefix(self,root):
        prefix = ""
        count = 0
        for i in range(26):
            if root.children[i] != None:
                count += 1
                prefix = chr(97 + i)
        
        if count == 1:
           return prefix
        else:
            return ""
        
    def walkTrie(self,root):
        pCrawl = root
        currentchar = self.getValidPrefix(pCrawl)
        print(currentchar)
        prefix = ""
        while currentchar != '' and pCrawl.isLeaf == False:
              ind = ord(currentchar) - ord('a')
              pCrawl = pCrawl.children[ind]
              prefix += currentchar
              currentchar = self.getValidPrefix(pCrawl)
              
            
        return prefix
        
          
