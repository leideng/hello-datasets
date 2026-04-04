# select

Pick specific row indices with `Dataset.select(...)`.

## What It Teaches

- `select` keeps rows by position.
- It is useful for slicing examples, debugging, or building small subsets.
- The selected indices are zero-based positions in the dataset.

## Run

From the repository root:

```bash
uv run python topics/02-process/select/main.py
```

## Expected Result

The script prints:

- the selected dataset summary
- only rows `0`, `2`, and `4`

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 18: `    selected_dataset = dataset.select([0, 2, 4])`
  Selects only specific row positions from the dataset.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- `select` is different from `filter`: it uses explicit row indices instead of a predicate function.
