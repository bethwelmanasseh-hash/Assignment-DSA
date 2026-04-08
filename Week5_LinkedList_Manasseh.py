class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initialize next as null

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as null
        self.count = 0  # Initialize count of nodes

    def is_empty(self):
        return self.head is None # Check if the linked list is empty

    def size(self):
        return self.count # Return the number of nodes in the linked list
    
    def append(self, data):
        new_node = Node(data) # Create a new node with the given data
        if self.is_empty():
            self.head = new_node # If the linked list is empty, set the new node as the head
        else:
            current = self.head
            while current.next: # Traverse to the end of the linked list
                current = current.next
            current.next = new_node # Set the next of the last node to the new node
        self.count += 1 # Increment the count of nodes

    def prepend(self, data):
        new_node = Node(data) # Create a new node with the given data
        new_node.next = self.head # Set the next of the new node to the current head
        self.head = new_node # Set the new node as the head of the linked list
        self.count += 1 # Increment the count of nodes

    def insert_at_position(self,data,pos):
        if pos < 0 or pos > self.count:
            print("Error: Position out of bounds")
            return
        if pos == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head # Start from the head of the linked list
        for _ in range(pos - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def delete_by_value(self, data):
        if self.is_empty():
            print("Error: Linked list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next # If the head node contains the data, set the head to the next node
            self.count -= 1 # Decrement the count of nodes
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next # Set the next of the current node to skip the node with the data
                self.count -= 1 # Decrement the count of nodes
                return
            current = current.next
        print("Error: Value not found in the linked list")

    def delete_by_position(self, pos):
        if pos < 0 or pos >= self.count:
            print("Error: Position out of bounds")
            return
        if pos == 0:
            self.head = self.head.next # If the position is 0, set the head to the next node
            self.count -= 1 # Decrement the count of nodes
            return
        current = self.head
        for _ in range(pos - 1):
            current = current.next
        current.next = current.next.next # Set the next of the current node to skip the node at the position
        self.count -= 1 # Decrement the count of nodes

    def search(self, data):
        current = self.head # Start from the head of the linked list
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        print("Error: Value not found in the linked list")
        return -1
    
    def display(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        current = self.head # Start from the head of the linked list
        while current:
            print(current.data, end=" -> ") # Print the data of the current node
            current = current.next
        print("None") # Indicate the end of the linked list


            #  ----Test Coverage ----- #
if __name__ == "__main__":
    # Creating a new linked list
    linked_list = SinglyLinkedList()
    
    #checking if the linked list is empty
    print("Empty linked list:")
    linked_list.display()
    print(f"Is the linked list empty? {linked_list.is_empty()}")


    # Appending some elements to the linked list
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    
    # Displaying the linked list  
    print("Linked List after appending 10, 20, 30:")
    linked_list.display()
    
    # Prepending an element to the linked list
    linked_list.prepend(5)
    
    # Displaying the linked list
    print("Linked List after prepending 5:")
    linked_list.display()
    
    # Insert an element at a specific position
    linked_list.insert_at_position(15, 2)
    # Display the linked list
    print("Linked List after inserting 15 at position 2:")
    linked_list.display()
    # Delete an element by value
    linked_list.delete_by_value(20)
    # Display the linked list
    print("Linked List after deleting value 20:")
    linked_list.display()
    # Delete an element by position
    linked_list.delete_by_position(1)
    # Display the linked list
    print("Linked List after deleting position 1:")
    linked_list.display()
    # Search for an element
    index = linked_list.search(15)
    if index != -1:
        print(f"Value 15 found at index: {index}")
    # Display the size of the linked list
    print(f"Size of the linked list: {linked_list.size()}")
