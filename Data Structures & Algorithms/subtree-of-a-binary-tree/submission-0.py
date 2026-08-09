# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        subStack = [subRoot]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                stack.clear()
                stack.append(node)
                break
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        if len(stack) == 0:
            return false

        while stack or subStack:
            if len(stack) != len(subStack):
                return False
            node1 = stack.pop()
            node2 = subStack.pop()
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False
            if node1 and node2 and (node1.val != node2.val):
                return False
            if node1.left:
                stack.append(node1.left)
            if node1.right:
                stack.append(node1.right)
            if node2.left:
                subStack.append(node2.left)
            if node2.right:
                subStack.append(node2.right)

        return True

                




        