__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '23/01/2021'


def solution(nums: list[int]) -> None:
    """Do not return anything, modify nums in-place instead."""
    index = 0

    for n in nums:
        if n != 0:
            nums[index] = n
            index += 1

    for i in range(index, len(nums)):
        nums[i] = 0


if __name__ == '__main__':
    N = [0, 1, 0, 3, 12]
    solution(N)
    print(N)
