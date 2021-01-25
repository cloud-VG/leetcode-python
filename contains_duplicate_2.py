__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '25/01/2021'


def solution(nums: list[int], k: int) -> bool:
    map_ = {}
    for i, n in enumerate(nums):
        if n in map_ and i - map_[n] <= k:
            return True
        map_[n] = i
    return False


if __name__ == '__main__':
    N = [1, 0, 1, 1]
    K = 1
    print(solution(N, K))
