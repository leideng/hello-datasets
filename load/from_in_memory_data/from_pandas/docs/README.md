# from_pandas

Create a Hugging Face `Dataset` from a Pandas DataFrame.

## What It Teaches

- `Dataset.from_pandas(...)` converts tabular in-memory data into a dataset.
- Pandas is convenient when data cleaning already happened in a DataFrame workflow.
- `preserve_index=False` avoids turning the DataFrame index into an extra dataset column.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_pandas/src/main.py
```

## Expected Result

The script prints:

- a dataset summary
- the inferred feature schema
- one example row

## Notes

- If you keep the index, it may appear as an extra column.
- This is a useful bridge when moving from Pandas-based exploration into `datasets`.
