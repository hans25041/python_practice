from data_structures.binary_tree.binary_search_tree import BinarySearchTree


class RedBlackTree(BinarySearchTree):

    def rbt_insert(self, item, node=None):
        item = super().insert(item, node)
        if not self._recolor(item):
            self._rotate(item)

    def rbt_delete(self, item):
        child = self._get_child(item)
        item_color = item.color
        item.replace(child)
        self._rebalance_deletion(item_color, child)

    def _rebalance_deletion(self, item_color, child):
        red = RedBlackTree.Node.RED
        black = RedBlackTree.Node.BLACK
        double_black = RedBlackTree.Node.DOUBLE_BLACK

        item_red = item_color == red
        item_black = item_color == black

        if item_red or child.is_red():
            child.color = black
            return True

        elif item_black and child.is_black():
            if child is self.root:
                child.color = black
                return True

            child.color = double_black
            sibling = self._get_sibling(child)

            if self._black_with_red_child(sibling):
                if sibling is sibling.parent.right and sibling.right and sibling.right.is_red():
                    self.left_rotate(sibling.parent)
                    sibling.right.color = black
                elif sibling is sibling.parent.right and sibling.left.is_red():
                    parent = sibling.parent
                    self.right_rotate(sibling)
                    self.left_rotate(parent)
                elif sibling is sibling.parent.left and sibling.left and sibling.left.is_red():
                    self.right_rotate(sibling.parent)
                    sibling.left.color = black
                elif sibling is sibling.parent.left and sibling.right.is_red():
                    parent = sibling.parent
                    self.left_rotate(sibling)
                    self.right_rotate(parent)
                return True
            elif self._black_without_red_child(sibling):
                u = child
                while u.is_double_black():
                    if u is self.root:
                        u.color = black
                        return True
                    elif u.parent.is_red():
                        u.parent.color = black
                        u.color = black
                        return True
                    else:
                        u.color = black
                        u.parent.color = double_black
                        u = u.parent
                raise Exception("Should never get here.")
            elif sibling.is_red():
                if sibling.parent and sibling is sibling.parent.left:
                    self.right_rotate(sibling)
                    sibling.color = black
                    sibling.right.color = red
                    return True
                elif sibling.parent and sibling is sibling.parent.right:
                    self.left_rotate(sibling)
                    sibling.color = black
                    sibling.left.color = red
                    return True

            raise NotImplementedError

    @staticmethod
    def _get_child(item):
        child = RedBlackTree.Node(None)
        child.parent = item
        child.color = RedBlackTree.Node.BLACK
        if item.left:
            child = item.left
        elif item.right:
            child = item.right
        return child

    @staticmethod
    def _get_sibling(node):
        sibling = RedBlackTree.Node(None)
        if node.sibling:
            sibling = node.sibling
        return sibling

    @staticmethod
    def _black_with_red_child(sibling):
        if sibling.is_red():
            return False
        return (
            (sibling.left and sibling.left.is_red()) or
            (sibling.right and sibling.right.is_red())
         )

    @staticmethod
    def _black_without_red_child(sibling):
        if sibling.is_red():
            return False
        return (
                (not sibling.left or sibling.left.is_black()) and
                (not sibling.right or sibling.right.is_black())
        )

    def _recolor(self, item) -> bool:
        black = RedBlackTree.Node.BLACK
        red = RedBlackTree.Node.RED
        if item is self.root:
            item.color = black
            return True
        elif item.parent.is_black():
            return True
        elif item.parent.is_red() and item.parent.sibling and item.parent.sibling.is_red():
            item.parent.color = black
            item.parent.sibling.color = black
            item.grandparent.color = red
            return self._recolor(item.grandparent)
        else:
            return False

    def _rotate(self, item):
        if self._is_left_left_node(item):
            tmp = item.parent.color
            item.parent.color = item.grandparent.color
            item.grandparent.color = tmp
            self.right_rotate(item.grandparent)
            return True
        elif self._is_right_right_node(item):
            tmp = item.parent.color
            item.parent.color = item.grandparent.color
            item.grandparent.color = tmp
            self.left_rotate(item.grandparent)
            return True
        elif self._is_left_right_node(item):
            parent_node = item.parent
            self.left_rotate(parent_node)
            self._rotate(parent_node)
            return True
        elif self._is_right_left_node(item):
            parent_node = item.parent
            self.right_rotate(parent_node)
            self._rotate(parent_node)
            return True
        raise NotImplementedError

    @staticmethod
    def _is_left_left_node(item):
        return (
            item.grandparent and item.parent is item.grandparent.left and
            item.parent and item is item.parent.left
        )

    @staticmethod
    def _is_right_right_node(item):
        return (
            item.grandparent and item.parent is item.grandparent.right and
            item.parent and item is item.parent.right
        )

    @staticmethod
    def _is_left_right_node(item):
        return (
            item.grandparent and item.parent is item.grandparent.left and
            item.parent and item is item.parent.right
        )

    @staticmethod
    def _is_right_left_node(item):
        return (
            item.grandparent and item.parent is item.grandparent.right and
            item.parent and item is item.parent.left
        )

    class Node(BinarySearchTree.Node):
        BLACK = "BLACK"
        RED = "RED"
        DOUBLE_BLACK = "DOUBLE_BLACK"
        colors = (BLACK, RED, DOUBLE_BLACK)

        def __init__(self, key, left=None, right=None):
            super().__init__(key=key, left=left, right=right)
            self.color = RedBlackTree.Node.RED

        @property
        def color(self):
            return self._color

        @color.setter
        def color(self, color):
            if color not in self.colors:
                raise ValueError("Color must be RED or BLACK.")
            self._color = color

        def is_red(self):
            return self.color == RedBlackTree.Node.RED

        def is_black(self):
            return self.color == RedBlackTree.Node.BLACK

        def is_double_black(self):
            return self.color == RedBlackTree.Node.DOUBLE_BLACK
