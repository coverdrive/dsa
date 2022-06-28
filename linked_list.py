from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar

X = TypeVar('X')


@dataclass
class LinkedListNode(Generic[X]):
    key: X
    link: LinkedList

    def __repr__(self) -> str:
        l: LinkedList = self
        ret_val = ""
        while l is not None:
            ret_val += str(l.key)
            ret_val += " -> "
            l = l.link
        ret_val += "None"
        return ret_val


LinkedList = Optional[LinkedListNode]


def create_empty_linked_list() -> LinkedList:
    return None


def car(ll: LinkedList) -> X:
    if ll is None:
        raise ValueError("Cannot car from an empty list")
    else:
        return ll.key


def cdr(ll: Linkedlist) -> LinkedList:
    if ll is None:
        raise ValueError("Cannot cdr from an empty list")
    else:
        return ll.link


def cons(elem: X, ll: LinkedList) -> LinkedListNode:
    return LinkedListNode(key=elem, link=ll)


def search(ll: LinkedList, elem: X) -> LinkedList:
    if ll is None:
        return None
    elif car(ll) == elem:
        return ll
    else:
        return search(cdr(ll), elem)


def delete(ll: LinkedList, elem: X) -> LinkedList:
    if ll is None:
        return None
    else:
        if car(ll) == elem:
            ll = cdr(ll)
        else:
            ll.link = delete(cdr(ll), elem)
        return ll


def insert_in_sorted_list(elem: X, sl: LinkedList) -> LinkedList:
    if sl is None:
        return LinkedListNode(key=elem, link=None)
    else:
        first: X = car(sl)
        if elem < first:
            return cons(elem, sl)
        else:
            return cons(first, insert_in_sorted_list(elem, cdr(sl)))


def sort(ll: LinkedList) -> LinkedList:
    if ll is None:
        return None
    else:
        return insert_in_sorted_list(car(ll), sort(cdr(ll)))


if __name__ == '__main__':
    ll: LinkedList = create_empty_linked_list()
    ll1: LinkedList = cons(3, ll)
    print(ll1)
    ll2: LinkedList = cons(5, ll1)
    print(ll2)
    ll3: LinkedList = cons(2, ll2)
    print(ll3)
    e: int = car(ll3)
    print(e)
    ll4: LinkedList = cdr(ll3)
    print(ll4)
    ll5: LinkedList = cons(7, ll4)
    print(ll5)
    ll6: LinkedList = search(ll5, 5)
    print(ll6)
    ll7: LinkedList = delete(ll5, 5)
    print(ll7)
    ll8: LinkedList = cons(10, ll7)
    print(sort(ll8))
