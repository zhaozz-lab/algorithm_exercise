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
# traverse(temp)

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
temp = head
print(head.next.val)  
# test1 = reverse_iter(temp)
test1 = reverse(temp)
print("the reverse_iter list is ")
traverse(test1)
print("the result is ")


    
                   