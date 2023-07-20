from typing import Callable, Any
from copy import deepcopy


class Grouper:
    def __init__(self, iterable: iter, key: Callable):
        self._key = key
        self._groups = {}

        for v in deepcopy(iterable):
            self._groups.setdefault(self._key(v), []).append(v)

    def __len__(self):
        return len(self._groups)

    def __iter__(self):
        yield from self._groups.items()

    def __contains__(self, item: Any):
        return item in self._groups

    def __getitem__(self, item: Any) -> list:
        return self._groups[item]

    def add(self, obj: Any) -> None:
        self._groups.setdefault(self._key(obj), []).append(obj)

    def group_for(self, obj: Any) -> Any:
        return self._key(obj)