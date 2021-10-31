from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
https://leetcode.com/problems/path-sum-ii/
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the 
node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
'''
class PathSum2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths = []
        self.findPathSum(root, targetSum, [], allPaths)
        return allPaths

    def findPathSum(self, node, sum, currentPath, allPaths):
        if not node:
            return

        currentPath.append(node.val)

        if sum == node.val and not node.left and not node.right:
            allPaths.append(list(currentPath))
        else:
            self.findPathSum(node.left, sum-node.val, currentPath, allPaths)
            self.findPathSum(node.right, sum - node.val, currentPath, allPaths)

        currentPath.pop()

obj = PathSum2()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(9)
root.right.right = TreeNode(16)
print(obj.pathSum(root, 27))