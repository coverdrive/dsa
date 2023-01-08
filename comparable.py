from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: CT, other: CT) -> bool:
        pass

    def __le__(self: CT, other: CT) -> bool:
        return self < other or self == other


CT = TypeVar("CT", bound=Comparable)
