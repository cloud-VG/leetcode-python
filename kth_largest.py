__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '10/02/2021'


def solution(nums: list[int], k: int) -> int:
    return sorted(nums)[-k]


if __name__ == '__main__':
    N = [2, 8, 9, 6, 1, 0, 3]
    print(solution(N, 2))
