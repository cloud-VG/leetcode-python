__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '25/01/2021'


def solution(s: str, t: str) -> str:
    for char in t:
        if t.count(char) != s.count(char):
            return char


if __name__ == '__main__':
    S = 'ae'
    T = 'aea'
    print(solution(S, T))
