class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # INSERT HELPER FUNCTION
    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node
    # INSERT ESSENTIAL FUNCTION
    def insert(self, value):
        self.root = self._insert(self.root, value)
    # CHECK TREE WITH VISUALISATION HELPER FUNCTION
    def _toNestedList(self, node):
        if node is None:
            return None
        left_subtree = self._toNestedList(node.left)
        right_subtree = self._toNestedList(node.right)
        nested_list = [node.value]
        if left_subtree is not None:
            nested_list.append(left_subtree)
        else: pass
        if right_subtree is not None:
            nested_list.append(right_subtree)
        else: pass
        return nested_list
    # CHECK TREE WITH VISUALISATION ESSENTIAL FUNCTION
    def toNestedList(self):
        return self._toNestedList(self.root)
    # SEARCH HELPER FUNCTION
    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
    # SEARCH ESSENTIAL FUNCTION
    def search(self, value):
        return self._search(self.root, value)
    # DELETE HELPER FUNCTION MINIMUM VALUE
    def _minimum_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value
    # DELETE HELPER FUNCTION
    def _delete(self, node, value):
        if node is None:
            return node
        elif value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.value = self._minimum_value(node.right)
                node.right = self._delete(node.right, node.value)
        return node
    # DELETE ESSENTIAL FUNCTION
    def delete(self, value):
        self.root = self._delete(self.root, value)
    # INORDER TRAVERSAL HELPER FUNCTION
    def _inorderTraversal(self, node, result):
        if node:
            self._inorderTraversal(node.left, result)
            result.append(node.value)
            self._inorderTraversal(node.right, result)
        else: pass
    # INORDER TRAVERSAL ESSENTIAL FUNCTION
    def inorderTraversal(self):
        result = []
        self._inorderTraversal(self.root, result)
        return result
if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    node_set = [53, 20, 50, 110, 70, 130, 170]
    for node in node_set:
        binary_search_tree.insert(node)
    print(f"\nTREE VISUALISATION\n{binary_search_tree.toNestedList()}")
    print(f"\nTREE VISUALISATION")