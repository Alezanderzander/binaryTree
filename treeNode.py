class treeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def recursiveInsert(self, value):
        if value < self.value:
            print(value, "<", self.value, "-> going left")
            if self.left is None:
                self.left = treeNode(value)
            else:
                # when the value is larger than the one the left to not re-write code reuse the same if statement
                self.left.recursiveInsert(value)
        else:
            print(value, ">=", self.value, "-> going right")
            #do the same on the right
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

    def depthFirst(self, target):
        if target == self.value:
            return self
        if target < self.value:
            if self.left is None:
                return None
            return self.left.depthFirst(target)
        else:
            if self.right is None:
                return None
            return self.right.depthFirst(target)