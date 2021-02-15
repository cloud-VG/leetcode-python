__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '24/01/2021'


def solution(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < 9:
            nums[i] += 1
            return nums
        nums[i] = 0

    return [1] + nums


if __name__ == '__main__':
    N = [9, 9, 9]
    print(solution(N))
