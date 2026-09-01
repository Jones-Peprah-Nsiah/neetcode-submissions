# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,left,right):
            if not node :
                return True

            if not(left<node.val and right>node.val):
                return False

            return(valid(node.left, left, node.val) and 
            valid(node.right, node.val, right))

        return valid(root,float("-inf"), float("inf"))

        """
I use DFS with a valid range for each node. Initially, every value is allowed, so the range is negative infinity to positive infinity. When I move to the left child, I update the upper bound to the current node's value. When I move to the right child, I update the lower bound. If any node falls outside its allowed range, the tree isn't a valid BST. This gives O(n) time because every node is visited once and O(h) space for the recursion stack.
        """