__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '06/02/2021'


def solution(a: list[int]) -> bool:
    increasing = True
    decreasing = True

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            decreasing = False
        if a[i] < a[i + 1]:
            increasing = False

    return increasing or decreasing


if __name__ == '__main__':
    A = [1, 2, 4, 5]
    print(solution(A))
