def merge(arr, lb, mid, ub):
    B = [0] * len(arr)

    i = lb
    j = mid + 1
    k = lb

    while i <= mid and j <= ub:
        if arr[i] <= arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        B[k] = arr[i]
        i += 1
        k += 1

    while j <= ub:
        B[k] = arr[j]
        j += 1
        k += 1

    for k in range(lb, ub + 1):
        arr[k] = B[k]


def merge_sort(arr, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid + 1, ub)
        merge(arr, lb, mid, ub)


# User input
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

print("Original array:", arr)

merge_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)