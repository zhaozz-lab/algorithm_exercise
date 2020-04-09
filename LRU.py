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

class LRUCache1:
 
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.used_list = []
        self.capacity = capacity
 
    # @return an integer
    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1
 
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value

if __name__ == '__main__':
    test = LRUCache1(3)
    test.set(1,3)
    test.set(2,2)
    test.set(3,3)
    test.set(4,3)
    print(test.get(1))
