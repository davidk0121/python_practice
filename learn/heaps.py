# Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0 
print(minHeap[0]) # 2

while len(minHeap):
    print(heapq.heappop(minHeap))

# -----------------
import heapq
# No max heaps by default, work around is 
# to use min heap and multiply by -1 when
# push & pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0 (negated)
print(-maxHeap[0])

while len(maxHeap):
    print(-heapq.heappop(maxHeap))
# -----------------
import heapq
#Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))