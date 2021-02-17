__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '17/02/2021'

from collections import Counter


def solution(s: str) -> str:
    result = ''
    counter = Counter(s)
    for k, v in counter.most_common():
        result += k * v
    return result


if __name__ == '__main__':
    S = 'loveleetcode'
    print(solution(S))
