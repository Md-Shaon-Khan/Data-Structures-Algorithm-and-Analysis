def binary_search_all(arr, low, high, target):
    if low > high:
        return []

    mid = (low + high) // 2

    if arr[mid] == target:
        # Check left and right for duplicates
        result = [mid]

        # Search left side
        left = mid - 1
        while left >= 0 and arr[left] == target:
            result.append(left)
            left -= 1

        # Search right side
        right = mid + 1
        while right < len(arr) and arr[right] == target:
            result.append(right)
            right += 1

        return sorted(result)

    elif arr[mid] < target:
        return binary_search_all(arr, mid + 1, high, target)
    else:
        return binary_search_all(arr, low, mid - 1, target)


# Input
arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target element: "))

indexes = binary_search_all(arr, 0, len(arr) - 1, target)

if indexes:
    print(f"Element {target} found at indexes: {indexes}")
else:
    print(f"Element {target} not found.")