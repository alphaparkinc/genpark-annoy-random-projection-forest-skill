import math
import random

class AnnoyForest:
    """
    Random Projection Hyperplane Forest for sub-linear vector retrieval.
    """
    def __init__(self, dim=4, n_trees=3):
        self.dim = dim
        self.n_trees = n_trees
        self.trees = []
        self.items = {}

    def build(self, items):
        self.items = items
        for _ in range(self.n_trees):
            plane = [random.gauss(0, 1) for _ in range(self.dim)]
            norm = math.sqrt(sum(p * p for p in plane))
            plane = [p / norm for p in plane]
            left = []
            right = []
            for idx, vec in items.items():
                dot = sum(p * v for p, v in zip(plane, vec))
                if dot < 0:
                    left.append(idx)
                else:
                    right.append(idx)
            self.trees.append({"plane": plane, "left": left, "right": right})

    def search(self, query_vec):
        candidates = set()
        for t in self.trees:
            plane = t["plane"]
            dot = sum(p * v for p, v in zip(plane, query_vec))
            bucket = t["left"] if dot < 0 else t["right"]
            candidates.update(bucket)
        return list(candidates)
