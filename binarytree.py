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
    
    def add(self,val):
        print("the val is ",val)
        node = Node(val)
        print(val)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            print(queue)
            while queue:
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                elif cur.right is None:
                    cur.right = node
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

        def trvaverse(self):
            if self.root is None:
                return
            print(self.root.val)
            self.traverse(self.left)
            self.traverse(self.right)
        

def isSameTree(tree1,tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.val != tree2.val:
        return False
    return isSameTree(tree1.left,tree2.left) and isSameTree(tree1.right,tree2.right)


if __name__ == '__main__':
    # testbinarytree = binarytree(10,binarytree(20),binarytree(30))
    # testbinarytree.traverse(testbinarytree)
    tree1 = Tree()
    tree1.add(100)
    tree1.traverse()
    for i in range(0,10):
       tree1.add(i)
    # test traverse   
    tree1.trvaverse()
    # test isSameTree
    # tree2 = tree1
    # print(isSameTree(tree1,tree2))