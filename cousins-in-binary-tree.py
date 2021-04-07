# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## simple python bfs solution using stack. 
class Solution:
      def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
          if not root:
             return False
            
          #initial depth of x,y  
          depth_x,depth_y = 0,0
          #initial parents of x,y
          par_x,par_y = None,None
          que = [(root,0,None)]
            
          while que:
            cur_node,cur_depth,cur_parent = que.pop()
            if cur_node:
                if cur_node.val == x:
                    # if found, update x depth and parent
                    depth_x,par_x = cur_depth,cur_parent
                elif cur_node.val == y:
                    # if found, update y depth and parent
                    depth_y,par_y = cur_depth,cur_parent
            
            if cur_node.left:
                que.append((cur_node.left,cur_depth+1,cur_node))
            if cur_node.right:
                que.append((cur_node.right,cur_depth+1,cur_node))
                
          return depth_x == depth_y and par_x != par_y
            
                   
