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
            
