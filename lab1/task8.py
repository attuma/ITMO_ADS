def swap_sort(arr):
    swaps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps.append(f"Swap elements at indices {i + 1} and {min_idx + 1}.")

    swaps.append("No more swaps needed.")
    return swaps