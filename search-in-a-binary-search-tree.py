class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        
        self.result = None
        
        def dfs(root,val):
            if root:
               if root.val == val:
                  self.result = root
                  return
            
            if root.right:
               dfs(root.right,val)
            if root.left:
               dfs(root.left,val)
         
        dfs(root,val)
        return self.result
