__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '05/02/2021'


def solution(n: int) -> bool:
    i = n % 2
    n = n // 2
    while n:
        if i == n % 2:
            return False
        i = n % 2
        n = n // 2
    return True


if __name__ == '__main__':
    N = 10
    print(solution(N))
