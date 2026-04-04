# shard

Take one shard of a dataset with `Dataset.shard(...)`.

## What It Teaches

- Sharding splits a dataset into deterministic pieces by row position.
- It is useful for distributed work, chunked processing, or manual partitioning.
- `index` selects which shard to keep.

## Run

From the repository root:

```bash
uv run python process/shard/main.py
```

## Expected Result

The script prints:

- the selected shard summary
- only the rows that belong to shard `1` out of `3`

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 6: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 7: `            "id": list(range(10)),`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": [f"row-{i}" for i in range(10)],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `    shard_dataset = dataset.shard(num_shards=3, index=1)`
  Saves a value into `shard_dataset` so later lines can reuse it.
- Line 14: `    print("Dataset after shard")`
  Prints information so you can observe what the dataset operation produced.
- Line 15: `    print(shard_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 16: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 17: `    print("Rows:", shard_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 21: `    main()`
  Calls `main()` to start the example.

## Notes

- This is a structural partition, not a random split.
