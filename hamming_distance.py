__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '31/01/2021'


def solution(x: int, y: int) -> int:
    result = 0
    while x > 0 or y > 0:
        result += (x % 2) ^ (y % 2)
        x >>= 1
        y >>= 1
    return result


if __name__ == '__main__':
    X = 1
    Y = 4
    print(solution(X, Y))
