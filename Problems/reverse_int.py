__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '24/01/2021'


def solution(x: int) -> int:
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0

    str_x = str(x)

    if x < 0:
        rev_x = int('-' + str_x[:0:-1])
    else:
        rev_x = int(str_x[::-1])

    if rev_x > 2 ** 31 - 1 or rev_x < -2 ** 31:
        return 0
    return rev_x


if __name__ == '__main__':
    X = -123
    print(solution(X))
