from dataclasses import dataclass
from typing import Sequence, Generic, TypeVar, List

X = TypeVar('X')


@dataclass
class Queue(Generic[X]):
    l: List[X]
    head: int  # index of head element in queue
    size: int  # number of elements in queue

    def tail(self) -> int:
        # index in queue where next enqueue will occur
        return (self.head + self.size) % len(self.l)

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.size == len(self.l):
            return True
        else:
            return False

    def dequeue(self) -> X:
        if self.is_empty():
            raise ValueError("Cannot dequeue from empty queue")
        else:
            ret_val: X = self.l[self.head]
            self.head = (self.head + 1) % len(self.l)
            self.size -= 1
            return ret_val

    def enqueue(self, elem: X) -> None:
        if self.is_full():
            raise ValueError("Cannot enqueue to full queue")
        else:
            self.l[self.tail()] = elem
            self.size += 1

    def __repr__(self) -> str:
        return str([self.l[(self.head + i) % len(self.l)]
                    for i in range(self.size)])


def create_empty_queue(capacity: int) -> Queue:
    return Queue(l=[0] * capacity, head=0, size=0)


def create_full_capacity_queue(seq: Sequence[X]) -> Queue:
    return Queue(l=[x for x in seq], head=0, size=len(seq))


if __name__ == '__main__':
    queue: Queue = create_empty_queue(10)
    print(queue)
    queue.enqueue(5)
    print(queue)
    queue.enqueue(7)
    print(queue)
    queue.enqueue(2)
    print(queue)
    x = queue.dequeue()
    print(x)
    print(queue)
    queue.enqueue(4)
    print(queue)
    x = queue.dequeue()
    print(x)
    print(queue)
    x = queue.dequeue()
    print(x)
    print(queue)
    queue.enqueue(8)
    print(queue)
