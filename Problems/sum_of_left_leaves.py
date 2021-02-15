__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '07/02/2021'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode) -> int:
    if not root:
        return 0
    elif root.left and not root.left.left and not root.left.right:
        return root.left.val + solution(root.right)
    else:
        return solution(root.left) + solution(root.right)
