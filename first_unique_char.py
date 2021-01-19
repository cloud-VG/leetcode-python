__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '19/01/2021'


def solution(s: str) -> int:
    for i, char in enumerate(s):
        if s.count(char) == 1:
            return i
    return -1


if __name__ == '__main__':
    S = 'loveleetcode'
    print(solution(S))
