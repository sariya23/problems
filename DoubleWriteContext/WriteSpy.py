from typing import TextIO


class WriteSpy:
    def __init__(self, file1: TextIO, file2: TextIO, to_close: bool=False):
        self._file1 = file1
        self._file2 = file2
        self._to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self._to_close:
            self.close()

    def write(self, text: str) -> None:
        """Write data in both files"""
        try:
            self._file1.write(text)
            self._file2.write(text)
        except Exception:
            raise ValueError('Файл закрыт или недоступен для записи')

    def close(self) -> None:
        """Close both files"""
        self._file1.close()
        self._file2.close()

    def writable(self) -> bool:
        """Checks if files are open for writing"""
        try:
            return self._file1.writable() and self._file2.writable()
        except ValueError:
            return False

    def closed(self) -> bool:
        """checks if files are close"""
        return self._file1.closed and self._file2.closed
