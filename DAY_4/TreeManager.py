class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self, ls_tree):
        # null = None
        fifo = []
        self.tree = TreeNode(ls_tree.pop(0))
        fifo.append(self.tree)

        while fifo:
            curr = fifo.pop(0)
            
            temp = None
            if ls_tree:
                temp = ls_tree.pop(0)
                if temp is not None:
                    curr.left = TreeNode(temp)
            if ls_tree:
                temp = ls_tree.pop(0)
                if temp is not None:
                    curr.right = TreeNode(temp)
            
            if curr.left: fifo.append(curr.left)
            if curr.right: fifo.append(curr.right)
        
        print('created BST')

    def print(self):
        init_canvas_width = 60
        init_canvas_height = 20
        root_position = 30
        self.tree_canvas = [[' ' for x in range(init_canvas_width)] for y in range(init_canvas_height)]

        self._drawNode(self.tree, 0, root_position, 8)
        for el in self.tree_canvas:
            print(''.join(el))

    def _drawNode(self, node, height, position, spread):
        self.tree_canvas[height][position] = str(node.val)
        if node.left: self._drawNode(node.left, height+1, position-spread+1, int(spread/2))
        if node.right: self._drawNode(node.right, height+1, position+spread-1, int(spread/2))








