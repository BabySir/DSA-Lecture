
class Queue:

    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity


    #This operation returns a boolean value that indicates whether the queue is isFull or not.
    def isFull(self):
        return self.size == self.capacity

    #This operation returns a boolean value that indicates whether the queue is empty or not.
    def isEmpty(self):
        return self.size == 0

    # Enqueue() operation in Queue adds (or stores) an element to the end of the queue.
    def EnQueue(self, item):
        if self.isFull():
            print("Already full")
            return
        #% (self.capacity): This ensures that if the rear index reaches the end of the queue (i.e., self.capacity), it wraps around back to the beginning (index 0), thus creating the circular effect.
        #This is a common technique used to avoid needing to shift elements in the queue, maintaining constant time complexity for both enqueue and dequeue operations.
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    # DeQueue() operation in Queue removes (or access) the first element from the queue.
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    #This operation returns the element at the front end without removing it.
    def q_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    #This operation returns the element at the rear end without removing it.
    def q_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])


# Driver Code
if __name__ == '__main__':

    queue = Queue(5)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.EnQueue(50)

    print('Trying to enqueue after reaching full capacity')
    queue.EnQueue(60)
    
    queue.q_front()
    queue.q_rear()
    queue.DeQueue()
    queue.DeQueue()
    queue.DeQueue()
    queue.DeQueue()
    queue.DeQueue()
    print('Trying to dequeue empty queue')
    queue.DeQueue()
