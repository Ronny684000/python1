import os

from framework.file_utils import FileCapture, PathFinder


class Task:
    def __init__(self):
        pass

    def solve(self):
        pass


class FindLastCreatedTask(Task):
    def __init__(self, path, extension):
        super().__init__()
        self.path = path
        self.extension = extension

    def solve(self):
        files = os.listdir(self.path)
        ext_files = list(filter(lambda f: f.endswith(self.extension), files))
        younger = min(ext_files, key=lambda f: os.stat(self.path + f).st_mtime)
        ext_files.remove(younger)
        younger_and_other = [younger,
                             list(filter(lambda f: os.stat(self.path + f).st_mtime >=
                                                   os.stat(self.path + younger).st_mtime - 10, ext_files))]
        return younger if len(ext_files) == 1 else younger_and_other


class ListSubtractionTask(Task):
    def __init__(self, minuend, subtrahend, mode):
        super().__init__()
        self.minuend = minuend
        self.subtrahend = subtrahend
        self.mode = mode

    def solve(self):
        res = []
        if self.mode == "index":
            for index, element in enumerate(self.minuend):
                if not self.subtrahend.__contains__(element):
                    res.append(element)
            return res
        elif self.mode == "collection":
            return list(set(self.minuend) - set(self.subtrahend))


class RewriteTestCasesTask(Task):
    def __init__(self, path, lines_number):
        super().__init__()
        self.path = path
        self.lines_number = lines_number

    def solve(self):
        source_file = FileCapture(self.path)
        source_file_contents = source_file.read_file_lines()
        source_file_contents.separate_lines(self.lines_number)
        header = source_file_contents.header
        source_file.write_file_contents(header, source_file_contents.lines_to_keep)
        result_file_path = PathFinder(self.path).get_result_path()
        result_file = FileCapture(result_file_path)
        result_file.write_file_contents(header, source_file_contents.lines_to_relocate)
        return result_file_path
