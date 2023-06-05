import sys, os

class TextFileSys:

    openModes = ["r", "r+", "w", "w+", "a", "a+"]
    fs = {}
    opened = {}

    def open(self, filename: str, mode: str) -> int:
        if mode not in self.openModes:
            return -1
        if len(mode) and mode[0] == 'r' and (not os.path.exists(filename) or os.path.isdir(filename)):
            return -1
        
        try:
            self.fs[filename] = open(filename, mode)
            self.opened[filename] = True
        except Exception:
            return -1

        return 0
    
    def close(self, filename: str) -> int:
        if filename in self.opened and self.opened[filename] and self.fs[filename]:
            self.fs[filename].close()
            self.opened[filename] = False
            del self.opened[filename]
            del self.fs[filename]
            return 0
        return -1
    
    def write(self, filename: str, content: str) -> int:
        if filename in self.opened and self.opened[filename]:
            f = self.fs[filename]
            try:
                f.write(content)
                f.flush()
                return os.path.getsize(filename)
            except Exception:
                return -1
        return -1
    
    def read_all(self, filename: str) -> str:
        try:
            if filename in self.opened and self.opened[filename]:
                f = self.fs[filename]
                last = f.tell()
                f.seek(0)
                content = f.read()
                f.seek(last)
                if len(content):
                    return content
                return "null"
        except Exception:
            return "error"
        return "error"
    

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())

    sys.stdin.readline()

    print("null")

    function = TextFileSys()

    for _ in range(num - 1):
        cmd, value = sys.stdin.readline().strip().split("=")
        paras = value.strip().split(' ')
        filename = paras[0]

        if cmd == "open":
            mode = paras[1]
            print(function.open(filename, mode))
        elif cmd == "write":
            content = paras[1]
            print(function.write(filename, content))
        elif cmd == "close":
            print(function.close(filename))
        elif cmd == "readAll":
            print(function.read_all(filename))
        else:
            print("error input")
