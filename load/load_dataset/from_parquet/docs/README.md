# load_dataset from_parquet

Load a local Parquet file with `load_dataset("parquet", ...)`.

## What It Teaches

- `load_dataset` has built-in Parquet support.
- Parquet is a common storage format for structured tabular data.
- Local Parquet files are a practical bridge between data engineering outputs and `datasets`.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_parquet/src/main.py
```

## Expected Result

The script:

- creates a small local Parquet file in `data/`
- loads it with `load_dataset`
- prints the schema and loaded rows

## Notes

- The example writes its own sample file to keep setup minimal.
- Parquet often preserves types more explicitly than CSV.
