from collections import namedtuple

Result = namedtuple("Result", ["tilt", "total"])

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return Result(0, 0)
            if not node.left and not node.right:
                return Result(0, node.val)
            left_result = dfs(node.left)
            right_result = dfs(node.right)
            print(left_result,right_result)
            tilt = left_result.tilt + right_result.tilt + abs(left_result.total - right_result.total)
            print(tilt)
            return Result(tilt, node.val + left_result.total + right_result.total)
        
        return dfs(root).tilt
