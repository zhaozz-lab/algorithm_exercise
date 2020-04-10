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
        

    
# class binarytree(object):
    # def __init__(self,val=None,left=None,right=None):
        # self.val = val
        # self.left = left
        # self.right = right
    # def traverse(self,root):
        # if root is None:
            # return
        # print(root.val)
        # self.traverse(root.left)
        # self.traverse(root.right)


if __name__ == '__main__':
    # testbinarytree = binarytree(10,binarytree(20),binarytree(30))
    # testbinarytree.traverse(testbinarytree)
    testtree = Tree()
    for i in range(0,10):
        testtree.add(i)
    testtree.trvaverse()