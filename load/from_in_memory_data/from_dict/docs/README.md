# from_dict

Create a Hugging Face `Dataset` directly from a Python dictionary of columns.

## What It Teaches

- `Dataset.from_dict(...)` expects a column-oriented input shape.
- Each dictionary key becomes a dataset column.
- Every column must have the same number of rows.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_dict/src/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the inferred feature schema
- the first row

## Notes

- This is one of the simplest ways to create a small in-memory dataset.
- Use it when your data is already organized as lists by column.
