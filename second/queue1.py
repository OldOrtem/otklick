class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:

    def __init__(self, max_size=None):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def add(self, val):
        if self.max_size:
            if self.size >= self.max_size:
                return None

        node = Node(val)
        if self.head:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
        else:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head

        self.size += 1

    def remove(self):
        if self.size == 0:
            return None
        val = self.head.val
        if self.size == 1:
            self.head = None

        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
        self.size -=1
        return val



    def print(self):
        if self.size == 0:
            print("empty")
            return
        cur = self.head
        print(cur.val, end=" ")
        cur = cur.next
        while cur != self.head:
            print(cur.val, end=" ")
            cur = cur.next


q = Queue(max_size=5)
for i in range(10):
    print(q.add(i))
    q.print()
    print()
for i in range(10):
    print(q.remove())
    q.print()
    print()