class TreeNode(object):
    def __init__(self,value = None,left = None,right = None):
        self.val = value
        self.left = left
        self.right = right
    def traverse(self,root):
        if root is None:
            return
        print(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


if __name__ == '__main__':
    testTreeNode = TreeNode(10,TreeNode(20),TreeNode(30))
    testTreeNode.traverse(testTreeNode)
    def quicksort(b):
        if len(b)<2:
            return b
        mid = b[len(b)//2]
        b.pop(len(b)//2)
        left = []
        right= []
        for item in b:
            if item >= mid:
                right.append(item)
            else:
                left.append(item)
        return quicksort(left) + mid + quicksort(right)
    def findk(b,k):
        b= quicksort(b)
        return b[k]
    test = [1,2,3,4,5,0,9]
    # print(findk(test,3))

    a = [0,1]
    import numpy as np
    s = np.ones((3,5))
    print(s)
    print(np.random.rand(100,100))