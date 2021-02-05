__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '05/02/2021'


def solution(jewels: str, stones: str) -> int:
    count = 0
    for jewel in jewels:
        count += stones.count(jewel)
    return count


if __name__ == '__main__':
    J = 'aA'
    S = 'aAAbbbb'
    print(solution(J, S))
