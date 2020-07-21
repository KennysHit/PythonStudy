if __name__ == '__main__':
    arr = [2, 4, 1, 7, 8, 3, 5, 9, 10, 6, 0, 22, 18, 17, 11, 12, 19, 15, 13, 14, 16, 21]
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr)