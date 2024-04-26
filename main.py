from collections import deque

opening_parenthesis: set = set('{[(')
closing_parenthesis: set = set('}])')
parenthesis_pairs: dict = {
        '}': '{',
        ']': '[',
        ')': '('
}


class Stack:
    def __init__(self):
        self._stack = deque()

    def __getitem__(self, index):
        return self._stack[index - 1]

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def size(self) -> int:
        return len(self._stack)

    def is_empty(self) -> bool:
        return self.size() == 0

    def top(self) -> str:
        return self._stack[-1]


def find_parentheses(text: str) -> int | str:
    stack: Stack = Stack()

    for index, char in enumerate(text, start=1):
        if char in opening_parenthesis:
            stack.push(char)
        elif char in closing_parenthesis:
            if stack.is_empty():
                return index
            if stack.top() != parenthesis_pairs[char]:
                return index
            stack.pop()

    if not stack.is_empty():
        return text.index(stack.top()) + 1

    return "Success"


if __name__ == "__main__":
    input_value: str = input()
    print(find_parentheses(input_value))
