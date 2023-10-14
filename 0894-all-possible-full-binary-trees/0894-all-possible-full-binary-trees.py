# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def helper(n):
            if n == 1:
                base = []
                base.append(TreeNode(0))
                return base
            ans = []
            for i in range(1, n, 2):
                left = helper(i)
                right = helper(n - i - 1)
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        return helper(n)
                        
                        
        
        