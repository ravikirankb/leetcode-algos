class Solution:
    def sumRootToLeaf(self, root: TreeNode,sum_ =0) -> int:
         self.result = 0
         self.dfs(root, 0)
         return self.result
    
    def dfs(self, node, curr_sum):
       if node is None:
          return
        
       if not node.left and not node.right:
          self.result += (curr_sum << 1) + node.val
          return
       
       self.dfs(node.left,(curr_sum << 1) + node.val)
       self.dfs(node.right,(curr_sum << 1) + node.val)
