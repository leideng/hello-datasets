# concatenate

Combine multiple datasets with `concatenate_datasets(...)`.

## What It Teaches

- Datasets with the same schema can be stacked vertically.
- Concatenation is useful when merging shards or appending extra examples.
- All input datasets should have compatible columns and feature types.

## Run

From the repository root:

```bash
uv run python process/concatenate/main.py
```

## Expected Result

The script prints:

- the combined dataset summary
- all rows from both source datasets in order

## Notes

- This operation keeps row order unless you shuffle afterward.
