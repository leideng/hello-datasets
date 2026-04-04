# shard

Take one shard of a dataset with `Dataset.shard(...)`.

## What It Teaches

- Sharding splits a dataset into deterministic pieces by row position.
- It is useful for distributed work, chunked processing, or manual partitioning.
- `index` selects which shard to keep.

## Run

From the repository root:

```bash
uv run python topics/02-process/shard/main.py
```

## Expected Result

The script prints:

- the selected shard summary
- only the rows that belong to shard `1` out of `3`

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 20: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This is a structural partition, not a random split.
