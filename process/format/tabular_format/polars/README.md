# tabular_format polars

Convert a dataset into a Polars DataFrame through Arrow.

## What It Teaches

- `datasets` stores Arrow-compatible data that Polars can consume efficiently.
- Polars is a good fit when you want a fast dataframe engine.
- Arrow is a practical interchange layer between `datasets` and Polars.

## Run

From the repository root:

```bash
uv run python process/format/tabular_format/polars/main.py
```

## Expected Result

The script prints:

- the dataset summary
- the Polars DataFrame type
- the DataFrame contents

## Notes

- This example goes through Arrow because that matches the dataset's native storage model.
