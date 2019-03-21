
# ---------------------------------------------- BINARY TREE----------------------------------------------------------

# Structure of a Basic Binary Tree Node


class Binary_tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def Pre_Order_Traversal(self, start, Resultant_string):
        if start:
            Resultant_string += str(start.data)+"-"
            Resultant_string = self.Pre_Order_Traversal(
                start.left, Resultant_string)
            Resultant_string = self.Pre_Order_Traversal(
                start.right, Resultant_string)
        return Resultant_string

    def InOrder_Traversal(self, start, Resultant_string):
        if start:
            Resultant_string = self.InOrder_Traversal(
                start.left, Resultant_string)
            Resultant_string += str(start.data)+"-"
            Resultant_string = self.InOrder_Traversal(
                start.right, Resultant_string)
        return Resultant_string

    def PostOrder_Traversal(self, start, Resultant_string):
        if start:
            Resultant_string = self.PostOrder_Traversal(
                start.left, Resultant_string)

            Resultant_string = self.PostOrder_Traversal(
                start.right, Resultant_string)
            Resultant_string += str(start.data)+"-"
        return Resultant_string


Rootnode = Binary_tree_node(5)
Tree = BinaryTree(Rootnode)
Tree.root.left = Binary_tree_node(6) 
Tree.root.left.left = Binary_tree_node(7)
Tree.root.left.right = Binary_tree_node(10)
Tree.root.right = Binary_tree_node(21)

print("PreOrder Traversal is "+Tree.Pre_Order_Traversal(Tree.root, "")[:-1])
print("InOrder Traversal is "+Tree.InOrder_Traversal(Tree.root, "")[:-1])
print("PostOrder Traversal is "+Tree.PostOrder_Traversal(Tree.root, "")[:-1])
