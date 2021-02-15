__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '15/02/2021'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        temp = []

        for node in queue:
            level.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

        result.append(level)
        queue = temp

    return result
