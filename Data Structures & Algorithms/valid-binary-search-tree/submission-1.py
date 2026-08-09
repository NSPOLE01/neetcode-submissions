# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, leftBound, rightBound = stack.pop()
            if node.right:
                rightBound = node.right.val
                if not (leftBound < node.right.val <= rightBound):
                    return False
                stack.append((node.right, node.val, node.right.val))
            if node.left:
                leftBound = node.left.val
                if not (leftBound <= node.left.val < node.val):
                    return False
                stack.append((node.left, node.left.val, node.val))

        return True
        