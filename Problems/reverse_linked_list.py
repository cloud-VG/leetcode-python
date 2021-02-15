__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '15/02/2021'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    stack = []
    while head:
        stack.append(head)
        head = head.next

    for i in range(len(stack) - 1, 0, -1):
        stack[i].next = stack[i - 1]

    stack[0].next = None
    return stack[-1]
