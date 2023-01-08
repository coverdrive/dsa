# Find the smallest index in the given non-empty sorted list l
# that is > than the given element e.
# If all elements of l are <= e,  we return len(l)

from dataclasses import dataclass
from typing import Sequence,  Generic, TypeVar, List
from heap import Heap

from comparable import Comparable

X = TypeVar('X', bound=Comparable)


@dataclass(frozen=True)
class Sort(Generic[X]):
    l: Sequence[X]

    def get_copy(self) -> List[X]:
        return [x for x in self.l]

    def bubble_sort(self) -> Sequence[X]:
        sl: List[X] = self.get_copy()
        sz: int = len(sl)
        for i in range(sz - 1):
            for j in range(sz - 2, i - 1, -1):
                if sl[j + 1] < sl[j]:
                    sl[j], sl[j + 1] = sl[j + 1], sl[j]
        return sl

    def insertion_sort(self) -> Sequence[X]:
        sl: List[X] = self.get_copy()
        sz: int = len(sl)
        for i in range(1, sz):
            val: X = sl[i]
            j: int = i - 1
            while j >= 0 and sl[j] > val:
                sl[j + 1] = sl[j]
                j -= 1
            sl[j + 1] = val
        return sl

    @staticmethod
    def merge(sl1: Sequence[X], sl2: Sequence[X]) -> Sequence[X]:
        # merge two sorted lists sl1, sl2 into sorted list sl
        i, j, k = 0, 0, 0
        sz1: int = len(sl1)
        sz2: int = len(sl2)
        sl: List[X] = [x for x in sl1] + [y for y in sl2]
        while i < sz1 and j < sz2:
            if sl1[i] < sl2[j]:
                val = sl1[i]
                i += 1
            else:
                val = sl2[j]
                j += 1
            sl[k] = val
            k += 1
        while i < sz1:
            sl[k] = sl1[i]
            i += 1
            k += 1
        while j < sz2:
            sl[k] = sl2[j]
            j += 1
            k += 1
        return sl

    def merge_sort(self) -> Sequence[X]:
        sz: int = len(self.l)
        if sz == 1:
            return [self.l[0]]
        else:
            half: int = int(sz / 2)
            sl1: Sequence[X] = Sort(self.l[:half]).merge_sort()
            sl2: Sequence[X] = Sort(self.l[half:]).merge_sort()
            return Sort.merge(sl1, sl2)

    @staticmethod
    def quick_sort_recurse(sl: List[X], left: int, right: int) -> None:
        if right > left + 1:
            # pivot is sl[right - 1], last element in the range sl[left: right]
            # indices from left upto i maintained to be <= sl[right - 1]
            # indices from i + 1 upto j - 1 maintained to be > sl[right - 1]
            # scan from j upto right - 2 to place sl[j] in correct interval
            i: int = left - 1
            for j in range(left, right - 1):
                if sl[j] <= sl[right - 1]:
                    sl[i + 1], sl[j] = sl[j], sl[i + 1]
                    i += 1
            # finally swap sl[right - 1] with sl[i + 1]
            sl[i + 1], sl[right - 1] = sl[right - 1], sl[i + 1]
            # this sets the pivot at index i + 1 between the two intervals
            # so then the two intervals can be recursively sorted
            Sort.quick_sort_recurse(sl, left, i + 1)
            Sort.quick_sort_recurse(sl, i + 2, right)

    def quick_sort(self) -> Sequence[X]:
        sl: List[X] = self.get_copy()
        Sort.quick_sort_recurse(sl, 0, len(sl))
        return sl

    def heap_sort(self, smallest_element: X) -> Sequence[X]:
        sl: List[X] = self.get_copy()
        heap: Heap = Heap(
            l=sl,
            heap_size=len(sl),
            smallest_element=smallest_element
        )
        return heap.heap_sort()


if __name__ == '__main__':
    seq: Sequence[int] = [7, 3, 1, 4, 5, 2, 8, 4, 9, 5]
    seq_obj: Sort = Sort(l=seq)
    insertion_sort_seq: Sequence[int] = seq_obj.insertion_sort()
    print(insertion_sort_seq)
    bubble_sort_seq: Sequence[int] = seq_obj.bubble_sort()
    print(bubble_sort_seq)
    merge_sort_seq: Sequence[int] = seq_obj.merge_sort()
    print(merge_sort_seq)
    quick_sort_seq: Sequence[int] = seq_obj.quick_sort()
    print(quick_sort_seq)
    heap_sort_seq: Sequence[int] = seq_obj.heap_sort(smallest_element=-1000000)
    print(heap_sort_seq)


