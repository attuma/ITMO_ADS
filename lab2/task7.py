def find_max_linear(arr):
    max_sum = float('-inf')
    curr_sum = 0
    start = end = temp_s = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_s
            end = i

        if curr_sum < 0:
            curr_sum = 0
            temp_s = i + 1

    return start, end, max_sum