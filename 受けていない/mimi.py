m = int(input())

def solve(tree,op,idx):

    # if the value of list is not symbol then return the number
    if op[idx] not in ['*','+']:
        return int(op[idx])

    if op[idx] == '+':
        ans = 0 
    elif op[idx] == '*':
        ans = 1    
    for i in range(len(tree[idx])):
        # print(idx,i)
        if op[idx] == '+':
            ans = ans + solve(tree,op,tree[idx][i])
        elif op[idx] == '*':
            ans = ans * solve(tree,op,tree[idx][i])

    # print(ans)
    return ans

for i in range(m):
    tree = list()
    a = input().split(',')
    b = input().split(',')
    a = [int(x) for x in a] # input is string, converting them to integers

    for j in range(len(a)):
        tree.append(list())

    root = 0
    for j in range(len(a)):
        if a[j] != -1:
            tree[a[j]].append(j) # creating adjacency list
        else:
            root = j
    # print(tree)
    print("answer: " ,str(solve(tree,b,root)))