from functools import partial

from data_structures.binary_tree.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    def insert(self, item, node=None, root_checked=False):
        key, item = self._get_key_and_item(item)

        if not self.root:
            self.root = item
            return item

        node = self._get_node(node, root_checked)
        if not node:
            raise Exception("Should never get here.")

        target, set_target = self._get_target_and_setter(key, node)

        if target is None or target.key == key:
            set_target(item)
            return item
        else:
            return self.insert(item, target, root_checked=True)

    def search(self, key, node=None, root_checked=False):
        node = self._get_node(node, root_checked)
        if not node:
            return None
        elif key == node.key:
            return node

        target, _ = self._get_target_and_setter(key, node)

        return self.search(key, target, root_checked=True)

    def delete(self, key):
        node = self.search(key)
        if not node:
            return False
        if node.is_leaf():
            if node is self.root:
                self.root = None
            else:
                node.remove()
            return True
        if node.left and not node.right:
            if node is self.root:
                self.root = node.left
            else:
                node.replace(node.left)
            return True
        if node.right and not node.left:
            if node is self.root:
                self.root = node.right
            else:
                node.replace(node.right)
            return True
        if node.right and node.left:
            successor = node.in_order_successor()
            new_node = BinaryTree.Node(successor.key, node.left, node.right)
            if node is self.root:
                self.root = new_node
            else:
                node.replace(new_node)
            successor.remove()
            return True
        raise Exception("Should never get here.")

    def _remove_target(self, target, set_target):
        left, right = target.children
        set_target(None)
        if right:
            self.insert(right)
        if left:
            self.insert(left)

    def _get_target_and_setter(self, key, node):
        target = None
        target_name = None
        if key == node.key and node == self.root:
            node = self
            target = self.root
            target_name = "root"
        elif key < node.key:
            target = node.left
            target_name = "left"
        elif key > node.key:
            target = node.right
            target_name = "right"

        set_target = partial(node.__setattr__, target_name)

        return target, set_target

    def _get_node(self, node, root_checked):
        if node:
            return node
        elif not node and not root_checked:
            return self.root

    @staticmethod
    def _get_key_and_item(item):
        if isinstance(item, BinaryTree.Node):
            key = item.key
        else:
            key = item
            item = BinaryTree.Node(key)
        return key, item
