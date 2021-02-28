from data_structures.binary_tree.binary_search_tree import BinarySearchTree


class TestBinarySearchTreeInsert:
    def test_initialization(self):
        bst = BinarySearchTree()
        assert isinstance(bst, BinarySearchTree)

    def test_insert_first_element(self):
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.root.key == 5
        assert bst.root.left is None
        assert bst.root.right is None

    def test_insert_element_larger_than_root(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(10)
        assert bst.root.key == 5
        assert bst.root.right.key == 10
        assert bst.root.right.left is None
        assert bst.root.right.right is None
        assert bst.root.left is None

    def test_insert_element_less_than_root(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        assert bst.root.key == 5
        assert bst.root.left.key == 3
        assert bst.root.left.left is None
        assert bst.root.left.right is None
        assert bst.root.right is None

    def test_insert_element_left_and_right_of_root(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(10)
        assert bst.root.key == 5
        assert bst.root.left.key == 3
        assert bst.root.left.left is None
        assert bst.root.left.right is None
        assert bst.root.right.key == 10
        assert bst.root.right.left is None
        assert bst.root.right.right is None

    def test_insert_pathological(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        assert bst.root.key == 1
        assert bst.root.right.key == 2
        assert bst.root.right.right.key == 3
        assert bst.root.right.right.right.key == 4


def tree_factory():
    """
    Build this tree:
          10
        /    \
      5       15
     / \     /  \
    1   7   12  20
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(1)
    bst.insert(7)
    bst.insert(15)
    bst.insert(12)
    bst.insert(20)
    return bst


class TestBinarySearchTreeSearch:
    def setup_method(self):
        self.bst = tree_factory()

    def test_search_for_key_that_does_not_exist(self):
        assert not self.bst.search(100)

    def test_search_for_root(self):
        assert self.bst.search(10)

    def test_search_for_leaf(self):
        assert self.bst.search(20)

    def test_search_for_inner_node(self):
        assert self.bst.search(5)


class TestBinarySearchTreeDelete:
    def setup_method(self):
        self.bst = tree_factory()

    def test_delete_key_that_does_not_exist(self):
        assert not self.bst.delete(100)

    def test_delete_leaf_node(self):
        assert self.bst.delete(20)
        assert self.bst.root.key == 10
        assert self.bst.root.left.key == 5
        assert self.bst.root.left.left.key == 1
        assert self.bst.root.left.right.key == 7
        assert self.bst.root.right.key == 15
        assert self.bst.root.right.left.key == 12
        assert self.bst.root.right.right is None

    def test_delete_inner_node_with_only_left_child(self):
        assert self.bst.delete(20)  # Remove the right child of 15.
        assert self.bst.delete(15)
        assert self.bst.root.key == 10
        assert self.bst.root.left.key == 5
        assert self.bst.root.left.left.key == 1
        assert self.bst.root.left.right.key == 7
        assert self.bst.root.right.key == 12
        assert self.bst.root.right.left is None
        assert self.bst.root.right.right is None

    def test_delete_inner_node_with_only_right_child(self):
        assert self.bst.delete(1)  # Remove the left child of 5
        assert self.bst.delete(5)
        assert self.bst.root.key == 10
        assert self.bst.root.left.key == 7
        assert self.bst.root.left.left is None
        assert self.bst.root.left.right is None
        assert self.bst.root.right.key == 15
        assert self.bst.root.right.left.key == 12
        assert self.bst.root.right.right.key == 20

    def test_delete_inner_node_with_both_children(self):
        assert self.bst.delete(5)
        assert self.bst.root.key == 10
        assert self.bst.root.left.key == 7
        assert self.bst.root.left.left.key == 1
        assert self.bst.root.left.right is None
        assert self.bst.root.right.key == 15
        assert self.bst.root.right.left.key == 12
        assert self.bst.root.right.right.key == 20

    def test_delete_root_node(self):
        assert self.bst.delete(10)
        assert self.bst.root.key == 12
        assert self.bst.root.right.key == 15
        assert self.bst.root.right.right.key == 20
        assert self.bst.root.left.key == 5
        assert self.bst.root.left.left.key == 1
        assert self.bst.root.left.right.key == 7
