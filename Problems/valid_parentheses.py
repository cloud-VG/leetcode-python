__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmail.vishwajeet@gmail.com'
__date__ = '16/01/2021'


def is_valid_string(s: str) -> bool:
    stack = []
    if len(s):
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif len(stack):
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
    return True


if __name__ == '__main__':
    string = input()
    print(is_valid_string(string))
