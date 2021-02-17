__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '17/02/2021'


def solution(s: str, k: int) -> str:
    result = ''
    length = 0
    i = len(s) - 1
    while i >= 0:
        if s[i] == '-':
            i -= 1
        elif length and length % k == 0:
            result = '-' + result
            length = 0
        else:
            result = s[i].upper() + result
            length += 1
            i -= 1
    return result


if __name__ == '__main__':
    S = '2-5g-3-J'
    K = 2
    print(solution(S, K))
