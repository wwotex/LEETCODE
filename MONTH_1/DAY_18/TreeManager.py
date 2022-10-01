class TreeNode:
    def __init__(self, x, height):
        self.val = x
        self.left = None
        self.right = None
        self.height = height


class BST:
    def __init__(self, ls_tree):
        self.max_height = 0

        if not ls_tree:
            self.tree = None
            return
        
        fifo = []
        self.tree = TreeNode(ls_tree.pop(0), 1)
        fifo.append(self.tree)

        while fifo:
            curr = fifo.pop(0)
            if curr.height > self.max_height:
                self.max_height = curr.height

            temp = None
            if ls_tree:
                temp = ls_tree.pop(0)
                if temp is not None:
                    curr.left = TreeNode(temp, curr.height + 1)
            if ls_tree:
                temp = ls_tree.pop(0)
                if temp is not None:
                    curr.right = TreeNode(temp, curr.height + 1)
            
            if curr.left: fifo.append(curr.left)
            if curr.right: fifo.append(curr.right)
        
        print('created BST')

    def print(self):
        if self.tree is None:
            print('nothing to print')
            return
        init_canvas_width = 2 **(self.max_height + 1)+20
        init_canvas_height = self.max_height + 2
        root_position = 2**(self.max_height)+10
        init_spread = 2**(self.max_height - 1)
        self.tree_canvas = [[' ' for x in range(init_canvas_width)] for y in range(init_canvas_height)]

        self._drawNode(self.tree, 0, root_position, init_spread)
        for el in self.tree_canvas:
            print(''.join(el))

    def _drawNode(self, node, height, position, spread):
        self.tree_canvas[height][position] = str(node.val)
        if node.left: self._drawNode(node.left, height+1, position-spread, int(spread/2))
        if node.right: self._drawNode(node.right, height+1, position+spread, int(spread/2))








