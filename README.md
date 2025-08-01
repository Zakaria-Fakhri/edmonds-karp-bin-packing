# Bin Packing Solver

A Python implementation of the bin packing problem using **S-T maximum flow** approach with **Edmonds-Karp** algorithm.

## 🔄 Algorithm Overview

Solves bin packing by modeling it as a maximum flow problem:
- **Source** connects to items
- **Items** connect to bins (if they fit)  
- **Bins** connect to sink
- Uses **Edmonds-Karp** for max flow computation

### 📝 Pseudocode

```pseudocode
function solve_bin_packing(items, k):
    G = create_flow_network()
    
    // Add source to items edges
    for each item i:
        add_edge(source, item_i, capacity=1)
    
    // Add item to bin edges  
    for each item i with size s:
        for each bin b:
            if s <= 1.0:
                add_edge(item_i, bin_b, capacity=1)
    
    // Add bin to sink edges
    for each bin b:
        add_edge(bin_b, sink, capacity=1)
    
    max_flow = edmonds_karp(G)
    return max_flow == number_of_items

function find_minimum_bins(items):
    for k = 1 to len(items):
        if solve_bin_packing(items, k):
            return k
```

## Approximation Quality

### **Worst-Case Performance:**
- **Approximation Factor:** Up to **2×** optimal
- **Reason:** Simple bipartite matching ignores bin capacity constraints


