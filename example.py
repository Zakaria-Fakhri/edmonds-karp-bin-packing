from solver import BinPackingFlowSolver

if __name__ == "__main__":
    items = [0.4, 0.8, 0.3, 0.5, 0.2]
    solver = BinPackingFlowSolver(items)
    result = solver.find_min_bins()
    print(f"Minimale Anzahl benötigter Bins: {result}")
