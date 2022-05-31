from project.task import FindLastCreatedTask, ListSubtractionTask, RewriteTestCasesTask


# task1
path_to_directory = 'C:/Users/Ronny/Desktop/test/'
extension = '.txt'
task1 = FindLastCreatedTask(path_to_directory, extension)
print(task1.solve())

# task2
listA = ["Alex", "Dima", "Kate", "Galina", "Ivan"]
listB = ["Dima", "Ivan", "Kate"]
task21 = ListSubtractionTask(listA, listB, "index")
task22 = ListSubtractionTask(listA, listB, "collection")
print(task21.solve())
print(task22.solve())

# task3
path_to_source_file = 'C:/Users/Ronny/Desktop/test/1.txt'
line_count = 4
task3 = RewriteTestCasesTask(path_to_source_file, line_count)
print(task3.solve())
