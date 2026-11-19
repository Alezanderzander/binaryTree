class treeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def recursiveInsert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = treeNode(value)
            else:
                self.left.recursiveInsert(value)
        else:
            if self.right is None:
                self.right = treeNode(value)
            else:
                self.right.recursiveInsert(value)

    def recursivePrint(self):
        if self.left is not None:
            self.left.recursivePrint()
        print(self.value)
        if self.right is not None:
            self.right.recursivePrint()