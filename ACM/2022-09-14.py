
# class TreeNode:
#     def __init__(self, val):
#         self.data: int = val
#         self.left: TreeNode | None = None
#         self.right: TreeNode | None = None
     
# def printTree(parent):
#     curr = parent
#     while (curr != None):
#         print(curr.data,end=' ')
#         curr = curr.right

# def inorder(cur, last):
#     if (not cur):
#         return
#     inorder(cur.left, last)
#     last.left = None
#     last.right = cur
#     last = cur
#     inorder(cur.right, last)
 
# def tolist(parent, last):
#     dummy = TreeNode(-1)
#     last = dummy
#     inorder(parent, last)
#     last.left = None
#     last.right = None
#     ret = dummy.right
 
#     return ret
 
 
# # Driver code
# if __name__ == '__main__':
#     root = TreeNode(5)
#     root.left = TreeNode(3)
#     root.right = TreeNode(7)
#     root.left.left = TreeNode(2)
#     root.left.right = TreeNode(4)
#     root.right.left = TreeNode(6)
#     root.right.right = TreeNode(8)
 
#     # Calling required function
#     printTree(tolist(root, None))

# Node of the binary tree

from collections import deque

global last

class TreeNode :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(curr):
    global last
    if (curr == None):
        return
    inorder(curr.left)
    last.left = None
    last.right = curr
    last = curr
    inorder(curr.right)
 
def to_list(parent):
    global last
    ps = TreeNode(-1)
    last = ps
    inorder(parent)
 
    last.left = None
    last.right = None
    ret = ps.right
 
    return ret

if __name__ == '__main__':

    root = TreeNode(int(input()))
    s = None
    qu = deque()
    qu.appendleft(root)
    # build tree
    while qu:
        lf = input()
        if not len(lf.strip()):
            break
        rt = input()
        this = qu.popleft()
        this.left = TreeNode(int(lf))
        this.right = TreeNode(int(rt)) if len(rt.strip()) else None
        qu.append(this.left)
        if this.right:
            qu.append(this.right)

    res = to_list(root)