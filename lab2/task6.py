def max_cross(arr, low, mid, high):
    left_sum = float('-inf')
    max_l = mid
    curr = 0
    for i in range(mid, low - 1, -1):
        curr += arr[i]
        if curr > left_sum:
            left_sum = curr
            max_l = i

    right_sum = float('-inf')
    max_r = mid + 1
    curr = 0
    for i in range(mid + 1, high + 1):
        curr += arr[i]
        if curr > right_sum:
            right_sum = curr
            max_r = i

    return max_l, max_r, left_sum + right_sum


def find_max(arr, low, high):
    if high == low:
        return low, high, arr[low]

    mid = (low + high) // 2

    l_low, l_high, l_sum = find_max(arr, low, mid)
    r_low, r_high, r_sum = find_max(arr, mid + 1, high)
    c_low, c_high, c_sum = max_cross(arr, low, mid, high)

    if l_sum >= r_sum and l_sum >= c_sum:
        return l_low, l_high, l_sum
    elif r_sum >= l_sum and r_sum >= c_sum:
        return r_low, r_high, r_sum
    else:
        return c_low, c_high, c_sum
