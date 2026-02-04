def scarecrow_sort(n, k, arr):
    for i in range(k):
        sub = []
        for j in range(i, n, k):
            sub.append(arr[j])
        sub.sort()
        idx = 0
        for j in range(i, n, k):
            arr[j] = sub[idx]
            idx += 1

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return "НЕТ"
    return "ДА"
