#here we are adding to the tail
# and deleting from the head


class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity=capacity
        self.dict={}
        self.tail=Node(0,0)
        self.head=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head



    def get(self, key):
        if key in self.dict:
            node=self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.dict:
            node=self.dict[key]
            self._remove(node)

        newnode = Node(key, value)
        self.dict[key] = newnode
        self._add(newnode)
        if len(self.dict)>self.capacity:
            n=self.head.next
            self._remove(n)
            del self.dict[n.key]


    def _remove(self, node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p


    def _add(self, node):
        p=self.tail.prev
        p.next=node
        node.prev=p
        self.tail.prev=node
        node.next=self.tail



obj = LRUCache(2)
param_1 = obj.get(1)
print(param_1)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))