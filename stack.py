from dataclasses import dataclass
from typing import Sequence, Generic, TypeVar, List

X = TypeVar('X')


@dataclass
class Stack(Generic[X]):
    l: List[X]
    top: int  # index of element at the top of the stack

    def is_empty(self) -> bool:
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.top == len(self.l) - 1:
            return True
        else:
            return False

    def pop(self) -> X:
        if self.is_empty():
            raise ValueError("Cannot pop from empty stack")
        else:
            self.top -= 1
            return self.l[self.top + 1]

    def push(self, elem: X) -> None:
        if self.is_full():
            raise ValueError("Cannot push on to full stack")
        else:
            self.top += 1
            self.l[self.top] = elem

    def __repr__(self) -> str:
        return str([self.l[i] for i in range(self.top, -1, -1)])


def create_empty_stack(capacity: int) -> Stack:
    return Stack(l=[0] * capacity, top=-1)


def create_full_capacity_stack(seq: Sequence[X]) -> Stack:
    return Stack(l=[x for x in seq], top=len(seq) - 1)


if __name__ == '__main__':
    stack: Stack = create_empty_stack(10)
    print(stack)
    stack.push(5)
    print(stack)
    stack.push(7)
    print(stack)
    stack.push(2)
    print(stack)
    x = stack.pop()
    print(x)
    print(stack)
    stack.push(4)
    print(stack)
    x = stack.pop()
    print(x)
    print(stack)
    x = stack.pop()
    print(x)
    print(stack)
    stack.push(8)
    print(stack)
