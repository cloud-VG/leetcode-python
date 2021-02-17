__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '17/02/2021'


def solution(stones: list[int]) -> bool:
    for i in range(3, len(stones)):
        if stones[i] > stones[i - 1] * 2:
            return False

    stones_set = set(stones)

    reachable_stones = [(0, 0)]
    last_stone = stones[-1]

    while reachable_stones:
        stone, dist = reachable_stones.pop()

        for jump in [dist - 1, dist, dist + 1]:
            if jump <= 0:
                continue

            next_stone = stone + jump

            if next_stone == last_stone:
                return True

            elif next_stone in stones_set:
                reachable_stones.append((next_stone, jump))

    return False


if __name__ == '__main__':
    S = [0, 1, 3, 5, 6, 8, 12, 17]
    print(solution(S))
