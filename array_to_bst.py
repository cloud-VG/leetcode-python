__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '25/01/2021'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(n: list[int], left: int, right: int) -> TreeNode:
    if left > right:
        return None
    mid = left + (right - left) // 2
    current = TreeNode(n[mid])
    current.left = build_tree(n, left, mid - 1)
    current.right = build_tree(n, mid + 1, right)
    return current


def solution(nums: list[int]) -> TreeNode:
    if not nums:
        return None
    return build_tree(nums, 0, len(nums) - 1)


# extra function to print result
def _inorder(root: TreeNode) -> list:
    """Perform inorder traversal on the tree"""
    if not root:
        return []
    value = [root.val]
    return _inorder(root.left) + value + _inorder(root.right)


if __name__ == '__main__':
    N = [-10, -3, 0, 5, 9]
    node = solution(N)
    print(_inorder(node))
