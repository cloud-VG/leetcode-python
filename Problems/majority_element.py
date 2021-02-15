__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '31/01/2021'


def solution(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == '__main__':
    N = [2, 2, 1, 1, 1, 2, 2]
    print(solution(N))
