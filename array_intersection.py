__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '28/01/2021'


def solution(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    N1 = [4, 9, 5]
    N2 = [9, 4, 9, 8, 4]
    print(solution(N1, N2))
