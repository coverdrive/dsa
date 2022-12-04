from dataclasses import dataclass
from typing import Sequence, Generic, TypeVar, Set, Tuple, Mapping
from itertools import groupby
from queue import Queue, create_empty_queue
from stack import Stack, create_empty_stack

X = TypeVar('X')


class DirGraph(Generic[X]):
    edges: Set[Tuple[X, X]]
    node_visited: Mapping[X, bool]
    node_edges_map: Mapping[X, Sequence[X]]

    def __init__(self, edges: Set[Tuple[X, X]]):
        self.edges = edges
        nodes: Set[X] = {x for x, _ in edges}.union({y for _, y in edges})
        self.node_visited = {n: False for n in nodes}
        self.node_edges_map = {n: [] for n in nodes}
        for x, y in edges:
            self.node_edges_map[x].append(y)

    def reset_visits(self):
        for n, _ in self.node_visited.items():
            self.node_visited[n] = False

    def breadth_first_walk(self, x: X) -> Sequence[X]:
        q: Queue[X] = create_empty_queue(len(self.node_edges_map))
        ret: List[X] = []
        self.node_visited[x] = True
        q.enqueue(x)
        while not q.is_empty():
            n: X = q.dequeue()
            ret.append(n)
            for m in self.node_edges_map[n]:
                if not self.node_visited[m]:
                    self.node_visited[m] = True
                    q.enqueue(m)
        return ret

    def depth_first_walk(self, x: X) -> Sequence[X]:
        s: Stack[X] = create_empty_stack(
            1 + sum(len(v) for v in self.node_edges_map.values())
        )
        ret: List[X] = []
        s.push(x)
        while not s.is_empty():
            n: X = s.pop()
            if not self.node_visited[n]:
                ret.append(n)
                self.node_visited[n] = True
            for m in reversed(self.node_edges_map[n]):
                if not self.node_visited[m]:
                    s.push(m)
        return ret

    def depth_first_walk_rec(self, x: X) -> Sequence[X]:
        self.node_visited[x] = True
        ret: List[X] = [x]
        for y in self.node_edges_map[x]:
            if not self.node_visited[y]:
                ret += self.depth_first_walk_rec(y)
        return ret


    def __repr__(self) -> str:
        ret: str = ""
        for n, ns in self.node_edges_map.items():
            ret += f"{str(n)}: {str(ns)}\n"
        return ret


if __name__ == '__main__':
    dg: DirGraph[int] = DirGraph({
        (1, 2),
        (1, 4),
        (2, 2),
        (2, 4),
        (2, 5),
        (2, 6),
        (3, 1),
        (3, 2),
        (3, 5),
        (3, 7),
        (3, 8),
        (4, 2),
        (4, 1),
        (4, 6),
        (4, 9),
        (5, 2),
        (5, 8),
        (6, 9),
        (6, 1),
        (6, 6),
        (6, 3),
        (7, 3),
        (9, 1),
        (9, 5),
        (9, 2),
        (9, 9),
        (9, 8)
    })
    print(dg)
    bf: Sequence[int] = dg.breadth_first_walk(3)
    dg.reset_visits()
    print(bf)
    df: Sequence[int] = dg.depth_first_walk(3)
    dg.reset_visits()
    print(df)
    df1: Sequence[int] = dg.depth_first_walk_rec(3)
    dg.reset_visits()
    print(df1)
