__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '19/01/2021'


def solution(nums: list[int], target: int) -> list[int]:
    h_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in h_map:
            return [h_map[diff], i]
        else:
            h_map[num] = i


if __name__ == '__main__':
    N = [2, 7, 11, 15]
    T = 9
    print(solution(N, T))
