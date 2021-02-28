from pytest import raises

from data_structures.binary_tree.binary_tree import BinaryTree


class TestBinaryTree:
    def test_initialization(self):
        tree = BinaryTree()
        assert isinstance(tree, BinaryTree)

    def test_initialized_tree_is_empty(self):
        tree = BinaryTree()
        assert tree.empty()

    def test_initialized_with_root_not_empty(self):
        root = BinaryTree.Node(0)
        tree = BinaryTree(root)
        assert not tree.empty()

    def test_access_root_data(self):
        root = BinaryTree.Node(0)
        tree = BinaryTree(root)
        assert tree.root.key == 0

    def test_root_must_be_node(self):
        with raises(BinaryTree.RootMustBeBinaryTreeNodeException):
            BinaryTree(0)

    def test_build_binary_tree(self):
        """
        Build a tree of the following structure:
            j    <-- root
           / \
          f   k
         / \   \
        a   h   z    <-- leaves
        """
        node = BinaryTree.Node
        j_node = node("j")
        f_node = node("f")
        k_node = node("k")
        a_node = node("a")
        h_node = node("h")
        z_node = node("z")

        tree = BinaryTree(j_node)
        j_node.left = f_node
        j_node.right = k_node
        f_node.left = a_node
        f_node.right = h_node
        k_node.right = z_node

        assert tree.root.key == "j"
        assert tree.root._left.key == "f"
        assert tree.root._right.key == "k"
        assert tree.root._left._left.key == "a"
        assert tree.root._left._left.is_leaf()
        assert tree.root._left._right.key == "h"
        assert tree.root._left._right.is_leaf()
        assert tree.root._right._right.key == "z"
        assert tree.root._right._right.is_leaf()


class TestBinaryTreeNode:
    def test_initialization(self):
        node = BinaryTree.Node()
        assert isinstance(node, BinaryTree.Node)
        assert not node.key
        assert not node.left
        assert not node.right

    def test_initialization_with_data(self):
        node = BinaryTree.Node(0)
        assert node.key == 0
        assert not node.left
        assert not node.right

    def test_initialization_with_left_node(self):
        left_node = BinaryTree.Node(1)
        node = BinaryTree.Node(0, left_node)
        assert node.key == 0
        assert node.left == left_node
        assert node.left.key == 1
        assert not node.left._left
        assert not node.left._right
        assert not node.right

    def test_initialization_with_right_node(self):
        right_node = BinaryTree.Node(1)
        node = BinaryTree.Node(0, right=right_node)
        assert node.key == 0
        assert node.right == right_node
        assert node.right.key == 1
        assert not node.right._left
        assert not node.right._right
        assert not node.left

    def test_initialization_with_left_and_right_node(self):
        left_node = BinaryTree.Node(1)
        right_node = BinaryTree.Node(2)
        node = BinaryTree.Node(0, left_node, right_node)
        assert node.key == 0

        assert node.left == left_node
        assert node.left.key == 1
        assert not node.left._left
        assert not node.left._right

        assert node.right == right_node
        assert node.right.key == 2
        assert not node.right._left
        assert not node.right._right

    def test_left_must_be_a_node(self):
        with raises(BinaryTree.Node.ChildMustBeNodeException):
            BinaryTree.Node(0, left=0)

    def test_right_must_be_a_node(self):
        with raises(BinaryTree.Node.ChildMustBeNodeException):
            BinaryTree.Node(0, right=0)

    def test_node_with_left_and_right_is_not_leaf(self):
        left_node = BinaryTree.Node(1)
        right_node = BinaryTree.Node(2)
        node = BinaryTree.Node(0, left_node, right_node)
        assert not node.is_leaf()

    def test_node_with_left_but_not_right_is_not_leaf(self):
        left_node = BinaryTree.Node(1)
        node = BinaryTree.Node(0, left_node)
        assert not node.is_leaf()

    def test_node_with_right_but_not_left_is_not_leaf(self):
        right_node = BinaryTree.Node(2)
        node = BinaryTree.Node(0, right=right_node)
        assert not node.is_leaf()

    def test_node_with_neither_left_nor_right_is_leaf(self):
        node = BinaryTree.Node(0)
        assert node.is_leaf()
