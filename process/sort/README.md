# sort

Order rows by a column with `Dataset.sort(...)`.

## What It Teaches

- Sorting reorders the dataset by one or more columns.
- `reverse=True` gives descending order.
- This is useful for ranking, inspection, or deterministic report generation.

## Run

From the repository root:

```bash
uv run python process/sort/main.py
```

## Expected Result

The script prints:

- the sorted dataset summary
- rows ordered by highest score first

## Notes

- Sorting changes row order but not row values.
