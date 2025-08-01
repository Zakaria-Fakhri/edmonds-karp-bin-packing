def build_flow_network(items, bin_count):
    # Create bipartite matching network
    capacity = {}
    
    # Source to items
    if "s" not in capacity:
        capacity["s"] = {}
    for i in range(len(items)):
        capacity["s"][f"i{i}"] = 1

    # Items to bins (if item fits)
    for i, size in enumerate(items):
        if f"i{i}" not in capacity:
            capacity[f"i{i}"] = {}
        for b in range(bin_count):
            if size <= 1.0:
                capacity[f"i{i}"][f"b{b}"] = 1

    # Bins to sink
    for b in range(bin_count):
        if f"b{b}" not in capacity:
            capacity[f"b{b}"] = {}
        capacity[f"b{b}"]["t"] = 1
    
    return capacity
