__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '17/01/2021'


def get_single_number(nums: list) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor


if __name__ == '__main__':
    n = [4, 1, 2, 1, 2]
    print(get_single_number(n))
