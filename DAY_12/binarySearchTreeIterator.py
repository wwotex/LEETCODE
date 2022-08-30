from re import L
from TreeManager import BST

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        next = self.stack.pop()
        
        if next.right:
            self._leftmost_inorder(next.right)

        return next.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


null = None
ls_tree = [7, 3, 15, null, null, 9, 20]
cop = ls_tree.copy()
bst = BST(ls_tree)
obj = BSTIterator(bst.tree)

for el in cop:
    if el is not None:
        print(obj.next())