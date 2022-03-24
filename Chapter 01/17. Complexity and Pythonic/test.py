l = [5, 2, 7, 9, 6, 4, 3, 0, 1]


def first_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(first_sort(l))