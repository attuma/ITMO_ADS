def primitive_calculator(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops = dp[i - 1] + 1

        if i % 2 == 0:
            min_ops = min(min_ops, dp[i // 2] + 1)
        if i % 3 == 0:
            min_ops = min(min_ops, dp[i // 3] + 1)

        dp[i] = min_ops

    nums = []
    curr = n
    while curr > 1:
        nums.append(curr)
        if curr % 3 == 0 and dp[curr // 3] == dp[curr] - 1:
            curr //= 3
        elif curr % 2 == 0 and dp[curr // 2] == dp[curr] - 1:
            curr //= 2
        else:
            curr -= 1
    nums.append(1)

    return dp[n], nums[::-1]