# flatten

Expand nested struct columns with `Dataset.flatten(...)`.

## What It Teaches

- Nested dictionary-like columns can be expanded into top-level columns.
- Flattening is useful before export or when downstream code expects simple schemas.
- Nested fields become dotted column names such as `meta.title`.

## Run

From the repository root:

```bash
uv run python process/flatten/main.py
```

## Expected Result

The script prints:

- the flattened dataset summary
- top-level columns such as `meta.title` and `meta.difficulty`

## Notes

- Flattening is especially useful after loading nested JSON-like records.
