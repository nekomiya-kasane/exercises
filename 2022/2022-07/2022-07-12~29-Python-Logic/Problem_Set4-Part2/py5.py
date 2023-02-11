def are_parts_nonoverlapping(p):
    n = len(p)
    if n < 2:
        return True
    for i in range(n-1):
        for j in range(i+1, n):
            for a in p[i]:
                for b in p[j]:
                    if a == b:
                        return False
    return True

def do_parts_contain_element(x, p):
    for s in p:
        if x in s:
            return True
    return False

def do_parts_cover_set(s, p):
    for x in s:
        if not do_parts_contain_element(x, p):
            return False
    return True

def do_parts_have_nothing_extra(s, p):
    for q in p:
        for e in q:
            if e not in s:
                return False
    return True

def is_partition(s, p):
    if (not do_parts_have_nothing_extra(s, p)) or \
       (not do_parts_cover_set(s,p)) or \
       (not are_parts_nonoverlapping(p)):
       return False
    return True