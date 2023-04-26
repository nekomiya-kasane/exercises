from diff import *

# DiffCommands('wrong_1.txt')
# DiffCommands('wrong_2.txt')
# DiffCommands('wrong_3.txt')
# DiffCommands('wrong_4.txt')
# DiffCommands('wrong_5.txt')
# DiffCommands('wrong_6.txt')
# DiffCommands('wrong_7.txt')

diff_1 = DiffCommands('diff_1.txt')
print(diff_1)
diff_2 = DiffCommands('diff_2.txt')
print(diff_2)
diff_3 = DiffCommands('diff_3.txt')
print(diff_3)

pair_of_files = OriginalNewFiles('file_1_1.txt',    'file_1_2.txt')

print(pair_of_files.is_a_possible_diff(diff_1))
print(pair_of_files.is_a_possible_diff(diff_2))
print(pair_of_files.is_a_possible_diff(diff_3))

pair_of_files.output_diff(diff_1)