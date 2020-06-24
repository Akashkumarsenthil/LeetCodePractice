# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        queue = [root,]
        cnt = 0
        while queue:
            cur = queue.pop(0)
            cnt += 1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return cnt
        
