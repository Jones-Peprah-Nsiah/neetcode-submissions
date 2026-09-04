# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        
        def dfs(root):
            if not root:
                return 0

            leftMax=dfs(root.left)
            rightMax=dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)


            res[0]=max(res[0], root.val+rightMax+leftMax)
            return root.val+max(rightMax,leftMax)
        
        dfs(root)
        return res[0]

        
        
        
        
        
        
        
        
        
        
        
        
        """I’ll use DFS to calculate the maximum path sum for each subtree.
For each node, I first recursively get the best path from its left and right children. If either path is negative, I ignore it because including a negative path would only decrease the sum.
Then I calculate the maximum path that passes through the current node:
leftMax + root.val + rightMax
This path can use both children, so I use it to update my global result.
However, when returning a value to the parent, I can only return one side because a path cannot split. So I return:
root.val + max(leftMax, rightMax)
I repeat this for every node, and the global result gives me the maximum path sum.”
        """