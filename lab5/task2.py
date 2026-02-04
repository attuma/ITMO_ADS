def tree_height(n, parents):
    adj = [[] for _ in range(n)]
    root = -1
    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            adj[p].append(i)

    q = [root]
    h = 0
    while q:
        h += 1
        new_q = []
        for u in q:
            for v in adj[u]:
                new_q.append(v)
        q = new_q
    return h