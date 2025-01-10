from TreeNode import TreeNode


class Tree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue, None, None)


    def read_fromFile(self, value):
        actual = self.root
        while actual.children is not None or actual.children != []:
