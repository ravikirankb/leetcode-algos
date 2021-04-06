    
### simple recursive solution

class Solution:
     def sumOfLeftLeaves(self, root: TreeNode,isLeft = False) -> int:
        if not root:
            return 0
        elif isLeft and root and not root.left and not root.right:
            return root.val
        else:
            return self.sumOfLeftLeaves(root.left,True) + self.sumOfLeftLeaves(root.right,False)
            
         
