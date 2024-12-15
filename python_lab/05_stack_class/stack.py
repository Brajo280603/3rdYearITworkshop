class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        return "Stack Underflow"

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return "Stack is Empty"


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(7)
print(stack.get_min())
stack.pop()
print(stack.get_min())
stack.pop()
print(stack.get_min())