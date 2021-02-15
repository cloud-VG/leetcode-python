__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '25/01/2021'


def solution(moves: str) -> bool:
    if moves:
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')
    return True


if __name__ == '__main__':
    M = 'DRUDLDURRLULLDRU'
    print(solution(M))
