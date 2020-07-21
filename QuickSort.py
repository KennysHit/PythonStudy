def quickSort(array, left, right):
    if left < right:
        mark = array[left]
        i = left
        j = right
        while i < j:

            while i < j and array[j] >= mark:
                j = j - 1
            if i < j:
                array[i] = array[j]
                i = i + 1

            while i < j and array[i] <= mark:
                i = i + 1
            if i < j:
                array[j] = array[i]
                j = j - 1

        array[i] = mark
        quickSort(array, left, i - 1)
        quickSort(array, i + 1, right)


if __name__ == '__main__':
    arr = [2, 4, 1, 7, 8, 3, 5, 9, 10, 6, 0, 22, 18, 17, 11, 12, 19, 15, 13, 14, 16, 21]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
