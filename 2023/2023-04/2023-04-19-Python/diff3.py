#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


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
            index = keys.index(DiffCommand.DICT[type])  # type: ignore
            self.abCommands.append(DiffCommand(type, int(keys[0]), int(
                keys[index - 1]), int(keys[index + 1]), int(keys[-1])))

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


class DiffCommandsError(Exception):
    def __init__(self):
        pass


class OriginalNewFiles():
    def __init__(self, file_1, file_2):
        def getcontents(fp):
            ret = []
            f_handle = open(fp, 'r')
            content = f_handle.readlines()
            for line in content:
                line = line.strip('\n')
                ret.append(line)
            return ret
        self.out = []
        self._private = {}
        self.all_formats = []
        self.x = getcontents(file_1)
        self.y = getcontents(file_2)
        self.get_all_diff_commands()

    def lcs(self):
        xlen = len(self.x)
        ylen = len(self.y)
        self.directions = [None] * xlen
        for i in range(xlen):
            self.directions[i] = [None] * ylen
        self.lengths = [None] * (xlen + 1)
        for j in range(xlen + 1):
            self.lengths[j] = [None] * (ylen + 1)  # type: ignore
        for i in range(0, xlen + 1):
            self.lengths[i][0] = 0
        for j in range(0, ylen + 1):
            self.lengths[0][j] = 0
        for i in range(1, xlen + 1):
            for j in range(1, ylen + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.lengths[i][j] = self.lengths[i - 1][j - 1] + 1
                    self.directions[i - 1][j - 1] = 0  # left or up
                elif self.lengths[i - 1][j] > self.lengths[i][j - 1]:
                    self.lengths[i][j] = self.lengths[i - 1][j]
                    self.directions[i - 1][j - 1] = 1  # up
                elif self.lengths[i - 1][j] < self.lengths[i][j - 1]:
                    self.lengths[i][j] = self.lengths[i][j - 1]
                    self.directions[i - 1][j - 1] = -1  # left
                else:
                    self.lengths[i][j] = self.lengths[i - 1][j]
                    self.directions[i - 1][j - 1] = 2  # left or up
        self.lcslength = self.lengths[-1][-1]
        return self.directions, self.lengths

    def returnLCS(self):
        self.getCandidateList(0, 0, 0, [], [])
        self.out = list(set(self.out))

    def getCandidateList(self, curlen, i, j, sx, sy):
        if i >= len(self.directions) or j >= len(self.directions[0]):
            return

        for idx in range(i, len(self.directions)):
            for idj in range(j, len(self.directions[0])):
                if self.directions[idx][idj] == 0:
                    sx.append(str(idx+1))
                    sy.append(str(idj+1))
                    curlen += 1
                    if curlen == self.lcslength:
                        self.out.append(','.join(sx)+'|'+','.join(sy))
                    else:
                        self.getCandidateList(curlen, idx+1, idj+1, sx, sy)
                    sx.pop()
                    sy.pop()
                    curlen -= 1

    def get_all_diff_commands(self):
        def getformat(lpos, rpos, lefts, rights, fm):
            if len(lefts) or len(rights):
                if len(rights) == 0:  # operate d
                    if len(lefts) > 1:
                        fm += str(lefts[0]) + ',' + str(lefts[-1]
                                                          ) + 'd' + str(rpos - 1) + '\n'
                    else:
                        fm += str(lefts[0]) + 'd' + str(rpos - 1) + '\n'
                    lp = lpos
                    rp = rpos

                elif len(lefts) == 0:  # operate a
                    if len(rights) > 1:
                        fm += str(lpos - 1) + 'a' + \
                            str(rights[0]) + ',' + str(rights[-1]) + '\n'
                    else:
                        fm += str(lpos - 1) + 'a' + str(rights[0]) + '\n'
                    lp = lpos
                    rp = rpos
                else:
                    if len(lefts) > 1:
                        fm += str(lefts[0]) + ',' + str(lefts[-1]) + 'c'
                    else:
                        fm += str(lefts[0]) + 'c'
                    if len(rights) > 1:
                        fm += str(rights[0]) + ',' + str(rights[-1]) + '\n'
                    else:
                        fm += str(rights[0]) + '\n'
                    lp = lpos
                    rp = rpos

            else:
                lp = lpos
                rp = rpos
            return lp, rp, fm

        self.lcs()
        self.returnLCS()
        top_right = len(self.y)
        top_left = len(self.x)
        for item in set(self.out):
            left = item.split('|')[0]
            right = item.split('|')[1]
            left = list(map(lambda x: int(x), left.split(',')))
            right = list(map(lambda x: int(x), right.split(',')))
            lp = 0
            rp = 0
            lefts = []
            rights = []
            fm = ''
            for lpos, rpos in zip(left, right):
                if lpos > lp+1:
                    lp += 1
                    while (lp < lpos):
                        lefts.append(lp)
                        lp += 1
                if rpos > rp+1:
                    rp += 1
                    while (rp < rpos):
                        rights.append(rp)
                        rp += 1
                lp, rp, fm = getformat(
                    lpos, rpos, lefts, rights, fm)
                lefts = []
                rights = []
            while (lp < top_left):
                lp += 1
                lefts.append(lp)
            while (rp < top_right):
                rp += 1
                rights.append(rp)

            if len(lefts) or len(rights):
                if len(lefts) == 0:
                    if len(rights) > 1:
                        fm += str(lp) + 'a' + \
                            str(rights[0]) + ',' + str(rights[-1]) + '\n'
                    else:
                        fm += str(lp) + 'a' + str(rights[0]) + '\n'
                if len(rights) == 0:
                    if len(lefts) > 1:
                        fm += str(lefts[0]) + ',' + \
                            str(lefts[-1]) + 'd'+str(rp)+'\n'
                    else:
                        fm += str(lefts[0]) + 'd' + str(rp) + '\n'
            # fm = fm.strip('\n')
            if fm not in self.all_formats:
                self.all_formats.append(fm)
            self._private.setdefault(fm, [])
            self._private[fm].append([left, right])
        self.all_formats.sort()

        ret = []
        for line in self.all_formats:
            ret.append(line.strip('\n'))
        return ret

    def is_a_possible_diff(self, diffobj: DiffCommands):
        vertify = '\n'.join(diffobj.commands)+'\n'
        for fm in self.all_formats:
            if vertify == fm:
                return True
        return False

    def output_diff(self, diff):
        commands = diff.commands
        out_str = ''
        for cmd in commands:
            out_str += cmd+'\n'
            if 'd' in cmd:
                idx = cmd.index('d')
                for i in cmd[:idx].split(','):
                    out_str += '< '+self.x[int(i)-1]+'\n'
            if 'a' in cmd:
                idx = cmd.index('a')
                for i in cmd[idx+1:].split(','):
                    out_str += '> ' + self.y[int(i)-1] + '\n'
            if 'c' in cmd:
                idx = cmd.index('c')
                ls = int(cmd[:idx].split(',')[0])
                le = int(cmd[:idx].split(',')[-1])
                rs = int(cmd[idx+1:].split(',')[0])
                re = int(cmd[idx + 1:].split(',')[-1])
                for i in range(ls, le+1):
                    out_str += '< ' + self.x[int(i)-1] + '\n'
                out_str += '---\n'
                for i in range(rs, re+1):
                    out_str += '> ' + self.y[int(i)-1] + '\n'
        print(out_str.strip('\n'))

    def output_unmodified_from_original(self, diffobj: DiffCommands):
        out_str = ''
        vertify = '\n'.join(diffobj.commands)+'\n'
        for fm in self.all_formats:
            if vertify == fm:
                left = self._private[fm][0][0]
        pre_idx = 0
        for idx in left:
            if idx - pre_idx > 1:
                out_str += '...\n'

            if idx <= len(self.x):
                out_str += self.x[idx - 1]+'\n'
            pre_idx = idx

        if pre_idx < len(self.x):
            out_str += '...\n'

        print(out_str.strip('\n'))

    def output_unmodified_from_new(self, diffobj: DiffCommands):
        out_str = ''
        vertify = '\n'.join(diffobj.commands)+'\n'
        for fm in self.all_formats:
            if vertify == fm:
                right = self._private[fm][0][1]
        pre_idx = 0
        for idx in right:
            if idx - pre_idx > 1:
                out_str += '...\n'
            if idx <= len(self.y):
                out_str += self.y[idx - 1]+'\n'
            pre_idx = idx
        if pre_idx < len(self.y):
            out_str += '...\n'
        print(out_str.strip('\n'))
