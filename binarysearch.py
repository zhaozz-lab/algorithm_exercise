class Node(object):
    """docstring for Node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    """docstring for Tree"""
    def __init__(self):
        self.root = None
 

def insertIntoBST(root,val):
    if root == None:
        return Node(val)
    if root.val < val:
        root.right = insertIntoBST(root.right,val)
    if root.val > val:
        root.left = insertIntoBST(root.left,val)
    return root

def traverse(root):
    if root is None:
        return
    print(root.val)
    traverse(root.left)
    traverse(root.right)
def isValidBST1(root,treemin,treemax):
    if root is None:
        return True
    if treemin != None and root.val < treemin.val:
        return False
    if treemax != None and root.val > treemax.val:
        return False
    return isValidBST1(root.left,treemin,root) and isValidBST1(root.right,root,treemax)
def isValidBST(root):
    return isValidBST1(root,None,None)

def isInBST(root,target):
    if root is None:
        return False
    if root.val < target:
        return isInBST(root.right,target)
    if root.val >target:
        return isInBST(root.left,target)
def getMin(node):
    while node.left is not None:
        node = node.left
    return node

def deleteNode(root,key):
    # print(root.val)
    # print("the key is",key )
    if root is None:
        return None
    # print(root.val)
    if root.val == key:
        # print("the start",root.val)
        # print("the root left is",root.left)
        if root.left is None:
            return root.right
        print(root.val)
        if root.right is None:
            return root.left
        print(root.val)
        minNode = getMin(root.right)
        root.val = minNode.val
        print(root.val)
        root.right = deleteNode(root.right,minNode.val)
    elif root.val > key:
        root.left = deleteNode(root.left,key)
    elif root.val < key:
        root.right = deleteNode(root.right,key)

    return root
if __name__ == '__main__':
    root = Node(1)
    insertIntoBST(root,2)
    insertIntoBST(root,3)
    traverse(root)
    print(isValidBST(root))
    print(isInBST(root,10))
    print("the traverse root is ")
    traverse(root)
    print("delete the node 1")
    deleteNode(root,3)
    print("delete the node 1")
    traverse(root)