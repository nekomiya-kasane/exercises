def properSubset(A, B):
    if len(A) >= len(B):
        return False
    for a in A:
        if not (a in B):
            return False
    return True

def even1(A):
    for a in A:
        if not (a & 0b1):
            return True
    return False

def evem2(A):
    for a in A:
        if a & 0b1:
            return False
    return True


    