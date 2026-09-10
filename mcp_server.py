import sys
import json
from client import AnnoyForest

def main():
    forest = AnnoyForest()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "build":
            items = {int(k): v for k, v in params.get("items", {}).items()}
            forest.dim = len(next(iter(items.values()))) if items else 4
            forest.build(items)
            res = {"status": "ok"}
        elif method == "search":
            res = {"candidates": forest.search(params.get("query_vec", []))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
