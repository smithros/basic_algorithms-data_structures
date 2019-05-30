# String permutation in lexicographically order with repetition of characters in the string


def permute(entry):
    count_map = {}
    for ch in entry:
        if ch in count_map.keys():
            count_map[ch] = count_map[ch] + 1
        else:
            count_map[ch] = 1

    keys = sorted(count_map)
    container = []
    count = []
    for key in keys:
        container.append(key)
        count.append(count_map[key])
    result = [0 for x in range(len(entry))]
    permute_util(container, count, result, 0)


def permute_util(container, count, result, level):
    if level == len(result):
        print(list(reversed(result)))
        return

    for i in range(len(container)):
        if count[i] == 0:
            continue
        result[level] = container[i]
        count[i] -= 1
        permute_util(container, count, result, level + 1)
        count[i] += 1


if __name__ == '__main__':
    data = ["A", "B", "C"]
    permute(data)
