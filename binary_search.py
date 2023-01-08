# Find the smallest index in the given non-empty sorted list l
# that is > than the given element e.
# If all elements of l are <= e,  we return len(l)

from dataclasses import dataclass
from typing import Sequence,  Generic, TypeVar
from comparable import Comparable

X = TypeVar("X", bound=Comparable)


@dataclass(frozen=True)
class BinarySearch(Generic[X]):
    l: Sequence[X]

    def find(self, e: X) -> int:
        return self.find_bounds(e, 0, len(self.l))

    def find_bounds(self, e: X, left: int, right: int) -> int:
        if right == left + 1:
            return left if self.l[left] > e else right
        else:
            mid: int = int((left + right) / 2)
            if self.l[mid] > e:
                return self.find_bounds(e, left, mid)
            else:
                return self.find_bounds(e, mid, right)


if __name__ == '__main__':
    seq: Sequence[int] = [1, 3, 4, 6, 7, 9]
    elem: int = 5
    bs: BinarySearch = BinarySearch(l=seq)
    res: int = bs.find(elem)
    print(res)


