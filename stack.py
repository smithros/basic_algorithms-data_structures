class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty!")

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(str(stack.size()))  # 3
    print(str(stack.peek()))  # 3
    print(stack.pop())        # 3
    print(stack.peek())       # 2


if __name__ == "__main__":
    main()
