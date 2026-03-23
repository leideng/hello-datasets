# batch

Iterate over a dataset in batches with `Dataset.iter(...)`.

## What It Teaches

- You do not need to materialize every row one by one.
- `iter(batch_size=...)` yields dictionaries of column lists.
- Batch iteration is useful for inspection, export loops, and lightweight processing outside `map`.

## Run

From the repository root:

```bash
uv run python process/batch/src/main.py
```

## Expected Result

The script prints:

- the dataset summary
- each batch as a dictionary of column lists

## Notes

- This is an iteration pattern, not a permanent dataset transformation.
