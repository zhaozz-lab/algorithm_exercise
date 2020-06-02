class node(object):
    """docstring for listnode"""
    def __init__(self, value,node=None):
        self.val = value
        self.next = node

head = node(1,None)
temp = head
i=0
while i<10:
    tempnode = node(i,None)
    temp.next = tempnode
    temp = temp.next
    i += 1

temp = head
def traverse(head):
    temp = head
    while temp.next is not None:
        print(temp.val)
        temp = temp.next

traverse(temp)

def reverse(head):
    if head.next is None:
        return head
    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last
# test1 = reverse(temp)
# print("the reverse list is ")
# traverse(test1)
def reverse_iter(head):
    newlist = None
    while head is not None:
        nextnode = head.next
        head.next = newlist
        newlist = head
        
        head = nextnode
    return newlist
# temp = head
# print(head.next.val)  
# test1 = reverse_iter(temp)
# test1 = reverse(temp)
# print("the reverse_iter list is ")
# traverse(test1)
# print("the result is ")

def reverse_k(a,b):
    if a.next is None:
        return a
    newlist = None
    print(a.val)
    while a != b:
        nextnode = a.next
        a.next =  newlist
        newlist = a
        a = nextnode
    return newlist

def reverseKGroup(head,k):
    if head is None:
        return None
    a,b = head,head
    for i in range(0,k):
        if b is None:
            return head
        b = b.next

    newHead = reverse_k(a,b)
    a.next = reverseKGroup(b,k)
    return newHead

traverse(temp)    
test2 = reverseKGroup(temp,2)
traverse(test2)


# reverse 
if __name__ == '__main__':
    pass
                   