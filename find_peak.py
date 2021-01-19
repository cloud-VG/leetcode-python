__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '19/01/2021'


def solution(nums: list[int]) -> int:
    nums.insert(0, int(-2e31 - 1))
    nums.append(int(-2e31))
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i - 1
    return -1


if __name__ == '__main__':
    N = [1, 2, 1, 3, 5, 6, 4]
    print(solution(N))
