import stack


def reverse_string_with_stack(str1):
    s = stack.Stack()
    rev_str = ""
    for c in str1:
        s.push(c)
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str


def test_method():
    str1 = "Juice WRLD - Wasted"
    print(reverse_string_with_stack(str1))
    print("Test passed!")


if __name__ == "__main__":
    test_method()
