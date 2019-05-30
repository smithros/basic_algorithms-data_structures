def insertion_sort(array):
    for i in range(1, len(array)):# to swap an item with the previous one we need to start 1
        j = i
        temp = array[j]  # temp used for comparing with previous item 
        while j > 0 and temp < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp
    return array


if __name__ == "__main__":
    array = [6, 1, 9, 8, 2, 5, 4, 3, 7]
    print("Before insertion sort: \n" + str(array))
    print("After insertion sort: ")
    print(insertion_sort(array))
