def quick_sort(seq):
    if len(seq) < 2: return seq
    mid = len(seq) // 2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid + 1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x >= pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)


if __name__ == "__main__":
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    print(quick_sort(seq))
