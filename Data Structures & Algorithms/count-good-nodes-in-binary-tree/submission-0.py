# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 1
        stack = [(root, root.val)]

        while stack:
            node, curMax = stack.pop()
            if node.left:
                if curMax <= node.left.val:
                    result +=1
                    curMax = node.left.val
                stack.append((node.left, curMax))
            if node.right:
                if curMax <= node.right.val:
                    result +=1
                    curMax = node.right.val
                stack.append((node.right, curMax))
        
        return result