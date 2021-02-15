__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '19/01/2021'


def solution(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    S = 'anagram'
    T = 'nagaram'
    print(solution(S, T))
