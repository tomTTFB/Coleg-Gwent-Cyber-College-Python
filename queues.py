from collections import deque

queue = deque()

queue.append('X')
queue.append('Y')
queue.append('Z')

print(f"Queue after enqueues: {queue}")

dequeued = queue.popleft()
print(f"Dequeued element: {dequeued}")
print(f"Queue after dequeue: {queue}")