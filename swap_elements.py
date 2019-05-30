def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
    return A


array = [1, 2, 3]
print(swap(array, 0, 1))
