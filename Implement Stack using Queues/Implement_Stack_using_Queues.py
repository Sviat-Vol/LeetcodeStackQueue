class Queue:
    def __init__(self):
        self.queue = []
    def push(self, elem):
        self.queue.append(elem)
    def pop(self):
        return self.queue.pop(0)
    def peek(self):
        st = self.queue.copy()
        return st.pop(0)
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0

class MyStack:

    def __init__(self):
        self.stack = Queue()
        

    def push(self, x: int) -> None:
        self.stack.push(x)
        

    def pop(self) -> int:
        queue_copy = Queue()
        while not self.empty():
            el = self.stack.pop()
            if not self.empty():
                queue_copy.push(el)
        
        while not queue_copy.is_empty():
            self.stack.push(queue_copy.pop())
        return el

    def top(self) -> int:
        queue_copy = Queue()
        while not self.empty():
            el = self.stack.pop()
            queue_copy.push(el)
        
        while not queue_copy.is_empty():
            self.stack.push(queue_copy.pop())
        return el
        

    def empty(self) -> bool:
        return self.stack.is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
