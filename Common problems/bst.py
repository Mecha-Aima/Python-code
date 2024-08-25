class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        # Recursive function to insert a key into the tree
        if node is None:
            # If the node is None, create a new TreeNode with the given key
            return TreeNode(key)

        if key < node.key:
            # If the key is less than the current node's key, insert it into the left subtree
            node.left = self._insert(node.left, key)
        elif key > node.key:
            # If the key is greater than the current node's key, insert it into the right subtree
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        # Public method to insert a key into the tree
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        # Recursive function to search for a key in the tree
        if node is None or node.key == key:
            # If the node is None or the key is found, return the node
            return node
        if key < node.key:
            # If the key is less than the current node's key, search in the left subtree
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        # Public method to search for a key in the tree
        return self._search(self.root, key)

    def _delete(self, node, key):
        # Recursive function to delete a key from the tree
        if node is None:
            # If the node is None, return None
            return node
        if key < node.key:
            # If the key is less than the current node's key, delete it from the left subtree
            node.left = self._delete(node.left, key)
        elif key > node.key:
            # If the key is greater than the current node's key, delete it from the right subtree
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                # If the node has no left child, replace it with its right child
                return node.right
            elif node.right is None:
                # If the node has no right child, replace it with its left child
                return node.left   
            
            # If the node has both left and right children, replace it with the minimum value from the right subtree
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        
        return node

    def delete(self, key):
        # Public method to delete a key from the tree
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        # Helper function to find the minimum value in a subtree
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        # Recursive function to perform an inorder traversal of the tree
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        # Public method to perform an inorder traversal of the tree
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))
print("Inorder traversal:", bst.inorder_traversal())
bst.delete(40)
print("Search for 40:", bst.search(40))