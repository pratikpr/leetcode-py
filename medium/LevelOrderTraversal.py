from typing import Optional, List
'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LevelOrder:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []
        if not root:
            return res
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for i in range(0,size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

obj = LevelOrder()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)
print(obj.levelOrder(root))
