def binary_search(lst, value):
    first = 0
    middle = 0
    last = len(lst) - 1

    while first <= last:
        middle = (first + last) // 2
        if value == lst[middle]:
            return middle
        elif value > lst[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return "Is not a list value"


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(lst, 11))
