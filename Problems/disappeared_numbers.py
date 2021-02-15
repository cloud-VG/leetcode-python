__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '06/02/2021'


def solution(nums: list[int]) -> list[int]:
    return list(set(list(range(1, len(nums) + 1))) - set(nums))


if __name__ == '__main__':
    N = [4, 3, 2, 7, 8, 2, 3, 1]
    print(solution(N))
