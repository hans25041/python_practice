from data_structures.binary_tree.binary_tree import BinaryTree


class TestBinaryTreeSingleRotation:
    """
    A rotation of a BinaryTree changes the structure of the tree without
    changing the order of the elements. The operation is used to balance
    a BinarySearchTree.
    """
    def setup_method(self):
        """
        Build a tree with this structure

                10
             /     \
            5       15
           / \     /   \
          3   8   12   18
         / \          /  \
        1   4        16   20
        :return:
        """
        root = BinaryTree.Node(10)
        root.left = BinaryTree.Node(5)
        root.left.left = BinaryTree.Node(3)
        root.left.right = BinaryTree.Node(8)
        root.left.left.left = BinaryTree.Node(1)
        root.left.left.right = BinaryTree.Node(4)
        root.right = BinaryTree.Node(15)
        root.right.left = BinaryTree.Node(12)
        root.right.right = BinaryTree.Node(18)
        root.right.right.left = BinaryTree.Node(16)
        root.right.right.right = BinaryTree.Node(20)
        self.tree = BinaryTree(root)

    def test_right_rotate(self):
        """
        Test rotating the subtree starting at 5 to the right.
        i.e.:
            5                      3
           / \                    / \
          3   8      ===>        1   5
         / \                        / \
        1   4                      4   8
        """
        self.tree.right_rotate(self.tree.root.left)
        assert self.tree.root.key == 10
        assert self.tree.root.left.key == 3
        assert self.tree.root.left.left.key == 1
        assert self.tree.root.left.right.key == 5
        assert self.tree.root.left.right.left.key == 4
        assert self.tree.root.left.right.right.key == 8

    def test_left_rotate(self):
        """
        Test rotating the subtree starting at 15 to the left.
        i.e.:
          15                 18
         /   \              /   \
        12   18     ===>   15   20
            /  \          /  \
           16   20       12  16

        """
        self.tree.left_rotate(self.tree.root.right)
        assert self.tree.root.key == 10
        assert self.tree.root.right.key == 18
        assert self.tree.root.right.left.key == 15
        assert self.tree.root.right.right.key == 20
        assert self.tree.root.right.left.left.key == 12
        assert self.tree.root.right.left.right.key == 16


class TestBinaryTreeDoubleRotation:
    """
    A double rotation of a BinaryTree is used in the special case where a node
    has a child to the left which in turn has a child to the right or the
    inverse case where a node has a child to the right which in turn has a
    child to the left. The double rotation will balance this structure.
    """

    def test_double_rotate_left_right(self):
        """
        Test a double rotation with a left-rotate followed by a right-rotate.

        The starting tree is on the left, the result is on the right:
            3              3             2
           /              /             / \
          1     ===>     2     ===>    1   3
           \            /
            2          1
        """
        root = BinaryTree.Node(3)
        root.left = BinaryTree.Node(1)
        root.left.right = BinaryTree.Node(2)
        tree = BinaryTree(root)
        tree.double_rotate_left_right(tree.root)
        assert tree.root.key == 2
        assert tree.root.left.key == 1
        assert tree.root.right.key == 3

    def test_double_rotate_right_left(self):
        """
        Test the double rotation with right-rotate followed by left-rotate.

        The starting tree is on the left, the result is on the right:
           1            1                 2
            \            \               / \
             3   ===>     2     ===>    1   3
            /              \
           2                3
        """
        root = BinaryTree.Node(1)
        root.right = BinaryTree.Node(3)
        root.right.left = BinaryTree.Node(2)
        tree = BinaryTree(root)
        tree.double_rotate_right_left(tree.root)
        assert tree.root.key == 2
        assert tree.root.left.key == 1
        assert tree.root.right.key == 3
