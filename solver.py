from network import build_flow_network
from maxflow import edmonds_karp

class BinPackingFlowSolver:
    def __init__(self, items):
        self.items = items
        self.n = len(items)

    def is_bin_packing_possible(self, bin_count):
        # Basic volume check
        total_size = sum(self.items)
        if total_size > bin_count:
            return False
        
        # Check if any item is too large
        if any(item > 1.0 for item in self.items):
            return False
        
        # Build flow network and solve
        network = build_flow_network(self.items, bin_count)
        flow = edmonds_karp(network)
        
        # For simple matching: all items must be matched
        return flow == self.n

    def find_min_bins(self):
        # Search for minimum bins needed
        for k in range(1, self.n + 1):
            if self.is_bin_packing_possible(k):
                return k
        return self.n
