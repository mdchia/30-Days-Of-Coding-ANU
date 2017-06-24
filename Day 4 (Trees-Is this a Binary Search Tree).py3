""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    def checkBSTBranch(root,min,max):
        if root is None:
            return True
        if not (min<root.data<max):
            return False
        if root.left!=None and root.left.data>=root.data:
            return False
        if root.right!=None and root.right.data<=root.data:
            return False
        return checkBSTBranch(root.left,min,root.data) and checkBSTBranch(root.right,root.data,max)
    return checkBSTBranch(root,-float("inf"),float("inf"))
    
