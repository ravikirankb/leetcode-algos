## memory efficient solution

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        que = [(root,1)]
        while que:
            cur_node,depth = que.pop(0)
            
            if cur_node and not cur_node.left and not cur_node.right:
              ## since the first found leaf is the minimum depth stop the loop and do not continue looking further nodes.
               return depth
              
            if cur_node.left:
              que.append((cur_node.left,depth + 1))
            if cur_node.right:
              que.append((cur_node.right,depth + 1))
            
            
        return 0
            
        
        
## unique solution using inline recursion (not efficient :))

class Solution:
     def minDepth(self,root: TreeNode,depth =1) -> int:
         if not root:
            return 0
        
         if root and not root.right and not root.left:
                return depth
          
         l_depth = self.minDepth(root.left,depth + 1)
         r_depth = self.minDepth(root.right,depth + 1)
        
         if l_depth or r_depth:
            return min(l_depth if l_depth else float("inf"),r_depth if r_depth else float("inf"))
         else:
            return depth
