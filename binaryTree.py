from treeNode import treeNode

class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = treeNode(value)
        else:
            self.root.recursiveInsert(value)

    def print(self):
        if self.root is not None:
            self.root.recursivePrint()

