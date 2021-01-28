__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '28/01/2021'


class Solution:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.window = []

    def next(self, n: int) -> float:
        if len(self.window) == self.window_size:
            self.window.pop(0)
        self.window.append(n)
        return round(sum(self.window) / len(self.window), 2)


if __name__ == '__main__':
    s = Solution(3)
    for i in [1, 10, 3, 5]:
        print(s.next(i))
