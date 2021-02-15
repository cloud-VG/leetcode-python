__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '15/02/2021'


def fill(image: list[list[int]], r: int, c: int, color: int, new_color: int):
    if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != color:
        return None

    image[r][c] = new_color
    fill(image, r + 1, c, color, new_color)
    fill(image, r - 1, c, color, new_color)
    fill(image, r, c + 1, color, new_color)
    fill(image, r, c - 1, color, new_color)


def solution(image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    if image[sr][sc] == new_color:
        return image
    fill(image, sr, sc, image[sr][sc], new_color)
    return image


if __name__ == '__main__':
    IMAGE = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    SR = 1
    SC = 1
    N_COLOR = 2
    print(solution(IMAGE, SR, SC, N_COLOR))
