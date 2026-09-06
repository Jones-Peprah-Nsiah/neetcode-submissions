# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]

        q=deque([root])

        while q:
            rightside=0
            lenq=len(q)

            for _ in range(lenq):
                node=q.popleft()
                rightside=node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            res.append(rightside)
        return res

            

        """
I use BFS because I need to process the tree level by level. For each level, I keep track of how many nodes are currently in the queue. I process all of them from left to right, and the last node processed is the rightmost node at that level, so I add it to the result.

        """

            
                

            
