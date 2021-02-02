__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '02/02/2021'


def solution(nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


if __name__ == '__main__':
    N = [0, 1, 2, 2, 3, 0, 4, 2]
    V = 2
    print(solution(N, V))
