
class TreeNode():
    def __init__(self, payload, left=None, right=None):
        self.payload = payload
        self.left = left
        self.right = right
        
class BinaryTree():
    def __init__(self, payload):
        self.root = TreeNode(payload=payload)
    
    def insert(self, payload):
        return self._insert(node=self.root, payload=payload)
        
    def _insert(self, node: TreeNode, payload):
        if payload < node.payload:
            if not node.left:
                node.left = TreeNode(payload=payload)
                return True
        
        if not node.right:
            node.right = TreeNode(payload=payload)
            return True
        self._insert(node.right, payload)
        
    def print_tree(self):
        self._print_tree(self.root)
        
    def _print_tree(self, node: TreeNode):
        if node.left:
            self._print_tree(node.left)
            
        print(node.payload)
        
        if node.right:
            self._print_tree(node.right)
        
        
tree = BinaryTree(50)
tree.insert(60)
tree.insert(40)
tree.print_tree()
