# A deque is a double-ended queue, which can roughly be seen as an union of
# a stack and a queue:
# deque also can be accessed from collections module


class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return '{}'.format(self.items)


def main():
    dq = Deque()
    dq.add_front(1)
    dq.add_front(2)
    dq.add_front(3)
    dq.add_rear(40)
    dq.add_rear(50)
    print(dq.size())
    print(dq)
if __name__ == "__main__":
    main()
