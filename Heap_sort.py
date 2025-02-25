def max_heapify(arr, n, i):
    largest = i  # Assume root (largest)
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Start from last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)
    
    # Extract elements one by one from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        max_heapify(arr, i, 0)

def main():
    user_input = input("Enter numbers separated by space: ")
    arr = list(map(int, user_input.split()))
    
    # Build Max Heap
    build_max_heap(arr)
    print("Max Heap:", ", ".join(map(str, arr)))
    
    # Apply Heapsort
    heapsort(arr)
    print("Sorted Array:", ", ".join(map(str, arr)))

if __name__ == "__main__":
    main()
