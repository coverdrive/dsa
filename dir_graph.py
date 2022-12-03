from dataclasses import dataclass
from typing import Sequence, Generic, TypeVar, Set, Tuple, Mapping
from itertools import groupby
from queue import Queue, create_empty_queue
from stack import Stack, create_empty_stack

X = TypeVar('X')


class DirGraph(Generic[X]):
    edges: Set[Tuple[X, X]]
    out_edges: Mapping[X, Sequence[X]]

    def __init__(self, edges: Set[Tuple[X, X]]):
        self.edges = edges
        self.out_edges = self.get_out_edges()

    def get_out_edges(self) -> Mapping[X, Sequence[X]]:
        def f(x: Tuple[X, X]) -> X:
            return x[0]
        return {n: [y for _, y in l] for n, l in groupby(sorted(self.edges, key=f), f)}

    def breadth_first_walk(self) -> Sequence[X]:
        q: Queue[X] = create_empty_queue(len(self.out_edges))
        return [k for k, _ in self.out_edges.items()]

    def depth_first_walk(self) -> Sequence[X]:
        q: Stack[X] = create_empty_stack(len(self.out_edges))
        return [k for k, _ in self.out_edges.items()]


    def __repr__(self) -> str:
        ret: str = ""
        for n, nl in self.out_edges.items():
            ret += f"{str(n)}: {str(nl)}\n"
        return ret


if __name__ == '__main__':
    dg: DirGraph[int] = DirGraph({
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 2),
        (2, 4),
        (3, 1),
        (3, 2),
        (4, 2)
    })
    print(dg)
    bf: Sequence[int] = dg.breadth_first_walk()
    print(bf)
    df: Sequence[int] = dg.depth_first_walk()
    print(df)
