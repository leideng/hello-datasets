# batch

Iterate over a dataset in batches with `Dataset.iter(...)`.

## What It Teaches

- You do not need to materialize every row one by one.
- `iter(batch_size=...)` yields dictionaries of column lists.
- Batch iteration is useful for inspection, export loops, and lightweight processing outside `map`.

## Run

From the repository root:

```bash
uv run python process/batch/main.py
```

## Expected Result

The script prints:

- the dataset summary
- each batch as a dictionary of column lists

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 16: `    for batch_index, batch in enumerate(dataset.iter(batch_size=2), start=1):`
  Loops over example items to build or transform the dataset input.
- Line 20: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This is an iteration pattern, not a permanent dataset transformation.
