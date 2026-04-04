# rename

Rename a column with `rename_column(...)`.

## What It Teaches

- Renaming columns is often useful when standardizing schema across datasets.
- The row values stay the same; only the column name changes.
- Clear names help later transformation code stay readable.

## Run

From the repository root:

```bash
uv run python process/rename/main.py
```

## Expected Result

The script prints:

- the renamed dataset summary
- the updated column names
- the rows using the new `text` column

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 15: `    renamed_dataset = dataset.rename_column("sentence", "text")`
  Renames a column so later code can use the new field name.
- Line 24: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Use this when two datasets express the same concept with different field names.
