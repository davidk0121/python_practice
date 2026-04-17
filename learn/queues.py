# Queues (double ened queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue) # output: deque([1, 2])

queue.pop()
print(queue) # output: deque([1])

queue.appendleft(1)
print(queue) # output: deque([1, 2])

queue.popleft()
print(queue) # output: deque([2])


