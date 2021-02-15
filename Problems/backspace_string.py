__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '21/01/2021'


def helper(s: str) -> str:
    list_s = []
    for c in s:
        if c != '#':
            list_s.append(c)
        elif list_s:
            list_s.pop()
    return ''.join(list_s)


def solution(s: str, t: str) -> bool:
    return helper(s) == helper(t)


if __name__ == '__main__':
    S = 'a##c'
    T = '#a#c'
    print(solution(S, T))
