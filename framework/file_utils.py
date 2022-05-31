import os
import pathlib
import random


class FileCapture:
    def __init__(self, path):
        super().__init__()
        self._path = path

    def read_file_lines(self):
        with open(self._path, "r+") as f:
            lines = f.read().splitlines()
            return FileContent(lines)

    def write_file_contents(self, header, lines):
        with open(self._path, "w+") as f:
            f.write(header + "\n")
            for line in lines:
                f.write(line + "\n")


class FileContent:
    def __init__(self, lines):
        super().__init__()
        self._lines_to_relocate = None
        self._lines_to_keep = None
        self._header = lines[0]
        self._lines = lines[1:]

    def separate_lines(self, count_lines):
        self._lines_to_relocate = random.sample(self._lines, count_lines)
        self._lines_to_keep = list(set(self._lines) - set(self._lines_to_relocate))

    @property
    def header(self):
        return self._header

    @property
    def lines_to_keep(self):
        return self._lines_to_keep

    @property
    def lines_to_relocate(self):
        return self._lines_to_relocate

    @lines_to_keep.setter
    def lines_to_keep(self, lines_to_keep):
        self._lines_to_keep = lines_to_keep

    @lines_to_relocate.setter
    def lines_to_relocate(self, lines_to_relocate):
        self._lines_to_relocate = lines_to_relocate


class PathFinder:
    def __init__(self, source_path):
        super().__init__()
        self._source_path = source_path

    def get_result_path(self):
        file_name = os.path.basename(self._source_path)
        file_pure_name = os.path.splitext(file_name)[0]
        file_extension = os.path.splitext(file_name)[1]
        return pathlib.Path(self._source_path).parent.resolve().__str__() + "/" + \
               file_pure_name + "_res" + file_extension
