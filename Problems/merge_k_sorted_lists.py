__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '17/02/2021'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(lists: list[ListNode]) -> ListNode:
    values = []

    for node in lists:
        while node:
            values.append(node.val)
            node = node.next
    
    head = current = ListNode(-1)

    for val in sorted(values):
        current.next = ListNode(val)
        current = current.next

    return head.next
