class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def reverse(self):
        ne = Stack()
        old = self.data.copy()
        for elem in old[::-1]:
            ne.push(elem)
        self.data = ne.data
    def __len__(self):
        return len(self.data)


class MyQueue:

    def __init__(self):
        self.queue = Stack()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        que = self.queue
        que.reverse()
        s = que.pop()
        que.reverse()
        return s

    def peek(self) -> int:
        self.queue.reverse()
        s = self.queue.peek()
        self.queue.reverse()
        return s

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
