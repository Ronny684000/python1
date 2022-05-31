import os
import random
import pathlib


def find_last_created(path, extension):
    files = os.listdir(path)
    ext_files = list(filter(lambda f: f.endswith(extension), files))
    younger = min(ext_files, key=lambda f: os.stat(path + f).st_mtime)
    ext_files.remove(younger)
    younger_and_other = [younger,
                         list(filter(lambda f: os.stat(path + f).st_mtime >= os.stat(path + younger).st_mtime - 10,
                                     ext_files))]
    return younger if len(ext_files) == 1 else younger_and_other


def collapse_lists_variant1(list1, list2):
    res = []
    for index, element in enumerate(list1):
        if not list2.__contains__(element):
            res.append(element)
    return res


def collapse_lists_variant2(list1, list2):
    return list(set(list1) - set(list2))


def select_cases(path, lines_number):
    f = open(path, "r+")
    header = f.readline()
    lines = f.readlines()
    print(lines)
    random_lines = random.sample(lines, lines_number)
    for line in random_lines:
        lines.remove(line)
    f.close()
    f = open(path, "w+")
    f.writelines(header)
    f.writelines(lines)
    f.close()
    file_name = os.path.basename(path)
    file_pure_name = os.path.splitext(file_name)[0]
    file_extension = os.path.splitext(file_name)[1]
    res_file_path = pathlib.Path(path).parent.resolve().__str__() + "/" + file_pure_name + "_res" + file_extension
    print(res_file_path)
    f = open(res_file_path, "w+")
    f.writelines(header)
    f.writelines(random_lines)
    return res_file_path


# task1
path_to_directory = 'C:\\Users\\Ronny\\Desktop\\test\\'
extension = '.txt'
file = find_last_created(path_to_directory, extension)
print(file)

# task2
listA = ["Alex", "Dima", "Kate", "Galina", "Ivan"]
listB = ["Dima", "Ivan", "Kate"]
subbedList1 = collapse_lists_variant1(listA, listB)
subbedList2 = collapse_lists_variant2(listA, listB)
print(subbedList1)
print(subbedList2)

# task3
path_to_source_file = 'C:\\Users\\Ronny\\Desktop\\test\\1.txt'
select_cases(path_to_source_file, 5)

