from client import AnnoyForest

def main():
    print("=== Testing Annoy Random Projection Forest ===")
    annoy = AnnoyForest(dim=3, n_trees=4)
    data = {1: [1.0, 0.0, 0.0], 2: [0.0, 1.0, 0.0], 3: [1.0, 0.1, 0.0]}
    annoy.build(data)

    cand = annoy.search([1.0, 0.0, 0.0])
    print("Candidate neighbor IDs:", cand)
    assert len(cand) > 0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
