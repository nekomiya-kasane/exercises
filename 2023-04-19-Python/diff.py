# Insert your code in this file
import re
from itertools import combinations


class DiffCommandsError(Exception):
    message: str = ''

    def __init__(self, message=''):
        self.message = message

class DiffCommand:
    INSERT, DELETE, KEEP, CHANGE = 0, 1, 2, 3
    DICT = {INSERT: 'a', CHANGE: 'c', DELETE: 'd'}
    lfs, lfe, rts, rte = -1, -1, -1, -1
    type = KEEP

    def __init__(self, type, lfs, lfe, rts, rte) -> None:
        self.type = type
        self.lfs, self.lfe, self.rts, self.rte = lfs, lfe, rts, rte 

    def __str__(self):
        return '{}'.format((self.DICT[self.type], self.lfs, self.lfe, self.rts, self.rte))

class DiffCommands:
    commands: list[str] = []
    abCommands: list[DiffCommand] = []
    pattern: re.Pattern = re.compile(
        r'^(?:(\d+)(a)(\d+)(?:,(\d+))?)|(?:(\d+)(?:,(\d+))?(c)(?:(\d+)(?:,(\d+))?)?)|(?:(?:(\d+)(?:,(\d+))?)(d)(\d+)?)$', re.MULTILINE)

    def __init__(self, cmdFilePath=None):
        # print(cmdFilePath)
        if not cmdFilePath:
            return
        try:
            f = open(cmdFilePath, 'r')
            self.commands = [line.strip('\n') for line in f.readlines()]

            for cmd in self.commands:
                match = self.pattern.match(cmd)
                keys = self.pattern.findall(cmd)
                if not len(cmd) or not match \
                        or (match.span()[1] - match.span()[0] != len(cmd)) \
                        or len(keys) != 1:
                    raise DiffCommandsError

            f.close()

            if not self.__verify_commands():
                raise DiffCommandsError
            
            self.__build()

        except DiffCommandsError:
            print(__name__ + '.' + DiffCommandsError.__name__ + ': ' +
                  'Cannot possibly be the commands for the diff of two files')
            
    def __build(self):
        for cmd in self.commands:
            keys = self.pattern.findall(cmd)
            keys = list(filter(lambda x: x != '', keys[0]))
            type = DiffCommand.INSERT if 'a' in keys else DiffCommand.DELETE if 'd' in keys else DiffCommand.CHANGE
            index = keys.index(DiffCommand.DICT[type]) # type: ignore
            self.abCommands.append(DiffCommand(type, int(keys[0]), int(keys[index - 1]), int(keys[index + 1]), int(keys[-1])))

    def __verify_commands(self):
        cmds = self.commands

        lf = 0
        rt = 0
        try:
            for cmd in cmds:
                tokens = [token for token in self.pattern.findall(cmd)[
                    0] if token != '']
                if 'd' in tokens:
                    delim = tokens.index('d')
                    lfs, lfe = int(tokens[0]), int(tokens[delim - 1])
                    rts = int(tokens[delim + 1])
                    if lfs - lf != rts + 1 - rt:
                        return False
                    lf, rt = lfe + 1, rts + 1
                elif 'c' in tokens:
                    delim = tokens.index('c')
                    lfs, lfe = int(tokens[0]), int(tokens[delim - 1])
                    rts, rte = int(tokens[delim + 1]), int(tokens[-1])
                    if rts - rt != lfs - lf or rts - rt == 0:
                        return False
                    lf, rt = lfe + 1, rte + 1
                elif 'a' in tokens:
                    delim = tokens.index('a')
                    lfs = int(tokens[0])
                    rts, rte = int(tokens[delim + 1]), int(tokens[-1])
                    if lfs - lf != rts - 1 - rt:
                        return False
                    lf, rt = lfs + 1, rte + 1
        except Exception:
            return False

        return True
    
    def __str__(self) -> str:
        return '\n'.join(self.commands)


class OriginalNewFiles:

    leftLines: list[str] = []
    rightLines: list[str] = []
    leftLen: int = 0
    rightLen: int = 0

    dp: list[list] | None = None
    keeps: list = []

    def __init__(self, leftFile: str, rightFile: str):
        leftFilePtr = open(leftFile, 'r')
        rightFilePtr = open(rightFile, 'r')

        self.leftLines = leftFilePtr.readlines()
        self.rightLines = rightFilePtr.readlines()

        self.leftLen = len(self.leftLines)
        self.rightLen = len(self.rightLines)

    def __build_dp(self, force=False):
        if not force and self.dp:
            return

        if self.leftLines == self.rightLines:
            return [DiffCommands()]
        self.dp = []
        for i in range(len(self.leftLines) + 1):
            self.dp.append([0 for _ in range(len(self.rightLines) + 1)])

        self.keeps = []
        for i in range(1, len(self.dp)):
            for j in range(1, len(self.dp[i])):
                if self.leftLines[i - 1] == self.rightLines[j - 1]:
                    self.dp[i][j]  = self.dp[i - 1][j - 1] + 1
                    self.keeps.append([i, j, self.dp[i][j]])
                else:
                    self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i][j - 1])

        #self.keeps = []
        #self.dp = [[0] * self.leftLen for _ in range(self.rightLen)]
        #for i in range(1, self.rightLen):  # i: right, j: left
        #    for j in range(1, self.leftLen):
        #        if self.rightLines[i - 1] == self.leftLines[j - 1]:
        #            self.dp[i][j] = self.dp[i - 1][j - 1] + 1
        #            self.keeps.append((i, j, self.dp[i][j]))
        #        else:
        #            self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i][j - 1])

    def get_all_diff_commands(self) -> list[DiffCommands]:
        self.__build_dp()

        mx = self.keeps[-1][-1]
        diffs = list(combinations(self.keeps, mx))
        rms = []
        for i in range(len(diffs)):
            if diffs[i][0][2] != 1 or diffs[i][-1][2] != mx:
                rms.append(i)
                continue
            for j in range(1, len(diffs[i]) - 1):
                if diffs[i][j][2] != diffs[i][j - 1][2] + 1 or \
                   diffs[i][j][0] <= diffs[i][j - 1][0] or \
                   diffs[i][j][1] <= diffs[i][j - 1][1]:
                    rms.append(i)
                    break
        rms = sorted(rms, reverse=True)
        for index in rms:
            diffs.pop(index)

        solutions = []
        for diff in diffs:
            solution = DiffCommands()
            leftDiff = [0] + [diff[i][0]
                              for i in range(len(diff))] + [len(self.leftLines) + 1]
            rightDiff = [0] + [diff[i][1]
                               for i in range(len(diff))] + [len(self.rightLines) + 1]
            for i in range(1, len(leftDiff)):
                if leftDiff[i] > leftDiff[i - 1] + 1 and rightDiff[i] == rightDiff[i - 1] + 1:
                    if leftDiff[i] - leftDiff[i - 1] > 2:
                        solution.commands.append('{},{}d{}'.format(
                            leftDiff[i - 1] + 1, leftDiff[i] - 1, rightDiff[i] - 1))
                    else:
                        solution.commands.append('{}d{}'.format(
                            leftDiff[i] - 1, rightDiff[i] - 1))
                if leftDiff[i] == leftDiff[i - 1] + 1 and rightDiff[i] > rightDiff[i - 1] + 1:
                    if rightDiff[i] - rightDiff[i - 1] > 2:
                        solution.commands.append('{}a{},{}'.format(
                            leftDiff[i] - 1, rightDiff[i - 1] + 1, rightDiff[i] - 1))
                    else:
                        solution.commands.append('{}a{}'.format(
                            leftDiff[i] - 1, rightDiff[i] - 1))
                if leftDiff[i] > leftDiff[i - 1] + 1 and rightDiff[i] > rightDiff[i - 1] + 1:
                    if leftDiff[i] > leftDiff[i - 1] + 2 and rightDiff[i] > rightDiff[i - 1] + 2:
                        solution.commands.append('{},{}c{},{}'.format(
                            leftDiff[i - 1] + 1, leftDiff[i] - 1, rightDiff[i - 1] + 1, rightDiff[i] - 1))
                    elif leftDiff[i] == leftDiff[i - 1] + 2 and rightDiff[i] > rightDiff[i - 1] + 2:
                        solution.commands.append('{}c{},{}'.format(
                            leftDiff[i] - 1, rightDiff[i - 1] + 1, rightDiff[i] - 1))
                    elif leftDiff[i] > leftDiff[i - 1] + 2 and rightDiff[i] == rightDiff[i - 1] + 2:
                        solution.commands.append('{},{}c{}'.format(
                            leftDiff[i - 1] + 1, leftDiff[i] - 1, rightDiff[i] - 1))
                    else:
                        solution.commands.append('{}c{}'.format(
                            leftDiff[i] - 1, rightDiff[i] - 1))
            solutions.append(solution)
        solutions = sorted(solutions, key=lambda x: x.commands)
        return solutions

    def is_a_possible_diff(self, diff: DiffCommands):
        solutions = self.get_all_diff_commands()
        for sol in solutions:
            if diff.commands == sol.commands:
                return True

        return False

    def output_diff(self, diff: DiffCommands):
        if not self.is_a_possible_diff(diff):
            return
        
        diff.__build()

        for abcmd in diff.abCommands:
            if abcmd.type == DiffCommand.CHANGE or abcmd.type == DiffCommand.DELETE:
                for i in range(abcmd.lfs, abcmd.lfe):
                    print('< {}\n'.format(self.leftLines[i]))
            elif abcmd.type == DiffCommand.CHANGE or abcmd.type == DiffCommand.INSERT:
                for i in range(abcmd.rts, abcmd.rte + 1):
                    print('> {}\n'.format(self.rightLines[i]))

        return 

    def output_unmodified_from_original(self, diff: DiffCommands):
        if not self.is_a_possible_diff(diff):
            return
        
        out = ['...'] * self.leftLen
        
        diff.__build()

        for i in range(len(diff.abCommands) - 1):
            cmd = diff.abCommands[i]
            if cmd.type == DiffCommand.INSERT:
               out[diff.abCommands[0 if not i else i - 1].lfe : diff.abCommands[i + 1].lfs] \
                    = self.leftLines[diff.abCommands[0 if not i else i - 1].lfe : diff.abCommands[i + 1].lfs]
            elif cmd.type == DiffCommand.CHANGE:
               out[diff.abCommands[0 if not i else i - 1].lfe : diff.abCommands[i + 1].lfs - 1] \
                    = self.leftLines[diff.abCommands[0 if not i else i - 1].lfe : diff.abCommands[i + 1].lfs - 1]                
            elif cmd.type == DiffCommand.DELETE:
               out[diff.abCommands[0 if not i else i - 1].lfe : diff.abCommands[i + 1].lfs - 1] \
                    = self.leftLines[diff.abCommands[0 if not i else i - 1].lfe : diff.abCommands[i + 1].lfs - 1]

        for line in out:
            print(line)

    def output_unmodified_from_new(self, diff: DiffCommands):
        if not self.is_a_possible_diff(diff):
            return
        
        out = self.rightLines[:]
        
        diff.__build()





#class Operations:
#    KEEP = 0
#    INSERT = 1
#    REMOVE = 2
#
#
#def myers(A, B):
#    frontiers = {1: (0, [])}
#
#    for D in range(len(A) + len(B) + 1):
#        pss = []
#        for k in range(-D, D + 1, 2):
#            cond = k == - \
#                D or k != D and frontiers[k - 1][0] < frontiers[k + 1][0]
#
#            x, history = frontiers[(k + 1) if cond else (k - 1)]
#            x += 0 if cond else 1
#            y = x - k
#
#            history = history[:]
#
#            if y > 0 and y <= len(B) and cond:
#                history.append((Operations.INSERT, B[y - 1]))
#            elif x > 0 and x <= len(A):
#                history.append((Operations.REMOVE, A[x - 1]))
#
#            while x < len(A) and y < len(B) and A[x] == B[y]:
#                x += 1
#                y += 1
#                history.append((Operations.KEEP, A[x - 1]))
#
#            if x >= len(A) and y >= len(B):
#                pss.append(history)
#                # return history
#
#            frontiers[k] = x, history  # type: ignore
#        if len(pss):
#            return
#
#    raise ValueError("Unexpected return.")
#
#
#if __name__ == "__main__":
#    with open("file_2_1.txt") as f1:
#        with open("file_2_2.txt") as f2:
#            As = f1.readlines()
#            Bs = f2.readlines()
#
#    res = myers(As, Bs)
#    res
#