__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '31/01/2021'


def solution(nums: list[int]) -> int:
    for n in nums:
        if nums.count(n) == 1:
            return n


if __name__ == '__main__':
    N = [0, 1, 0, 1, 0, 1, 99]
    print(solution(N))
