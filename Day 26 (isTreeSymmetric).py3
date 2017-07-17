#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def flattenTree(t):
    if t == None:
        return [0]
    return flattenTree(t.left) + [t.value] + flattenTree(t.right)

def isTreeSymmetric(t):
    if t == None:
        return True
    left_flat_tree=flattenTree(t.left)
    right_flat_tree=flattenTree(t.right)
    print(left_flat_tree)
    return left_flat_tree==right_flat_tree[::-1]
