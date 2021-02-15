__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '15/02/2021'


def solution(points: list[list[int]], k: int) -> list[list[int]]:
    points.sort(key=lambda point: ((0 - point[0]) ** 2 + (0 - point[1]) ** 2) ** 0.5)
    return points[:k]


if __name__ == '__main__':
    P = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(solution(P, K))
