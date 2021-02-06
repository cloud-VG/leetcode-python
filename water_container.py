__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '06/02/2021'


def solution(height: list[int]) -> int:
    max_area = 0
    i, j = 0, len(height) - 1
    while i < j:
        h = min(height[i], height[j])
        w = j - i
        max_area = max(max_area, h * w)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area


if __name__ == '__main__':
    H = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution(H))
