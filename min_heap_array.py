class MinHeapArray:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop() 
            self._bubble_down(0)
        else:
            self.heap.pop()
        return min_value

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        length = len(self.heap)
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        smallest = index
        if left_child_index < length and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < length and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)