from data_structures.binary_tree.red_black_tree import RedBlackTree
from data_structures.binary_tree.binary_search_tree import BinarySearchTree
from data_structures.binary_tree.binary_tree import BinaryTree


RED = RedBlackTree.Node.RED
BLACK = RedBlackTree.Node.BLACK


class TestRedBlackTreeInsert:
    def test_initialization(self):
        rbt = RedBlackTree()
        assert isinstance(rbt, RedBlackTree)
        assert isinstance(rbt, BinarySearchTree)
        assert isinstance(rbt, BinaryTree)

    def test_insert_root_into_red_black_tree(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        assert rbt.root.key == 20
        assert rbt.root.is_black()

    def test_insert_a_second_node_to_left(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(10))
        assert rbt.root.key == 20
        assert rbt.root.is_black()
        assert rbt.root.left.key == 10
        assert rbt.root.left.is_red()

    def test_insert_a_second_node_to_right(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(30))
        assert rbt.root.key == 20
        assert rbt.root.is_black()
        assert rbt.root.right.key == 30
        assert rbt.root.right.is_red()

    def test_insert_nodes_to_left_and_right(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(10))
        rbt.rbt_insert(RedBlackTree.Node(30))
        assert rbt.root.key == 20
        assert rbt.root.is_black()
        assert rbt.root.left.key == 10
        assert rbt.root.left.is_red()
        assert rbt.root.right.key == 30
        assert rbt.root.right.is_red()

    def test_insert_two_nodes_to_the_right(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(10))
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(40))
        assert rbt.root.key == 20
        assert rbt.root.is_black()
        assert rbt.root.left.key == 10
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 30
        assert rbt.root.right.is_black()
        assert rbt.root.right.right.key == 40
        assert rbt.root.right.right.is_red()

    def test_force_right_rotate(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(10))
        rbt.rbt_insert(RedBlackTree.Node(5))
        assert rbt.root.key == 10
        assert rbt.root.is_black()
        assert rbt.root.left.key == 5
        assert rbt.root.left.is_red()
        assert rbt.root.right.key == 20
        assert rbt.root.right.is_red()

    def test_force_left_rotate(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(40))
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_red()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_red()

    def test_force_double_rotate_left_then_right(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(10))
        rbt.rbt_insert(RedBlackTree.Node(15))
        assert rbt.root.key == 15
        assert rbt.root.is_black()
        assert rbt.root.left.key == 10
        assert rbt.root.left.is_red()
        assert rbt.root.right.key == 20
        assert rbt.root.right.is_red()

    def test_force_double_rotate_right_then_left(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(25))
        assert rbt.root.key == 25
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_red()
        assert rbt.root.right.key == 30
        assert rbt.root.right.is_red()


class TestRedBlackTreeDeleteWhenItemOrChildIsRed:

    def four_node_factory(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(40))
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(10))
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()
        assert rbt.root.left.left.key == 10
        assert rbt.root.left.left.is_red()
        return rbt

    def test_delete_black_node_with_red_child(self):
        rbt = self.four_node_factory()
        rbt.rbt_delete(rbt.root.left)
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 10
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()

    def test_delete_red_node_with_black_child(self):
        rbt = self.four_node_factory()
        rbt.root.left.color = RedBlackTree.Node.RED
        rbt.root.left.left.color = RedBlackTree.Node.BLACK

        rbt.rbt_delete(rbt.root.left)
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 10
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()


class TestRedBlackTreeDeleteWhenItemAndChildAreBlackSiblingBlackWithRedChild:
    def test_left_left_case(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(40))
        rbt.rbt_insert(RedBlackTree.Node(15))
        rbt.rbt_insert(RedBlackTree.Node(25))
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_black()
        assert rbt.root.left.left.key == 15
        assert rbt.root.left.left.is_red()
        assert rbt.root.left.right.key == 25
        assert rbt.root.left.right.is_red()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()

        rbt.rbt_delete(rbt.root.right)
        assert rbt.root.key == 20
        assert rbt.root.is_black()
        assert rbt.root.left.key == 15
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 30
        assert rbt.root.right.is_black()
        assert rbt.root.right.left.key == 25
        assert rbt.root.right.left.is_red()

    def test_left_right_case(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(40))
        rbt.rbt_insert(RedBlackTree.Node(25))
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_black()
        assert rbt.root.left.right.key == 25
        assert rbt.root.left.right.is_red()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()

        rbt.rbt_delete(rbt.root.right)
        assert rbt.root.key == 25
        # assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        # assert rbt.root.left.is_black()
        assert rbt.root.right.key == 30
        # assert rbt.root.right.is_black()

    def test_right_right_case(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(40))
        rbt.rbt_insert(RedBlackTree.Node(35))
        rbt.rbt_insert(RedBlackTree.Node(50))
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()
        assert rbt.root.right.left.key == 35
        assert rbt.root.right.left.is_red()
        assert rbt.root.right.right.key == 50
        assert rbt.root.right.right.is_red()

        rbt.rbt_delete(rbt.root.left)
        assert rbt.root.key == 40
        assert rbt.root.is_black()
        assert rbt.root.left.key == 30
        assert rbt.root.left.is_black()
        assert rbt.root.left.right.key == 35
        assert rbt.root.left.right.is_red()
        assert rbt.root.right.key == 50
        assert rbt.root.right.is_black()

    def test_right_left_case(self):
        rbt = RedBlackTree()
        rbt.rbt_insert(RedBlackTree.Node(30))
        rbt.rbt_insert(RedBlackTree.Node(20))
        rbt.rbt_insert(RedBlackTree.Node(40))
        rbt.rbt_insert(RedBlackTree.Node(35))
        assert rbt.root.key == 30
        assert rbt.root.is_black()
        assert rbt.root.left.key == 20
        assert rbt.root.left.is_black()
        assert rbt.root.right.key == 40
        assert rbt.root.right.is_black()
        assert rbt.root.right.left.key == 35
        assert rbt.root.right.left.is_red()

        rbt.rbt_delete(rbt.root.left)
        assert rbt.root.key == 35
        # assert rbt.root.is_black()
        assert rbt.root.left.key == 30
        # assert rbt.root.left.is_black()
        assert rbt.root.right.key == 40
        # assert rbt.root.right.is_black()


class TestRedBlackTreeNode:
    def test_initialization(self):
        node = RedBlackTree.Node(20)
        assert isinstance(node, RedBlackTree.Node)
        assert node.is_red()

    def test_can_change_from_red_to_black_and_back(self):
        node = RedBlackTree.Node(20)
        assert node.is_red()
        node.color = BLACK
        assert node.is_black()
        node.color = RED
        assert node.is_red()
