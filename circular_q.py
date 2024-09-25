class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity  # Create a list with a fixed capacity
        self.front = -1  # Points to the front element in the queue
        self.rear = -1   # Points to the last element in the queue

    # Check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Enqueue an element to the queue
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.front = 0  # If inserting the first element, set front to 0

        self.rear = (self.rear + 1) % self.capacity  # Move rear circularly
        self.queue[self.rear] = value
        print(f"Enqueued {value}")

    # Dequeue an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        value = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot

        if self.front == self.rear:  # If only one element was present
            self.front = self.rear = -1  # Reset queue
        else:
            self.front = (self.front + 1) % self.capacity  # Move front circularly

        print(f"Dequeued {value}")
        return value

    # Peek at the front element without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    # Display the queue elements
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.capacity  # Move index circularly
            print()

# Example usage:
cq = CircularQueue(5)  # Capacity of the queue is 5

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # Queue should now be full

cq.display()  # Displays the queue

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue(60)
cq.enqueue(70)

cq.display()