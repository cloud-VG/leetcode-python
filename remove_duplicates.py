__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '07/02/2021'


def solution(nums: list[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


if __name__ == '__main__':
    N = [0, 0, 1, 2, 2, 2, 3]
    print(solution(N))
