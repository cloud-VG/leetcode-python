__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '16/01/2021'


def is_pow_of_two(n: int) -> bool:
    i = 1

    while i < n:
        i *= 2

    return i == n


if __name__ == '__main__':
    num = int(input())
    print(is_pow_of_two(num))
