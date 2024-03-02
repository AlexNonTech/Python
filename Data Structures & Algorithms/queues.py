from _collections import deque


class Deque:
    def __init__(self):
        self.data = deque()

    def enqueue(self, node):
        self.data.append(node)

    def dequeue(self):
        self.data.popleft()

    def display(self):
        return self.data


queue = Deque()
queue.enqueue(31)
queue.enqueue(40)
queue.dequeue()
