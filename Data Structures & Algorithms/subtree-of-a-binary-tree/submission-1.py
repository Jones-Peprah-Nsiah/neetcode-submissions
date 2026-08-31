# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        if self.issametree(root,subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))



    def issametree(self,root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot or root.val!=subRoot.val:
            return False
            
        return (self.issametree(root.left,subRoot.left) and self.issametree(root.right,subRoot.right)
            )
        
   

        """
"I recursively search through the main tree. At each node, I use a helper function to check if the subtree starting at that node is identical to subRoot. If they match, I return true. If they don't, I continue searching the left and right subtrees. The base cases handle when either tree is empty."
If they ask for complexity:
"The time complexity is O(nm), where n is the number of nodes in the main tree and m is the number of nodes in subRoot, because I may compare subRoot against every node in the main tree. The space complexity is O(n + m) in the worst case due to the recursive call stacks."


        """

        
        