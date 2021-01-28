__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '28/01/2021'

from functools import reduce


def solution(nums: list[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums) ^ reduce(lambda x, y: x ^ y, range(len(nums) + 1))


if __name__ == '__main__':
    N = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(solution(N))
