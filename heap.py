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
        # get index of parent node of node with index i
        return int((i - 1) / 2)

    @staticmethod
    def left(i: int) -> int:
        # get index of left child node of node with index i
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        # get index of right child node of node with index i
        return 2 * i + 2

    def last_non_leaf(self) -> int:
        # get index of last non-leaf node
        return Heap.parent(self.heap_size - 1)

    def make_node_max(self, i: int) -> None:
        # assuming left and right subtrees of node with index i
        # are each heaps, make a heap out of the subtree rooted
        # at node with index i, i.e., the max value in subtree
        # rooted at index i should be at node with index i
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
        # heapify the given tree
        self.heap_size = len(self.l)
        for i in range(self.last_non_leaf(), -1, -1):
            self.make_node_max(i)

    def heap_sort(self) -> Sequence[X]:
        # heap sort the sequence self.l
        # sorted sequence is returned and the heap itself
        # becomes an empty heap at termination since self.heap_size
        # gets decremented to 0 at termination
        self.make_heap()
        heap_sz: int = self.heap_size
        for i in range(heap_sz - 1, 0, -1):
            self.l[i], self.l[0] = self.l[0], self.l[i]
            self.heap_size -= 1
            self.make_node_max(0)
        return self.l[:heap_sz]

# the following functions implement an efficient priority queue     

    def get_heap_max(self) -> X:
        return self.l[0]

    def extract_heap_max(self) -> X:
        if self.heap_size < 1:
            raise ValueError("Cannot extract as heap size is 0")
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
            raise ValueError("cannot insert as heap size is at full capacity")
        else:
            self.l[self.heap_size] = SMALL_NUM
            self.heap_size += 1
            self.increase_node_val(self.heap_size - 1, x)

    def __repr__(self) -> str:
        return str(heap.l[:heap.heap_size])


def create_empty_heap(capacity: int) -> Heap:
    return Heap(l=[0] * capacity, heap_size=0)


if __name__ == '__main__':
    heap: Heap = create_empty_heap(10)
    print(heap)
    heap.insert_in_heap(5)
    print(heap)
    heap.insert_in_heap(7)
    print(heap)
    heap.insert_in_heap(3)
    print(heap)
    heap.insert_in_heap(9)
    print(heap)
    heap.insert_in_heap(2)
    print(heap)
    heap.insert_in_heap(6)
    print(heap)
    x = heap.extract_heap_max()
    print(x)
    print(heap)
    heap.insert_in_heap(1)
    print(heap)
    x = heap.extract_heap_max()
    print(x)
    print(heap)
    # seq: Sequence[int] = [3, 5, 1, 9, 2, 8, 7]
    # heap: Heap = Heap(l=seq, heap_size=len(seq))
    # print(heap.heap_sort())
