__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '02/02/2021'


def solution_1(num: int) -> int:
    num = bin(num)[2:]
    temp = []
    for n in num:
        if n == '1':
            temp.append('0')
        else:
            temp.append('1')
    return int(''.join(temp), 2)


def solution_2(num: int) -> int:
    result = 0
    i = 1
    while num:
        result += (num % 2 ^ 1) * i
        num >>= 1
        i <<= 1
    return result


if __name__ == '__main__':
    N = 5
    print(solution_1(N))
    print(solution_2(N))
