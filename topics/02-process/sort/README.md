# sort

Order rows by a column with `Dataset.sort(...)`.

## What It Teaches

- Sorting reorders the dataset by one or more columns.
- `reverse=True` gives descending order.
- This is useful for ranking, inspection, or deterministic report generation.

## Run

From the repository root:

```bash
uv run python topics/02-process/sort/main.py
```

## Expected Result

The script prints:

- the sorted dataset summary
- rows ordered by highest score first

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 12: `    sorted_dataset = dataset.sort("score", reverse=True)`
  Sorts the dataset by a chosen column.
- Line 20: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Sorting changes row order but not row values.
