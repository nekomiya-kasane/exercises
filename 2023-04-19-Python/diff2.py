import re
import itertools

class DiffCommands:
    def __init__(self, file = None):
        try:
            self.file = file
            self.diffcommands = []
            self.left = [[0]]
            self.action = ['*']
            self.right = [[0]]
            if file is None:
                return
            with open(file) as file:
                for line in file:
                    self.diffcommands.append(line)
                    get_info = re.match('^(\d+(?:,\d+)?)([acd])(\d+(?:,\d+)?)$', line)
                    if get_info:
                        self.left.append([int(i) for i in get_info.groups()[0].split(',')])
                        self.action.append(get_info.groups()[1])
                        self.right.append([int(i) for i in get_info.groups()[2].split(',')])
                    else:
                        raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')

            for i in range(1, len(self.action)):
                if self.action[i] == 'a':
                    if len(self.left[i]) != 1:
                        raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                    else:
                        if self.left[i][0] - self.left[i - 1][-1] != self.right[i][0] - 1 - self.right[i - 1][-1]:
                            raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                if self.action[i] == 'c':
                    if self.left[i - 1][-1] + 1 >= self.left[i][0]:
                        raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                    else:
                        if self.left[i][0] - self.left[i - 1][-1] != self.right[i][0] - self.right[i - 1][-1]:
                            raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                if self.action[i] == 'd':
                    if len(self.right[i]) != 1:
                        raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                    else:
                        if self.left[i][0] - 1 - self.left[i - 1][-1] != self.right[i][0] - self.right[i - 1][-1]:
                            raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
        except Exception as e:
            print("sdf")
    def __str__(self):
        return (''.join(self.diffcommands)).strip()

class DiffCommandsError(Exception):
    def __init__(self, message):
        self.message = message

class OriginalNewFiles:
    def __init__(self, file1 = None, file2 = None):
        self.file1 = file1
        self.file2 = file2
        if not file1 or not file2:
            return
        self.leftLines = []
        self.rightLines = []
        with open(file1) as file:
            for line in file:
                self.leftLines.append(line)
        with open(file2) as file:
            for line in file:
                self.rightLines.append(line)

    def is_a_possible_diff(self, diffs):
        solutions = self.get_all_diff_commands()
        L = [solutions[i].diffcommands for i in range(len(solutions))]
        if diffs.diffcommands in [solutions[i].diffcommands for i in range(len(solutions))]:
            return True
        return False
    def output_diff(self, diffs):
        if not self.is_a_possible_diff(diffs):
            return
        for i in range(1, len(diffs.action)):
            print(diffs.diffcommands[i - 1], end = '')
            if diffs.action[i] == 'a':
                for j in range(diffs.right[i][0] - 1, diffs.right[i][-1]):
                    print('> ' + self.rightLines[j], end = '')
            elif diffs.action[i] == 'c':
                for j in range(diffs.left[i][0] - 1, diffs.left[i][-1]):
                    print('< ' + self.leftLines[j], end = '')
                print('---')
                for j in range(diffs.right[i][0] - 1, diffs.right[i][-1]):
                    print('> ' + self.rightLines[j], end = '')
            elif diffs.action[i] == 'd':
                for j in range(diffs.left[i][0] - 1, diffs.left[i][-1]):
                    print('< ' + self.leftLines[j], end = '')
        return
                
    def output_unmodified_from_original(self, diffs):
        if not self.is_a_possible_diff(diffs):
            return
        output_leftLines = []
        for line in self.leftLines:
            output_leftLines.append('...')

        for i in range(1, len(diffs.action)):
            if diffs.action[i] == 'a':
               output_leftLines[diffs.left[i - 1][-1] : diffs.left[i][0]] = self.leftLines[diffs.left[i - 1][-1] : diffs.left[i][0]]
            elif diffs.action[i] == 'c':
               output_leftLines[diffs.left[i - 1][-1] : diffs.left[i][0] - 1] = self.leftLines[diffs.left[i - 1][-1] : diffs.left[i][0] - 1]                
            elif diffs.action[i] == 'd':
               output_leftLines[diffs.left[i - 1][-1] : diffs.left[i][0] - 1] = self.leftLines[diffs.left[i - 1][-1] : diffs.left[i][0] - 1]

        if len(self.leftLines) > diffs.left[-1][-1]:
            for i in range(diffs.left[-1][-1], len(self.leftLines)):
                output_leftLines[i] = self.leftLines[i]
        output_leftLines.insert(0, '*')
        print(output_leftLines)
        for i in range(1, len(output_leftLines)):
            if output_leftLines[i] == '...' and output_leftLines[i - 1] != '...':
                print('...')
            elif output_leftLines[i] != '...':
                print(output_leftLines[i], end = '')
        return 
    def output_unmodified_from_new(self, diffs):
        if not self.is_a_possible_diff(diffs):
            return
        
        output_rightLines = []
        for line in self.rightLines:
            output_rightLines.append(line)
            
        for i in range(1, len(diffs.action)):
            if diffs.action[i] == 'a':
                start = diffs.right[i][0] - 1
                end = diffs.right[i][-1]
            elif diffs.action[i] == 'c':
                start = diffs.right[i][0] - 1
                end = diffs.right[i][-1]
            else:
                continue
            if start == end:
                output_rightLines[start] = '...'
            else:
                output_rightLines[start : end] = ['...'] * (end - start)
            
        output_rightLines.insert(0, '*')
        print(output_rightLines)
        for i in range(1, len(output_rightLines)):
            if output_rightLines[i] == '...' and output_rightLines[i - 1] != '...':
                print('...')
            elif output_rightLines[i] != '...':
                print(output_rightLines[i], end = '')
        return
    
    def get_all_diff_commands(self):
        if self.leftLines == self.rightLines:
            return [DiffCommands()]
        lcs_table = []
        for i in range(len(self.leftLines) + 1):
            lcs_table.append([0 for _ in range(len(self.rightLines) + 1)])

        
        same_commands = []
        for i in range(1, len(lcs_table)):
            for j in range(1, len(lcs_table[i])):
                if self.leftLines[i - 1] == self.rightLines[j - 1]:
                    lcs_table[i][j]  = lcs_table[i - 1][j - 1] + 1
                    same_commands.append([i, j, lcs_table[i][j]])
                else:
                    lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
        max_index_number = same_commands[-1][-1]
        diffs = list(itertools.combinations(same_commands, max_index_number))
        remove_position = []
        for i in range(len(diffs)):
            if diffs[i][0][2] != 1 or diffs[i][-1][2] != max_index_number:
                remove_position.append(i)
                continue
            for j in range(1, len(diffs[i]) - 1):
                if diffs[i][j][2] != diffs[i][j - 1][2] + 1 or \
                   diffs[i][j][0] <= diffs[i][j - 1][0] or \
                   diffs[i][j][1] <= diffs[i][j - 1][1]:
                    remove_position.append(i)
                    break
        remove_position = sorted(remove_position, reverse = True)
        for index in remove_position:
            diffs.pop(index)
        
        solutions = []
        for diff in diffs:
            solution = DiffCommands()
            diff_left = [0] + [diff[i][0] for i in range(len(diff))] + [len(self.leftLines) + 1]
            diff_right = [0] + [diff[i][1] for i in range(len(diff))] + [len(self.rightLines) + 1]
            for i in range(1, len(diff_left)):
                if diff_left[i] > diff_left[i - 1] + 1 and diff_right[i] == diff_right[i - 1] + 1:
                    if diff_left[i] - diff_left[i - 1] > 2:
                        solution.diffcommands.append('{},{}d{}\n'.format(diff_left[i - 1] + 1, diff_left[i] - 1, diff_right[i] - 1))
                    else:
                        solution.diffcommands.append('{}d{}\n'.format(diff_left[i] - 1, diff_right[i] - 1))
                if diff_left[i] == diff_left[i - 1] + 1 and diff_right[i] > diff_right[i - 1] + 1:
                    if diff_right[i] - diff_right[i - 1] > 2:
                        solution.diffcommands.append('{}a{},{}\n'.format(diff_left[i] - 1, diff_right[i - 1] + 1, diff_right[i] - 1))
                    else:
                        solution.diffcommands.append('{}a{}\n'.format(diff_left[i] - 1, diff_right[i] - 1))
                if diff_left[i] > diff_left[i - 1] + 1 and diff_right[i] > diff_right[i - 1] + 1:
                    if diff_left[i] > diff_left[i - 1] + 2 and diff_right[i] > diff_right[i - 1] + 2:
                        solution.diffcommands.append('{},{}c{},{}\n'.format(diff_left[i - 1] + 1, diff_left[i] - 1, diff_right[i - 1] + 1, diff_right[i] - 1))
                    elif diff_left[i] == diff_left[i - 1] + 2 and diff_right[i] > diff_right[i - 1] + 2:
                        solution.diffcommands.append('{}c{},{}\n'.format(diff_left[i] - 1, diff_right[i - 1] + 1,diff_right[i] - 1))
                    elif diff_left[i] > diff_left[i - 1] + 2 and diff_right[i] == diff_right[i - 1] + 2:
                        solution.diffcommands.append('{},{}c{}\n'.format(diff_left[i - 1] + 1, diff_left[i] - 1, diff_right[i] - 1))
                    else:
                        solution.diffcommands.append('{}c{}\n'.format(diff_left[i] - 1, diff_right[i] - 1))
            solutions.append(solution)
        solutions = sorted(solutions, key = lambda x : x.diffcommands)
        return solutions
                        
                        
            
        
