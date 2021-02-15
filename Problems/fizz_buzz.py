__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '18/01/2021'


def fizz_buzz(n: int) -> list[str]:
    lst = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append('FizzBuzz')
        elif i % 3 == 0:
            lst.append('Fizz')
        elif i % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(str(i))
    return lst


if __name__ == '__main__':
    N = 15
    print(fizz_buzz(N))
