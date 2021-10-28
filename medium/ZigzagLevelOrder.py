from collections import deque
from typing import Optional, List

'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ZigzagLevelOrder:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []
        if not root:
            return queue

        ltr = 1
        queue.append(root)
        while len(queue) != 0:
            size = len(queue)
            level = []

            for i in range(0, size):
                node = queue.pop(0)
                if ltr == 1:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    # if ltr == 1:
                    queue.append(node.left)
                    # else:
                        # queue.insert(0, node.left)
                if node.right:
                    # if ltr == 1:
                        queue.append(node.right)
                    # else:
                    #     queue.insert(0, node.right)
            ltr *= -1
            res.append(level)
        return res

    def zigzagLevelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []

        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level + 1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results

obj = ZigzagLevelOrder()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)
print(obj.zigzagLevelOrder(root))
print(obj.zigzagLevelOrderDFS(root))