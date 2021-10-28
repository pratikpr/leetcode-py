from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SymmetricTree:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, r1: TreeNode, r2: TreeNode):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False

        return (r1.val == r2.val) and self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)

    def isSymmetricQueue(self, root: Optional[TreeNode]) -> bool:
        return self.isMirrorQ(root)

    def isMirrorQ(self, root: TreeNode):
        queue = []
        queue.append(root)
        queue.append(root)

        while queue:
            r1 = queue.pop(0)
            r2 = queue.pop(0)

            if not r1 and not r2:
                continue
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False

            queue.append(r1.left)
            queue.append(r2.right)
            queue.append(r1.right)
            queue.append(r2.left)

        return True
obj = SymmetricTree()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(9)
root.right.right = TreeNode(16)
print(obj.isSymmetric(root))
print(obj.isSymmetricQueue(root))