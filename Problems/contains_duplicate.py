__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '18/01/2021'


def solution(nums: list[int]) -> bool:
    nums_set = set(nums)
    if len(nums_set) == len(nums):
        return False
    return True


if __name__ == '__main__':
    N = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(solution(N))
