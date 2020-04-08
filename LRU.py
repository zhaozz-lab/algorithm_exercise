class Node(object):
    """docstring for Node"""
    def __init__(self, key,val):
        super(Node, self).__init__()
        self.key = key
        self.val = val
        self.next = Node()
        self.pre = Node()

class DoubleList(object):
    def __init__(self):
        self.prev = None
        self.next = None
    def addFirst(x):
        print()

    def remove(x):
        print()

    def removeLast():
        print()

    def size():
        return 1


class LRUCache(object):
    def __init__(self,capacity,hashmap,doublelist):
        self.map = hashmap
        self.cache = doublelist
        self.cap = capacity
    
    def get(self,key):
        if key not in self.map:
            return -1
        val = self.map[key]
        self.put(key,val)
        return val

    def put(self,key,val):
        x = Node(key,val)
        if key in self.map:
            cache.remove(self.map.get(key))
            cache.addFirst(x)
            self.put(key,x)
        else:
            if self.cap == cache.size():
                last = cache.removeLast()
                del self.map[key]
        cache.addFirst(x)
        self.map.put(key,x)