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


#_____CLASS DEQUE _____
class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)
        print(f"Added to front: {item}")

    def add_rear(self, item):
        self.deque.append(item)
        print(f"Added to rear: {item}")

    def remove_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.deque.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.deque.pop()

    def is_empty(self):
        return len(self.deque) == 0

    def display(self):
        print(f"Deque: {self.deque}")

Dequevalues = Deque()
Dequevalues.add_front(10)
Dequevalues.add_rear(20)
Dequevalues.add_front(30)
Dequevalues.add_rear(40)
Dequevalues.add_front(50)
Dequevalues.add_rear(60)

Dequevalues.display()

print("Remove from front:", Dequevalues.remove_front())
print("Remove from rear:", Dequevalues.remove_rear())

Dequevalues.display()


