# Insert your code in this file

class DiffCommands:
    pass

class DiffCommandsError(Exception):


class Operations:
    KEEP = 0
    INSERT = 1
    REMOVE = 2

def myers(A, B):
    frontiers = {1: (0, [])}

    for D in range(len(A) + len(B) + 1):
        for k in range(-D, D + 1, 2):
            cond = k == -D or k != D and frontiers[k - 1][0] < frontiers[k + 1][0]

            x, history = frontiers[(k + 1) if cond else (k - 1)]
            x += 0 if cond else 1
            y = x - k

            history = history[:]

            if y > 0 and y <= len(B) and cond:
                history.append((Operations.INSERT, B[y - 1]))
            elif x > 0 and x <= len(A):
                history.append((Operations.REMOVE, A[x - 1]))

            while x < len(A) and y < len(B) and A[x] == B[y]:
                x += 1
                y += 1
                history.append((Operations.KEEP, A[x - 1]))
            
            if x >= len(A) and y >= len(B):
                return history

            frontiers[k] = x, history

    raise ValueError("Unexpected return.")


            
if __name__ == "__main__":
    with open("file_1_1.txt") as f1:
        with open("file_1_2.txt") as f2:
            As = f1.readlines()
            Bs = f2.readlines()

    res = myers(As, Bs)
    res
