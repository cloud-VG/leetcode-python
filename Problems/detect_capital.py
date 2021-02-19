__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '19/02/2021'


def solution(word: str) -> bool:
    if word.isupper():
        return True
    elif word.islower():
        return True
    else:
        if word[0].isupper() and word[1:].islower():
            return True
    return False


if __name__ == '__main__':
    W = 'Google'
    print(solution(W))
