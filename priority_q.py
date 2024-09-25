import heapq

# Initialize an empty priority queue (min-heap)
priority_queue = []

# Adding elements to the priority queue
def push(queue, item):
    heapq.heappush(queue, item)

# Removing and returning the smallest element (highest priority)
def pop(queue):
    return heapq.heappop(queue)

# Peek at the smallest element without popping
def peek(queue):
    return queue[0] if queue else None

# Check if the priority queue is empty
def is_empty(queue):
    return len(queue) == 0

# Example usage
if __name__ == "__main__":
    # Add items to the priority queue
    push(priority_queue, (2, "task 2"))
    push(priority_queue, (1, "task 1"))  # Higher priority (smaller value)
    push(priority_queue, (3, "task 3"))
    
    print("Priority Queue:", priority_queue)

    # Pop items from the queue based on priority
    while not is_empty(priority_queue):
        priority, task = pop(priority_queue)
        print(f"Processing {task} with priority {priority}")