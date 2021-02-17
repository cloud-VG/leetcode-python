__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '17/02/2021'


def dfs(grid: list[list[int]], i: int, j: int) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return 0

    grid[i][j] = 0
    count = 1

    count += dfs(grid, i + 1, j)
    count += dfs(grid, i - 1, j)
    count += dfs(grid, i, j + 1)
    count += dfs(grid, i, j - 1)

    return count


def solution(grid: list[list[int]]) -> int:
    max_area = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                max_area = max(max_area, dfs(grid, i, j))

    return max_area


if __name__ == '__main__':
    G = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(solution(G))
