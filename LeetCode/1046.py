#
# LeetCode
#
# Problem - 1046
# URL - https://leetcode.com/problems/kth-largest-element-in-a-stream/
#

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    max_heap = []
    for stone in stones:
      max_heap.append(stone)
      self.heapifyTop(max_heap, len(max_heap) - 1)

    while len(max_heap) > 1:
      first = self.deleteRoot(max_heap)
      second = self.deleteRoot(max_heap)
      
      if first != second:
        max_heap.append(abs(first - second))
        self.heapifyTop(max_heap, len(max_heap) - 1)

    return max_heap[0] if max_heap else 0

  def deleteRoot(self, max_heap) -> int:
    root_val = max_heap.pop(0)
    
    if max_heap:
      max_heap.insert(0, max_heap.pop())
      self.heapifyDown(max_heap, 0)

    return root_val

  def heapifyTop(self, max_heap, inserted):
    parent = int( (inserted - 1) / 2)

    if max_heap[inserted] > max_heap[parent]:
      max_heap[inserted], max_heap[parent] = max_heap[parent], max_heap[inserted]

      self.heapifyTop(max_heap, parent)

  def heapifyDown(self, max_heap, parent):
    largest = parent
    l = parent * 2 + 1
    r = parent * 2 + 2

    if l < len(max_heap) and max_heap[l] > max_heap[largest]:
      largest = l
    
    if r < len(max_heap) and max_heap[r] > max_heap[largest]:
      largest = r

    if largest != parent:
      max_heap[parent], max_heap[largest] = max_heap[largest], max_heap[parent]
 
      self.heapifyDown(max_heap, largest)
