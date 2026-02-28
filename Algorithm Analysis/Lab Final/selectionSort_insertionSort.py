import time
import random

# ------------------ Input Orders ------------------
# 25 orders with random order_ID and quantity
orders = [(random.randint(100, 200), random.randint(1, 10)) for _ in range(25)]

print("Original Orders:")
print(orders)

# ------------------ Extract Order_IDs ------------------
order_ids = [order[0] for order in orders]
print("\nOrder IDs to sort:")
print(order_ids)

# ------------------ Selection Sort ------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# ------------------ Insertion Sort ------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# ------------------ Selection Sort Execution ------------------
ids_sel = order_ids.copy()
start = time.time()
selection_sort(ids_sel)
end = time.time()
print("\nSelection Sort Result (Order IDs):")
print(ids_sel)
print("Execution time:", int((end - start) * 1e9), "ns")

# ------------------ Insertion Sort Execution ------------------
ids_ins = order_ids.copy()
start = time.time()
insertion_sort(ids_ins)
end = time.time()
print("\nInsertion Sort Result (Order IDs):")
print(ids_ins)
print("Execution time:", int((end - start) * 1e9), "ns")