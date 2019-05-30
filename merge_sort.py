def merge_sort(seq):
    if len(seq) < 2:
        return seq
    result = []
    mid = int(len(seq)/2)
    y = merge_sort(seq[:mid])
    z = merge_sort(seq[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result

array = [6, 1, 9, 8, 2, 5, 4, 3, 7]
print(merge_sort(array))
