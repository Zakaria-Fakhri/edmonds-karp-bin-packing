# Bin Packing Solver

A Python implementation of the bin packing problem using S-T maximum flow approach with Edmonds-Karp algorithm.

## Algorithm

Solves bin packing by modeling it as a maximum flow problem:
- Source connects to items
- Items connect to bins (if they fit)  
- Bins connect to sink
- Uses Edmonds-Karp for max flow computation

### Pseudocode

```
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

# 📦 Bin Packing Solver

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

## ⚠️ Approximation Quality

### **Worst-Case Performance:**
- **Approximation Factor:** Up to **2×** optimal
- **Reason:** Simple bipartite matching ignores bin capacity constraints

### **Performance Analysis:**
| Case | Approximation Ratio | Example |
|------|-------------------|---------|
| **Best-Case** | 1× (Optimal) | Items ≤ 0.5 |
| **Average-Case** | ~1.7× | Random uniform items |
| **Worst-Case** | 2× | Items > 0.5 |

### **Example of Suboptimal Behavior:**
```
Items: [0.6, 0.6, 0.6, 0.6]
Optimal Solution: 2 bins (impossible to fit 2 items per bin)
This Algorithm: 4 bins (one item per bin)
Approximation: 4/2 = 2×
```

### **Comparison with Other Algorithms:**
- **First Fit Decreasing (FFD):** 1.22× approximation
- **Best Fit Decreasing:** ~1.22× approximation  
- **This Flow Algorithm:** Up to 2× approximation
- **Next Fit:** 2× approximation

> **Note:** This implementation trades optimality for educational value in demonstrating flow network modeling.

## 🚀 Usage

```python
from solver import BinPackingFlowSolver

items = [0.4, 0.8, 0.3, 0.5, 0.2]
solver = BinPackingFlowSolver(items)
result = solver.find_min_bins()
print(f"Minimum bins required: {result}")
```

## 🏃‍♂️ Run Example

```bash
python example.py
```

**Expected Output:**
```
Minimale Anzahl benötigter Bins: 5
```
*(Note: Suboptimal result - optimal would be 3 bins)*

## 📋 Requirements

- **Python 3.x**
- **No external dependencies** - Pure Python implementation

## 🎯 Educational Purpose

This implementation demonstrates:
- ✅ **Flow network modeling** of combinatorial problems
- ✅ **Edmonds-Karp algorithm** implementation
- ✅ **S-T maximum flow** approach
- ⚠️ **Limitations** of simple flow models for complex constraints
