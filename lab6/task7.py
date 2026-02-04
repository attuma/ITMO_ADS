def solve_stones(n, k, s, pairs):
    is_valid = [[False] * 26 for _ in range(26)]
    for p in pairs:
        u = ord(p[0]) - 97
        v = ord(p[1]) - 97
        is_valid[u][v] = True

    cnt = [0] * 26
    ans = 0

    for char in s:
        curr_code = ord(char) - 97

        for prev_code in range(26):
            if cnt[prev_code] > 0:
                if is_valid[prev_code][curr_code]:
                    ans += cnt[prev_code]

        cnt[curr_code] += 1

    return ans