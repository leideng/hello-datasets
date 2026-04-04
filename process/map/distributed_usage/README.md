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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def annotate_rank(rank: int):`
  Defines the function `annotate_rank` so the example logic is grouped into a named step.
- Line 5: `    def add_rank(batch: dict[str, list]) -> dict[str, list]:`
  Defines the function `add_rank` so the example logic is grouped into a named step.
- Line 6: `        return {"worker_rank": [rank] * len(batch["text"])}`
  Returns the computed value back to the caller.
- Line 8: `    return add_rank`
  Returns the computed value back to the caller.
- Line 11: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 12: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 13: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 14: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `                "row-0",`
  Provides one literal sample value used by the example data or configuration.
- Line 16: `                "row-1",`
  Provides one literal sample value used by the example data or configuration.
- Line 17: `                "row-2",`
  Provides one literal sample value used by the example data or configuration.
- Line 18: `                "row-3",`
  Provides one literal sample value used by the example data or configuration.
- Line 19: `                "row-4",`
  Provides one literal sample value used by the example data or configuration.
- Line 20: `                "row-5",`
  Provides one literal sample value used by the example data or configuration.
- Line 21: `            ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 22: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 23: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 25: `    rank0_dataset = dataset.shard(num_shards=2, index=0).map(annotate_rank(0), batched=True)`
  Stores the result of a dataset operation so the next lines can inspect it.
- Line 26: `    rank1_dataset = dataset.shard(num_shards=2, index=1).map(annotate_rank(1), batched=True)`
  Stores the result of a dataset operation so the next lines can inspect it.
- Line 28: `    print("Distributed-style preprocessing by shard")`
  Prints information so you can observe what the dataset operation produced.
- Line 29: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 30: `    print("Rank 0 rows:", rank0_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 31: `    print("Rank 1 rows:", rank1_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 34: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 35: `    main()`
  Calls `main()` to start the example.

## Notes

- This example simulates distributed preprocessing locally without needing a real multi-node setup.
