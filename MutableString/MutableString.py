class MutableString:
    def __init__(self, string: str = ''):
        self.string = list(string)

    def __str__(self):
        return ''.join(self.string)

    def __repr__(self):
        return f"MutableString('{''.join(self.string)}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        yield from self.string

    def __getitem__(self, key: slice | int):
        if isinstance(key, slice):
            return MutableString(''.join(self.string)[key])
        elif not isinstance(key, int):
            return
        else:
            return self.string[key]

    def __setitem__(self, index: int | slice, value: str):
        if isinstance(index, slice):
            self.string[index] = value
        elif not isinstance(index, int):
            return
        else:
            self.string[index] = value
        self.normalize_elements()

    def __delitem__(self, index: int | slice):
        if isinstance(index, slice):
            del self.string[index]
        elif not isinstance(index, int):
            return
        else:
            del self.string[index]

    def __add__(self, other: 'MutableString'):
        if isinstance(other, MutableString):
            return MutableString(''.join(self.string) + ''.join(other.string))

    def lower(self) -> None:
        self.string = ''.join(self.string).lower()

    def upper(self) -> None:
        self.string = ''.join(self.string).upper()

    def normalize_elements(self) -> None:
        """In case when self.string present [a, b, c, dd]
        BC setitem using index"""
        self.string = [i for i in ''.join(self.string)]
