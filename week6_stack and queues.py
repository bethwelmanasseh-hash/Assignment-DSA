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
stackvalues.push(10)
stackvalues.push(20)
stackvalues.push(30)
stackvalues.push(40)
stackvalues.push(50)
stackvalues.push(60)

stackvalues.display()

print("Top element in the stack:", stackvalues.peek())
print("Remove elements in the stack:", stackvalues.pop())
stackvalues.display()


#_____CLASS QUEUE _____
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueue: {item}")

    def dequeue(self):
       if  self.is_empty():
            return "Queue is empty"
       return self.queue.pop()

    def frontelement(self):
        if self.is_empty():
            return "Queues is empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        print(f"Queue:{self.queue}")

Queuevalues = Queue()
Queuevalues.enqueue(10)
Queuevalues.enqueue(20)
Queuevalues.enqueue(30)
Queuevalues.enqueue(40)
Queuevalues.enqueue(50)
Queuevalues.enqueue(60)

Queuevalues.display()

print("Top element: ", Queuevalues.frontelement)
print("Remove element:", Queuevalues.dequeue)
Queuevalues.display()
