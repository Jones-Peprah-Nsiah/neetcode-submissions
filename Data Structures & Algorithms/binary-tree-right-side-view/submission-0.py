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

        q=deque([root])
        res=[]

        while q:
            rightside=None
            qlen=len(q)
            for _ in range(qlen):
                node=q.popleft()
                rightside=node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            res.append(rightside)
        return res

            

