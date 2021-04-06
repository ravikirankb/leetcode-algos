# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(root,isLeaf):
            if not root:return 0
            if isLeaf and not root.left and not root.right:
                return root.val
                
            return dfs(root.left,1) + dfs(root.right,0)
            
        return dfs(root,0)
            
         
