__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '18/01/2021'


def solution(nums: list[int]) -> int:
    max_profit = 0
    min_price = 10e4 + 1
    for i, price in enumerate(nums):
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, nums[i] - min_price)
    return max_profit


if __name__ == '__main__':
    N = [7, 1, 5, 3, 6, 4]
    print(solution(N))
