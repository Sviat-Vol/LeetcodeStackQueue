class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, elem):
        self.__stack.append(elem)
    def pop(self):
        return self.__stack.pop()
    def peek(self):
        st = self.__stack.copy()
        return st.pop()
    def size(self):
        return len(self.__stack)
    def is_empty(self):
        return self.size() == 0
    



class MyQueue:

    def __init__(self):
        self.queue = Stack()
    def push(self, x: int) -> None:
        self.queue.push(x)
    def pop(self) -> int:
        stack_copy = Stack()
        while not self.empty():
            el = self.queue.pop()
            if not self.empty():
                stack_copy.push(el)
        
        while not stack_copy.is_empty():
            self.queue.push(stack_copy.pop())
        return el
        

    def peek(self) -> int:
        stack_copy = Stack()
        while not self.empty():
            el = self.queue.pop()
            stack_copy.push(el)
        
        while not stack_copy.is_empty():
            self.queue.push(stack_copy.pop())

        return el

    def empty(self) -> bool:
        return self.queue.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
