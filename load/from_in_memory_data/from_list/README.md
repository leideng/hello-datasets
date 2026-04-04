# from_list

Create a Hugging Face `Dataset` from a row-oriented Python list of dictionaries.

## What It Teaches

- `Dataset.from_list(...)` works well when your data starts as records.
- Each dictionary in the list represents one row.
- Feature types are inferred from the Python values.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_list/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the column names
- one sample row

## Notes

- Compared with `from_dict`, this input is row-oriented instead of column-oriented.
- This is usually more convenient when prototyping from JSON-like records.
