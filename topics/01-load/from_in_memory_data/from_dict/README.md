# from_dict

Create a Hugging Face `Dataset` directly from a Python dictionary of columns.

## What It Teaches

- `Dataset.from_dict(...)` expects a column-oriented input shape.
- Each dictionary key becomes a dataset column.
- Every column must have the same number of rows.

## Run

From the repository root:

```bash
uv run python topics/01-load/from_in_memory_data/from_dict/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the inferred feature schema
- the first row

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This is one of the simplest ways to create a small in-memory dataset.
- Use it when your data is already organized as lists by column.
