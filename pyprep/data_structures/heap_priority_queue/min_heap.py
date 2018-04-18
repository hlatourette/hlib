from data_structures.heap_priority_queue.heap import Heap


class MinHeap(Heap):
    def __init__(self):
        super().__init__(lambda x, y: x < y)