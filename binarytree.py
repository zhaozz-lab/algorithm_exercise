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
            # print(queue)
            while queue:
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

    # def traverse(self,root):
    #     if root is None:
    #         return
    #     print(root.val)
    #     self.traverse(root.left)
    #     self.traverse(root.right)
        
def traverse(root):
    if root is None:
        return
    print(root.val)
    traverse(root.left)
    traverse(root.right)


def isSameTree(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)


if __name__ == '__main__':
    # testbinarytree = binarytree(10,binarytree(20),binarytree(30))
    # testbinarytree.traverse(testbinarytree)
    tree1 = Tree()
    # tree1.add(100)
    # tree1.traverse()
    for i in range(0,10):
       tree1.add(i)
    # test traverse   
    traverse(tree1.root)
    # test isSameTree
    tree2 = tree1
    traverse(tree2.root)
    print(isSameTree(tree1.root,tree2.root))