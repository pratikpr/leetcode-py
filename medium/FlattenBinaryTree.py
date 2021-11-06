from typing import Optional
'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list 
and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FlattenBinaryTree:
    def flattenTree(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        leftTail = self.flattenTree(root.left)
        rightTail = self.flattenTree(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        return rightTail if rightTail else leftTail

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.flattenTree(root)

obj = FlattenBinaryTree()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)
print(obj.flattenTree(root))
