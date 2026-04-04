# distributed_usage

Use sharding plus `map(...)` as a simple distributed preprocessing pattern.

## What It Teaches

- A common distributed pattern is to shard a dataset by worker or rank.
- Each worker can map over its own shard independently.
- This keeps preprocessing logic deterministic and easy to reason about.

## Run

From the repository root:

```bash
uv run python process/map/distributed_usage/main.py
```

## Expected Result

The script prints:

- the rows handled by simulated rank `0`
- the rows handled by simulated rank `1`

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def annotate_rank(rank: int):`
  Defines `annotate_rank`, the function that groups one logical step of the example.
- Line 5: `    def add_rank(batch: dict[str, list]) -> dict[str, list]:`
  Defines `add_rank`, the function that groups one logical step of the example.
- Line 6: `        return {"worker_rank": [rank] * len(batch["text"])}`
  Returns the transformed value that the dataset API will store or use next.
- Line 8: `    return add_rank`
  Returns the transformed value that the dataset API will store or use next.
- Line 11: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 12: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 25: `    rank0_dataset = dataset.shard(num_shards=2, index=0).map(annotate_rank(0), batched=True)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 26: `    rank1_dataset = dataset.shard(num_shards=2, index=1).map(annotate_rank(1), batched=True)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 34: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This example simulates distributed preprocessing locally without needing a real multi-node setup.
