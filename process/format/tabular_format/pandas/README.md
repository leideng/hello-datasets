# tabular_format pandas

Convert a dataset to a Pandas DataFrame with `to_pandas()`.

## What It Teaches

- `to_pandas()` is a convenient bridge into the Pandas ecosystem.
- This is useful for quick inspection, plotting, and familiar dataframe workflows.
- The conversion materializes the data as a DataFrame.

## Run

From the repository root:

```bash
uv run python process/format/tabular_format/pandas/main.py
```

## Expected Result

The script prints:

- the dataset summary
- the resulting DataFrame type
- the DataFrame contents

## Notes

- Use this when you specifically want Pandas operations, not when you need to stay in `datasets`.
