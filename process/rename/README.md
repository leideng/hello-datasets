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

## Notes

- Use this when two datasets express the same concept with different field names.
