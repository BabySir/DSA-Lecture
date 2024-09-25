class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # Pointer to the previous node

class Deque:
    def __init__(self):
        self.front = None  # Points to the front node
        self.rear = None   # Points to the rear node
        self.size = 0      # Tracks the size of the deque

    # Add an element to the front
    def add_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front  # Link the new node to the current front
            self.front.prev = new_node  # Link current front back to the new node
            self.front = new_node       # Move front pointer to the new node
        self.size += 1
        print(f"Added {value} to the front")

    # Add an element to the rear
    def add_rear(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear  # Link the new node to the current rear
            self.rear.next = new_node  # Link current rear forward to the new node
            self.rear = new_node       # Move rear pointer to the new node
        self.size += 1
        print(f"Added {value} to the rear")

    # Remove an element from the front
    def remove_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        else:
            value = self.front.value
            self.front = self.front.next  # Move front pointer to the next node
            if self.front is None:  # If the deque becomes empty
                self.rear = None
            else:
                self.front.prev = None  # Unlink the previous front node
            self.size -= 1
            print(f"Removed {value} from the front")
            return value

    # Remove an element from the rear
    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        else:
            value = self.rear.value
            self.rear = self.rear.prev  # Move rear pointer to the previous node
            if self.rear is None:  # If the deque becomes empty
                self.front = None
            else:
                self.rear.next = None  # Unlink the next rear node
            self.size -= 1
            print(f"Removed {value} from the rear")
            return value

    # Check if the deque is empty
    def is_empty(self):
        return self.size == 0

    # Return the size of the deque
    def get_size(self):
        return self.size

    # Display the deque elements from front to rear
    def display(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            print("Deque elements from front to rear:", end=" ")
            current = self.front
            while current:
                print(current.value, end=" ")
                current = current.next
            print()

# Example usage
dq = Deque()

dq.add_front(10)
dq.add_rear(20)
dq.add_front(30)
dq.add_rear(40)

dq.display()

dq.remove_front()
dq.remove_rear()

dq.display()

dq.add_front(50)
dq.add_rear(60)

dq.display()