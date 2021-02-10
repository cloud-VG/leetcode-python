__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '10/02/2021'


def solution(a: list[list[int]]) -> list[list[int]]:
    result = []
    for row in a:
        result.append([x ^ 1 for x in row[::-1]])
    return result


if __name__ == '__main__':
    A = [[1, 1, 0], [1, 0, 0], [0, 1, 0]]
    print(solution(A))
