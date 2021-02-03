__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '02/02/2021'


def solution(n: int) -> int:
    fib = [1, 1]
    i = 1
    while n >= len(fib):
        fib.append(fib[i] + fib[i - 1])
        i += 1
    return fib[-1]


if __name__ == '__main__':
    N = 3
    print(solution(N))
