__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '24/01/2021'


def solution(n: int) -> int:
    """The isBadVersion(version) API is already defined for you."""
    min_ = 1
    max_ = n
    while min_ < max_:
        version = min_ + (max_ - min_) // 2
        if isBadVersion(version):
            max_ = version
        else:
            min_ = version + 1
    return min_

