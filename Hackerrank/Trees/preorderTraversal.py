class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

def preOrder(root):
    if root:
        print(root.info,end=" ")
        if root.left:
            preOrder(root.left)
        if root.right:
            preOrder(root.right)
    return


def postOrder(root):
    if root:
        
        if root.left:
            postOrder(root.left)
        if root.right:
            postOrder(root.right)
        print(root.info,end=" ")
    return


def inOrder(root):
    if root:
        
        if root.left:
            inOrder(root.left)
        print(root.info,end=" ")
        if root.right:
            inOrder(root.right)
        
    return

def height(root):
    if root:
        right_length = 0
        left_length = 0
        if root.left:
            left_length = 1 + height(root.left)
        if root.right:
            right_length = 1 + height(root.right)
        return max(right_length,left_length)


def verticalOrder(root,hd,node_map):
    if root:
        if hd in node_map:
            node_map[hd] = node_map[hd] + " " + str(root)
        else:
            node_map[hd] = str(root)
        
        if root.right:
            verticalOrder(root.right,hd+1,node_map)
        elif root.left:
            verticalOrder(root.left,hd-1,node_map)
    return node_map

def printTree(node_map):
    for i in node_map:
        print(i)




q=[]

def levelOrder(root):
    if root:
        print(root.info,end=" ")
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
        
        if len(q) > 0:
            levelOrder(q.pop(0))




    