class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"pushed: {item}")

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) ==0
    
    def display(self):
        print(f"stack:{self.stack}")


stackvalues = stack()