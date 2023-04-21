# Insert your code in this file

class Operations:
    KEEP = 0
    INSERT = 1
    REMOVE = 2

def myers(A, B):
    frontiers = {1: (0, [])}

    for D in range(len(A) + len(B) + 1):
        for k in range(-D, D + 1, 2):
            cond = k == -D or k != D and frontiers[k - 1][0] < frontiers[k + 1][0]

            x, history = frontier[(k + 1) if cond else (k - 1)]
            x += 0 if cond else 1
            y = x - k

            history = history[:]

            if y > 0 and y <= len(B) and cond:
                history.append((Operations.INSERT, B[y - 1]))
            elif x > 0 and x <= len(A):
                history.append((Operations.REMOVE, A[x - 1]))

            while x < len(A) and y < len(B)
            
            
