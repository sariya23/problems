class HistoryDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}
        self._cash = {}

        for k, v in self._data.items():
            if k not in self._cash:
                self._cash[k] = [v]
            else:
                self._cash[k].append(v)

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def history(self, key):
        return self._cash.get(key, [])

    def all_history(self):
        return self._cash

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

        if key not in self._cash:
            self._cash[key] = [value]
        else:
            self._cash[key].append(value)

    def __delitem__(self, key):
        del self._cash[key]
        del self._data[key]