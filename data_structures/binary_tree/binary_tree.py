class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def empty(self):
        return not self.root

    def right_rotate(self, node):
        parent = node.parent
        old_node = node
        new_node = node.left
        old_node.left = new_node.right
        new_node.right = old_node
        if parent and node is parent.left:
            parent.left = new_node
        elif parent and node is parent.right:
            parent.right = new_node
        else:
            self.root = new_node

    def left_rotate(self, node):
        parent = node.parent
        old_node = node
        new_node = node.right
        old_node.right = new_node.left
        new_node.left = old_node
        if parent and node is parent.left:
            parent.left = new_node
        elif parent and node is parent.right:
            parent.right = new_node
        else:
            self.root = new_node

    def double_rotate_left_right(self, node):
        self.left_rotate(node.left)
        self.right_rotate(node)

    def double_rotate_right_left(self, node):
        self.right_rotate(node.right)
        self.left_rotate(node)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._raise_exception_if_root_is_not_node(node)
        self._root = node

    @staticmethod
    def _raise_exception_if_root_is_not_node(node):
        if node is not None and not isinstance(node, BinaryTree.Node):
            raise BinaryTree.RootMustBeBinaryTreeNodeException

    class RootMustBeBinaryTreeNodeException(Exception):
        """Raised when a root is assigned that is not a BinaryTree.Node."""

    class Node:
        def __init__(self, key=None, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.parent = None

        def __repr__(self):
            return f"BinaryTree.Node(key={self.key!r}, left={self.left.key!r}, right={self.right.key!r}"

        def remove(self):
            self.replace(None)

        def replace(self, node):
            if self.parent:
                if self is self.parent.left:
                    self.parent.left = node
                else:
                    self.parent.right = node

        def in_order_successor(self):
            candidate = self.right
            if not candidate:
                return None
            while candidate.left:
                candidate = candidate.left
            return candidate

        def is_leaf(self):
            return self.left is None and self.right is None

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, node):
            self._raise_exception_if_node_is_invalid(node)
            self._parent = node

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, node):
            self._raise_exception_if_node_is_invalid(node)
            if node:
                node.parent = self
            self._left = node

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, node):
            self._raise_exception_if_node_is_invalid(node)
            if node:
                node.parent = self
            self._right = node

        @property
        def children(self):
            return self.left, self.right

        @property
        def sibling(self):
            if not self.parent:
                return None
            elif self is self.parent.left:
                return self.parent.right
            else:
                return self.parent.left

        @property
        def grandparent(self):
            if not self.parent:
                return None
            return self.parent.parent

        @staticmethod
        def _raise_exception_if_node_is_invalid(node):
            if node is not None and not isinstance(node, BinaryTree.Node):
                raise BinaryTree.Node.ChildMustBeNodeException

        class ChildMustBeNodeException(Exception):
            """Raised when assigning an invalid value to a child."""
