#
# LeetCode
#
# Problem - 703
# URL - https://leetcode.com/problems/kth-largest-element-in-a-stream/
#

class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.k = k - 1
    self.min_heap = []

    for num in nums:
      self.add(num)

  def add(self, val: int) -> int:
    if len(self.min_heap) <= self.k:
      self.min_heap.append(val)
      self.heapifyTop(len(self.min_heap) - 1)
    elif len(self.min_heap) > self.k and val > self.min_heap[0]:
      self.min_heap[0] = val
      self.heapifyDown(0)

    return self.min_heap[0]

  def heapifyTop(self, child):
    parent = int((child - 1) / 2)

    if self.min_heap[parent] > self.min_heap[child]:
      self.min_heap[parent], self.min_heap[child] = self.min_heap[child], self.min_heap[parent]

      self.heapifyTop(parent)

  def heapifyDown(self, parent):
    left = parent * 2 + 1
    right = parent * 2 + 2

    smallest = parent
    if len(self.min_heap) > left and self.min_heap[smallest] > self.min_heap[left]:
      smallest = left
    if len(self.min_heap) > right and self.min_heap[smallest] > self.min_heap[right]:
      smallest = right

    if smallest != parent:
      self.min_heap[smallest], self.min_heap[parent] = self.min_heap[parent], self.min_heap[smallest]

      self.heapifyDown(smallest)  
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
