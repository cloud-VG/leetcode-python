__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '21/01/2021'


def solution(s: str, t: str) -> bool:
    list_s = []
    list_t = []
    for c in s:
        if c != '#':
            list_s.append(c)
        elif list_s:
            list_s.pop()
    for c in t:
        if c != '#':
            list_t.append(c)
        elif list_t:
            list_t.pop()
    return ''.join(list_s) == ''.join(list_t)


if __name__ == '__main__':
    S = 'a##c'
    T = '#a#c'
    print(solution(S, T))
