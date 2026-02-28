def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Recursively sort left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # pivot as last element
    i = low - 1        # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place pivot correctly
    return i + 1


# Input
arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)