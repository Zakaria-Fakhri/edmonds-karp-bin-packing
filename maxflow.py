def edmonds_karp(capacity):
    # Create flow dictionary
    flow = {}
    for u in capacity:
        flow[u] = {}
        for v in capacity[u]:
            flow[u][v] = 0
    
    max_flow = 0

    def bfs():
        parent = {}
        visited = {"s"}
        queue = ["s"]  # Use list as queue

        while queue:
            u = queue.pop(0)  # FIFO behavior
            for v in capacity.get(u, {}):
                if v not in visited and capacity[u][v] - flow[u].get(v, 0) > 0:
                    parent[v] = u
                    visited.add(v)
                    queue.append(v)
                    if v == "t":
                        return parent
        return {}

    while True:
        parent = bfs()
        if not parent or "t" not in parent:
            break

        v = "t"
        path_flow = float('inf')
        while v != "s":
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u].get(v, 0))
            v = u

        v = "t"
        while v != "s":
            u = parent[v]
            if u not in flow:
                flow[u] = {}
            if v not in flow:
                flow[v] = {}
            flow[u][v] = flow[u].get(v, 0) + path_flow
            flow[v][u] = flow[v].get(u, 0) - path_flow
            v = u

        max_flow += path_flow

    return max_flow
