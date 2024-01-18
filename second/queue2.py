class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = [None] * max_size
        self.size = 0
        self.front = 0
        self.rear = -1

    def add(self, val):
        if self.size < self.max_size:
            self.rear = (self.rear + 1) % self.max_size
            self.buffer[self.rear] = val
            self.size += 1
        else:
            return None

    def remove(self):
        if self.size > 0:
            val = self.buffer[self.front]
            self.buffer[self.front] = None
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return val
        else:
            return None

q = Queue(max_size=5)
for i in range(10):
    print(q.add(i))
    print(q.buffer)
    print()

print("e")
for i in range(10):
    print(q.remove())
    print(q.buffer)
    print()