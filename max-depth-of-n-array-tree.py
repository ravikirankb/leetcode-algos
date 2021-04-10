class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        self.depth = float("-inf")
        def dfs(root,depth):
            if root and not root.children:
                self.depth = max(depth,self.depth)
                return
            
            for c in root.children:
                dfs(c,depth+1)
                
        dfs(root,1)
                
        return self.depth
                
