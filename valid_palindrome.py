__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '06/02/2021'

from re import sub


def solution(s: str) -> bool:
    s = s.lower()
    s = sub(r'[^a-zA-Z0-9]', '', s)
    return s == s[::-1]


if __name__ == '__main__':
    S = 'A man, a plan, a canal: Panama'
    print(solution(S))
