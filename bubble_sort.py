def bubble_sort(seq):
    size = len(seq) - 1
    for num in range(size, 0, -1):
        for i in range(num):
            if seq[i] > seq[i + 1]:
                temp = seq[i]
                seq[i] = seq[i + 1]
                seq[i + 1] = temp
    return seq


if __name__ == "__main__":
    seq = [9, 6, 2, 4, 5, 6, 8, 1]
    print(bubble_sort(seq))
