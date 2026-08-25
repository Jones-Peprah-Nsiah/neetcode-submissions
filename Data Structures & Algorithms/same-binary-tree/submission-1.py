# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val!=q.val:
            return False

        return (self.isSameTree(p.left,q.left) and
         self.isSameTree(p.right,q.right))

        """

I recursively compare corresponding nodes in both trees. If both nodes are null, they match. If one is null or their values are different, I return false. Otherwise, I recursively compare their left subtrees and right subtrees, and both comparisons must be true."

        """
        
        