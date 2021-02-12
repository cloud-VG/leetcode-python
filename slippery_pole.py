"""The Slippery Pole.

Baba is partying hard and drinking hard drinks as his friend Vipul has won a big Coding Contest.
It has been several hours and now he is totally drunk. He is out of his senses and has started to climb a pole. The
rest of the people are trying to get him down but his dazed mind is unable to react and he is therefore not listening
to anyone. The pole is long and slippery. The drinks were super hard and the hangover is going to be for days. Vipul
is enjoying, laughing and observed that Baba slips down Y metre in the night and climbs X metre in the day time.

Now, he wants to know after how many days will Baba be at the top of the slippery pole, if the length of the pole is
N metre. Since he is out too, you have to find the answer for him.

Input Format:
-------------
    The first line of input consists of numbers of test cases, T
    Next T lines each consists of three space-separated integers X, Y and N.

Constraints:
-------------
    1<= T <=100
    1<= N <=10000000
    1<= Y < X <=N

Output Format:
-------------
    For each test case, print the number of days Baba will take to reach at top of the pole in a separate line.
========================================================================================================================

Sample TestCase:
-------------
    Input:
    -----
        2
        6 2 10
        4 3 10
    Output:
    -----
        2
        7
"""

__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '12/02/2021'


def solution():
    n_tests = int(input())

    for _ in range(n_tests):
        input_ = input()
        x, y, n = [int(i) for i in input_.split()]
        climbed = 0
        days = 0
        while climbed < n:
            days += 1
            climbed += x
            if climbed >= n:
                break
            climbed -= y
        print(days)


if __name__ == '__main__':
    solution()
