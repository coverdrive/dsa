# A heap is a tree with n elements maintained as an array
# where Find the smallest index in the given non-empty sorted list l
# that is > than the given element e.
# If all elements of l are <= e,  we return len(l)

from dataclasses import dataclass
from typing import Sequence,  Generic, TypeVar

X = TypeVar('X')
SMALL_NUM = -100000


@dataclass
class Heap(Generic[X]):
    l: Sequence[X]
    heap_size: int

    @staticmethod
    def parent(i: int) -> int:
        return int((i - 1) / 2)

    @staticmethod
    def left(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        return 2 * i + 2

    def last_non_leaf(self) -> int:
        return Heap.parent(self.heap_size - 1)

    def make_node_max(self, i: int) -> None:
        lft: int = Heap.left(i)
        rght: int = Heap.right(i)
        if lft < self.heap_size and self.l[lft] > self.l[i]:
            m = lft
        else:
            m = i
        if rght < self.heap_size and self.l[rght] > self.l[m]:
            m = rght
        if m != i:
            self.l[i], self.l[m] = self.l[m], self.l[i]
            self.make_node_max(m)

    def make_heap(self) -> None:
        self.heap_size = len(self.l)
        for i in range(self.last_non_leaf(), -1, -1):
            self.make_node_max(i)

    def heap_sort(self) -> None:
        self.make_heap()
        for i in range(self.heap_size - 1, 0, -1):
            self.l[i], self.l[0] = self.l[0], self.l[i]
            self.heap_size -= 1
            self.make_node_max(0)

    def get_heap_max(self) -> X:
        return self.l[0]

    def extract_heap_max(self) -> X:
        if self.heap_size < 1:
            raise ValueError("Heap size insufficient to extract")
        max_val: X = self.l[0]
        self.l[0] = self.l[self.heap_size - 1]
        self.heap_size -= 1
        self.make_node_max(0)
        return max_val

    def increase_node_val(self, i: int, val: X) -> None:
        if val < self.l[i]:
            raise ValueError("New value at node cannot be less than old value")
        self.l[i] = val
        j = i
        while j > 0 and self.l[Heap.parent(j)] < self.l[j]:
            self.l[Heap.parent(j)], self.l[j] = self.l[j], self.l[Heap.parent(j)]
            j = Heap.parent(j)


    def insert_in_heap(self, x: X) -> None:
        if self.heap_size == len(self.l):
            self.l.append(SMALL_NUM)
        else:
            self.l[self.heap_size] = SMALL_NUM
        self.heap_size += 1
        self.increase_node_val(self.heap_size - 1, x)


if __name__ == '__main__':
    seq: Sequence[int] = []
    heap_sz: int = len(seq)
    heap: Heap = Heap(l=seq, heap_size=heap_sz)
    heap.make_heap()
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(5)
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(7)
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(3)
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(9)
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(2)
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(6)
    print(heap.l[:heap.heap_size])
    x = heap.extract_heap_max()
    print(x)
    print(heap.l[:heap.heap_size])
    heap.insert_in_heap(1)
    print(heap.l[:heap.heap_size])
    x = heap.extract_heap_max()
    print(x)
    print(heap.l[:heap.heap_size])
    # heap.heap_sort()
    # print(heap.l)
