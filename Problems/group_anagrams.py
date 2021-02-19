__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '19/02/2021'


def solution(s: list[str]) -> list[list[str]]:
    result = {}
    for word in s:
        key = tuple(sorted(word))
        if key not in result:
            result[key] = [word]
        else:
            result[key].append(word)

    return list(result.values())


if __name__ == '__main__':
    S = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution(S))
